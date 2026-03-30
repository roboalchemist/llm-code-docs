# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/deploy-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/deploy-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/deploy-a-workflow.md

# Source: https://docs.roboflow.com/workflows/deploy-a-workflow.md

# Deploy a Workflow

You can deploy a Workflow in four ways:

1. Send images to the [Roboflow API](https://inference.roboflow.com/workflows/modes_of_running/#http-api-request) for processing using your Workflow.
2. Create a [Roboflow Dedicated Deployment](https://docs.roboflow.com/deploy/dedicated-deployments) on infrastructure provisioned exclusively for your use.
3. Run your Workflow on your own hardware using [Roboflow Inference](https://inference.roboflow.com/install/).
4. Schedule a [batch job in Roboflow Cloud ](https://inference.roboflow.com/workflows/batch_processing/about/)to automate the processing of large amounts of data without coding.

If you run your Workflow on your own hardware, you can run it on both images and video files (including streams from regular **webcams** and professional **CCTV cameras**).

By choosing on-premises deployment, you can run Workflows on any system where you can deploy Inference. This includes:

* NVIDIA Jetson
* AWS EC2, GCP Cloud Engine, and Azure Virtual Machines
* Raspberry Pi

{% hint style="info" %}
Roboflow Enterprise customers have access to additional video stream options, such as running inference on Basler cameras. To learn more about our offerings, [contact the Roboflow sales team](https://roboflow.com/sales).
{% endhint %}

### Deploy a Workflow

To deploy a workflow, click the "Deploy" button in the top left corner of the Workflows editor. All deployment options are documented on this page.

The code snippets in your Workflows editor will be pre-filled with your Workflows URL and API key.

{% hint style="info" %}
To learn more about usage limits for Workflows, refer to the [Roboflow pricing page](https://roboflow.com/workflows).
{% endhint %}

#### Process Images

You can run your Workflow on single images using the Roboflow API or local Inference server.

First, install the Roboflow Inference SDK:

```python
pip install inference-sdk inference-cli 
```

If you run locally, follow the [official Docker installation instructions](https://docs.docker.com/get-docker/) to install Docker on your machine and start Inference server:

```
inference server start
```

Then, create a new Python file and add the following code:

```python
from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",  # or "http://127.0.0.1:9001" for local deployment
    api_key="API_KEY"
)

result = client.run_workflow(
    workspace_name="workspace-name",
    workflow_id="workflow-id",
    images={
        "image": "YOUR_IMAGE.jpg"
    }
)

```

Above, replace `API_KEY` with your Roboflow API key. Replace `workspace-name` and `workflow-id` with your Roboflow workspace name and Workflow IDs.

To find these values, open your Roboflow Workflow and click "Deploy Workflow". Then, copy your workspace name and workflow ID from the code snippet that appears on the page.

Local execution works on CPU and NVIDIA CUDA GPU devices. For the best performance, deploy on a GPU-enabled device such as an NVIDIA Jetson or a cloud server with an NVIDIA GPU.

#### Process Video Stream (RTSP, Webcam)

You can deploy your Workflow on frames from a video stream. This can be a webcam or an RTSP stream. You can also run your Workflow on video files.

First, install Inference:

```
pip install inference  # or inference-gpu for GPU machines
```

It may take a few minutes for Inference to install.

Then, create a new Python file and add the following code:

```python
# Import the InferencePipeline object
from inference import InferencePipeline

def my_sink(result, video_frame):
    print(result) # do something with the predictions of each frame
    

# initialize a pipeline object
pipeline = InferencePipeline.init_with_workflow(
    api_key="API_KEY",
    workspace_name="workspace-name",
    workflow_id="workflow-id",
    video_reference=0, # Path to video, RSTP stream, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=my_sink
)
pipeline.start() #start the pipeline
pipeline.join() #wait for the pipeline thread to finish

```

Above, replace `API_KEY` with your Roboflow API key. Replace `workspace-name` and `workflow-id` with your Roboflow workspace name and Workflow IDs.

To find these values, open your Roboflow Workflow and click "Deploy Workflow". Then, copy your workspace name and workflow ID from the code snippet that appears on the page.

When you run the code above, your Workflow will run on your video or video stream.

#### Process Batches of Data

You can efficiently process entire batches of data—directories of images and video files—using the Roboflow Batch Processing service. This fully managed solution requires no coding or local computation. Simply select your data and Workflow, and let Roboflow handle the rest.

We support both UI, CLI and REST API interactions with Batch Processing. Below, we present CLI commands. Discover [all options](https://inference.roboflow.com/workflows/batch_processing/about/#cli).

To run the processing, install Inference CLI:

```
pip install inference-cli
```

Then you can ingest your data:

```
inference rf-cloud data-staging create-batch-of-images \
    --images-dir <your-images-dir-path> \
    --batch-id <your-batch-id>
```

When data are loaded, start the processing job:

```
inference rf-cloud batch-processing process-images-with-workflow \
    --workflow-id <workflow-id> \
    --batch-id <batch-id>
```

Progress of the job can be displayed using:

```
inference rf-cloud batch-processing show-job-details \
    --job-id <your-job-id>  # job-id will be displayed when you create a job
```

And when the job is done, export the results:

```
inference rf-cloud data-staging export-batch \
    --target-dir <dir-to-export-result> \
    --batch-id <output-batch-of-a-job>
```
