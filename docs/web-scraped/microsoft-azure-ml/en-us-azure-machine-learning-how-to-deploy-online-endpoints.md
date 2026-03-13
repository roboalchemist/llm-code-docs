# Source: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2

Title: Deploy Machine Learning Models to Online Endpoints - Azure Machine Learning

URL Source: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2

Markdown Content:
**APPLIES TO:**![Image 1](https://learn.microsoft.com/en-us/azure/machine-learning/media/yes.png?view=azureml-api-2)[Azure CLI ml extension v2 (current)](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2)![Image 2](https://learn.microsoft.com/en-us/azure/machine-learning/media/yes.png?view=azureml-api-2)[Python SDK azure-ai-ml v2 (current)](https://aka.ms/sdk-v2-install)

In this article, you learn to deploy your model to an online endpoint for use in real-time inferencing. You begin by deploying a model on your local machine to debug any errors. Then, you deploy and test the model in Azure, view the deployment logs, and monitor the service-level agreement (SLA). By the end of this article, you have a scalable HTTPS/REST endpoint that you can use for real-time inference.

Online endpoints are endpoints that are used for real-time inferencing. There are two types of online endpoints: managed online endpoints and Kubernetes online endpoints. For more information about the differences, see [Managed online endpoints vs. Kubernetes online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2#managed-online-endpoints-vs-kubernetes-online-endpoints).

Managed online endpoints help to deploy your machine learning models in a turnkey manner. Managed online endpoints work with powerful CPU and GPU machines in Azure in a scalable, fully managed way. Managed online endpoints take care of serving, scaling, securing, and monitoring your models. This assistance frees you from the overhead of setting up and managing the underlying infrastructure.

The main example in this article uses managed online endpoints for deployment. To use Kubernetes instead, see the notes in this document that are inline with the managed online endpoint discussion.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_1_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_1_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_1_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_1_arm)

**APPLIES TO:**![Image 3](https://learn.microsoft.com/en-us/azure/machine-learning/media/yes.png?view=azureml-api-2)[Azure CLI ml extension **v2 (current)**](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2)

*   The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) and the `ml` extension to the Azure CLI, installed and configured. For more information, see [Install and set up the CLI (v2)](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2).

*   A Bash shell or a compatible shell, for example, a shell on a Linux system or [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/about). The Azure CLI examples in this article assume that you use this type of shell.

*   An Azure Machine Learning workspace. For instructions to create a workspace, see [Set up](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2#set-up).

*   Azure role-based access control (Azure RBAC) is used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the Owner or Contributor role for the Azure Machine Learning workspace, or a custom role must allow `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. If you use Azure Machine Learning studio to create and manage online endpoints or deployments, you need the extra permission `Microsoft.Resources/deployments/write` from the resource group owner. For more information, see [Manage access to Azure Machine Learning workspaces](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles?view=azureml-api-2).

*   (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We _highly recommend_ this option, which makes it easier to debug issues.

*   Ensure that you have enough virtual machine (VM) quota allocated for deployment. Azure Machine Learning reserves 20% of your compute resources for performing upgrades on some VM versions. For example, if you request 10 instances in a deployment, you must have a quota of 12 for each number of cores for the VM version. Failure to account for the extra compute resources results in an error. Some VM versions are exempt from the extra quota reservation. For more information on quota allocation, see [Virtual machine quota allocation for deployment](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2#virtual-machine-quota-allocation-for-deployment).

*   Alternatively, you could use quota from the Azure Machine Learning shared quota pool for a limited time. Azure Machine Learning provides a shared quota pool from which users across various regions can access quota to perform testing for a limited time, depending upon availability. When you use the studio to deploy Llama-2, Phi, Nemotron, Mistral, Dolly, and Deci-DeciLM models from the model catalog to a managed online endpoint, Azure Machine Learning allows you to access its shared quota pool for a short time so that you can perform testing. For more information on the shared quota pool, see [Azure Machine Learning shared quota](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2#azure-machine-learning-shared-quota).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_2_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_2_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_2_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_2_arm)

If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

```
az account set --subscription <subscription ID>
az configure --defaults workspace=<Azure Machine Learning workspace name> group=<resource group>
```

To follow along with this article, first clone the [azureml-examples repository](https://github.com/azure/azureml-examples), and then change into the repository's _azureml-examples/cli_ directory:

```
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples/cli
```

Use `--depth 1` to clone only the latest commit to the repository, which reduces the time to complete the operation.

The commands in this tutorial are in the files _deploy-local-endpoint.sh_ and _deploy-managed-online-endpoint.sh_ in the _cli_ directory. The YAML configuration files are in the _endpoints/online/managed/sample/_ subdirectory.

Note

The YAML configuration files for Kubernetes online endpoints are in the _endpoints/online/kubernetes/_ subdirectory.

To define an online endpoint, specify the endpoint name and authentication mode. For more information on managed online endpoints, see [Online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2#online-endpoints).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_3_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_3_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_3_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_3_arm)

To set your endpoint name, run the following command. Replace `<YOUR_ENDPOINT_NAME>` with a name that's unique in the Azure region. For more information on the naming rules, see [Endpoint limits](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2#azure-machine-learning-online-endpoints-and-batch-endpoints).

```
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
```

The following snippet shows the _endpoints/online/managed/sample/endpoint.yml_ file:

```
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-endpoint
auth_mode: key
```

The reference for the endpoint YAML format is described in the following table. To learn how to specify these attributes, see the [online endpoint YAML reference](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-endpoint-online?view=azureml-api-2). For information about limits related to managed endpoints, see [Azure Machine Learning online endpoints and batch endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas?view=azureml-api-2#azure-machine-learning-online-endpoints-and-batch-endpoints).

| Key | Description |
| --- | --- |
| `$schema` | (Optional) The YAML schema. To see all available options in the YAML file, you can view the schema in the preceding code snippet in a browser. |
| `name` | The name of the endpoint. |
| `auth_mode` | Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. Use `aad_token` for Microsoft Entra token-based authentication (preview). For more information on authenticating, see [Authenticate clients for online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-online-endpoint?view=azureml-api-2). |

A deployment is a set of resources required for hosting the model that does the actual inferencing. For this example, you deploy a `scikit-learn` model that does regression and use a scoring script _score.py_ to run the model on a specific input request.

To learn about the key attributes of a deployment, see [Online deployments](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2#online-deployments).

Your deployment configuration uses the location of the model that you want to deploy.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_4_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_4_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_4_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_4_arm)

The following snippet shows the _endpoints/online/managed/sample/blue-deployment.yml_ file, with all the required inputs to configure a deployment:

```
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
endpoint_name: my-endpoint
model:
  path: ../../model-1/model/
code_configuration:
  code: ../../model-1/onlinescoring/
  scoring_script: score.py
environment: 
  conda_file: ../../model-1/environment/conda.yaml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu22.04:latest
instance_type: Standard_DS3_v2
instance_count: 1
```

The _blue-deployment.yml_ file specifies the following deployment attributes:

*   `model`: Specifies the model properties inline by using the `path` parameter (where to upload files from). The CLI automatically uploads the model files and registers the model with an autogenerated name.
*   `environment`: Uses inline definitions that include where to upload files from. The CLI automatically uploads the _conda.yaml_ file and registers the environment. Later, to build the environment, the deployment uses the `image` parameter for the base image. In this example, it's `mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest`. The `conda_file` dependencies are installed on top of the base image.
*   `code_configuration`: Uploads the local files, such as the Python source for the scoring model, from the development environment during deployment.

For more information about the YAML schema, see the [online endpoint YAML reference](https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-endpoint-online?view=azureml-api-2).

Note

To use Kubernetes endpoints instead of managed online endpoints as a compute target:

1.   Create and attach your Kubernetes cluster as a compute target to your Azure Machine Learning workspace by using [Azure Machine Learning studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-attach-kubernetes-to-workspace?view=azureml-api-2).
2.   Use the [endpoint YAML](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/kubernetes/kubernetes-endpoint.yml) to target Kubernetes instead of the managed endpoint YAML. You need to edit the YAML to change the value of `compute` to the name of your registered compute target. You can use this [deployment.yaml](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/kubernetes/kubernetes-blue-deployment.yml) that has other properties that apply to a Kubernetes deployment.

All the commands that are used in this article for managed online endpoints also apply to Kubernetes endpoints, except for the following capabilities that don't apply to Kubernetes endpoints:

*   The optional [SLA monitoring and Azure Log Analytics integration by using Azure Monitor](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#optional-monitor-sla-by-using-azure-monitor).
*   Use of Microsoft Entra tokens.
*   Autoscaling as described in the optional [Configure autoscaling](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#optional-configure-autoscaling) section.

The format of the scoring script for online endpoints is the same format that's used in the preceding version of the CLI and in the Python SDK.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_5_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_5_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_5_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_5_arm)

The scoring script specified in `code_configuration.scoring_script` must have an `init()` function and a `run()` function.

This example uses the [score.py file](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/model-1/onlinescoring/score.py) from the repo that you cloned or downloaded earlier:

```
import os
import logging
import json
import numpy
import joblib

def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # Please provide your model's folder name if there is one
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "model/sklearn_regression_model.pkl"
    )
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)
    logging.info("Init complete")

