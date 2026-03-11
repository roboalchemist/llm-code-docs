# Source: https://docs.edgeimpulse.com/knowledge/guides/getting-started-for-embedded-engineers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting started for embedded engineers

Welcome to Edge Impulse! When we started Edge Impulse, we initially focused on developing a suite of engineering tools designed to empower embedded engineers to harness the power of machine learning on edge devices. As we grew, we also started to develop advanced tools for ML practitioners to ease the collaboration between teams in organizations.

In this getting started guide, we'll walk you through the essential steps to dive into Edge Impulse and leverage it for your embedded projects.

### Why Edge Impulse, for embedded engineers?

Embedded systems are becoming increasingly intelligent, and Edge Impulse is here to streamline the integration of machine learning into your hardware projects. Here's why embedded engineers are turning to Edge Impulse:

* **Extend hardware capabilities:** Edge Impulse can extend hardware capabilities by enabling the integration of machine learning models, allowing edge devices to process complex tasks, recognize patterns, and make intelligent decisions that are complex to develop using rule-based algorithms.
* **Open-source export formats:** Exported models and libraries contain both digital signal processing code and machine learning models, giving you full explainability of the code.
* **Powerful integrations:** Edge Impulse provides complete and documented integrations with various hardware platforms, allowing you to focus on the application logic rather than the intricacies of machine learning.
* **Support for diverse sensors:** Whether you're working with accelerometers, microphones, cameras, or custom sensors, Edge Impulse accommodates a wide range of data sources for your projects.
* **Predict on-device performances:** Models trained in Edge Impulse run directly on your edge devices, ensuring real-time decision-making with minimal latency. We provide tools to ensure the DSP and models developed with Edge Impulse can fit your device constraints.
* **Device-aware optimization:** You have full control over model optimization, enabling you to tailor your machine-learning models to the specific requirements and constraints of your embedded systems. Our [EON tuner](/studio/projects/eon-tuner) can help you select the best model by training many different variants of models only from an existing dataset and your device constraints!

### Getting started in a few steps

Ready to embark on your journey with Edge Impulse? Follow these essential steps to get started:

#### 1. Sign Up

Start by creating your [Edge Impulse account](https://studio.edgeimpulse.com/signup). Registration is straightforward, granting you immediate access to the comprehensive suite of tools and resources.

#### 2. Create a Project

Upon logging in, initiate your first project. Select a name that resonates with your project's objectives. If you already which hardware target or system architecture you will be using, you can set it up directly in the [dashboard's project info](/studio/projects/dashboard#6-project-info) section. This will help you to make sure your model fits your device constraints.

#### 3. Data Collection and Labeling

We offer various methods to collect data from your sensors or to import datasets (see [Data acquisition](/studio/projects/data-acquisition) for all methods). For the [officially supported hardware targets](/hardware), we provide binaries or simple steps to attach your device to Edge Impulse Studio and collect data from the Studio. However, as an embedded engineer, you might want to collect data from sensors that are not necessarily available on these devices. To do so, you can use the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) and print out your sensor values over serial (up to 8kHz) or use our [C Ingestion SDK](/tools/libraries/sdks/ingestion/c), a portable header-only library (designed to reliably store sampled data from sensors at a high frequency in very little memory).

#### 4. Pre-process your data and train your model

Edge Impulse offers an intuitive model training process through [processing blocks](/studio/projects/processing-blocks) and [learning blocks](/studio/projects/learning-blocks). You don't need to write Python code to train your model; the platform guides you through feature extraction, model creation, and training. Customize and fine-tune your blocks for optimal performance on your hardware. Each block will provide on-device performance information showing you the estimated **RAM, flash, and latency.**

#### 5. Run the inference on a device

This is where the fun start, you can easily [export your model](/studio/projects/deployment) as ready-to-flash binaries for all the officially supported hardware targets. This method will let you test your model on real hardware very quickly.

In addition, we also provide a wide variety of export methods to easily integrate your model with your application logic. See [C++ library](/hardware/deployments/run-cpp-desktop) to **run your model on any device that supports C++** or our guides for [Arduino library](/hardware/deployments/run-arduino-2-0), [Cube.MX CMSIS-PACK](/hardware/deployments/run-cubemx), [DRP-AI library](/hardware/deployments/run-drpai-rzv2l), [DRP-AI TVM i8 library](/hardware/deployments/run-drpai-rzv2h), [OpenMV library](/hardware/deployments/run-openmv), Ethos-U library, Meta TF model, Simplicity Studio Component, Tensai Flow library, TensorRT library, TIDL-RT library, etc...

<Info>
  The C++ inferencing library is a portable library for digital signal processing and machine learning inferencing, and it contains native implementations for both processing and learning blocks in Edge Impulse. It is written in C++11 with all dependencies bundled and can be built on both desktop systems and microcontrollers.\
  \
  See [Inferencing SDK](/tools/libraries/sdks/inference/cpp) documentation.
</Info>

#### 6. Go further

Building Edge AI solutions is an iterative process. Feel free to try our [organization hub](/studio/organizations/dashboard) to automate your machine-learning pipelines, collaborate with your colleagues, and create custom blocks.

### Tutorials and resources, for embedded engineers

#### End-to-end tutorials

If you want to get familiar with the full end-to-end flow, please have a look at our end-to-end tutorials:

* [Motion recognition + anomaly detection](/tutorials/end-to-end/motion-recognition),&#x20;
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting),&#x20;
* [Sound recognition](/tutorials/end-to-end/sound-recognition),&#x20;
* [Image classification](/tutorials/end-to-end/image-classification/),&#x20;
* [Object detection using bounding boxes (size and location)](/tutorials/end-to-end/object-detection-bounding-boxes),
* [Object detection using centroids (location)](/tutorials/end-to-end/object-detection-centroids)

#### Additional tutorials

In the other tutorial sections, you will discover useful techniques categorized by topics within the ML Ops workflow, Edge Impulse tools, and third party integrations. Please refer to the [tutorials](/tutorials) page for more information.

#### Other useful resources

* [EON compiler](/studio/projects/deployment/eon-compiler)
* [Inference performance metrics](/knowledge/metrics/inference-performance)

### Join the Edge Impulse Community

Edge Impulse offers a [thriving community](https://forum.edgeimpulse.com) of embedded engineers, developers, and experts. Connect with like-minded professionals, share your knowledge, and collaborate to enhance your embedded machine-learning projects.

Now that you have a roadmap, it's time to explore Edge Impulse and discover the exciting possibilities of embedded machine learning. Let's get started!


Built with [Mintlify](https://mintlify.com).