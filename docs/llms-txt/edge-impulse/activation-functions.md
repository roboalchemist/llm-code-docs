# Source: https://docs.edgeimpulse.com/knowledge/concepts/machine-learning/neural-networks/activation-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Activation functions

An activation function is a mathematical equation that determines the output of a neural network node, or "neuron." It adds non-linearity to the network, allowing it to learn complex patterns in the data. Without activation functions, a neural network would simply be a linear regression model, incapable of handling complex tasks like image recognition or language processing.

## Types of activation functions in neural networks

Several activation functions are used in neural networks, each with its characteristics and typical use cases. Some of the most common include:

* **ReLU (Rectified Linear Unit)**: It allows only positive values to pass through, introducing non-linearity. ReLU is efficient and widely used in deep learning. It is used by default in Edge Impulse for hidden layers.
* **Sigmoid**: This function maps values into a range between 0 and 1, **making it ideal for binary classification problems.**
* **Tanh (Hyperbolic Tangent)**: Similar to the sigmoid but maps values between -1 and 1. It is useful in hidden layers of a neural network.
* **Softmax**: Often used in the output layer of a neural network **for multi-class classification**; it turns logits into probabilities that sum to one.
* **Leaky ReLU**: A variation of ReLU, it allows a small, non-zero gradient when the unit is not active.

<Info>
  #### When to use different activation functions

  The choice of activation function depends on the specific task and the characteristics of the input and output data. For instance:

  **ReLU** and its variants are generally preferred **in hidden layers** due to their computational efficiency.

  **Sigmoid** or **Softmax** functions are often used in the **output layer** for binary and multi-class classification tasks, respectively.

  Note that for regression tasks, the last layer is connected to the target variable `y_pred`. Thus, there is no need for an activation function in the output layer (like sigmoid or softmax).

  Please note that the default activation functions in Edge Impulse have been selected to work well for your project tasks. We would advise you to primarily focus on your dataset quality and neural network architecture to improve your model performances.
</Info>

## Implementing activation functions in Expert Mode

In Edge Impulse, the [Expert Mode](/studio/projects/learning-blocks#expert-mode) allows for advanced customization, including the use of custom activation functions. Here is how you can do it:

1. Import the necessary libraries

```python  theme={"system"}
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation  # Import activation functions
```

2. Define your neural network architecture

When adding layers to your model, specify the activation function you want to use:

```python  theme={"system"}
model = Sequential()
model.add(Dense(units=64, activation='relu'))  # Using ReLU activation
model.add(Dense(units=10, activation='softmax'))  # Using Softmax for output layer
```

3. Compile and train your model:

```python  theme={"system"}
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10)
```


Built with [Mintlify](https://mintlify.com).