def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    logging.info("model 1: request received")
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    result = model.predict(data)
    logging.info("Request processed")
    return result.tolist()
```

The `init()` function is called when the container is initialized or started. Initialization typically occurs shortly after the deployment is created or updated. The `init` function is the place to write logic for global initialization operations like caching the model in memory (as shown in this _score.py_ file).

The `run()` function is called every time the endpoint is invoked. It does the actual scoring and prediction. In this _score.py_ file, the `run()` function extracts data from a JSON input, calls the scikit-learn model's `predict()` method, and then returns the prediction result.

We _highly recommend_ that you test run your endpoint locally to validate and debug your code and configuration before you deploy to Azure. The Azure CLI and Python SDK support local endpoints and deployments, but Azure Machine Learning studio and ARM templates don't.

To deploy locally, [Docker Engine](https://docs.docker.com/engine/install/) must be installed and running. Docker Engine typically starts when the computer starts. If it doesn't, you can [troubleshoot Docker Engine](https://docs.docker.com/config/daemon/#start-the-daemon-manually).

You can use the [Azure Machine Learning inference HTTP server Python package](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-inference-server-http?view=azureml-api-2) to debug your scoring script locally _without Docker Engine_. Debugging with the inference server helps you to debug the scoring script before you deploy to local endpoints so that you can debug without being affected by the deployment container configurations.

For more information on debugging online endpoints locally before you deploy to Azure, see [Online endpoint debugging](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2#online-endpoint-debugging).

First, create an endpoint. Optionally, for a local endpoint, you can skip this step. You can create the deployment directly (next step), which in turn creates the required metadata. Deploying models locally is useful for development and testing purposes.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_6_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_6_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_6_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_6_arm)

```
az ml online-endpoint create --local -n $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
```

Now, create a deployment named `blue` under the endpoint.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_7_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_7_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_7_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_7_arm)

```
az ml online-deployment create --local -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml
```

The `--local` flag directs the CLI to deploy the endpoint in the Docker environment.

Check the deployment status to see whether the model was deployed without error:

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_8_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_8_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_8_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_8_arm)

```
az ml online-endpoint show -n $ENDPOINT_NAME --local
```

The output should appear similar to the following JSON. The `provisioning_state` parameter is `Succeeded`.

```
{
  "auth_mode": "key",
  "location": "local",
  "name": "docs-endpoint",
  "properties": {},
  "provisioning_state": "Succeeded",
  "scoring_uri": "http://localhost:49158/score",
  "tags": {},
  "traffic": {}
}
```

The following table contains the possible values for `provisioning_state`:

| Value | Description |
| --- | --- |
| `Creating` | The resource is being created. |
| `Updating` | The resource is being updated. |
| `Deleting` | The resource is being deleted. |
| `Succeeded` | The create or update operation succeeded. |
| `Failed` | The create, update, or delete operation failed. |

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_9_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_9_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_9_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_9_arm)

Invoke the endpoint to score the model by using the `invoke` command and passing query parameters that are stored in a JSON file:

```
az ml online-endpoint invoke --local --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
```

If you want to use a REST client (like curl), you must have the scoring URI. To get the scoring URI, run `az ml online-endpoint show --local -n $ENDPOINT_NAME`. In the returned data, find the `scoring_uri` attribute.

In the example _score.py_ file, the `run()` method logs some output to the console.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_10_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_10_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_10_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_10_arm)

You can view this output by using the `get-logs` command:

```
az ml online-deployment get-logs --local -n blue --endpoint $ENDPOINT_NAME
```

Next, deploy your online endpoint to Azure. As a best practice for production, we recommend that you register the model and environment that you use in your deployment.

We recommend that you register your model and environment before deployment to Azure so that you can specify their registered names and versions during deployment. After you register your assets, you can reuse them without the need to upload them every time you create deployments. This practice increases reproducibility and traceability.

Unlike deployment to Azure, local deployment doesn't support using registered models and environments. Instead, local deployment uses local model files and uses environments with local files only.

For deployment to Azure, you can use either local or registered assets (models and environments). In this section of the article, the deployment to Azure uses registered assets, but you have the option of using local assets instead. For an example of a deployment configuration that uploads local files to use for local deployment, see [Configure a deployment](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#configure-a-deployment).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_11_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_11_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_11_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_11_arm)

To register the model and environment, use the form `model: azureml:my-model:1` or `environment: azureml:my-env:1`.

For registration, you can extract the YAML definitions of `model` and `environment` into separate YAML files in the _endpoints/online/managed/sample_ folder, and use the commands `az ml model create` and `az ml environment create`. To learn more about these commands, run `az ml model create -h` and `az ml environment create -h`.

1.   Create a YAML definition for the model. Name the file _model.yml_:

```
$schema: https://azuremlschemas.azureedge.net/latest/model.schema.json
name: my-model
path: ../../model-1/model/
```
2.   Register the model:

```
az ml model create -n my-model -v 1 -f endpoints/online/managed/sample/model.yml
```
3.   Create a YAML definition for the environment. Name the file _environment.yml_:

```
$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
name: my-env
image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
conda_file: ../../model-1/environment/conda.yaml
```
4.   Register the environment:

```
az ml environment create -n my-env -v 1 -f endpoints/online/managed/sample/environment.yml
```

For more information on how to register your model as an asset, see [Register a model by using the Azure CLI or Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-models?view=azureml-api-2#register-your-model-as-an-asset-in-machine-learning-by-using-the-cli). For more information on creating an environment, see [Create a custom environment](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2#create-a-custom-environment).

Important

When you define a custom environment for your deployment, ensure that the `azureml-inference-server-http` package is included in the conda file. This package is essential for the inference server to function properly. If you're unfamiliar with how to create your own custom environment, use one of our curated environments such as `minimal-py-inference` (for custom models that don't use `mlflow`) or `mlflow-py-inference` (for models that use `mlflow`). You can find these curated environments on the **Environments** tab of your instance of Azure Machine Learning studio.

Your deployment configuration uses the registered model that you want to deploy and your registered environment.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_12_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_12_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_12_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_12_arm)

Use the registered assets (model and environment) in your deployment definition. The following snippet shows the _endpoints/online/managed/sample/blue-deployment-with-registered-assets.yml_ file, with all the required inputs to configure a deployment:

```
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
endpoint_name: my-endpoint
model: azureml:my-model:1
code_configuration:
  code: ../../model-1/onlinescoring/
  scoring_script: score.py
