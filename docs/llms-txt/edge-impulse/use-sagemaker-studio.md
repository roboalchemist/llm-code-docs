# Source: https://docs.edgeimpulse.com/tutorials/tools/sdks/studio/python/use-sagemaker-studio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the Edge Impulse Python SDK with SageMaker Studio

<Columns cols={4}>
  <a href="https://github.com/edgeimpulse/notebooks/blob/main/notebooks/python-sdk-with-sagemaker-studio.ipynb" target="_blank">
    <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/badge-view-on-github.svg" alt="View on GitHub" noZoom />
  </a>

  <a href="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/notebooks/python-sdk-with-sagemaker-studio.ipynb" target="_blank">
    <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/badge-download-notebook.svg" alt="Download notebook" noZoom />
  </a>
</Columns>

Amazon SageMaker Studio is an integrated development environment (IDE) that provides a single web-based visual interface where you can access purpose-built tools to perform all machine learning (ML) development steps, from preparing data to building, training, and deploying your ML models, improving data science team productivity by up to 10x. You can quickly upload data, create new notebooks, train and tune models, move back and forth between steps to adjust experiments, collaborate seamlessly within your organization, and deploy models to production without leaving SageMaker Studio.

<Frame caption="SageMaker Studio">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/python-sdk-sagemaker-studio.png" />
</Frame>

To learn more about using the Python SDK, please see: [Edge Impulse Python SDK Overview](/tools/libraries/sdks/studio/python).

This guide has been built from AWS reference project **Introduction to SageMaker TensorFlow - Image Classification**, please have a look at this [AWS documentation page](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification-tensorflow.html).

Below are the changes made to the original training script and configuration:

* The `Python 3 (Data Science 3.0)` kernel was used.
* We used a dataset to classify images as `car` vs `unknown`.
* The dataset has been imported in the Edge Impulse S3 bucket configured when creating the SageMaker Studio domain. Make sure to adapt to your path or use the AWS reference project.
* The training instance used is `ml.m5.large`.

<iframe src="https://www.youtube.com/embed/r1XxGcKDR6M" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Install dependencies

```python  theme={"system"}
# If you have not done so already, install the following dependencies
!python -m pip install tensorflow==2.12.0 edgeimpulse
```

## Transfer Learning

### Dataset

Below is the structure of our dataset in our S3 bucket

```
car-vs-unknown
    |--training
        |--car
            |--abc.jpg
            |--def.jpg
        |--unknown
            |--ghi.jpg
            |--jkl.jpg
    |--testing
            |--car
                |--mno.jpg
                |--prs.jpg
            |--unknown
                |--tuv.jpg
                |--wxy.jpg
```

We have used the default bucket created when configuring SageMaker Studio domain:

<Frame caption="S3 Bucket overview">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/python-sdk-s3-bucket-cars.png" />
</Frame>

```python  theme={"system"}
import sagemaker, boto3, json
from sagemaker.session import Session

sagemaker_session = Session()
aws_role = sagemaker_session.get_caller_identity_arn()
aws_region = boto3.Session().region_name
print(aws_region)
sess = sagemaker.Session()
```

```python  theme={"system"}
bucket = sess.default_bucket()
subfolder = 'car-vs-unknown/training/'

s3 = boto3.client('s3')
files = s3.list_objects(Bucket=bucket, Prefix=subfolder)['Contents']
print(f"Number of images: {len(files)}")
# or print the files
# for f in files:
#     print(f['Key'])
```

### Train

