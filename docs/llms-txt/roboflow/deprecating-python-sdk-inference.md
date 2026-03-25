# Source: https://docs.roboflow.com/changelog/explore-by-month/march-2025/deprecating-python-sdk-inference.md

# Deprecating Python SDK Inference

{% hint style="warning" %}
⚠️ **Deprecated**\
Running inference using the `roboflow` Python SDK was deprecated. This method is no longer actively maintained, and we recommend migrating to the new **Inference SDK** and **Serverless Hosted APIs** for all current and future projects.
{% endhint %}

## What's Changed?

Roboflow has introduced more powerful and flexible inference options, including:

* Native support for **all models**
* Access to **foundation models** (YOLO-World, CLIP, OCR, SAM, Florence2, etc.)
* Improved performance and latency using **GPU-accelerated infrastructure**
* A simplified and unified inference endpoint

***

### Use These Instead

<table data-view="cards"><thead><tr><th></th></tr></thead><tbody><tr><td><h4><a href="https://inference.roboflow.com">Inference SDK</a></h4><p>Use this package for running inference across a wide range of model types, with local and hosted backends supported out-of-the-box. It supports modern use cases like versionless models and foundation models.<br></p><p>👉 Explore: <a href="https://inference.roboflow.com">https://inference.roboflow.com</a></p></td></tr><tr><td><h4><a href="https://docs.roboflow.com/deploy/serverless-hosted-api-v2">Serverless Hosted API V2</a></h4><p>A GPU-accelerated cloud API with unified endpoints for all tasks. Offers lower latency for inference requests and support for powerful models such as Florence2 and SAM2.<br></p><p>🔗 Learn more: <a href="https://app.gitbook.com/s/-M6S9nPJhEX9FYH6clfW/deploy/serverless-hosted-api-v2">Serverless Hosted API V2 Documentation</a></p></td></tr><tr><td><h4><a href="https://docs.roboflow.com/deploy/serverless">Serverless API</a></h4><p>If you're using older models or workflows, the original serverless API is still available. This includes individual endpoints for object detection, classification, segmentation, and more.</p><p>🔗 Learn more: <a href="https://docs.roboflow.com/deploy/serverless">Serverless Hosted API (V1)</a></p></td></tr></tbody></table>

### Why Deprecate the Python SDK Inference Method?

While the `roboflow` Python SDK remains useful for other interactions (e.g., uploading data, managing datasets), its inference capabilities have been replaced by more efficient and modern solutions:

* It does not support all models (models uploaded without dataset version, Roboflow Instant)
* It offers **limited access** to newer model types
* It lacks performance improvements found in GPU-accelerated APIs
* It is not compatible with newer deployment workflows

***

### Need Help Migrating?

If you're using the legacy SDK for inference and want help transitioning to the new tools, check out our guides at:

* 🔧 <https://inference.roboflow.com>
* 📘 [Roboflow Documentation](https://docs.roboflow.com)
