# Source: https://dagshub.com/docs/troubleshooting/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/troubleshooting.md "Edit this page")

# Troubleshooting[¶](#troubleshooting "Permanent link")

Here you can find information about common problems users encounter and how to solve them. If you can\'t find your problem here, reach out to us on our [Discord Channel](https://discord.gg/CCDmPf9ujb) and let us know.

## General[¶](#general "Permanent link")

### Unauthorized to push files to DagsHub[¶](#unauthorized-to-push-files-to-dagshub "Permanent link")

Users might get an error when trying to push files to DagsHub while pulling files might work.

Danger

`ERROR: unexpected error - 401 Client Error: Unauthorized for url: http://<remote_url>`

**Root cause 1:** You donâ€™t have write permissions for the repository. Either ask the maintainers to add you as a collaborator **or** fork the repository, make the changes, and create a pull request to the original project.

**Root cause 2:** You didn\'t configure your DVC remote authentication. You can either [set DagsHub as the remote Storage](https://dagshub.com/docs/quick_start/create_a_dagshub_project/#configure-dagshub-as-dvc-remote-storage) or [use an S3 compatible as the remote storage](../integration_guide/set_up_remote_storage_for_data_and_models/).

### Git failing to push files[¶](#git-failing-to-push-files "Permanent link")

When trying to push files using Git, the operation fails.

Danger

`fatal: could not read Username for 'https://dagshub.com': No such device or address error: failed to push some refs to 'https://dagshub.com/<path>.git'`

**Root cause 1:** You donâ€™t have your Git credentials for DagsHub set on the machine youâ€™re working on. Please use the following command structure to push files: `git push https://:@dagshub.com//`

------------------------------------------------------------------------

## DVC[¶](#dvc "Permanent link")

### Working with DVC in a monorepo architecture[¶](#working-with-dvc-in-a-monorepo-architecture "Permanent link")

DagsHub supports working with DVC in a monorepo architecture. This means that you can have multiple `.dvc/` folders in subdirectories. Files would still be scanned and visualized properly. However, to detect that a monorepo has a DVC integration, the root must contain a `.dvc/config` file as well. This config file can be **empty**, but it needs to appear in order for scanning to work properly.

### DVC failing to push files[¶](#dvc-failing-to-push-files "Permanent link")

When trying to push files using DVC, the operation fails.

Danger

`ERROR: failed to push data to the cloud - '503 Service Temporarily Unavailable'`

Danger

`ERROR: failed to push data to the cloud - 1 files failed to upload`

Danger

`ERROR: failed to transfer 'md5: ...' - 400, message='Bad Request', url=URL('http...')`

**Root cause 1:** There are a few versions of DVC with bugs that could cause these errors. **The safe versions of DVC are earlier than 2.3.0, 2.8.1, or 2.18.0 and up to the latest version**. The latest version is preferred. Upgrade to the latest DVC version by:

    pip3 install --upgrade dvc

To downgrade or install a specific version, run:

    pip3 install --upgrade dvc==2.8.1

------------------------------------------------------------------------

## Label Studio[¶](#label-studio "Permanent link")

### Error loading Label Studio project[¶](#error-loading-label-studio-project "Permanent link")

When trying to load a Label Studio project from DagsHub Annotations, it fails with the following error:

Danger

`Runtime error. Load failed`

**Root cause 1:** Your user tier doesn\'t have access to DagsHub Annotations. Community tier users can only use DagsHub annotations for open source projects. You can either make the repository public or upgrade your user tier.

------------------------------------------------------------------------

## MLflow[¶](#mlflow "Permanent link")

### Error Logging a Pyfunc-based Model[¶](#error-logging-a-pyfunc-based-model "Permanent link")

When trying to log an `mlflow.pyfunc` model, you get:

Danger

`yaml.representer.RepresenterError: ('cannot represent an object', <__main__.MarioModelWrapper object at 0x105772f70>)`

**Root cause 1:** Check that your `conda_env` parameter is properly set when calling `mlflow.pyfunc.log_model` and is a type that can be converted to YAML

### Model Registry Features are Not Supported[¶](#model-registry-features-are-not-supported "Permanent link")

If when trying to interact with the MLflow Model Registry, you get the error:

Danger

`mlflow.exceptions.MlflowException: Model Registry features are not supported by the store with URI: 'file:///Users/***/repos/mario_vs_wario_102/mlruns'. Stores with the following URI schemes are supported: ['databricks', 'http', 'https', 'postgresql', 'mysql', 'sqlite', 'mssql'].`

**Root cause 1:** Ensure that you\'ve set your tracking URI or have saved a model locally

### Using an MLflow command that takes a `model_uri`[¶](#using-an-mlflow-command-that-takes-a-model_uri "Permanent link")

While using an MLflow command that takes a `model_uri` as a parameter, you see:

Danger

`mlflow.exceptions.RestException: RESOURCE_DOES_NOT_EXIST: Response: `

or:

**Root cause 1:** Either the model name is incorrect or the version number doesn\'t exist.

Danger

`mlflow.exceptions.MlflowException: API request to endpoint /api/2.0/mlflow/runs/get failed with error code 400 != 200. Response body: '"repo not associated with run"'`

**Root cause 1:** This can happen if you use a `run_id` that doesn\'t exist.

### Deploying to Amazon SageMaker[¶](#deploying-to-amazon-sagemaker "Permanent link")

If you get the following error:

Danger

`The repository with name 'mlflow-pyfunc' does not exist in the registry with id '***'`

**Root cause 1:** Ensure you have run `mlflow sagemaker build-and-push-container` at least once first.

**Root cause 2:** Specify the SageMaker execution role in your command.

or:

Danger

`The role with name *** cannot be found.`

**Root cause 3:** You may need to specify the region name.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).