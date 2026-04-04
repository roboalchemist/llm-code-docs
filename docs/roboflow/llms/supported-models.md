# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/supported-models.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/supported-models.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/supported-models.md

# Source: https://docs.roboflow.com/deploy/supported-models.md

# Supported Models

With Roboflow, you can deploy object detection, segmentation, classification, keypoint, and multimodal models.

These models can be deployed with [Workflows](https://docs.roboflow.com/workflows/what-is-workflows) using:

* [Serverless Hosted API](https://docs.roboflow.com/deploy/serverless-hosted-api-v2)
* [Dedicated Deployment (CPU or GPU)](https://docs.roboflow.com/deploy/dedicated-deployments)
* Self-hosted ([Roboflow Inference](https://inference.roboflow.com/))

The table below shows common models and their support for training, [model weights upload](https://docs.roboflow.com/deploy/upload-custom-weights) and [model weights export/download](https://docs.roboflow.com/deploy/download-roboflow-model-weights).

The table describes models that can be deployed with the Serverless Hosted API.

{% hint style="info" %}
If a model is not supported on a Serverless Hosted API, it must be deployed either with a [Dedicated Deployment](https://docs.roboflow.com/deploy/dedicated-deployments) with a GPU or on your own hardware with Roboflow Inference.
{% endhint %}

All models can be used with [Batch Processing](https://docs.roboflow.com/deploy/batch-processing).

We recommend using Dedicated Deployments or Batch Processing with a GPU configured for optimal performance when using multimodal models.

<table data-full-width="true"><thead><tr><th>Model</th><th>Task Type(s)</th><th data-type="checkbox">Training Supported on Roboflow?</th><th data-type="checkbox">Model Weights Upload Supported?</th><th data-type="checkbox">Model Weights Export Supported?</th><th data-type="checkbox">Supported on Serverless Hosted API</th></tr></thead><tbody><tr><td>Roboflow 3.0</td><td>Object Detection, Classification, Keypoint Detection, Instance Segmentation, Semantic Segmentation</td><td>true</td><td>false</td><td>false</td><td>true</td></tr><tr><td>RF-DETR</td><td>Object Detection, Instance Segmentation</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>YOLO26</td><td>Object Detection, Keypoint Detection, Instance Segmentation</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>YOLOv12</td><td>Object Detection</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>YOLO11</td><td>Object Detection, Instance Segmentation, Keypoint Detection</td><td>true</td><td>true</td><td>true</td><td>true</td></tr><tr><td>YOLOv9</td><td>Object Detection</td><td>false</td><td>true</td><td>true</td><td>true</td></tr><tr><td>YOLOv7</td><td>Instance Segmentation</td><td>false</td><td>true</td><td>false</td><td>true</td></tr><tr><td>YOLOv5</td><td>Object Detection, Instance Segmentation</td><td>false</td><td>true</td><td>false</td><td>true</td></tr><tr><td>Roboflow Instant</td><td>Object Detection</td><td>true</td><td>false</td><td>false</td><td>true</td></tr><tr><td>ViT</td><td>Classification</td><td>true</td><td>false</td><td>false</td><td>true</td></tr><tr><td>ResNet</td><td>Classification</td><td>true</td><td>false</td><td>false</td><td>true</td></tr><tr><td>Dino v3</td><td>Classification</td><td>true</td><td>false</td><td>false</td><td>true</td></tr><tr><td>Florence 2</td><td>Multimodal</td><td>true</td><td>true</td><td>false</td><td>false</td></tr><tr><td>PaliGemma 2</td><td>Multimodal, Object Detection</td><td>true</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Qwen2.5-VL</td><td>Multimodal</td><td>true</td><td>true</td><td>false</td><td>false</td></tr><tr><td>SmolVLM2</td><td>Multimodal</td><td>true</td><td>true</td><td>false</td><td>false</td></tr><tr><td>SmolVLM 256M</td><td>Multimodal</td><td>true</td><td>true</td><td>false</td><td>false</td></tr><tr><td><a href="supported-models/sam3">SAM3</a></td><td>Segmentation</td><td>true</td><td>false</td><td>false</td><td>true</td></tr></tbody></table>

### Models Supported in Workflows

You can run all of the above models in Workflows, as well as other models like Segment Anything 2, CLIP, OpenAI's GPT models, and more. [See a full list of models you can run in a Workflow.](https://inference.roboflow.com/workflows/blocks/#Models)
