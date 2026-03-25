# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/dedicated-deployments/make-requests-to-a-dedicated-deployment.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/dedicated-deployments/make-requests-to-a-dedicated-deployment.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/dedicated-deployments/make-requests-to-a-dedicated-deployment.md

# Source: https://docs.roboflow.com/deploy/dedicated-deployments/make-requests-to-a-dedicated-deployment.md

# Make Requests to a Dedicated Deployment

### Use Python SDK

Please install the latest version of our Python SDK [inference\_sdk](https://pypi.org/project/inference-sdk/) with `pip install --upgrade inference-sdk`.

When your dedicated deployment is ready, copy its URL:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3f9f20ce34b5e1d96ea7cf7f6644bcb859b1fa33%2Fimage.png?alt=media" alt=""><figcaption><p>Copy URL of your dedicated deployment when it's ready</p></figcaption></figure>

and paste it to the parameter `api_url` when initialise `InferenceHTTPClient` , and that's it!

Here is an example for running model inference, you can find more details in [the documentation of inference\_sdk](https://inference.roboflow.com/inference_helpers/inference_sdk/).

```
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://dev-testing.roboflow.cloud",
    api_key="ROBOFLOW_API_KEY"
)

image_url = "https://source.roboflow.com/pwYAXv9BTpqLyFfgQoPZ/u48G0UpWfk8giSw7wrU8/original.jpg"
result = CLIENT.infer(image_url, model_id="soccer-players-5fuqs/1")
```

### Use HTTP API

You can also access [the HTTP APIs](https://inference.roboflow.com/api/) which are listed under `/docs`, e.g,, `https://dev-testing.roboflow.cloud/docs` .

Please attach your workspace `api_key` as a query parameter when access these endpoints.

Here is an example for making the same request as above using HTTP API:

```
import requests
import json

api_url = "https://dev-testing.roboflow.cloud"
model_id = "soccer-players-5fuqs/1"
image_url = "https://source.roboflow.com/pwYAXv9BTpqLyFfgQoPZ/u48G0UpWfk8giSw7wrU8/original.jpg"

resp = requests.get(f"{api_url}/{model_id}", params = {"api_key": "ROBOFLOW_API_KEY", "image": image_url})
result = json.loads(resp.content)
```

### Use Workflow UI

A dedicated deployment can also be used as the backend server for running [Roboflow Workflows](https://roboflow.com/workflows/build). Roboflow Workflows is a low-code, web-based application builder for creating computer vision applications.

After creating your workflow, click on the **Running on Hosted API** link in the top left corner:

<figure><img src="https://blog.roboflow.com/content/images/2024/09/Screenshot-2024-09-03-at-18.26.29.png" alt="" height="102" width="354"><figcaption><p>Changing the backend where the workflow will execute.</p></figcaption></figure>

Click **Dedicated Deployments** to see the list of your dedicated deployments, select the target deployment, then click **Connect**:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-f185515ed2f41a881135fa87cc861b9e905bf25e%2FScreenshot%202024-12-09%20at%2015.04.54.png?alt=media" alt=""><figcaption><p>Select a target dedicated deployment as the backend server for workflow execution.</p></figcaption></figure>

Now you are ready to use your dedicated deployment in the workflow editor.
