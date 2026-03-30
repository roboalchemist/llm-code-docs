# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/upload-custom-weights.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/upload-custom-weights.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/upload-custom-weights.md

# Source: https://docs.roboflow.com/deploy/upload-custom-weights.md

# Upload Custom Model Weights

Once you've completed training your custom model, upload your model weights back to your Roboflow project to take advantage of [Roboflow Inference](https://inference.roboflow.com/).

### Model Support

Refer to the [Supported Models table](https://docs.roboflow.com/deploy/supported-models) for details on weights upload compatibility.

{% hint style="warning" %}

* YOLOv8 models must be trained on `ultralytics==8.0.196`
* YOLOv9 models must be trained and uploaded using `ultralytics` from <https://github.com/WongKinYiu/yolov9>
* YOLOv10 models must be trained and uploaded using `ultralytics` from

  <https://github.com/THU-MIG/yolov10>
* YOLOv11 models must be trained on `ultralytics<=8.3.40`
* YOLOv12 models must be trained and uploaded using `ultralytics` from <https://github.com/sunsmarterjie/yolov12>
  {% endhint %}

{% hint style="info" %}
Larger model sizes provide better training results. However, the larger the model size, the slower the training time, and inference (model prediction) speed. Consider whether you're looking for real-time inference on fast-moving objects or video feeds (better to use a smaller model), or you are processing data after it is collected, and more concerned with higher prediction accuracy (choose a larger model).
{% endhint %}

### Versioned vs. Versionless Models Upload

Roboflow provides two distinct approaches for deploying models to your projects, each serving different use cases and organizational needs. The choice between versioned and versionless deployments depends on whether you need to track model evolution alongside dataset versions or want to share models across multiple projects in your workspace.

* **Versionless Deployments**
  * Tied to the workspace level
  * Can be deployed to multiple projects simultaneously
  * Ideal for sharing models across different projects within the same workspace
* **Versioned Deployments**
  * Tied to specific project versions
  * One model per dataset version
  * Ideal for tracking model evolution alongside dataset versions
  * Ideal for using model on Label Assist
  * Ideal for using model as checkpoint for training other models

### Upload Custom Weights

First, make sure you have latest `roboflow` Python package installed:&#x20;

```bash
pip install --update roboflow
```

{% tabs %}
{% tab title="Python SDK (Versionless)" %}
To upload versionless custom weights, use the `workspace.deploy_model()` method:

```python
workspace.deploy_model(
    model_type="yolov8",  # Type of the model
    model_path="path/to/model",  # Path to model directory
    project_ids=["project1", "project2"],  # List of project IDs
    model_name="my-model",  # Name for the model (must have at least 1 letter, and accept numbers and dashes)
    filename="weights/best.pt"  # Path to weights file (default)
)
```

**Parameters**

* model\_type (str): The type of model being deployed (e.g., "yolov8", "yolov11")
* model\_path (str): File path to the directory containing the model weights
* project\_ids (list\[str]): List of project IDs to deploy the model to
* model\_name (str): Name to identify the model - (must have at least 1 letter, and accept numbers and dashes)
* filename (str, optional): Name of the weights file (defaults to "weights/best.pt")

**Example**

```python
from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
workspace = rf.workspace("YOUR_WORKSPACE")

workspace.deploy_model(
  model_type="yolov8",
  model_path="./runs/train/weights",
  project_ids=["project-1", "project-2", "project-3"],
  model_name="my-custom-model"
)
```

{% endtab %}

{% tab title="Python SDK (Versioned)" %}
{% hint style="info" %}
One versioned model must be linked to just one corresponding dataset version. If you do not have a version generated in your dataset, you can create on [in-app](https://docs.roboflow.com/datasets/dataset-versions/create-a-dataset-version) or via the [API](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/python-sdk/create-a-dataset-version).

See docs on [how to load a version through the API](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/rest-api/versions/view-a-version) or reference the example below.
{% endhint %}

To upload custom weights, use the `version.deploy()` method in the Python SDK.

**Usage**

```python
version.deploy(
    model_type="yolov8",  # Type of the model
    model_path="path/to/model",  # Path to model directory
    filename="weights/best.pt"  # Path to weights file (default)
)
```

**Parameters**

* model\_type (str): The type of model to be deployed (e.g., "yolov8", "yolov11")
* model\_path (str): File path to the directory containing the model weights
* filename (str, optional): Name of the weights file (defaults to "weights/best.pt")

**Example**

```python
from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("PROJECT_ID")

#can specify weights_filename, default is "weights/best.pt"
version = project.version(VERSION_ID)

#example1 - directory path is "training1/model1.pt" for yolov8 model
version.deploy("yolov8", "training1", "model1.pt")

#example2 - directory path is "training1/weights/best.pt" for yolov8 model
version.deploy("yolov8", "training1")
```

**Important Notes**

1. A version can only have one trained model at a time
2. Attempting to upload to a version that already has a model will result in a 429 error
   {% endtab %}

{% tab title="CLI (Versionless and versioned)" %}
**Authentication**

Before using any CLI commands, you need to authenticate with Roboflow:

1. Run the authentication command: `roboflow login`
2. Visit the URL shown in the terminal: <https://app.roboflow.com/auth-cli>
3. Get your authentication token from the website
4. Paste the token in your terminal

The credentials will be automatically saved to `~/.config/roboflow/config.json`

**Uploading Model Weights**

The Roboflow CLI provides a command to upload trained model weights to your Roboflow projects. This is useful when you want to deploy custom-trained models to Roboflow.

**Basic Usage**

{% code overflow="wrap" %}

```bash
roboflow upload_model -w <workspace> -p <project> -t <model_type> -m <model_path> [-v <version>] [-f <filename>] [-n <model_name>]
```

{% endcode %}

**Parameters**

* `-w, --workspace`: Your workspace ID or URL (optional - will use default workspace if not specified)
* `-p, --project`: Project ID to upload the model into (for versionless upload can be specified multiple times for multiple projects)
* `-t, --model_type`: Type of the model (e.g., yolov8, paligemma2)
* `-m, --model_path`: Path to the directory containing the trained model file
* `-v, --version_number`: Version number to upload the model to (optional)
* `-f, --filename`: Name of the model file (default: "weights/best.pt")
* `-n, --model_name`: Name of the model (required for versionless model deploy)

**Examples**

<pre class="language-bash" data-overflow="wrap"><code class="lang-bash"># 1. Upload a model to a specific version: 
<strong>roboflow upload_model -w my-workspace -p my-project -v 1 -t yolov8 -m ./weights
</strong>
# 2. Upload a versionless model to multiple projects:
roboflow upload_model -w my-workspace -p project1 -p project2 -t yolov11 -n my-model-v1 -m ./weights
# 3. Upload a versionless RF-DETR medium model to a single project: 
roboflow upload_model -w my-workspace -p my-project -t rfdetr-medium -n my-model-name -m ./ -f weights.pt
</code></pre>

{% endtab %}
{% endtabs %}

## Next Steps

1. Check out your model in the "Models" tab of Roboflow
2. Run your model locally with [Roboflow Inference Server](https://inference.roboflow.com/).
3. [Deploy your model](https://docs.roboflow.com/deploy/deployment-overview)
