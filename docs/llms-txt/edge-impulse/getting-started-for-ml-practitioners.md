# Source: https://docs.edgeimpulse.com/knowledge/guides/getting-started-for-ml-practitioners.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting started for machine learning practitioners

Welcome to Edge Impulse! Whether you are a machine learning engineer, MLOps engineer, data scientist, or researcher, we have developed professional tools to help you build and optimize models to run efficiently on any edge device.&#x20;

In this guide, we'll explore how Edge Impulse empowers you to bring your expertise and your own models to the world of edge AI using either the Edge Impulse Studio, our visual interface, and the Edge Impulse Python SDK, available as a pip package.

<iframe src="https://www.youtube.com/embed/Mw1L4URFshk" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Why Edge Impulse, for ML practitioners?

**Flexibility:** You can choose to work with the tools they are already familiar with and import your models, architecture, and feature processing algorithms into the platform. This means that you can leverage your existing knowledge and workflows seamlessly. Or, for those who prefer an all-in-one solution, Edge Impulse provides enterprise-grade tools for your entire machine-learning pipeline.

**Optimized for edge devices**: Edge Impulse is designed specifically for deploying machine learning models on edge devices, which are typically resource-constrained, from low-power MCUs up to powerful edge GPUs. We provide tools to optimize your models for edge deployment, ensuring efficient resource usage and peak performance. Focus on developing the best models, we will provide feedback on whether they can run on your hardware target!&#x20;

**Data pipelines:** We developed a strong expertise in complex data pipelines (including clinical data) while working with our customers. We support data coming from multiple sources, in any format, and provide tools to perform data alignment and validation checks. All of this in customizable multi-stage pipelines. This means you can build gold-standard labeled datasets that can then be imported into your project to train your models.

### Getting started in a few steps

In this getting started guide, we'll walk you through the two different approaches to bringing your expertise to edge devices. Either starting from your dataset or from an existing model.

