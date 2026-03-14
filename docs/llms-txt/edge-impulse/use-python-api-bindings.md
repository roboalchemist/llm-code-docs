# Source: https://docs.edgeimpulse.com/tutorials/tools/api-bindings/studio/python/use-python-api-bindings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the Python API bindings

<Columns cols={4}>
  <a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/python-api-bindings-example.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
  </a>

  <a href="https://github.com/edgeimpulse/notebooks/blob/main/notebooks/python-api-bindings-example.ipynb" target="_blank">
    <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/badge-view-on-github.svg" alt="View on GitHub" noZoom />
  </a>

  <a href="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/notebooks/python-api-bindings-example.ipynb" target="_blank">
    <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/badge-download-notebook.svg" alt="Download notebook" noZoom />
  </a>
</Columns>

The [Python SDK](/tools/libraries/sdks/studio/python) is built on top of the [Edge Impulse Python API bindings](https://pypi.org/project/edgeimpulse-api/), which is known as the *edgeimpulse\_api* package. These are Python wrappers for all of the [web API calls](/apis/studio) that you can use to interact with Edge Impulse projects programmatically (i.e. without needing to use the Studio graphical interface).

The API reference guide for using the Python API bindings can be found [here](/tools/libraries/api-bindings/studio/python/edgeimpulse_api/index).

This example will walk you through the process of using the Edge Impulse API bindings to upload data, define an impulse, process features, train a model, and deploy the impulse as a C++ library.

After creating your project and copying the API key, feel free to leave the project open in a browser window so you can watch the changes as we make API calls. You might need to refresh the browser after each call to see the changes take affect.

> **Important!** This project will add data and remove any current features and models in a project. We highly recommend creating a new project when running this notebook! Don't say we didn't warn you if you mess up an existing project.

```python  theme={"system"}
# Install the Edge Impulse API bindings and the requests package
!python -m pip install edgeimpulse-api requests
```

```python  theme={"system"}
import json
import re
import os
import pprint
import time

import requests
```

```python  theme={"system"}
# Import the API objects we plan to use
from edgeimpulse_api import (
    ApiClient,
    BuildOnDeviceModelRequest,
    Configuration,
    DeploymentApi,
    DSPApi,
    DSPConfigRequest,
    GenerateFeaturesRequest,
    Impulse,
    ImpulseApi,
    JobsApi,
    ProjectsApi,
    SetKerasParameterRequest,
    StartClassifyJobRequest,
    UpdateProjectRequest,
)
```

You will need to obtain an API key from an Edge Impulse project. Log into [edgeimpulse.com](https://edgeimpulse.com/) and create a new project. Open the project, navigate to **Dashboard** and click on the **Keys** tab to view your API keys. Double-click on the API key to highlight it, right-click, and select **Copy**.

<Frame caption="Copy API key from Edge Impulse project">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/python-sdk-copy-ei-api-key.png" />
</Frame>

Note that you do not actually need to use the project in the Edge Impulse Studio. We just need the API Key.

Paste that API key string in the `EI_API_KEY` value in the following cell:

```python  theme={"system"}
# Settings
API_KEY = "ei_dae2..." # Change this to your Edge Impulse API key
API_HOST = "https://studio.edgeimpulse.com/v1"
DATASET_PATH = "dataset/gestures"
OUTPUT_PATH = "."
```

## Initialize API clients

The Python API bindings use a series of submodules, each encapsulating one of the API subsections (e.g. Projects, DSP, Learn, etc.). To use these submodules, you need to instantiate a generic API module and use that to instantiate the individual API objects. We'll use these objects to make the API calls later.

To configure a client, you generally create a configuration object (often from a dict) and then pass that object as an argument to the client.

```python  theme={"system"}
# Create top-level API client
config = Configuration(
    host=API_HOST,
    api_key={"ApiKeyAuthentication": API_KEY}
)
client = ApiClient(config)

# Instantiate sub-clients
deployment_api = DeploymentApi(client)
dsp_api = DSPApi(client)
impulse_api = ImpulseApi(client)
jobs_api = JobsApi(client)
projects_api = ProjectsApi(client)
```

## Initialize project

Before uploading data, we should make sure the project is in the regular impulse flow mode, rather than [BYOM mode](/studio/projects/dashboard/byom). We'll also need the project ID for most of the other API calls in the future.

Notice that the general pattern for calling API functions is to instantiate a configuration/request object and pass it to the API method that's part of the submodule. You can find which parameters a specific API call expects by looking at [the call's documentation page](/apis/studio/projects/update-project).

API calls (links to associated documentation):

* [Projects / List (active) projects](/apis/studio/rojects/list-active-projects)
* [Projects / Update project](/apis/studio/projects/update-project)

```python  theme={"system"}
# Get the project ID, which we'll need for future API calls
response = projects_api.list_projects()
if not hasattr(response, "success") or getattr(response, "success") == False:
    raise RuntimeError("Could not obtain the project ID.")
else:
    project_id = response.projects[0].id

# Print the project ID
print(f"Project ID: {project_id}")
```

```python  theme={"system"}
# Create request object with the required parameters
update_project_request = UpdateProjectRequest.from_dict({
    "inPretrainedModelFlow": False,
})

# Update the project and check the response for errors
response = projects_api.update_project(
    project_id=project_id,
    update_project_request=update_project_request,
)
if not hasattr(response, "success") or getattr(response, "success") == False:
    raise RuntimeError("Could not obtain the project ID.")
else:
    print("Project is now in impulse workflow.")
```

## Upload dataset

We'll start by downloading the gesture dataset from [this link](/datasets/time-series/continuous-motion-recognition). Note that the [Ingestion API](/apis/ingestion) is separate from the regular Edge Impulse API: the URL and interface are different. As a result, we must construct the request manually and cannot rely on the Python API bindings.

We rely on the ingestion service using the string before the first period in the filename to determine the label. For example, "idle.1.cbor" will be automatically assigned the label "idle." If you wish to set a label manually, you must specify the `x-label` parameter in the headers. Note that you can only define a label this way when uploading a group of data at a time. For example, setting `"x-label": "idle"` in the headers would give all data uploaded with that call the label "idle."

API calls used with associated documentation:

* [Ingestion API](/apis/ingestion)

```python  theme={"system"}
# Download and unzip gesture dataset
!mkdir -p dataset/
!wget -P dataset -q https://cdn.edgeimpulse.com/datasets/gestures.zip
!unzip -q dataset/gestures.zip -d {DATASET_PATH}
```

```python  theme={"system"}
def upload_files(api_key, path, subset):
    """
    Upload files in the given path/subset (where subset is "training" or
    "testing")
    """

    # Construct request
    url = f"https://ingestion.edgeimpulse.com/api/{subset}/files"
    headers = {
        "x-api-key": api_key,
        "x-disallow-duplicates": "true",
    }

    # Get file handles and create dataset to upload
    files = []
    file_list = os.listdir(os.path.join(path, subset))
    for file_name in file_list:
        file_path = os.path.join(path, subset, file_name)
        if os.path.isfile(file_path):
            file_handle = open(file_path, "rb")
            files.append(("data", (file_name, file_handle, "multipart/form-data")))

    # Upload the files
    response = requests.post(
        url=url,
        headers=headers,
        files=files,
    )

    # Print any errors for files that did not upload
    upload_responses = response.json()["files"]
    for resp in upload_responses:
        if not resp["success"]:
            print(resp)

    # Close all the handles
    for handle in files:
        handle[1][1].close()
```

```python  theme={"system"}
# Upload the dataset to the project
print("Uploading training dataset...")
upload_files(API_KEY, DATASET_PATH, "training")
print("Uploading testing dataset...")
upload_files(API_KEY, DATASET_PATH, "testing")
```

## Create an impulse

Now that we uploaded our data, it's time to create an impulse. An "impulse" is a combination of processing (feature extraction) and learning blocks. The general flow of data is:

> data -> input block -> processing block(s) -> learning block(s)

Only the processing and learning blocks make up the "impulse." However, we must still specify the input block, as it allows us to perform preprocessing, like windowing (for time series data) or cropping/scaling (for image data).

Your project will have one input block, but it can contain multiple processing and learning blocks. Specific outputs from the processing block can be specified as inputs to the learning blocks. However, for simplicity, we'll just show one processing block and one learning block.

> **Note:** Historically, processing blocks were called "DSP blocks," as they focused on time series data. In Studio, the name has been changed to "Processing block," as the blocks work with different types of data, but you'll see it referred to as "DSP block" in the API.

It's important that you define the input block with the same parameters as your captured data, especially the sampling rate! Additionally, the processing block axes names **must** match up with their names in the dataset.

API calls (links to associated documentation):

* [Impulse / Get impulse blocks](/apis/studio/impulse/get-impulse-blocks)
* [Impulse / Delete impulse](/apis/studio/impulse/delete-impulse)
* [Impulse / Create impulse](/apis/studio/impulse/create-impulse)

```python  theme={"system"}
# To start, let's fetch a list of all the available blocks
response = impulse_api.get_impulse_blocks(
    project_id=project_id
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not get impulse blocks.")
```

```python  theme={"system"}
# Print the available input blocks
print("Input blocks")
print(json.dumps(json.loads(response.to_json())["inputBlocks"], indent=2))
```

```python  theme={"system"}
# Print the available processing blocks
print("Processing blocks")
print(json.dumps(json.loads(response.to_json())["dspBlocks"], indent=2))
```

```python  theme={"system"}
# Print the available learning blocks
print("Learning blocks")
print(json.dumps(json.loads(response.to_json())["learnBlocks"], indent=2))
```

```python  theme={"system"}
# Give our impulse blocks IDs, which we'll use later
processing_id = 2
learning_id = 3

# Impulses (and their blocks) are defined as a collection of key/value pairs
impulse = Impulse.from_dict({
    "inputBlocks": [
        {
            "id": 1,
            "type": "time-series",
            "name": "Time series",
            "title": "Time series data",
            "windowSizeMs": 1000,
            "windowIncreaseMs": 500,
            "frequencyHz": 62.5,
            "padZeros": True,
        }
    ],
    "dspBlocks": [
        {
            "id": processing_id,
            "type": "spectral-analysis",
            "name": "Spectral Analysis",
            "implementationVersion": 4,
            "title": "processing",
            "axes": ["accX", "accY", "accZ"],
            "input": 1,
        }
    ],
    "learnBlocks": [
        {
            "id": learning_id,
            "type": "keras",
            "name": "Classifier",
            "title": "Classification",
            "dsp": [processing_id],
        }
    ],
})
```

```python  theme={"system"}
# Delete the current impulse in the project
response = impulse_api.delete_impulse(
    project_id=project_id
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not delete current impulse.")

# Add blocks to impulse
response = impulse_api.create_impulse(
    project_id=project_id,
    impulse=impulse
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not create impulse.")
```

## Configure processing block

Before generating features, we need to configure the processing block. We'll start by printing all the available parameters for the `spectral-analysis` block, which we set when we created the impulse above.

API calls (links to associated documentation):

* [DSP / Get config](/apis/studio/dsp/get-config)
* [DSP / Set config](/apis/studio/dsp/set-config)

```python  theme={"system"}
# Get processing block config
response = dsp_api.get_dsp_config(
    project_id=project_id,
    dsp_id=processing_id
)

# Construct user-readable parameters
settings = []
for group in response.config:
    for item in group.items:
        element = {}
        element["parameter"] = item.param
        element["description"] = item.help
        element["currentValue"] = item.value
        element["defaultValue"] = item.default_value
        element["type"] = item.type
        if hasattr(item, "select_options") and \
            getattr(item, "select_options") is not None:
            element["options"] = [i.value for i in item.select_options]
        settings.append(element)

# Print the settings
print(json.dumps(settings, indent=2))
```

```python  theme={"system"}
# Define processing block configuration
config_request = DSPConfigRequest.from_dict({
    "config": {
        "scale-axes": 1.0,
        "input-decimation-ratio": 1,
        "filter-type": "none",
        "analysis-type": "FFT",
        "fft-length": 16,
        "do-log": True,
        "do-fft-overlap": True,
        "extra-low-freq": False,
    }
})

# Set processing block configuration
response = dsp_api.set_dsp_config(
    project_id=project_id,
    dsp_id=processing_id,
    dsp_config_request=config_request
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not start feature generation job.")
else:
    print("Processing block has been configured.")
```

## Run processing block to generate features

After we've defined the impulse, we then want to use our processing block(s) to extract features from our data. We'll skip feature importance and feature explorer to make this go faster.

Generating features kicks off a job in Studio. A "job" involves instantiating a Docker container and running a custom script in the container to perform some action. In our case, that involves reading in data, extracting features from that data, and saving those features as Numpy (.npy) files in our project.

Because jobs can take a while, the API call will return immediately. If the call was successful, the response will contain a job number. We can then monitor that job and wait for it to finish before continuing.

API calls (links to associated documentation):

* [Jobs / Generate features](/apis/studio/jobs/generate-features)
* [Jobs / Get job status](/apis/studio/jobs/get-job-status)

```python  theme={"system"}
def poll_job(jobs_api, project_id, job_id):
    """Wait for job to complete"""

    # Wait for job to complete
    while True:

        # Check on job status
        response = jobs_api.get_job_status(
            project_id=project_id,
            job_id=job_id
        )
        if not hasattr(response, "success") or getattr(response, "success") is False:
            print("ERROR: Could not get job status")
            return False
        else:
            if hasattr(response, "job") and hasattr(response.job, "finished"):
                if response.job.finished:
                    print(f"Job completed at {response.job.finished}")
                    return response.job.finished_successful
            else:
                print("ERROR: Response did not contain a 'job' field.")
                return False

        # Print that we're still running and wait
        print(f"Waiting for job {job_id} to finish...")
        time.sleep(2.0)
```

```python  theme={"system"}
# Define generate features request
generate_features_request = GenerateFeaturesRequest.from_dict({
    "dspId": processing_id,
    "calculate_feature_importance": False,
    "skip_feature_explorer": True,
})

# Generate features
response = jobs_api.generate_features_job(
    project_id=project_id,
    generate_features_request=generate_features_request,
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not start feature generation job.")

# Extract job ID
job_id = response.id

# Wait for job to complete
success = poll_job(jobs_api, project_id, job_id)
if success:
    print("Features have been generated.")
else:
    print(f"ERROR: Job failed. See https://studio.edgeimpulse.com/studio/{project_id}/jobs#show-job-{job_id} for more details.")
```

```python  theme={"system"}
# Optional: download NumPy features (x: training data, y: training labels)
print("Go here to download the generated features in NumPy format:")
print(f"https://studio.edgeimpulse.com/v1/api/{project_id}/dsp-data/{processing_id}/x/training")
print(f"https://studio.edgeimpulse.com/v1/api/{project_id}/dsp-data/{processing_id}/y/training")
```

## Use learning block to train model

Now that we have trained features, we can run the learning block to train the model on those features. Note that Edge Impulse has a number of learning blocks, each with different methods of configuration. We'll be using the "keras" block, which uses TensorFlow and Keras under the hood.

You can use the [get\_keras](/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/learn_api#get_keras) and [set\_keras](/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/learn_api#set_keras) functions to configure the granular settings. We'll use the defaults for that block and just set the number of epochs and learning rate for training.

API calls (links to associated documentation):

* [Jobs / Train model (Keras)](/apis/studio/jobs/train-model-keras)
* [Jobs / Get job status](/apis/studio/jobs/get-job-status)
* [Jobs / Get logs](/apis/studio/jobs/get-logs)

```python  theme={"system"}
 # Define training request
keras_parameter_request = SetKerasParameterRequest.from_dict({
    "mode": "visual",
    "training_cycles": 10,
    "learning_rate": 0.001,
    "train_test_split": 0.8,
    "skip_embeddings_and_memory": True,
})

# Train model
response = jobs_api.train_keras_job(
    project_id=project_id,
    learn_id=learning_id,
    set_keras_parameter_request=keras_parameter_request,
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not start training job.")

# Extract job ID
job_id = response.id

# Wait for job to complete
success = poll_job(jobs_api, project_id, job_id)
if success:
    print("Model has been trained.")
else:
    print(f"ERROR: Job failed. See https://studio.edgeimpulse.com/studio/{project_id}/jobs#show-job-{job_id} for more details.")
```

Now that the model has been trained, we can go back to the job logs to find the accuracy metrics for both the float32 and int8 quantization levels. We'll need to parse the logs to find these. Because the logs are printed with the most recent events first, we'll work backwards through the log to find these metrics.

```python  theme={"system"}
def get_metrics(response, quantization=None):
    """
    Parse the response to find the accuracy/training metrics for a given
    quantization level. If quantization is None, return the first set of metrics
    found.
    """
    metrics = None
    delimiter_str = "calculate_classification_metrics"

    # Skip finding quantization metrics if not given
    if quantization:
        quantization_found = False
    else:
        quantization_found = True

    # Parse logs
    for log in reversed(response.to_dict()["stdout"]):
        data_field = log["data"]
        if quantization_found:
            substrings = data_field.split("\n")
            for substring in substrings:
                substring = substring.strip()
                if substring.startswith(delimiter_str):
                    metrics = json.loads(substring[len(delimiter_str):])
                    break
        else:
            if data_field.startswith(f"Calculating {quantization} accuracy"):
                quantization_found = True

    return metrics
```

```python  theme={"system"}
# Get the job logs for the previous job
response = jobs_api.get_jobs_logs(
    project_id=project_id,
    job_id=job_id
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not get job log.")

# Print training metrics (quantization is "float32" or "int8")
quantization = "float32"
metrics = get_metrics(response, quantization)
if metrics:
    print(f"Training metrics for {quantization} quantization:")
    pprint.pprint(metrics)
else:
    print("ERROR: Could not get training metrics.")
```

## Test the impulse

As with any good machine learning project, we should test the accuracy of the model using our holdout ("testing") set. We'll call the `classify` API function to make that happen and then parse the job logs to get the results.

In most cases, using `int8` quantization will result in a faster, smaller model, but you will slightly lose some accuracy.

API calls (links to associated documentation):

* [Jobs / Classify](/apis/studio/jobs/classify)
* [Jobs / Get job status](/apis/studio/jobs/get-job-status)
* [Jobs / Get logs](/apis/studio/jobs/get-logs)

```python  theme={"system"}
 # Set the model quantization level ("float32", "int8", or "akida")
quantization = "int8"
classify_request = StartClassifyJobRequest.from_dict({
    "model_variants": quantization
})

# Start model testing job
response = jobs_api.start_classify_job(
    project_id=project_id,
    start_classify_job_request=classify_request
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not start classify job.")

# Extract job ID
job_id = response.id

# Wait for job to complete
success = poll_job(jobs_api, project_id, job_id)
if success:
    print("Inference performed on test set.")
else:
    print(f"ERROR: Job failed. See https://studio.edgeimpulse.com/studio/{project_id}/jobs#show-job-{job_id} for more details.")
```

```python  theme={"system"}
# Get the job logs for the previous job
response = jobs_api.get_jobs_logs(
    project_id=project_id,
    job_id=job_id
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not get job log.")

# Print
metrics = get_metrics(response)
if metrics:
    print(f"Test metrics for {quantization} quantization:")
    pprint.pprint(metrics)
else:
    print("ERROR: Could not get test metrics.")
```

## Deploy the impulse

Now that you've trained the model, let's build it as a C++ library and download it. We'll start by printing out the available target devices. Note that this list changes depending on how you've configured your impulse. For example, if you use a Syntiant-specific learning block, then you'll see Syntiant boards listed. We'll use the "zip" target, which gives us a generic C++ library that we can use for nearly any hardware.

The `engine` must be one of:

```
tflite
tflite-eon
tflite-eon-ram-optimized
tensorrt
tensaiflow
drp-ai
tidl
akida
syntiant
memryx
```

We'll use `tflite`, as that's the most ubiquitous.

`modelType` is the quantization level. Your options are:

```
float32
int8
```

In most cases, using `int8` quantization will result in a faster, smaller model, but you will slightly lose some accuracy.

API calls (links to associated documentation):

* [Deployment / Deployment targets (data sources)](/apis/studio/deployment/deployment-targets-data-sources)
* [Jobs / Build on-device model](/apis/studio/jobs/build-on-device-model)
* [Deployment / Download](/apis/studio/deployment/download)

```python  theme={"system"}
# Get the available devices
response = deployment_api.list_deployment_targets_for_project_data_sources(
    project_id=project_id
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not get device list.")

# Print the available devices
targets = [x.to_dict()["format"] for x in response.targets]
for target in targets:
    print(target)
```

```python  theme={"system"}
# Choose the target hardware (from the list above), engine,
target_hardware = "zip"
engine = "tflite"
quantization = "int8"

# Construct request
device_model_request = BuildOnDeviceModelRequest.from_dict({
    "engine": engine,
    "modelType": quantization
})

# Start build job
response = jobs_api.build_on_device_model_job(
    project_id=project_id,
    type=target_hardware,
    build_on_device_model_request=device_model_request,
)
if not hasattr(response, "success") or getattr(response, "success") is False:
    raise RuntimeError("Could not start feature generation job.")

# Extract job ID
job_id = response.id

# Wait for job to complete
success = poll_job(jobs_api, project_id, job_id)
if success:
    print("Impulse built.")
else:
    print(f"ERROR: Job failed. See https://studio.edgeimpulse.com/studio/{project_id}/jobs#show-job-{job_id} for more details.")
```

```python  theme={"system"}
# Get the download link information
response = deployment_api.download_build(
    project_id=project_id,
    type=target_hardware,
    model_type=quantization,
    engine=engine,
    _preload_content=False,
)
if response.status != 200:
    raise RuntimeError("Could not get download information.")

# Find the file name in the headers
file_name = re.findall(r"filename\*?=(.+)", response.headers["Content-Disposition"])[0].replace("utf-8''", "")
file_path = os.path.join(OUTPUT_PATH, file_name)

# Write the contents to a file
with open(file_path, "wb") as f:
    f.write(response.data)
```

You should have a .zip file in the same directory as this notebook. Download or move it to somewhere else on your computer and unzip it. You can now follow [this guide](/hardware/deployments/run-cpp) to link and compile the library as part of an application.


Built with [Mintlify](https://mintlify.com).