You can continue with the default model, or can choose a different model from the list. Note that this tutorial has been tested with MobileNetv2 based models.
A complete list of SageMaker pre-trained models can also be accessed at [Sagemaker pre-trained Models](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html#).

```python  theme={"system"}
from sagemaker.jumpstart.notebook_utils import list_jumpstart_models

# Retrieves all image classification models available by SageMaker Built-In Algorithms.
filter_value = "task in ['ic']"
ic_models = list_jumpstart_models(filter=filter_value)
# od_models = list_jumpstart_models()

print(f"Number of models available for inference: {len(ic_models)}")

# display the model-ids.
for model in ic_models:
    print(model)
```

```python  theme={"system"}
from sagemaker import image_uris, model_uris

model_id, model_version = "tensorflow-ic-imagenet-mobilenet-v3-small-075-224", "*" # You can change the based model with one from the list generated above

# Retrieve the base model uri
base_model_uri = model_uris.retrieve( model_id=model_id, model_version=model_version, model_scope="inference")

print(base_model_uri)
```

*Optional*, ship this next cell if you don't want to retrain the model. And uncomment the last line of the cell after

```python  theme={"system"}
from sagemaker import image_uris, model_uris, script_uris, hyperparameters
from sagemaker.estimator import Estimator

training_instance_type = "ml.m5.large"

# Retrieve the Docker image
train_image_uri = image_uris.retrieve(model_id=model_id,model_version=model_version,image_scope="training",instance_type=training_instance_type,region=None,framework=None)

# Retrieve the training script
train_source_uri = script_uris.retrieve(model_id=model_id, model_version=model_version, script_scope="training")

# Retrieve the pretrained model tarball for transfer learning
train_model_uri = model_uris.retrieve(model_id=model_id, model_version=model_version, model_scope="training")

# Retrieve the default hyper-parameters for fine-tuning the model
hyperparameters = hyperparameters.retrieve_default(model_id=model_id, model_version=model_version)

# [Optional] Override default hyperparameters with custom values
hyperparameters["epochs"] = "5"

# The sample training data is available in the following S3 bucket
training_data_bucket = f"{bucket}"
training_data_prefix = f"{subfolder}"
# training_data_bucket = f"jumpstart-cache-prod-{aws_region}"
# training_data_prefix = "training-datasets/tf_flowers/"

training_dataset_s3_path = f"s3://{training_data_bucket}/{training_data_prefix}"

output_bucket = sess.default_bucket()
output_prefix = "ic-car-vs-unknown"
s3_output_location = f"s3://{output_bucket}/{output_prefix}/output"

# Create SageMaker Estimator instance
tf_ic_estimator = Estimator(
    role=aws_role,
    image_uri=train_image_uri,
    source_dir=train_source_uri,
    model_uri=train_model_uri,
    entry_point="transfer_learning.py",
    instance_count=1,
    instance_type=training_instance_type,
    max_run=360000,
    hyperparameters=hyperparameters,
    output_path=s3_output_location
)

# Use S3 path of the training data to launch SageMaker TrainingJob
tf_ic_estimator.fit({"training": training_dataset_s3_path}, logs=True)
```

## Retrieve and prepare the newly trained model

```python  theme={"system"}
def download_from_s3(url):
    # Remove 's3://' prefix from URL
    url = url[5:]
    # Split URL by '/' to extract bucket name and key
    parts = url.split('/')
    bucket_name = parts[0]
    s3_key = '/'.join(parts[1:])
    # Download the file from S3
    s3.download_file(bucket_name, s3_key, 'model.tar.gz')

# Download
trained_model_s3_path = f"{s3_output_location}/{tf_ic_estimator._current_job_name}/output/model.tar.gz"
print(trained_model_s3_path)
download_from_s3(trained_model_s3_path)
# or if you just want to use the based model
#download_from_s3(base_model_uri)
```

```python  theme={"system"}
import shutil, os

# Extract the .tar.gz file to a temporary directory
temp_directory = 'tmp'  # Replace with your actual temporary directory
tar_gz_file = 'model.tar.gz'  # Replace with the path to your .tar.gz file

# Create directory if does not exist
if not os.path.exists(temp_directory):
    os.makedirs(temp_directory)

shutil.unpack_archive(tar_gz_file, temp_directory)
```

```python  theme={"system"}
import tensorflow as tf

print(tf.__version__)

model = tf.keras.models.load_model('tmp/1/')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)
```

## Edge Impulse

You will need to obtain an API key from an Edge Impulse project. Log into [edgeimpulse.com](https://edgeimpulse.com/) and create a new project. Open the project, navigate to **Dashboard** and click on the **Keys** tab to view your API keys. Double-click on the API key to highlight it, right-click, and select **Copy**.

<Frame caption="Copy API key from Edge Impulse project">
  <img src="https://raw.githubusercontent.com/edgeimpulse/notebooks/main/.assets/images/python-sdk-copy-ei-api-key.png" />
</Frame>

Note that you do not actually need to use the project in the Edge Impulse Studio. We just need the API Key.

Paste that API key string in the `ei.API_KEY` value in the following cell:

```python  theme={"system"}
import edgeimpulse as ei
ei.API_KEY = "ei_0a85c3a5ca92a35ee6f61aab18aadb9d9e167bd152f947f2056a4fb6a60977d8" # Change to your key
```

```python  theme={"system"}
ei.model.list_profile_devices()
```

```python  theme={"system"}
# Estimate the RAM, ROM, and inference time for our model on the target hardware family
try:
    profile = ei.model.profile(model='model.tflite',
                               device='raspberry-pi-4')
    print(profile.summary())
except Exception as e:
    print(f"Could not profile: {e}")
```

```python  theme={"system"}
# List the available profile target devices
ei.model.list_deployment_targets()
```

```python  theme={"system"}
# Get the labels from the label_info.json
import json

labels_info = open('tmp/labels_info.json')
labels_obj = json.load(labels_info)
labels = labels_obj['labels']
print(labels)
```

```python  theme={"system"}
# Set model information, such as your list of labels
model_output_type = ei.model.output_type.Classification(labels=labels)
deploy_filename = "my_model_cpp.zip"

# Create C++ library with trained model
deploy_bytes = None
try:

    deploy_bytes = ei.model.deploy(model=model,
                                   model_output_type=model_output_type,
                                   engine='tflite',
                                   deploy_target='zip"')
except Exception as e:
    print(f"Could not deploy: {e}")

# Write the downloaded raw bytes to a file
if deploy_bytes:
    with open(deploy_filename, 'wb') as f:
        f.write(deploy_bytes.getvalue())
```

Voila!
You now have a C++ library ready to be compiled and integrated in your embedded targets. Feel free to have a look at Edge Impulse deployment options on the [documentation](/hardware/deployments/run-cpp-overview) to understand how you can integrate that to your embedded systems.

You can also have a look at the deployment page of your project to test your model on a web browser or test


Built with [Mintlify](https://mintlify.com).