environment: azureml:my-env:1
instance_type: Standard_DS3_v2
instance_count: 1
```

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_13_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_13_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_13_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_13_arm)

You can specify the CPU or GPU instance types and images in your deployment definition for both local deployment and deployment to Azure.

Your deployment definition in the _blue-deployment-with-registered-assets.yml_ file used a general-purpose type `Standard_DS3_v2` instance and the non-GPU Docker image `mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest`. For GPU compute, choose a GPU compute type version and a GPU Docker image.

For supported general-purpose and GPU instance types, see [Managed online endpoints SKU list](https://learn.microsoft.com/en-us/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list?view=azureml-api-2). For a list of Azure Machine Learning CPU and GPU base images, see [Azure Machine Learning base images](https://github.com/Azure/AzureML-Containers).

Next, deploy your online endpoint to Azure.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_14_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_14_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_14_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_14_arm)

1.   Create the endpoint in the Azure cloud:

```
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
```
2.   Create the deployment named `blue` under the endpoint:

```
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment-with-registered-assets.yml --all-traffic
```

The deployment creation can take up to 15 minutes, depending on whether the underlying environment or image is being built for the first time. Subsequent deployments that use the same environment are processed faster.

If you prefer not to block your CLI console, you can add the flag `--no-wait` to the command. However, this option stops the interactive display of the deployment status.

The `--all-traffic` flag in the code `az ml online-deployment create` that's used to create the deployment allocates 100% of the endpoint traffic to the newly created blue deployment. Using this flag is helpful for development and testing purposes, but for production, you might want to route traffic to the new deployment through an explicit command. For example, use `az ml online-endpoint update -n $ENDPOINT_NAME --traffic "blue=100"`.

To debug errors in your deployment, see [Troubleshooting online endpoint deployments](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-online-endpoints?view=azureml-api-2).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_15_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_15_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_15_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_15_arm)

1.   Use the `show` command to display information in the `provisioning_state` for the endpoint and deployment:

```
az ml online-endpoint show -n $ENDPOINT_NAME
```
2.   List all the endpoints in the workspace in a table format by using the `list` command:

```
az ml online-endpoint list --output table
```

Check the logs to see whether the model was deployed without error.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_16_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_16_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_16_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_16_arm)

To see log output from a container, use the following CLI command:

```
az ml online-deployment get-logs --name blue --endpoint $ENDPOINT_NAME
```

By default, logs are pulled from the inference server container. To see logs from the storage initializer container, add the `--container storage-initializer` flag. For more information on deployment logs, see [Get container logs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-online-endpoints?view=azureml-api-2#get-container-logs).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_17_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_17_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_17_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_17_arm)

1.   Use either the `invoke` command or a REST client of your choice to invoke the endpoint and score some data:

```
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
```
2.   Get the key used to authenticate to the endpoint:

You can control which Microsoft Entra security principals can get the authentication key by assigning them to a custom role that allows `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/token/action` and `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/listkeys/action`. For more information on how to manage authorization to workspaces, see [Manage access to an Azure Machine Learning workspace](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-assign-roles?view=azureml-api-2).

```
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME -o tsv --query primaryKey)
```
3.   Use curl to score data.

```
SCORING_URI=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query scoring_uri)

curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --data @endpoints/online/model-1/sample-request.json
```

Notice that you use `show` and `get-credentials` commands to get the authentication credentials. Also notice that you use the `--query` flag to filter only the attributes that are needed. To learn more about the `--query` flag, see [Query Azure CLI command output](https://learn.microsoft.com/en-us/cli/azure/query-azure-cli).

4.   To see the invocation logs, run `get-logs` again.

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_18_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_18_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_18_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_18_arm)

If you want to update the code, model, or environment, update the YAML file. Then run the `az ml online-endpoint update` command.

If you update instance count (to scale your deployment) along with other model settings (such as code, model, or environment) in a single `update` command, the scaling operation is performed first. The other updates are applied next. It's a good practice to perform these operations separately in a production environment.

To understand how `update` works:

1.   Open the file _online/model-1/onlinescoring/score.py_.

2.   Change the last line of the `init()` function: After `logging.info("Init complete")`, add `logging.info("Updated successfully")`.

3.   Save the file.

4.   Run this command:

```
az ml online-deployment update -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment-with-registered-assets.yml
```

Updating by using YAML is declarative. That is, changes in the YAML are reflected in the underlying Resource Manager resources (endpoints and deployments). A declarative approach facilitates [GitOps](https://www.atlassian.com/git/tutorials/gitops): _All_ changes to endpoints and deployments (even `instance_count`) go through the YAML.

You can use [generic update parameters](https://learn.microsoft.com/en-us/cli/azure/use-cli-effectively#generic-update-parameters), such as the `--set` parameter, with the CLI `update` command to override attributes in your YAML _or_ to set specific attributes without passing them in the YAML file. Using `--set` for single attributes is especially valuable in development and test scenarios. For example, to scale up the `instance_count` value for the first deployment, you could use the `--set instance_count=2` flag. However, because the YAML isn't updated, this technique doesn't facilitate [GitOps](https://www.atlassian.com/git/tutorials/gitops).

Specifying the YAML file _isn't_ mandatory. For example, if you wanted to test different concurrency settings for a specific deployment, you can try something like `az ml online-deployment update -n blue -e my-endpoint --set request_settings.max_concurrent_requests_per_instance=4 environment_variables.WORKER_COUNT=4`. This approach keeps all the existing configuration but updates only the specified parameters.

5.   Because you modified the `init()` function, which runs when the endpoint is created or updated, the message `Updated successfully` appears in the logs. Retrieve the logs by running:

```
az ml online-deployment get-logs --name blue --endpoint $ENDPOINT_NAME
```

The `update` command also works with local deployments. Use the same `az ml online-deployment update` command with the `--local` flag.

Note

The update to the deployment in this section is an example of an in-place rolling update.

*   For a managed online endpoint, the deployment is updated to the new configuration with 20% of the nodes at a time. That is, if the deployment has 10 nodes, 2 nodes at a time are updated.
*   For a Kubernetes online endpoint, the system iteratively creates a new deployment instance with the new configuration and deletes the old one.
*   For production usage, consider [blue-green deployment](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-safely-rollout-online-endpoints?view=azureml-api-2), which offers a safer alternative for updating a web service.

Autoscale automatically runs the right amount of resources to handle the load on your application. Managed online endpoints support autoscaling through integration with the Azure Monitor autoscale feature. To configure autoscaling, see [Autoscale online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-autoscale-endpoints?view=azureml-api-2).

To view metrics and set alerts based on your SLA, follow the steps that are described in [Monitor online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-monitor-online-endpoints?view=azureml-api-2).

The `get-logs` command for the CLI or the `get_logs` method for the SDK provides only the last few hundred lines of logs from an automatically selected instance. However, Log Analytics provides a way to durably store and analyze logs. For more information on how to use logging, see [Use logs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-monitor-online-endpoints?view=azureml-api-2#use-logs).

*   [Azure CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_19_cli)
*   [Python SDK](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_19_python)
*   [Studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_19_azure-studio)
*   [ARM template](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2#tabpanel_19_arm)

Use the following command to delete the endpoint and all its underlying deployments:

```
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
```

*   [Perform safe rollout of new deployments for real-time inference](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-safely-rollout-online-endpoints?view=azureml-api-2)
*   [Deploy models with REST](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-with-rest?view=azureml-api-2)
*   [Autoscale online endpoints in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-autoscale-endpoints?view=azureml-api-2)
*   [Monitor online endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-monitor-online-endpoints?view=azureml-api-2)
