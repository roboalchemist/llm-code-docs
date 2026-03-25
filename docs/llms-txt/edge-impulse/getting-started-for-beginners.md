# Source: https://docs.edgeimpulse.com/knowledge/guides/getting-started-for-beginners.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting started for beginners

Welcome to Edge Impulse! If you're new to the world of edge machine learning, you've come to the right place. This guide will walk you through the essential steps to get started with Edge Impulse, a suite of engineering tools for building, training, and deploying machine learning models on edge devices.

<iframe src="https://www.youtube.com/embed/r1bjEn6UApI" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

> Check out our [Edge AI Fundamentals course](/knowledge/courses/edge-ai-fundamentals/intro-to-edge-ai) to learn more about edge computing, machine learning, and edge MLOps.

### Why Edge Impulse, for beginners?

Edge Impulse empowers you to bring intelligence to your embedded projects by enabling devices to understand and respond to their environment. Whether you want to recognize sounds, identify objects, or detect motion, Edge Impulse makes it accessible and straightforward. Here's why beginners like you are diving into Edge Impulse:

* **No Coding Required:** You don't need to be a coding expert to use Edge Impulse. Our platform provides a user-friendly interface that guides you through the process - this includes many optimized preprocessing and learning blocks, various neural network architectures, and pre-trained models and can generate ready-to-flash binaries to test your models on real devices.
* **Edge Computing:** Your machine learning models are optimized to run directly on your edge devices, ensuring low latency and real-time processing.
* **Support for Various Sensors:** Edge Impulse supports a wide range of sensors, from accelerometers and microphones to cameras, making it versatile for different projects.
* **Community and Resources:** You're not alone on this journey. Edge Impulse offers a supportive community and extensive documentation to help you succeed.

### Getting started in a few steps

Ready to begin? Follow these simple steps to embark on your Edge Impulse journey:

#### 1. Sign up

Start by creating an [Edge Impulse account](https://studio.edgeimpulse.com/signup). It's free to get started, and you'll gain access to all the tools and resources you need.

#### 2. Create a project

Once you're logged in, create your first [project](/studio/projects/dashboard). Give it a name that reflects your project's goal, whether it's recognizing sounds, detecting objects, or something entirely unique.

#### 3. Collect/import data

To teach your device, you need data. Edge Impulse provides[ user-friendly tools](/studio/projects/data-acquisition) for collecting data from your sensors, such as recording audio, capturing images, or reading sensor values. We recommend using a [hardware target from this list](/hardware) or your [smartphone](/hardware/devices/mobile-phone) to start collecting data when you begin with Edge Impulse.

You can also [import existing datasets](/studio/projects/data-acquisition/uploader) or clone a [public project](https://edgeimpulse.com/projects/overview) to get familiar with the platform.

<Info>
  #### Edge Impulse Datasets

  Need inspiration? Check out our [Edge Impulse datasets collection](/datasets) that contains publicly available datasets collected, generated or curated by Edge Impulse or its partners.

  These datasets highlight specific use cases, helping you understand the types of data commonly encountered in projects like object detection, audio classification, and visual anomaly detection.
</Info>

#### 4. Label your data

Organize your data by labeling it. For example, if you're working on sound recognition, label audio clips with descriptions like "dog barking" or "car horn." You can label your data as you collect it or add labels later, our [data explorer](/studio/projects/data-acquisition/data-explorer) is also particularly useful to understand your data.

#### 5. Pre-process your data and train your model

This is where the magic happens. Edge Impulse offers an intuitive model training process through [processing blocks](/studio/projects/processing-blocks) and [learning blocks](/studio/projects/learning-blocks). You don't need to write complex code; the platform guides you through feature extraction, model creation, and training.

#### 6. Run the inference on a device

After training your model, you can easily [export your model](/studio/projects/deployment) to run in a web browser or on your smartphone, but you can also run it on a wide variety of edge devices, whether it's a Raspberry Pi, Arduino, or other compatible hardware. We also provide ready-to-flash binaries for all the officially supported hardware targets. You don't even need to write embedded code to test your model on real devices!&#x20;

If you have a device that is not supported, no problem, you can export your model as a C++ library that runs on any embedded device. See [Running C++ libraries](/hardware/deployments/run-cpp-overview) for more information.

#### 7. Go further

Building Edge AI solutions is an iterative process. Feel free to try our [organization hub](/studio/organizations/dashboard) to automate your machine-learning pipelines, collaborate with your colleagues, and create custom blocks.

### Tutorials and resources for beginners

The end-to-end tutorials are perfect for learning how to use Edge Impulse Studio. Try the tutorials:

* [Motion recognition + anomaly detection](/tutorials/end-to-end/motion-recognition)
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification/)
* [Object detection using bounding boxes (size and location)](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Object detection using centroids (location)](/tutorials/end-to-end/object-detection-centroids)

These will let you build machine-learning models that detect things in your home or office.

### Join the Edge Impulse Community

Remember, you're not alone on your journey. Join the [Edge Impulse community](https://forum.edgeimpulse.com) to connect with other beginners, experts, and enthusiasts. Share your experiences, ask questions, and learn from others who are passionate about embedded machine learning.

Now that you have a roadmap, it's time to explore Edge Impulse and discover the exciting possibilities of embedded machine learning. Let's get started!


Built with [Mintlify](https://mintlify.com).