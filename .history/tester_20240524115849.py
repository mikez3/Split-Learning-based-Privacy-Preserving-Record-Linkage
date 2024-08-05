# %%
import time
import dask_cudf
import numpy as np
import cupy as cp
from fastdist import fastdist
import rmm
import joblib
import time
import pandas as pd
from dask.diagnostics import ProgressBar

def process_chunk(chunk):
    if chunk.empty:
        chunk_fp = chunk_fn = chunk_tp = 0
        return chunk_fp, chunk_fn, chunk_tp
    predictions_joblib = model.predict(chunk.drop(chunk.columns[0], axis=1)).astype(np.int64)
    test_true_label = chunk.iloc[:, 0].astype('int64')
    if cp.unique(predictions_joblib).size > 1:
        _, chunk_fp, chunk_fn, chunk_tp = fastdist.confusion_matrix(test_true_label.to_numpy(), predictions_joblib.to_numpy()).ravel()
    else:
        chunk_fp = chunk_fn = chunk_tp = 0
    return chunk_fp, chunk_fn, chunk_tp

current_time = time.ctime()
print("Start time:", current_time)
metric = 'cosine'
kernels = ['linear', 'rbf']
refs = ['200', '2000']
trainings = ['500', '2000']
testings_1 = [215, 2000, 5000, 10000]
testings_2 = [858, 2000, 5000, 10000]
test_results = []
for kernel in kernels:
    for ref in refs:
        for lines_trained in trainings:
            if lines_trained == '500':
                testings = testings_1
            else:
                testings=testings_2
            for lines_to_test in testings:
                for part in range(0,3):
                    for site in range(1,3):

                            start_time = time.time()
                            print(kernel, ',lines trained:', lines_trained)
                            total_p = 0
                            total_r = 0
                            model = joblib.load('./trained_models/shuffle/'+kernel+'/part'+str(part)+'_clean_ref_cosine_n'+lines_trained+'_ref'\
                                                +ref+'.joblib')
                           
                            data_path = 'Data/test_samples/part'+str(part)+'_'+metric+'_n'+str(lines_to_test)+'_ref'+ref+'.csv'
                            print('filepath =',data_path)

                            chunksize = 500000
                            csv_lines = lines_to_test**2
                            num_chunks = csv_lines // chunksize + 1
                            tp = fp = fn = 0
                            chunk = dask_cudf.read_csv(data_path, header=None, blocksize=chunksize)

                            with ProgressBar():
                                results = chunk.map_partitions(process_chunk, meta=(None, 'int64')).compute()
                            tp = fp = fn = 0
                            for _, (chunk_fp, chunk_fn, chunk_tp) in results.items():
                                tp += chunk_tp
                                fp += chunk_fp
                                fn += chunk_fn
                            print(tp,fp,fn)
                            if not(tp+fp == 0):  
                                precision = np.round(tp/(tp+fp),4)
                            else:
                                precision = 0
                            if not(tp+fn == 0):
                                recall = np.round(tp/(tp+fn),4)
                            else:
                                recall = 0
                            print("\nP =", precision)
                            print("R =", recall)
                            end_time = time.time()
                            test_time = round(end_time - start_time, 4)
                            pr_str = 'P='+str(precision)+', R='+str(recall)
                            test_results.append({'kernel': kernel, 'reference rows':int(ref), 'train rows':int(lines_trained), 'test rows':lines_to_test, 'part':part,'site':site,'P,R':pr_str, 'test time (in loop)':test_time})
test_results_df = pd.DataFrame(test_results)
test_results_df.to_csv('results.csv', index=False)
