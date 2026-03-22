# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/serverless-hosted-api-v2/use-with-python-sdk.md

# Source: https://docs.roboflow.com/deploy/serverless-hosted-api-v2/use-with-python-sdk.md

# Use with Python SDK

If you are working in Python, the most convenient way to interact with the Serverless API is to use the Inference Python SDK.

To use the [Inference SDK](https://inference.roboflow.com/inference_helpers/inference_sdk/), first install it:

```
pip install inference-sdk
```

To make a request to the Serverless Hosted API, use the following code:

<pre class="language-python"><code class="lang-python"><strong>from inference_sdk import InferenceHTTPClient
</strong>
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="API_KEY"
)

result = CLIENT.infer("image.jpg", model_id="model-id/1")
print(result)
</code></pre>

Above, specify your [model ID](https://docs.roboflow.com/developer/authentication/workspace-and-project-ids) and [API key](https://docs.roboflow.com/developer/authentication/find-your-roboflow-api-key). This code will run your model and return the results.

#### Roboflow Instant Model

Serverless API also supports running Roboflow [Instant Model](https://docs.roboflow.com/train/roboflow-instant). You can run Instant Model just like any other model, just note that the confidence threshold can be sensitive for Instant Models.

{% hint style="info" %}
An optimal confidence depends on the number of images the model has been trained on. Optimal confidence thresholds usually range from 0.85 to 0.99.
{% endhint %}

```python
configuration = InferenceConfiguration(
    confidence_threshold=0.95
)
CLIENT.configure(configuration)

result = CLIENT.infer("image.jpg", model_id="roboflow-instant-model-id/1")
```
