# Source: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2

Title: Tutorial: Model Development on a Cloud Workstation - Azure Machine Learning

URL Source: https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2

Markdown Content:
This article describes how to develop a training script by using a notebook on an Azure Machine Learning cloud workstation. The tutorial covers the basic steps that you need to get started:

*   Set up and configure the cloud workstation. Your cloud workstation is powered by an Azure Machine Learning compute instance, which is pre-configured with environments to support your model development needs.
*   Use cloud-based development environments.
*   Use MLflow to track your model metrics.

To use Azure Machine Learning, you need a workspace. If you don't have one, complete [Create resources you need to get started](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2) to create a workspace and learn more about using it.

Important

If your Azure Machine Learning workspace is configured with a managed virtual network, you might need to add outbound rules to allow access to the public Python package repositories. For more information, see [Scenario: Access public machine learning packages](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-managed-network#scenario-access-public-machine-learning-packages).

You can create compute resources in the **Compute** section in your workspace. A compute instance is a cloud-based workstation that's fully managed by Azure Machine Learning. This tutorial series uses a compute instance. You can also use it to run your own code, and to develop and test models.

1.   Sign in to [Azure Machine Learning studio](https://ml.azure.com/).
2.   Select your workspace, if it isn't already open.
3.   In the left pane, select **Compute**.
4.   If you don't have a compute instance, you see **New** in the middle of the page. Select **New** and fill out the form. You can use all the defaults.
5.   If you have a compute instance, select it from the list. If it's stopped, select **Start**.

After you have a running compute instance, you can access it in various ways. This tutorial describes how to use the compute instance from Visual Studio Code. Visual Studio Code provides a full integrated development environment (IDE) for creating compute instances.

In the compute instance list, select the **VS Code (Web)** or **VS Code (Desktop)** link for the compute instance you want to use. If you choose **VS Code (Desktop)**, you might see a message asking if you want to open the application.

[![Image 1: Screenshot that shows links for starting Visual Studio Code (Web or Desktop).](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/launch-vs-code.png?view=azureml-api-2)](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/launch-vs-code.png?view=azureml-api-2#lightbox)

This Visual Studio Code instance is attached to your compute instance and your workspace file system. Even if you open it on your desktop, the files you see are files in your workspace.

In order for your script to run, you need to be working in an environment that's configured with the dependencies and libraries the code expects. This section helps you create an environment that's tailored to your code. To create the new Jupyter kernel your notebook connects to, you use a YAML file that defines the dependencies.

*   **Upload a file.**

Files that you upload are stored in an Azure file share, and these files are mounted to each compute instance and shared within the workspace.

    1.   Go to [azureml-examples/tutorials/get-started-notebooks/workstation_env.yml](https://github.com/Azure/azureml-examples/blob/main/tutorials/get-started-notebooks/workstation_env.yml).

    2.   Download the Conda environment file _workstation\_env.yml_ to your computer by selecting the ellipsis button (**...**) in the top-right corner of the page and then selecting **Download**.

    3.   Drag the file from your computer to the Visual Studio Code window. The file is uploaded to your workspace.

    4.   Move the file into your username folder.

![Image 2: Screenshot that shows the workstation_env.yml file in the username folder.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/upload-file.png?view=azureml-api-2)

    5.   Select the file to preview it. Review the dependencies that it specifies. You should see something like this:

```
name: workstation_env
# This file serves as an example - you can update packages or versions to fit your use case
dependencies:
  - python=3.8
  - pip=21.2.4
  - scikit-learn=0.24.2
  - scipy=1.7.1
  - pandas>=1.1,<1.2
  - pip:
    - mlflow-skinny 
    - azureml-mlflow
    - psutil>=5.8,<5.9
    - ipykernel~=6.0
    - matplotlib
```
*   **Create a kernel.**

Now use the terminal to create a new Jupyter kernel that's based on the _workstation\_env.yml_ file.

    1.   In the menu at the top of Visual Studio Code, select **Terminal > New Terminal**.

![Image 3: Screenshot of open terminal tool in notebook toolbar.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/open-terminal.png?view=azureml-api-2)

    1.   View your current Conda environments. The active environment is marked with an asterisk (*).

```
conda env list
```
    2.   Use `cd` to navigate to the folder where you uploaded the _workstation\_env.yml_ file. For example, if you uploaded it to your user folder, use this command:

```
cd Users/myusername
```
    3.   Make sure workstation_env.yml is in the folder.

```
ls
```
    4.   Create the environment based on the Conda file provided. It takes a few minutes to build the environment.

```
conda env create -f workstation_env.yml
```
    5.   Activate the new environment.

```
conda activate workstation_env
```
Note

If you see CommandNotFoundError, follow instructions to run `conda init bash`, close the terminal, and then open a new one. Then try the `conda activate workstation_env` command again. 
    6.   Verify that the correct environment is active, again looking for the environment marked with a *.

```
conda env list
```
    7.   Create a new Jupyter kernel that's based on your active environment.

```
python -m ipykernel install --user --name workstation_env --display-name "Tutorial Workstation Env"
```
    8.   Close the terminal window.

You now have a new kernel. Next, you'll open a notebook and use this kernel.

1.   In the menu at the top of Visual Studio Code, select **File > New File**.
2.   Name your new file **develop-tutorial.ipynb** (or use another name). Be sure to use the **.ipynb** extension.

1.   In the top-right corner of the new file, select **Select Kernel**.
2.   Select **Azure ML compute instance (computeinstance-name)**.
3.   Select the kernel you created: **Tutorial Workstation Env**. If you don't see the kernel, select the refresh button above the list.

In this section, you develop a Python training script that predicts credit card default payments by using the prepared test and training datasets from the [UCI dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).

This code uses `sklearn` for training and MLflow for logging metrics.

1.   Start with code that imports the packages and libraries that you'll use in the training script.

```
import os
import argparse
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
```
2.   Next, load and process the data for the experiment. In this tutorial, you read the data from a file on the internet.

```
# load the data
credit_df = pd.read_csv(
    "https://azuremlexamples.blob.core.windows.net/datasets/credit_card/default_of_credit_card_clients.csv",
    header=1,
    index_col=0,
)

train_df, test_df = train_test_split(
    credit_df,
    test_size=0.25,
)
```
3.   Prepare the data for training.

```
# Extracting the label column
y_train = train_df.pop("default payment next month")

# convert the dataframe values to array
X_train = train_df.values

# Extracting the label column
y_test = test_df.pop("default payment next month")

# convert the dataframe values to array
X_test = test_df.values
```
4.   Add code to start autologging with MLflow so that you can track the metrics and results. With the iterative nature of model development, MLflow helps you log model parameters and results. Refer to different runs to compare and understand how your model performs. The logs also provide context for when you're ready to move from the development phase to the training phase of your workflows within Azure Machine Learning.

```
# set name for logging
mlflow.set_experiment("Develop on cloud tutorial")
# enable autologging with MLflow
mlflow.sklearn.autolog()
```
5.   Train a model.

```
# Train Gradient Boosting Classifier
print(f"Training with data of shape {X_train.shape}")

mlflow.start_run()
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))
# Stop logging for this model
mlflow.end_run()
```
Note

You can ignore the MLflow warnings. The results you need will still be tracked. 
6.   Select **Run All** above the code.

Now that you have model results, change something and run the model again. For example, try a different classification technique:

```
# Train  AdaBoost Classifier
from sklearn.ensemble import AdaBoostClassifier

print(f"Training with data of shape {X_train.shape}")

mlflow.start_run()
ada = AdaBoostClassifier()

ada.fit(X_train, y_train)

y_pred = ada.predict(X_test)

print(classification_report(y_test, y_pred))
# Stop logging for this model
mlflow.end_run()
```

Note

You can ignore the MLflow warnings. The results you need will still be tracked.

Select **Run All** to run the model.

Now that you've tried two different models, use the results tracked by MLFfow to decide which model is better. You can reference metrics like accuracy, or other indicators that matter the most for your scenarios. You can review these results in more detail by looking at the jobs created by MLflow.

1.   Return to your workspace in the [Azure Machine Learning studio](https://ml.azure.com/).

2.   In the left pane, select **Jobs**.

![Image 4: Screenshot that shows the Jobs item in the left pane.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/jobs.png?view=azureml-api-2)

3.   Select **Develop on cloud tutorial**.

4.   There are two jobs shown, one for each of the models you tried. The names are autogenerated. If you want to rename the job, hover over the name and select the pencil button next to it.

5.   Select the link for the first job. The name appears at the top of the page. You can also rename it here by using the pencil button.

6.   The page shows job details, like properties, outputs, tags, and parameters. Under **Tags**, you see the **estimator_name**, which describes the type of model.

7.   Select the **Metrics** tab to view the metrics that were logged by MLflow. (Your results will be different because you have a different training set.)

[![Image 5: Screenshot that shows metrics for a job.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/metrics.png?view=azureml-api-2)](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/metrics.png?view=azureml-api-2#lightbox)

8.   Select the **Images** tab to view the images generated by MLflow.

![Image 6: Screenshot that shows images for a job.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/images.png?view=azureml-api-2)

9.   Go back and review the metrics and images for the other model.

You'll now create a Python script from your notebook for model training.

1.   In Visual Studio Code, right-click the notebook file name and select **Import Notebook to Script**.

2.   Select **File > Save** to save the new script file. Call it **train.py**.

3.   Look through the file and delete code that you don't want in the training script. For example, keep the code for the model you want to use, and delete code for the model you don't want to use.

    *   Be sure you keep the code that starts autologging (`mlflow.sklearn.autolog()`).
    *   When you run the Python script interactively (as you're doing here), you can keep the line that defines the experiment name (`mlflow.set_experiment("Develop on cloud tutorial")`). Or you can give it a different name to see it as a different entry in the **Jobs** section. But when you prepare the script for a training job, that line doesn't apply and should be omitted: the job definition includes the experiment name.
    *   When you train a single model, the lines for starting and ending a run (`mlflow.start_run()` and `mlflow.end_run()`) aren't necessary (they have no effect), but you can leave them in.

4.   When you're finished with your edits, save the file.

You now have a Python script to use for training your preferred model.

For now, you're running this code on your compute instance, which is your Azure Machine Learning development environment. [Tutorial: Train a model](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-train-model?view=azureml-api-2) shows how to run a training script in a more scalable way on more powerful compute resources.

1.   Select the environment you created earlier in this tutorial as your Python version (workstations_env). In the lower-right corner of the notebook, you'll see the environment name. Select it, and then select the environment at the top of Visual Studio Code.

[![Image 7: Screenshot that shows selecting the new environment.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/select-python.png?view=azureml-api-2)](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/select-python.png?view=azureml-api-2#lightbox)

2.   Run the Python script by selecting the **Run All** button above the code.

[![Image 8: Screenshot that shows the Run button.](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/run-python.png?view=azureml-api-2)](https://learn.microsoft.com/en-us/azure/machine-learning/media/tutorial-cloud-workstation/run-python.png?view=azureml-api-2#lightbox)

Note

You can ignore the MLflow warnings. You'll still get all the metrics and images from autologging.

Go back to **Jobs** in your workspace in Azure Machine Learning studio to see the results of your training script. Keep in mind that the training data changes with each split, so the results differ between runs.

If you plan to continue on to other tutorials, skip to [Next steps](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-cloud-workstation?view=azureml-api-2#next-steps).

If you're not going to use it now, stop the compute instance:

1.   In the studio, in the left pane, select **Compute**.
2.   At the top of the page, select **Compute instances**.
3.   In the list, select the compute instance.
4.   At the top of the page, select **Stop**.

Important

The resources that you created can be used as prerequisites to other Azure Machine Learning tutorials and how-to articles.

If you don't plan to use any of the resources that you created, delete them so you don't incur any charges:

1.   In the Azure portal, in the search box, enter _Resource groups_ and select it from the results.

2.   From the list, select the resource group that you created.

3.   In the **Overview** page, select **Delete resource group**.

![Image 9: Screenshot of the selections to delete a resource group in the Azure portal.](https://learn.microsoft.com/en-us/azure/machine-learning/includes/media/aml-delete-resource-group/delete-resources.png?view=azureml-api-2)

4.   Enter the resource group name. Then select **Delete**.

See these resources to learn more:

*   [Artifacts and models in MLflow](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow-models?view=azureml-api-2)
*   [Using Git with Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration?view=azureml-api-2)
*   [Running Jupyter notebooks in your workspace](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2)
*   [Working with a compute instance terminal in your workspace](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-access-terminal?view=azureml-api-2)
*   [Manage notebook and terminal sessions](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-compute-sessions?view=azureml-api-2)

This tutorial shows the early steps of creating a model, prototyping on the same machine where the code resides. For your production training, learn how to use that training script on more powerful remote compute resources:
