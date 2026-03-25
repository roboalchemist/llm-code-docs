# Source: https://docs.edgeimpulse.com/knowledge/concepts/machine-learning/neural-networks/loss-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Loss functions

A loss function, also known as a cost function, is a method to measure the performance of a machine learning model. Essentially, it calculates the difference between the model's predictions and the actual target values. The goal of training a neural network is to minimize this difference, thereby improving the model's accuracy.

The loss function quantifies how well the model is performing. A higher loss indicates greater deviation from the actual values, while a lower loss signifies that the model's predictions are closer to the target values.

<Info>
  #### What's the difference between the loss function and the optimizer?

  **Loss Function:** The loss function is a mathematical expression that measures the difference or 'error' between the actual output (prediction) of a model and the desired output (label). It helps us evaluate how well our model is performing. In other words, it quantifies the cost of misclassification.

  **Optimizer:** An optimizer is an algorithmic entity designed to minimize the loss function. Its goal is to adjust the parameters (weights and biases) of a neural network in such a way that the loss is minimized. This is typically done through iterative processes like gradient descent or its variations. The optimizer calculates the partial derivative of the loss with respect to each parameter, which indicates the direction and magnitude of changes needed to reduce the loss.

  So, while the loss function quantifies how 'wrong' our model is, the optimizer tries to minimize this error by changing the parameters of the model.
</Info>

## Types of loss functions

Each type of neural network task generally has a different loss function that is most suitable for it. Here are some of the common loss functions used:

* **Mean Squared Error (MSE):** Used primarily for regression problems. It calculates the square of the difference between the predicted values and the actual values. It can be used for both single-step prediction tasks and time series forecasting problems. The goal is to minimize this average error, resulting in more accurate predictions. It is **used by default in Edge Impulse** [**regression learning blocks**](/studio/projects/learning-blocks/blocks/regression).
* **Mean Absolute Error (MAE)**: The MAE is another regression loss function that measures the average absolute difference between the predicted and actual target values. Unlike MSE, which considers squared errors, MAE uses the direct absolute value of the error, making it more sensitive to outliers but less affected by them. This makes it a good choice for problems with skewed or imbalanced data.
* **Binary Cross-Entropy Loss**: Ideal for binary classification problems. It measures the difference between the predicted probabilities and the actual labels by minimizing the sum of the losses for each sample. Note that this loss function is commonly used in conjunction with the sigmoid activation function.
* **Categorical Cross-Entropy**: Similar to the Binary Cross-Entropy, the Categorical Cross-Entropy is mostly used for multi-class classification. It measures the difference between the predicted probabilities and the actual labels for each class in a sample. The sum of these losses across all samples is then minimized. It is **used by default in Edge Impulse** [**classification learning blocks**](/studio/projects/learning-blocks/blocks/classification). Note that this loss function is commonly used in conjunction with the softmax activation function (also used by default in Edge Impulse for classification problems).
* **Huber Loss**: A combination of MSE and MAE (Mean Absolute Error). It is less sensitive to outliers than MSE. It starts as the square of the difference between the predicted and actual values for small errors, similar to MSE. However, once the error exceeds a certain threshold, it switches to a linear relationship like MAE. This makes Huber loss more robust against outliers compared to MSE, while still maintaining its smoothness.
* **Log Loss**: Similar to cross-entropy loss, it measures the performance of a classification model where the output is a probability value between 0 and 1.

<Info>
  #### When to change the loss function?

  Choosing the right loss function is an integral part of model design. The choice depends on the type of problem (regression, classification, etc.) and the specific requirements of your application (like sensitivity to outliers).

  Just as with [optimizers](/knowledge/concepts/machine-learning/neural-networks/optimizers), once you have settled on your overall model structure and chosen an appropriate loss function, you may want to fine-tune the settings further to achieve even better performance. This can involve testing different loss functions or adjusting their parameters to see what works best for your specific task.

  In Edge Impulse, by default, we use:

  * Mean Squared Error (MSE) for regression tasks.
  * Categorical Cross-Entropy for classification tasks.

  You can change them in the **Expert Mode** (see below). Please note that the default loss functions in Edge Impulse have been selected to work well with most tasks. We would advise you to primarily focus on your dataset quality and neural network architecture to improve your model performances.
</Info>

## Customizing the loss function in Expert Mode

In Edge Impulse, the [Expert Mode](/studio/projects/learning-blocks#expert-mode) allows for advanced customization, including the use of custom loss functions. Here is how you can do it:

1. Import the necessary libraries

```python  theme={"system"}
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy  # Import loss functions
```

2. Define your neural network architecture

```python  theme={"system"}
model = Sequential()
# Add model layers
```

3. Select a loss function

Choose the loss function that suits your problem.

For instance, for a regression problem, you might choose Mean Squared Error:

```python  theme={"system"}
loss_function = MeanSquaredError()
```

For a binary classification problem, Binary Cross-Entropy might be more appropriate:

```python  theme={"system"}
loss_function = BinaryCrossentropy()
```

4. Compile and train your model with your chosen loss function

```python  theme={"system"}
model.compile(optimizer='adam', loss=loss_function, metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10)
```


Built with [Mintlify](https://mintlify.com).