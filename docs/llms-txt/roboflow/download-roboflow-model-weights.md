# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/download-roboflow-model-weights.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/download-roboflow-model-weights.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/download-roboflow-model-weights.md

# Source: https://docs.roboflow.com/deploy/download-roboflow-model-weights.md

# Download Model Weights

### Automatic Download via Roboflow Inference (Recommended)

[Roboflow Inference](https://inference.roboflow.com/) is our open-source, scalable system for running models locally on CPU and GPU devices.

**This is the fastest and most reliable way to get started**. When you use Inference, you don’t need to manage files or versioning; Roboflow Inference automatically fetches and caches your model weights the first time you run your code.

* **How it works**: On your first inference request, the weights are downloaded from Roboflow’s servers and stored locally. All future predictions use this local cache—images are not sent to the cloud.
* **Deployment options**:
  * [Workflows](https://docs.roboflow.com/workflows/deploy-a-workflow): For production-ready multi-step computer vision workflows
  * [Python inference SDK](https://inference.roboflow.com/quickstart/run_a_model/): For Python integration

### Manual Model Weights Download

Sometimes you may need the raw weights file (e.g., a PyTorch `.pt` file) to run on devices Roboflow does not yet natively support, such as custom Android implementations.

See the [Supported Models table](https://docs.roboflow.com/deploy/supported-models) for weights download compatibility.

{% hint style="warning" %}
**Premium Feature**: Manual weights download is only available for paid users on Core plans and certain Enterprise customers. Read more on our [Pricing page](https://roboflow.com/pricing).
{% endhint %}

#### Method A: Roboflow Platform

Navigate to the Model version within your Project. If your plan allows, clicking the "Download Weights" button will allow you to download the weights . This will provide a file you can convert for use on embedded devices.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FyR3TZH3SjkcIIDt9tjU9%2Fdownload-weights.png?alt=media&#x26;token=21956d62-1eed-49f5-a198-5969c5bac9e2" alt="Download Weights button"><figcaption></figcaption></figure>

#### Method B: Python SDK

You can also use the Roboflow Python package to download weights directly to your directory:

```python
import roboflow

rf = roboflow.Roboflow(api_key="YOUR_API_KEY")
model = rf.workspace().project("PROJECT_ID").version("1").model
model.download() # Downloads 'weights.pt' to your local folder
```

**Note**: Roboflow does not provide technical support for model weights used outside of the Roboflow Inference ecosystem. For the best experience, we recommend using the Inference path outlined in Section 1.
