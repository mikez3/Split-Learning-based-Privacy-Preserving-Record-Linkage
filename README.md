# Split Learning approach for Privacy Preserving Record Linkage
<!-- > **Notice**: This project is currently under development. -->

This project investigates the application of Split Learning for Privacy-Preserving Record Linkage, aiming to identify the same entity across different databases without compromising privacy, using Reference sets (publicly available data collections). This method has minimal impact on matching performance compared to a traditional centralized SVM-based approach.

## Quick info:
`SL_training_data_generator.py`: Generates data for training and testing.

`SL_test_data_generatror.py`: Responsible for the creation of test datasets for Split Learning models.

`local_training_data_generator.py`: Generates data for local training (no Split Learning and Reference Set here).

<!-- `prepare_job_config.sh`: Generates the configuration files -->

<!-- [`run_experiment_simulator.sh`](#run-experiment-with-fl-simulator): Runs the FL simulator -->

`local_test_data_generatror.py`: Responsible for the creation of test datasets for local models.

`tester.py`: Tests saved models on datasets.

<!-- [`jobs`](#prepare-clients-configs-with-proper-data-information): Contains python and config files for clients and server in FL simulator -->

<!-- `workspace`: Contains files that used during FL (like configs and python) and files that created after FL for server and each client -->


<!-- ## NVFLare

This project was implemented using NVFlare.

For more detailed information about the framework, you may refer to the [Scikit-learn SVM example](https://github.com/NVIDIA/NVFlare/tree/main/examples/advanced/sklearn-svm) in the [NVIDIA NVFlare](https://github.com/NVIDIA/NVFlare/tree/main) repository. -->
<!-- ## cuML - Scikit-learn
For faster execution times with large datasets, it is recommended to use [cuML](https://docs.rapids.ai/api/cuml/stable/). Alternatively, [Scikit-learn](https://scikit-learn.org/) can be used as a backend instead of cuML. -->


<!-- ## Train and save models 
A script is used to automatically train and also create the configuration files for a specific setting.
This script saves each model from split learning to `trained_models/shuffle` folder. Each part represents a different shuffle of the data.
You can run the script with the following command:

```bash
./train.sh
``` -->

<!-- Please note that this script will recreate the `jobs/sklearn_svm_base/` folder for each client and also for the server. For instance, if you modify the number of clients in this bash file to 2, it will create a new folder under the `jobs/` directory named `sklearn_svm_2_uniform`.

The newly created folder will contain the same files and code as in the `jobs/sklearn_svm_base/` directory. If you wish to make more detailed modifications, such as changing the model kernel for the client and server, you will need to modify the `jobs/sklearn_svm_base/app/config/config_fed_server.json` file.

In this example, we chose the Radial Basis Function (RBF) kernel to experiment with three clients under the uniform data split.  -->


<!-- ## Run experiment with FL simulator
We can run the [FL simulator](https://nvflare.readthedocs.io/en/2.3/user_guide/fl_simulator.html) with three clients under the uniform data split with
```commandline
nvflare simulator ./jobs/sklearn_svm_2_uniform -w ./workspace -n 2 -t 2
```
or
```commandline
bash run_experiment_simulator.sh
```
You can monitor the Precision and Recall metrics of the resulting global model through the clients' logs and Google TensorBoard. To launch TensorBoard, execute the following command:
```bash
python3 -m tensorboard.main --logdir='workspace'
```
 -->
