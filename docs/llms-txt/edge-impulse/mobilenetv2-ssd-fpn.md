# Source: https://docs.edgeimpulse.com/studio/projects/learning-blocks/blocks/object-detection/mobilenetv2-ssd-fpn.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MobileNetV2 SSD FPN

It's very hard to build a computer vision model from scratch, as you need a wide variety of input data to make the model generalize well, and training such models can take days on a GPU. To make building your model easier and faster we are using transfer learning. This lets you piggyback on a well-trained model, only re-training the upper layers of a neural network, leading to much more reliable models that train in a fraction of the time and work with substantially smaller datasets.

<Info>
  **Tutorial**

  Want to see **MobileNetV2 SSD FPN-Lite** models in action? Check out our [Detect objects with bounding boxes](/tutorials/end-to-end/object-detection-bounding-boxes) tutorial.
</Info>

## How to get started?

To build your first object detection models using MobileNetV2 SSD FPN-Lite:

1. Create a new project in Edge Impulse.
2. Make sure to set your labelling method to 'Bounding boxes (object detection)'.
3. Collect and prepare your dataset as in [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
4. Resize your image to fit 320x320px
5. Add an 'Object Detection (Images)' block to your impulse.
6. Under **Images**, choose RGB.
7. Under **Object detection**, select 'Choose a different model' and select 'MobileNetV2 SSD FPN-Lite 320x320'
8. You can start your training with a learning rate of '0.15'

<Frame caption="Select model">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-detection-select-model.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=c4b97013f298269ebed3fb1647ef586b" width="1291" height="1000" data-path=".assets/images/object-detection-select-model.png" />
</Frame>

1. Click on 'Start training'

<Frame caption="Object Detection view">
  <img src="https://mintcdn.com/edgeimpulse/Z1Offd_0m7N7yP2K/.assets/images/object-detection-view.png?fit=max&auto=format&n=Z1Offd_0m7N7yP2K&q=85&s=4b8bb371405059a751be5e78959e6052" width="1600" height="854" data-path=".assets/images/object-detection-view.png" />
</Frame>

MobileNetV2 SSD FPN-Lite 320x320 is available with [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux)

## How does this 🪄 work?

Here, we are using the MobileNetV2 SSD FPN-Lite 320x320 pre-trained model. The model has been trained on the COCO 2017 dataset with images scaled to 320x320 resolution.

In the MobileNetV2 SSD FPN-Lite, we have a **base network** (MobileNetV2), a **detection network** (Single Shot Detector or SSD) and a **feature extractor** (FPN-Lite).

**Base network:**

MobileNet, like VGG-Net, LeNet, AlexNet, and all others, are based on neural networks. The base network provides high-level features for classification or detection. If you use a fully connected layer and a softmax layer at the end of these networks, you have a classification.

<Frame caption="Example of a network composed of many convolutional layers. Filters are applied to each training image at different resolutions, and the output of each convolved image is used as input to the next layer (source Mathworks)">
  <img src="https://mintcdn.com/edgeimpulse/Vf24THMl-WGxho9U/.assets/images/cnn-network-example.jpeg?fit=max&auto=format&n=Vf24THMl-WGxho9U&q=85&s=9b8ab77ef8373ab1a708dc94cfb3b9ef" width="1000" height="340" data-path=".assets/images/cnn-network-example.jpeg" />
</Frame>

But you can remove the fully connected and the softmax layers, and replace it with detection networks, like SSD, Faster R-CNN, and others to perform object detection.

**Detection network:**

The most common detection networks are **SSD (Single Shot Detection)** and **RPN (Regional Proposal Network)**.

When using SSD, we only need to take one single shot to detect multiple objects within the image. On the other hand, regional proposal networks (RPN) based approaches, such as R-CNN series, need two shots, one for generating region proposals, one for detecting the object of each proposal.

As a consequence, SSD is much faster compared with RPN-based approaches but often trades accuracy with real-time processing speed. They also tend to have issues in detecting objects that are too close or too small.

**Feature Pyramid Network:**

Detecting objects in different scales is challenging in particular for small objects. Feature Pyramid Network (FPN) is a feature extractor designed with feature pyramid concept to improve accuracy and speed.


Built with [Mintlify](https://mintlify.com).