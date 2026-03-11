# Source: https://docs.edgeimpulse.com/knowledge/concepts/machine-learning/neural-networks/layers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Layers

Neural network architectures can be composed of multiple layers, each with specific roles and functions. These layers act as the building blocks of the network. The configuration and interaction of these layers define the capabilities of different neural network architectures, allowing them to learn from data and perform a wide array of tasks. From the initial data reception in the input layer through various transformation stages in hidden layers, and finally to the output layer where results are produced, each layer contributes to the network's overall intelligence and performance.

<Info>
  #### How can I make sure these layers will work on edge device?

  In Edge AI applications, these layers need to be optimized not just for accuracy, but also for computational and memory efficiency to perform well within the constraints of edge devices. Some architectures may not be suitable for constrained devices because of the computational complexity, resource availability or unsupported operators.

  If you don't know where to start, try out the [EON Tuner](/studio/projects/eon-tuner), our device-aware Auto ML tool.

  Also, feel free to profile your models for edge deployments using our [BYOM](/studio/projects/dashboard/byom) feature or using our [Python SDK](/tools/libraries/sdks/studio/python).
</Info>

With this page, we want to provide an overview of various neural network layers commonly used in edge machine learning.

## Input layer

The input Layer serves as the initial phase of the neural network. It is responsible for receiving all the input data for the model. This layer does not perform any computation or transformation. It simply passes the features to the subsequent layers. The dimensionality of the Input Layer must match the shape of the data you're working with. For instance, in image processing tasks, the input layer's shape would correspond to the dimensions of the image, including the width, height, and color channels.

## Dense layer (or fully connected layer)

A Dense layer, often referred to as a fully connected layer, is the most basic form of a layer in neural networks. Each neuron in a dense layer receives input from all the neurons of the previous layer, hence the term "fully connected". It's a common layer that can be used to process data that has been flattened or transformed from a higher to a lower dimension.

<Frame caption="Dense layer with 5 neurons">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/Fully-Connected-Layer.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=3946f20f11e6dd9900918d57f7ed1347" width="1018" height="786" data-path=".assets/images/Fully-Connected-Layer.png" />
</Frame>

## Reshape layer

The reshape layer is used to change the shape of the input data without altering its contents. It's particularly useful when you need to prepare the dataset for certain types of layers that require the input data to be in a particular shape.

## Flatten layer

Flatten layers are used to convert multi-dimensional data into a one-dimensional array. This is typically done before feeding the data into a Dense layer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/Flatten-ei.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=005a490c230648fae7be21c7c6d4c7c7" width="928" height="735" data-path=".assets/images/Flatten-ei.png" />
</Frame>

## Dropout layer

The dropout layer is a regularization technique that reduces the risk of overfitting in neural networks. It does so by randomly setting a fraction of the input units to zero during each update of the training phase, which helps to make the network more robust and less sensitive to the specific weights of neurons.

<Frame caption="Dropout Layer">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/Dropout.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=dff5e1d134cb07058fc3042767930596" width="1600" height="668" data-path=".assets/images/Dropout.png" />
</Frame>

## 1D convolution layer

The 1D convolution layer is specifically designed for analyzing sequential data, such as audio signals or time-series data. This type of layer applies a series of filters to the input data to extract features. These filters slide over the data to produce a feature map, capturing patterns like trends or cycles that span over a sequence of data points.

<Frame caption="1D Convolution Layer">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1D-Convolution.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=9e921a4d4cb5a5984356d3cb28df8c59" width="1324" height="624" data-path=".assets/images/1D-Convolution.png" />
</Frame>

## 1D pooling layer

Complementing the 1D convolution layer, the 1D pooling layer aims to reduce the spatial size of the feature maps, thus reducing the number of parameters and computation in the network. It works by aggregating the information within a certain window, usually by taking the maximum (Max Pooling) or the average (Average Pooling) of the values. This operation also helps to make the detection of features more invariant to scale and orientation changes in the input data.

<Frame caption="1D Average Pooling Layer">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1D-Average-Pooling.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=efd8888710e335c4e3d1850dee74bf56" width="1410" height="624" data-path=".assets/images/1D-Average-Pooling.png" />
</Frame>

## 2D convolution layer

The 2D convolution layer is used primarily for image data and other two-dimensional input (like spectrograms). This layer operates with filters that move across the input image's height and width to detect patterns like edges, corners, or textures. Each filter produces a 2D activation map that represents the locations and strength of detected features in the input.

<Frame caption="2D Convolution Layer">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/2D-Convolution.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=75210a943d5479dca5e9719b45345e36" width="1600" height="450" data-path=".assets/images/2D-Convolution.png" />
</Frame>

## 2D pooling layer

The 2D Pooling layer serves a similar purpose as its 1D counterpart but in two dimensions. After the convolution layer has extracted features from the input, the pooling layer reduces the spatial dimensions of these feature maps. It summarizes the presence of features in patches of the feature map and reduces sensitivity to the exact location of features. Max Pooling and Average Pooling are common types of pooling operations used in 2D Pooling layers.

<Frame caption="2D Max Pooling Layer">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/2D-Max-Pooling.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=c6308020daed7259509055b7102eef19" width="1438" height="768" data-path=".assets/images/2D-Max-Pooling.png" />
</Frame>

## Output layer

The Output Layer is the final layer in a neural network architecture, responsible for producing the results based on the learned features and representations from the previous layers. Its design is closely aligned with the specific objective of the neural network, such as classification, regression, or even more complex tasks like image segmentation or language translation.

<Info>
  #### Customizing layers in Edge Impulse

  There are two options to modify the layers with Edge Impulse Studio. Either directly from the [Neural Network Architecture](/studio/projects/learning-blocks#neural-network-architecture) panel where you can choose from a wide range of predefined layers, or using the [expert mode](/studio/projects/learning-blocks#expert-mode) to access the TensorFlow/Keras APIs. See below to understand how to [build a model with multiple layers in Expert Mode](/knowledge/concepts/machine-learning/neural-networks/layers#building-a-model-with-multiple-layers-in-expert-mode).

  If you are an experienced ML practitioner, you can also [bring your own model](/studio/projects/dashboard/byom) or [bring your own architecture](/studio/organizations/custom-blocks/custom-learning-blocks).
</Info>

## Building a model with multiple layers in Expert Mode

1. Import the necessary libraries

```python  theme={"system"}
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
```

2. Define your neural network architecture

```python  theme={"system"}
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))
```

3. Compile and train your model

```python  theme={"system"}
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10)
```


Built with [Mintlify](https://mintlify.com).