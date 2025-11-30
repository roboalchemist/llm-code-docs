# Source: https://dagshub.com/docs/use_cases/deploy_ml_model_to_cloud/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/deploy_ml_model_to_cloud.md "Edit this page")

# Deploy ML Models to a Cloud Platform[¶](#deploy-ml-models-to-a-cloud-platform "Permanent link")

Get early access to new Deployment feature

We\'re working on a new and improved deployment experience on DagsHub. If deploying models automatically onto your infrastructure is something you need. Contact us using [this form](https://meetings.hubspot.com/dean-p/deployment-meeting) to get early access.

**Using the MLflow server integrated with each DagsHub repo, you can deploy ML models to a cloud platform.**

MLflowâ€™s Model Registry allows us to store models alongside experiments and runs. It also includes model versioning and stage transitions. Put together, it simplifies determining which model we need to deploy to which environment. The whole process becomes less prone to error.

Once weâ€™ve logged and registered models to our Model Registry, we can thenÂ **load**Â andÂ **deploy**Â them.

## Automatic Model Registration[¶](#automatic-model-registration "Permanent link")

MLflow contains functions to log and register a model in one shot. These functions are available for several popular frameworks, which can be found [in their official documentation](https://www.mlflow.org/docs/latest/python_api/index.html#python-api).

The general call for logging a model is `mlflow.<framework>.log_model()`. For instance, to log a Keras model, we can do something like:

    import mlflow

    # Set MLflow server URI
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

    # Training code
    # ...

    # Log model
    mlflow.keras.log_model(keras_model=model,
                           artifact_path=MODELS_DIR,
                           registered_model_name="Super Cool Model")

The `MLFLOW_TRACKING_URI` is the same as the URL for your DagsHub repo, with `.mlflow` appended to the end. For example:

    https://dagshub.com/yonomitt/BetterSquirrelDetector.mlflow

## Manual Model Registration[¶](#manual-model-registration "Permanent link")

Sometimes, however, our framework either isnâ€™t supported, or we need more control over how the model is logged. In this instance, MLflow provides us with the ability to log any Python function.

To support the logging of generic Python functions we need to:

1.  Create a wrapper class that inherits fromÂ `mlflow.pyfunc.PythonModel`.
2.  Write aÂ `predict`Â method, which takes aÂ `context`Â and theÂ `model_input`.
3.  Optionally write aÂ `load_context`Â method to setup our model.

Letâ€™s say we wanted to log and register a custom YOLOv5 model. This could look something like this:

    import mlflow
    import torch

    class SquirrelDetectorWrapper(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=context.artifacts['path'])

        def predict(self, context, img):
            objs = self.model(img).xywh[0]

            return objs.numpy()

We then need to provide a dictionary with the dependencies we have:

    PYTHON_VERSION = "..1".format(major=version_info.major,
                                                minor=version_info.minor)

    conda_env = '.format(PYTHON_VERSION),
            'pip',
              '.format(cloudpickle.__version__),
                    'torch>=1.12.0'
                ],
              },
        ],
        'name': 'squirrel_env'
    }

We can then log and register the model with the following code:

    import mlflow

    # Set MLflow server URI
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

    with mlflow.start_run(experiment_id=exp_id):
        mlflow.pyfunc.log_model(
            'mymodel',
            python_model=SquirrelDetectorWrapper(),
            conda_env=conda_env,
            artifacts=,
            registered_model_name='Ultra Cool Model'
        )

## Loading a Model[¶](#loading-a-model "Permanent link")

Once a model has been logged and registered, we can load it using \`mlflow.:

    model_uri = f'models:/<model name>/<version>'
    model = mlflow.<framework>.load_model(model_uri)

The `version` of the model can be either a version number, which is an auto-incremented integer or the stage of the model (`Staging`, `Production`).

One easy way to get the latest registered version of your model is to use the following code:

    client = mlflow.MlflowClient()

    name = "Ultra Cool Model"
    version = client.get_latest_versions(name=name)[0].version
    model_uri = f'models://'

    model = mlflow.keras.load_model(model_uri)

## Deploying to Amazon SageMaker[¶](#deploying-to-amazon-sagemaker "Permanent link")

Before we can start with Amazon SageMaker, we need to make sure we create and setup our AWS account properly.

1.  [How to Create an AWS Account](https://aws.plainenglish.io/getting-started-to-aws-creating-an-aws-account-b11d685cbeea) \<- you will need a credit card
2.  [Setup IAM (Identity and Access Management) Role(s)](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-set-up.html)
3.  Install the AWS CLI using `pip install awscli`
4.  Add your credentials to `~/.aws/credentials`

The AWS credentials file should look like this:

    [default]
    aws_access_key_id = ***
    aws_secret_access_key = ***

The following command only needs to be run once for each AWS account. It creates the docker image that gets used by MLflow to serve the model and pushes it to Amazon SageMaker. However, it does not hurt if it is run multiple times.

    mlflow sagemaker build-and-push-container

In order to deploy, we need to know:

1.  The model URI
2.  Our SageMaker execution role
3.  The AWS region we are going to deploy the endpoint to

    mlflow sagemaker deploy --app-name mario \
                            --model-uri "models:/Ultra Cool Model/1" \
                            -e arn:aws:iam::***:role/SageMakerRole \
                            --region-name us-east-2

## Creating Docker Images to Deploy Anywhere[¶](#creating-docker-images-to-deploy-anywhere "Permanent link")

We can also use MLflow to create docker images to deploy anywhere we want.

    mlflow models build-docker --name mario \
                               --model-uri "models:/Ultra Cool Model/1"

This will create a Docker image tagged with the name `mario:latest`. To spin up a container from this image, we can run:

    docker run -d -p 8080:8080 mario:latest

## Running Inference on our Deployed Model[¶](#running-inference-on-our-deployed-model "Permanent link")

We can run inference using our Docker container with aÂ `curl`Â command.

The image input, as discussed, will need to be a base64 encoded image. However, we can\'t just send the base64 string. We need to include it in a JSON dictionary with this format:

    

Here is ourÂ `bash`Â command, which uses the built inÂ `base64`Â command to convert our image into a string:

    curl http://localhost:8080/invocations \
            -H 'Content-Type: application/json' \
            -d ''

For more information, see our [MLflow Crash Course Workshop](../../workshops/mlflow_crash_course/#model-registry-model-deployment), which includes a recording and a Colab notebook.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lLO8CmqJ2wLY5nTHNMvvMYwHEJQtqQNo)

[![](https://dagshub.com/img/favicon.svg) See the project on DagsHub](https://dagshub.com/DagsHub/mario_vs_wario)

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).