First, start by creating your [Edge Impulse account](https://studio.edgeimpulse.com/signup).

<Tabs>
  <Tab title="Start with existing data">
    #### Start with existing data

    You can import data using [Studio Uploader](/studio/projects/data-acquisition/uploader), [CLI Uploader](/docs/tools//edge-impulse-cli/cli-uploader), or our [Ingestion API](/apis/ingestion). These allow you to easily upload and manage your existing data samples and datasets to Edge Impulse Studio.

    We currently accept various file types, including `.cbor`, `.json`, `.csv`, `.wav`, `.jpg`, `.png`, `.mp4`, and `.avi`.&#x20;

    If you are working with **image datasets**, the Studio uploader and the CLI uploader currently handle these types of [dataset annotation formats](/knowledge/guides/getting-started-for-ml-practitioners#understanding-image-dataset-annotation-formats): Edge Impulse object detection, COCO JSON, Open Images CSV, Pascal VOC XML, Plain CSV, and YOLO TXT.

    <Info>
      #### Organization data

      Since the creation of Edge Impulse, we have been helping our customers deal with complex data pipelines, complex data transformation methods and complex clinical validation studies.

      The organizational data gives you tools to centralize, validate and transform datasets so they can be easily imported into your projects.

      See the [Organization data](/studio/organizations/data) documentation.
    </Info>

    To visualize how your labeled data items are clustered, use the [Data explorer](/studio/projects/data-acquisition/data-explorer) feature available for most dataset types, where we apply dimensionality reduction techniques (t-SNE or PCA) on your embeddings.

    To **extract features** from your data items, either choose an available [processing block](/studio/projects/processing-blocks) (MFE, MFCC, spectral analysis using FFT or Wavelets, etc.) or [create your own](/studio/organizations/custom-blocks/custom-processing-blocks) from your expertise. These can be written in any language.

    Similarly, to **train your machine learning model**, you can choose from different [learning blocks](/studio/projects/learning-blocks) (Classification, Anomaly Detection, Regression, Image or Audio Transfer Learning, Object Detection). In most of these blocks, we expose the Keras API in an [expert mode](/studio/projects/learning-blocks/expert-mode). You can also bring your own architecture/training pipeline as a [custom learning block](/studio/organizations/custom-blocks/custom-learning-blocks).&#x20;

    Each block will provide on-device performance information showing you the estimated **RAM, flash, and latency.**
  </Tab>

  <Tab title="Start with an existing model">
    #### Start with an existing model

    If you already have been working on different models for your Edge AI applications, Edge Impulse offers an easy way to upload your models and profile them. This way, in just a few minutes, you will know if your model can run on real devices and what will be the on-device performances (RAM, flash usage, and latency).&#x20;

    You can do this directly from the [Studio BYOM feature](/studio/projects/dashboard/byom) or using [Edge Impulse Python SDK](/tools/libraries/sdks/studio/python).

    Edge Impulse Python SDK is available as a `pip` package:

    ```sh  theme={"system"}
    python -m pip install edgeimpulse
    ```

    From there, you can profile your existing models:

    ```python  theme={"system"}
    import edgeimpulse as ei
    ei.API_KEY = "ei_dae27..."
    profile = ei.model.profile(model=model, device='cortex-m4f-80mhz')
    print(profile.summary())
    ```

    And then directly generate a customizable library or any other supported [deployment type](/studio/projects/deployment)

    ```python  theme={"system"}
    ei.model.deploy(model=model,
                    model_output_type=ei.model.output_type.Classification(),
                    deploy_target='zip')
    ```
  </Tab>
</Tabs>

#### Run the inference on a device

You can easily [export your model](/studio/projects/deployment) in a `.eim` format, a Linux executable that contains your signal processing and ML code, compiled with optimizations for your processor or GPU. This executable can then be called with our [Linux inferencing libraries](/tools/libraries/sdks/inference/linux). We have inferencing libraries and examples for Python, Node.js, C++, and Go.

If you target MCU-based devices, you can generate ready-to-flash binaries for all the officially supported hardware targets. This method will let you test your model on real hardware very quickly.&#x20;

In both cases, we will provide profiling information about your models so you can make sure your model will fit your edge device constraints.

### Tutorials and resources, for ML practitioners

#### End-to-end tutorials

If you want to get familiar with the full end-to-end flow using Edge Impulse Studio, please have a look at our end-to-end [tutorials](/tutorials):

* [Motion recognition + anomaly detection](/tutorials/end-to-end/motion-recognition),&#x20;
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting),&#x20;
* [Sound recognition](/tutorials/end-to-end/sound-recognition),&#x20;
* [Image classification](/tutorials/end-to-end/image-classification/),&#x20;
* [Object detection using bounding boxes (size and location)](/tutorials/end-to-end/object-detection-bounding-boxes),
* [Object detection using centroids (location)](/tutorials/end-to-end/object-detection-centroids)

To understand the full potential of Edge Impulse, see our [**health reference design**](/knowledge/guides/reference-designs/health-reference-design) that describes an end-to-end ML workflow for building a wearable health product using Edge Impulse. It handles data coming from multiple sources, data alignment, and a multi-stage pipeline before the data is imported into an Edge Impulse project.

#### Edge Impulse Python SDK tutorials

While the Edge Impulse Studio is a great interface for guiding you through the process of collecting data and training a model, the [edgeimpulse](https://pypi.org/project/edgeimpulse/) Python SDK allows you to programmatically Bring Your Own Model (BYOM), developed and trained on any platform:

* [Using the Edge Impulse Python SDK with TensorFlow and Keras](/tutorials/tools/sdks/studio/python/use-tf-keras)
* [Using the Edge Impulse Python SDK with Hugging Face](/tutorials/tools/sdks/studio/python/use-hugging-face)
* [Using the Edge Impulse Python SDK with Weights & Biases](/tutorials/tools/sdks/studio/python/use-wandb)
* [Using the Edge Impulse Python SDK with SageMaker Studio](/tutorials/tools/sdks/studio/python/use-sagemaker-studio)

#### Other useful resources

* [Expert mode](/studio/projects/learning-blocks/blocks/classification#expert-mode) (access Keras API in the studio)
* [BYOM (Bring Your Own Model)](/studio/projects/dashboard/byom)
* [Custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks)
* [Generate synthetic datasets](/tutorials/topics/data/generate-image-data-dall-e)

#### Integrations

* [Weight & Biases](/tutorials/integrations/weights-and-biases)
* [NVIDIA Omniverse](/tutorials/integrations/nvidia-omniverse)


Built with [Mintlify](https://mintlify.com).