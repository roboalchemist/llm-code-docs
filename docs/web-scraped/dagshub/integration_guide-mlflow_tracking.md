# Source: https://dagshub.com/docs/integration_guide/mlflow_tracking/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/mlflow_tracking.md "Edit this page")

# MLflow Tracking[¶](#mlflow-tracking "Permanent link")

[MLflow](https://mlflow.org/) is an open-source tool to manage the machine learning lifecycle. It supports live logging of parameters, metrics, metadata, and artifacts when running a machine learning experiment. To manage the post training stage, it provides a model registry with deployment functionality to custom serving tools.

DagsHub provides a free hosted MLflow server with team-based access control for every repository. You can log experiments with MLflow to it, view its information under the [experiment tab](../../feature_guide/experiment_tracking/), and manage your trained models from the full-fledged MLflow UI built into your DagsHub project.

# An error occurred. 

Unable to execute JavaScript.

## How does the integration of DagsHub with MLflow work?[¶](#how-does-the-integration-of-dagshub-with-mlflow-work "Permanent link")

When you create a repository on DagsHub, a remote MLflow server is automatically created and configured with the project. The repository\'s MLflow tracking server will be located at:

    https://dagshub.com/<DagsHub-user-name>/<repository-name>.mlflow

The server endpoint can also be found under the â€˜Remoteâ€™ button:

[![MLflow Experiments](../assets/mlflow/remote-mlflow-zoom-in.png)](../assets/mlflow/remote-mlflow-zoom-in.png)

~MLflow\ remote~

Team based access control

- Only a repository contributor can log experiments and access the DagsHub MLflow UI.

## How to set DagsHub as the remote MLflow server?[¶](#how-to-set-dagshub-as-the-remote-mlflow-server "Permanent link")

### 1. Install and import MLflow[¶](#1-install-and-import-mlflow "Permanent link") 

- Start by installing the [MLflow python package](https://pypi.org/project/mlflow/) in your virtual environment using pip:

  ::::: 
  ::: tabbed-labels
  Mac, Linux, Windows
  :::

  ::: tabbed-content
  :::
  :::::

- Then, you will import MLflow to our python module using `import mlflow` and log the information with [MLflow logging functions](https://www.mlflow.org/docs/latest/tracking.html#logging-functions). .

### 2. Set DagsHub as the remote URI[¶](#2-set-dagshub-as-the-remote-uri "Permanent link") 

You can set the MLflow server URI by adding the following line to our code:

    mlflow.set_tracking_uri('https://dagshub.com/<DagsHub-user-name>/<repository-name>.mlflow')

Set the MLflow server URI using an environment variable

You can also define your MLflow server URI using the `MLFLOW_TRACKING_URI` environment variable.

**We don\'t recommend this approach**, since you might forget to reset the environment variable when switching between different projects. This might result in logging experiments to the wrong repository.

If you still prefer using the environment variable, we recommend setting it only for the current command, like the following:

Mac, Linux, Windows

### 3. Set-up your credentials[¶](#3-set-up-your-credentials "Permanent link") 

The DagsHub MLflow server has built-in access controls. Only a repository contributor can log experiments (someone who can `git push` to the repository).

- In order to use basic authentication with MLflow, you need to set the following environment variables:

  - `MLFLOW_TRACKING_USERNAME` - DagsHub username
  - `MLFLOW_TRACKING_PASSWORD` - DagsHub password or preferably an [access token](https://dagshub.com/user/settings/tokens)

You can set these by typing in the terminal:

Mac, Linux, Windows

You can also use [your token](https://dagshub.com/user/settings/tokens) as username; in this case the password is not needed:

Mac, Linux, Windows

**Congratulations**, you are ready to start logging experiments. Now, when you run your code, you will see new runs appear in the experiment tables, with their status and origin:

[![MLflow Experiments](../assets/mlflow/mlflow_experiment_table.png)](../assets/mlflow/mlflow_experiment_table.png)

## How to log models and artifacts to DagsHub?[¶](#how-to-log-models-and-artifacts-to-dagshub "Permanent link")

Info

MLflow experiments created before August 10th 2022 won\'t be affected by that change. This means **you cannot log artifacts using this technique for your existing Default MLflow experiment**. If you already have a repository with MLflow runs, the recommended way to start using the proxy artifacts is by creating a new experiment through the MLflow [CLI](https://www.mlflow.org/docs/latest/cli.html#mlflow-experiments-create), the [Python client](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.create_experiment), or the MLflow UI.

### Option 1: Use DagsHub Storage[¶](#option-1-use-dagshub-storage "Permanent link")

DagsHub\'s MLflow integration supports directly logging artifacts through the tracking server. In the past the MLflow tracking server used to manage the location of artifacts and models, but uploading and downloading was done using the client\'s local credentials and available packages (i.e `boto3` or `google-cloud-storage`). Support for proxying upload and download requests through the tracking server was added in MLflow 1.24.0.

DagsHub lets you leverage this capability by directly hosting your artifacts by default. For every newly created repository or MLflow experiment, DagsHub will generate a dedicated artifact location similar to `mlflow-artifacts:/<UUID>`.

### Option 2: Use external buckets[¶](#option-2-use-external-buckets "Permanent link")

DagsHub\'s tracking server allows you to specify AWS S3 buckets for storing artifacts for newly created MLflow experiments. In order to configure this, you must create a new experiment and provide an `s3://` URI as the artifact store. You can either do this by clicking the \"Create Experiment (`+`)\" button in the DagsHub MLflow UI, and entering the artifact location in the dialog box, or running the following python code.

[![Create MLflow Experiment dialog](../assets/mlflow/create_experiment_dialog.png)](../assets/mlflow/create_experiment_dialog.png)

#### Set up MLflow[¶](#set-up-mlflow "Permanent link")

    import mlflow
    artifact_location = f"s3:///mlruns"
    mlflow.create_experiment("Deploy", artifact_location)

Once the experiment is created, you must tell your code to select it over the default experiment. You can do this either by setting the environment variable

    export MLFLOW_EXPERIMENT_NAME=Deploy

or adding this line of python code to your training code:

    mlflow.set_experiment(experiment_name="Deploy")

#### Set up AWS[¶](#set-up-aws "Permanent link")

Before logging models or other artifacts to MLflow, you will need to download the `boto3` package to allow MLflow to interact with the AWS S3 API.

Mac, Linux, Windows

You\'ll also need to ensure that your code has the required permissions to upload files to AWS S3. Obtain an AWS Access Token (consisting of a pair of an Access Key ID and a Secret Access Key), then either set them as the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables, or run the `aws configure` command to save them on the filesystem.

Securely providing AWS credentials

If you don\'t want to give your code permanent AWS credentials, you could make use of [aws-vault](https://github.com/99designs/aws-vault) to provide time-limited temporary tokens instead.

Doing all this will allow you to call [`mlflow.log_artifact()`](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_artifact) or [`mlflow.autolog(log_models=True)`](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) to instruct MLflow to upload models or other artifacts to the artifact store and note their locations on the tracking server.

## How to launch the DagsHub MLflow UI[¶](#how-to-launch-the-dagshub-mlflow-ui "Permanent link")

The DagsHub MLflow tracking server provides access to the MLflow server user interface (MLflow UI). To view the MLflow UI, visit the tracking server URI (`https://dagshub.com/<username>/<repo>.mlflow`) in a browser. If you haven\'t interacted with the main DagsHub interface in a while, you may have to enter your DagsHub username and password/[access token](https://dagshub.com/user/settings/tokens) in to the authentication popup shown by your browser.

You should have full access to all views and actions provided by the MLflow UI. This includes viewing run details, comparing runs (within the same experiment only, to compare runs across experiments, visit the DagsHub experiment tracking interface), creating and managing experiments, and viewing and updating the model registry.

\

~launch\ the\ DagsHub\ MLflow\ UI~

\

## How to deploy an MLflow model using DagsHub?[¶](#how-to-deploy-an-mlflow-model-using-dagshub "Permanent link")

DagsHub\'s MLflow integration includes support for logged artifacts and the MLflow model registry. With this, you can use MLflow to deploy your trained models as batteries-included inference servers to the cloud with ease.

### How to register MLflow model in DagsHub Model Registry?[¶](#how-to-register-mlflow-model-in-dagshub-model-registry "Permanent link")

Once you have logged a model as part of an MLflow run, you can save that model to the Model Registry for your repository. You run the following python code to do so:

    import mlflow
    run_id = '<run-id-here>'
    artifact_name = 'model'
    model_name = '<name-of-model-in-model-registry>'
    mlflow.register_model(f'runs://', model_name)

### How to deploy an MLflow model from DagsHub Model Registry?[¶](#how-to-deploy-an-mlflow-model-from-dagshub-model-registry "Permanent link")

Once the model is registered as a part of the DagsHub Model Registry, you can make use of standard MLflow tooling to deploy the model as a container, on AWS SageMaker, Azure ML, Apache Spark UDF, or any other platform.

Simply follow [the instructions provided by MLflow](https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools) to do so.

#### Process to deploy an MLflow model to Amazon AWS SageMaker[¶](#process-to-deploy-an-mlflow-model-to-amazon-aws-sagemaker "Permanent link")

    mlflow sagemaker build-and-push-container
    mlflow sagemaker deploy \
        -m "models:/<name-of-model-in-model-registry>/latest" \
        -a <sagemaker-deployment-name> \
        --region-name <aws-region> \
        -e <sagemaker-role-arn> \
        --mode replace

#### Process to build a Docker container image from an MLflow model[¶](#process-to-build-a-docker-container-image-from-an-mlflow-model "Permanent link")

    mlflow models build-docker \
        -m "models:/<name-of-model-in-model-registry>/latest" \
        -n <name-of-docker-image> \
        --enable-mlserver

To run inference server locally:

    docker run -p 80:8080 <name-of-docker-image>

#### Process to deploy an MLflow model to Microsoft Azure ML[¶](#process-to-deploy-an-mlflow-model-to-microsoft-azure-ml "Permanent link")

    mlflow deployments create \
        --name <azureml-deployment-name> \
        -m "models:/<name-of-model-in-model-registry>/latest" \
        -t <azureml-mlflow-tracking-url> \
        --deploy-config-file <(echo '')

## How To Use MLflow In A Colab Environment?[¶](#how-to-use-mlflow-in-a-colab-environment "Permanent link")

We shared two examples of experiment logging to DagsHubâ€™s MLflow server in a Colab environment.

- [Using MLflow with Tensorflow](https://colab.research.google.com/drive/1TrN7YEgiIzt7EelvshJPx2n4j-Qa6LBf?usp=sharing)
- [Using MLflow with fast.ai](https://colab.research.google.com/drive/1DhHzI5blVbniFwx98EKXYSi0z_Icm07t?usp=sharing)

## How to import MLflow local objects to DagsHub MLflow remote?[¶](#how-to-import-mlflow-local-objects-to-dagshub-mlflow-remote "Permanent link")

Generally, you can use [`mlflow-export-import`](https://github.com/mlflow/mlflow-export-import) to export MLflow experiments, runs and models from one server to another.

The following example demonstrates how to bulk export all objects that are created locally, then bulk import to DagsHub remote tracking server.

### 1. Install `mlflow-export-import`[¶](#1-install-mlflow-export-import "Permanent link") 

- In the same environment that you originally install `mlflow`, you can install `mlflow-export-import` with:

  ::: highlight
      pip install mlflow-export-import
  :::

- If you need to install the latest version from Github source, do this instead:

  ::: highlight
      pip install git+https://github.com/mlflow/mlflow-export-import
  :::

### 2. Export all local objects[¶](#2-export-all-local-objects "Permanent link") 

- In one terminal, start the local `mlflow` server, for example with:

  ::: highlight
      mlflow server --host 0.0.0.0 --port 8888
  :::

- In **another** terminal, in the same virtual environment, export all objects to a folder called `mlflow-export` with:

  ::: highlight
      # note: the port needs to be same one that you request in the other terminal
      MLFLOW_TRACKING_URI=http://localhost:8888 \
          export-all --output-dir mlflow-export
  :::

- If succeeded, you should see a report saying so, for example

  ::: highlight
      3 experiments exported
      37/37 runs succesfully exported
      Duration for experiments export: 10.6 seconds
      Duration for entire tracking server export: 10.8 seconds
  :::

- At this point, you can stop the local server in the first terminal.

### 3. Import to DagsHub server[¶](#3-import-to-dagshub-server "Permanent link") 

- Find your DagsHub repository\'s MLflow remote variables, for example by going through the `Remote` button in your repository, then click on the `Experiments` tab.

- Do the following in terminal:

  ::: highlight
      MLFLOW_TRACKING_URI=https://dagshub.com/<USER>/<REPO>.mlflow \
      MLFLOW_TRACKING_USERNAME=<USER> \
      MLFLOW_TRACKING_PASSWORD=<PASSWORD_OR_TOKEN> \
          import-all --input-dir mlflow-export
  :::

- If successful, you can launch the local server again, and visit `https://dagshub.com/<USER>/<REPO>.mlflow` to inspect if there are any discrepancies between the logged data, artifacts, models, runs, experiments. For example, see if there\'s anything missing.

### Importing issues & workarounds[¶](#importing-issues-workarounds "Permanent link")

There may be some issues with in **Step 3** with importing. Below are some potential workarounds to try, essentially by editing the package source codes after installation.

Warning

- These workarounds are used with `mlflow-export-import 1.2.0`. In the future, these may be patched.
- These workarounds may work for only certain cases and issues.
- You should backup `mlflow-export` directory just in case.
- Always try to compare the local server and DagsHub remote tracking server after every `import-all` step to ensure they are the same.

- First, find the source code directory by inspecting at the `Location` field when doing `pip show`, for example:

  ::: highlight
      pip show mlflow-export-import
      ...
      Location: .venv/lib/python3.10/site-packages/mlflow_export_import
      ...
  :::

  Alternative to editing in `site-packages`

  The alternative to editing source codes in `site-packages` is using editable installation with `mlflow-export-import`.

  ::: highlight
      # clone the repository
      git clone https://github.com/mlflow/mlflow-export-import

      # install in editable mode
      pip install -e ./mlflow-export-import/
  :::

  Then you can edit files in the local `mlflow-export-import/mlflow_export_import` directory instead of your environment\'s `site-packages` directory.

- If you see `` in the outputs of `import-all`, comment out/delete the following lines in `common/mlflow_utils.py` file, under `set_experiment` function

  ::: highlight
      if ex.error_code != "RESOURCE_ALREADY_EXISTS":
          raise MlflowExportImportException(ex, f"Cannot create experiment ''")
  :::

- Re-run **Step 3** with the same `import-all` command again.

- If you still encounter issues, it could be because your local experiments did not log any data inputs. If none of your experiments did, attempt to comment out/delete the following line in `run/import_run.py` source file, under `import_run` function, inside the `try` block

  ::: highlight
      _import_inputs(http_client, src_run_dct, run_id)
  :::

  ::: 
  Warning

  Please note that this workaround assumes **none** of your experiments or runs log any inputs.

  If there are some that do and some that do not, you will need to modify the logic of `_import_inputs` and/or the code surround this line to accommodate that.
  :::

- Re-run **Step 3** with the same `import-all` command again.

If there are still issues or there are discrepancies between the local server and the remote DagsHub server, please open a ticket on DagsHub and/or `mlflow-export-import` Github repository.

## Known Issues, Limitations & Restrictions[¶](#known-issues-limitations-restrictions "Permanent link")

The MLflow UI provided by DagsHub currently doesn\'t support displaying artifacts pushed to an external storage like S3. Please, contact us in our [Discord channel](https://discord.com/channels/698874030052212737/737944278692790343) if you find it important.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).