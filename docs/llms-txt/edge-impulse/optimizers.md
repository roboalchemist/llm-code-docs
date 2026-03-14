# Source: https://docs.edgeimpulse.com/knowledge/concepts/machine-learning/neural-networks/optimizers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Optimizers

If you are not familiar with optimizers, here is a brief overview of what an optimizer is and its role in machine learning, particularly in neural networks.

An optimizer is an algorithmic entity designed to minimize a specific function called the loss function. The [loss function](/knowledge/concepts/machine-learning/neural-networks/loss-functions) quantitatively expresses the difference between the predicted output of the neural network and the actual target values. Simply put, an optimizer's role is to change the attributes of the neural network, such as weights and learning rate, to reduce this loss., thereby enhancing the network's accuracy.

Optimizers work through an iterative process. They start by calculating the gradient, which is a partial derivative of the loss function. This gradient indicates how much the weights need to be adjusted to minimize the loss. The optimizer then updates the weights in the opposite direction of the gradient. This process is repeated over multiple iterations or epochs until the loss is minimized, and the model's predictions become as accurate as possible.

Each optimizer has its unique way of navigating the path to minimize loss. Here are a few:

* **Adam:** Known for its adaptability, it's especially good for large datasets. **It is used by default in Edge Impulse**.
* **VeLO:** VeLO represents a novel approach where the optimizer is itself a neural network that is trained on prior training jobs. See [Learned Optimizer (VeLO)](/knowledge/concepts/machine-learning/neural-networks/learned-optimizer-velo) dedicated page.
* **Gradient Descent:** Works by iteratively adjusting the values of parameters in the function until the minimum value is reached. In other words, it involves moving downhill along the steepest slope of the function towards its lowest point, hence its name "descent."
* **Stochastic Gradient Descent (SGD):** A more dynamic cousin of Gradient Descent, updating weights more frequently for quicker learning.
* **RMSprop and Adagrad:** These optimizers bring their own tweaks to the learning rate, making the journey smoother in specific scenarios.

<Info>
  #### When to change the optimizer & parameters?

  Not sure which optimizer to use? Have a look at the [Learned Optimizer (VeLO)](/knowledge/concepts/machine-learning/neural-networks/learned-optimizer-velo)!

  Once you have settled on the overall model structure but want to achieve an even better model it can be appropriate to test another optimizer. This is classic hyperparameter fine-tuning where you try and see what works best. Any of these optimizers may achieve superior results, though getting there can sometimes require a lot of tuning. Note that each optimizer has its own parameters that you can customize.

  In Edge Impulse, you can change the **learning rate settings** directly in the [Neural Network settings](/studio/projects/learning-blocks/blocks/classification#neural-network-settings) section. To change the optimizer, you can do this using the expert mode (see the section below).
</Info>

## Changing the optimizer in expert Mode

When using the [Expert mode](/studio/projects/learning-blocks#expert-mode) in Edge Impulse, you can access the full Keras API:

1. Import the necessary libraries:

First, make sure to import the necessary modules from Keras. You'll need the model you're working with (like Sequential) and the optimizer you want to use.

```python  theme={"system"}
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam, SGD, RMSprop  # Import optimizers
```

2. Define your neural network architecture:

Define your model architecture as you normally would. For example, using Sequential:

```python  theme={"system"}
model = Sequential()
# Add model layers like Dense, Conv2D, etc.
```

3. Select an optimizer

Choose the optimizer you wish to use. You can use one of the built-in optimizers in Keras, and even customize its parameters. For example, to use the Adam optimizer with a custom learning rate:

```python  theme={"system"}
optimizer = Adam(learning_rate=0.001)
```

Alternatively, you can use other optimizers like SGD or RMSprop in a similar way:

```python  theme={"system"}
optimizer = SGD(learning_rate=0.01, momentum=0.9)
optimizer = RMSprop(learning_rate=0.001, rho=0.9)
```

4. Compile and train your model with your optimizer

```python  theme={"system"}
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10)
```


Built with [Mintlify](https://mintlify.com).