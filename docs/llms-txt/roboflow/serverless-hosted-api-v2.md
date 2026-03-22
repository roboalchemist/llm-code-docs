# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/serverless-hosted-api-v2.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/serverless-hosted-api-v2.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/serverless-hosted-api-v2.md

# Source: https://docs.roboflow.com/deploy/serverless-hosted-api-v2.md

# Serverless Hosted API

Models deployed to Roboflow have a REST API available through which you can run inference on images. This deployment method is ideal for environments where you have a persistent internet connection on your deployment device.

You can use Serverless Hosted API:

* [in Workflows](https://docs.roboflow.com/deploy/serverless-hosted-api-v2/use-in-a-workflow)
* [with the REST API](https://docs.roboflow.com/deploy/serverless-hosted-api-v2/use-with-the-rest-api)
* with the [Inference Python SDK](https://docs.roboflow.com/deploy/serverless-hosted-api-v2/use-with-python-sdk)

### Inference server

Our Serverless Hosted API is powered by the [Inference Server](https://inference.roboflow.com/api/). This means you can easily switch between our Serverless Hosted API and self-hosting option and vice versa, as shown below:

```python
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    # api_url="http://localhost:9001" # Self-hosted Inference server
    api_url="https://serverless.roboflow.com", # Our Serverless hosted API
    api_key="API_KEY" # optional to access your private models and data
)

result = CLIENT.infer("image.jpg", model_id="model-id/1")
print(result)
```

### Limits

Our Serverless Hosted API supports file uploads up to 20MB. You may run into limitations with higher resolution images. Should you run into an issue, please reach out to your enterprise support contact or post a message to the [forum](https://discuss.roboflow.com).

{% hint style="info" %}
In the cases that requests are too large, we recommend downsizing any attached images. This usually will not result in poor performance as images are downsized regardless after they've been received on our servers to the input size that the model architecture accepts.\
\
Some of our SDKs, like the Python SDK, automatically downsize images to the model architecture's input size before they are sent to the API.
{% endhint %}

***

This is the V2 of our Serverless Hosted API. See [Serverless Hosted API v1](https://docs.roboflow.com/deploy/serverless) for the v1 (legacy) API documentation.
