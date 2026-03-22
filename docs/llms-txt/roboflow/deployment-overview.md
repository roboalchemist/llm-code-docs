# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/deployment-overview.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/deployment-overview.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/deployment-overview.md

# Source: https://docs.roboflow.com/deploy/deployment-overview.md

# Deploy a Model or Workflow

We support both managed deployments and self-hosted deployment of both models and workflows.

### Managed Deployments

These options leverage Roboflow's cloud infrastructure to run your models and workflows, eliminating the need for you to manage your own hardware or software.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Serverless Hosted API</strong></td><td>Get started immediately and scale automatically.</td><td><a href="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FoKW42bcMX8fDUOccDDeX%2Fserverless-bg.png?alt=media&#x26;token=8845f5bc-4ab5-41d3-9c19-c80e007656f7">serverless-bg.png</a></td><td><a href="serverless-hosted-api-v2">serverless-hosted-api-v2</a></td></tr><tr><td><strong>Dedicated Deployment</strong></td><td>For large models and predictable workloads.</td><td><a href="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FQ9lPa8CUrDY2khi93tuV%2Fbox-bg.png?alt=media&#x26;token=c2f28bf9-77eb-40f9-8997-ff0fe0affda7">box-bg.png</a></td><td><a href="dedicated-deployments">dedicated-deployments</a></td></tr><tr><td><strong>Batch Processing</strong></td><td>Cost-effective processing of stored data.</td><td><a href="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FkmKoibwSR9GIaxKExJo3%2Fbatchpbg.png?alt=media&#x26;token=9b5e1757-d8c2-40ac-9e6a-6bb64ae7907b">batchpbg.png</a></td><td><a href="batch-processing">batch-processing</a></td></tr></tbody></table>

### Self-Hosted Deployment

You can also deploy your models and workflows on self-hosted [Roboflow Inference](https://inference.roboflow.com/), which provides greater control over your environment, resources, and latency.

* [Self-hosting on your own cloud server](https://inference.roboflow.com/install/cloud/)
* [Self-hosting on an Edge device](https://inference.roboflow.com/install/)

{% hint style="info" %}
This option requires infrastructure management and expertise.
{% endhint %}

<details>

<summary>What is Inference?</summary>

{% hint style="info" %}
In computer vision, inference refers to the process of using a trained model to analyze new images or videos and make predictions. For example, an object detection model might be used to identify and locate objects in a video stream, or a classification model might be used to categorize images based on their content.
{% endhint %}

[***Roboflow Inference***](https://inference.roboflow.com/) is an open-source project that provides a powerful and flexible framework for deploying computer vision models and workflows. It is s the engine that powers most of Roboflows managed deployment services. You can also self host it or use it to deploy your vision workflows to edge devices. Roboflow Inference offers a range of features and capabilities, including:

* Support for various model architectures and tasks, including object detection, classification, instance segmentation, and more.
* Workflows, which lets you build computer vision applications by combining different models, pre-built logic, and external applications by choosing from hundreds of building Blocks.
* Hardware acceleration for optimized performance on different devices, including CPUs, GPUs, and edge devices like NVIDIA Jetson.
* Multiprocessing for efficient use of resources.
* Video decoding for seamless processing of video streams.
* HTTP interface, APIs and docker images to simplify deployment
* Integration with Roboflow's hosted deployment options and the Roboflow platform.

</details>

<details>

<summary>What is a Workflow?</summary>

[Workflows](https://github.com/roboflow-ai/roboflow-docs/blob/main/deploy/deployment-overview/broken-reference/README.md) enable you to build complex computer vision applications by combining different models, pre-built logic, and external applications. They provide a visual, low-code environment for designing and deploying sophisticated computer vision pipelines.

With Workflows, you can:

* Chain multiple models together to perform complex tasks.
* Add custom logic and decision-making to your applications.
* Integrate with external systems and APIs.
* Track, count, time, measure, and visualize objects in images and videos.

</details>

### Choosing the Right Deployment Option

{% hint style="info" %}
There is great guide on how to choose the best deployment method for your use case in the inference [Getting Started guide](https://inference.roboflow.com/start/getting-started/).&#x20;
{% endhint %}

The best deployment option for you depends on your specific needs and requirements. Consider the following factors when making your decision:

* Scalability: If your application needs to handle varying levels of traffic or data volume, the serverless API offers excellent scalability for real-time use-cases; otherwise, [Batch Processing](https://docs.roboflow.com/deploy/batch-processing) is a suggested option.
* Latency: If you need low latency or video processing, dedicated deployments or self-hosted deployments with powerful hardware might be the best choice.
* Control: Self-hosted deployments provide the most control over your environment and resources.
* Expertise: Self-hosted deployments require more technical expertise to set up and manage.
