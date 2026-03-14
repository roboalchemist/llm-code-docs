# Source: https://docs.edgeimpulse.com/knowledge/concepts/machine-learning/neural-networks/learned-optimizer-velo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Learned optimizer (VeLO)

Machine learning model development involves several critical choices, such as the type of problem (classification or regression), the model architecture (e.g., dense layers, convolutions), and the available data. However, one often overlooked choice is the optimizer. This component is essential in the training loop, which typically involves:

* Starting with a model with randomly initialized weights.
* Passing labeled data through the model and comparing the output with the correct output using a "loss function".
* Using an optimizer to make adjustments to the model weights based on the loss function results.
* Repeating the process until the model's performance ceases to improve.

While there are various optimizers available, Adam \[[1](/knowledge/concepts/machine-learning/neural-networks/learned-optimizer-velo#resources)] has become a default choice for many projects due to its general effectiveness. Unlike these traditional optimizers which are described by human-designed function, VeLO represents a novel approach where the optimizer is itself a neural network that is trained on prior training jobs.

<Info>
  #### What is an optimizer?

  If you are not familiar with optimizers, see this page: [Optimizers](/knowledge/concepts/machine-learning/neural-networks/optimizers)
</Info>

## VeLO: A learned optimizer

VeLO (Versatile Learned Optimizers) is an innovative concept where the optimizer is trained using a large number of training jobs, as detailed in the paper "VeLO: Training Versatile Learned Optimizers by Scaling Up" \[[2](/knowledge/concepts/machine-learning/neural-networks/learned-optimizer-velo#resources)]. This approach contrasts with traditional optimizers, like Adam, which are handcrafted functions.

<Info>
  #### When to use the learned optimizer?

  The learned optimizer can help you get some extra performance for certain models. For optimal results with VeLO, **it is recommended to use as large a batch size as possible, potentially equal to the dataset's size**. This approach, however, may lead to out-of-memory issues for some projects. Here are some pros and cons of using the learned optimizer:

  **Pros**

  * VeLO generally requires less tuning compared to Adam.
  * The learned optimizer works well across various scenarios without specific adjustments.

  **Cons**

  * VeLO comprises a large LSTM model, often larger than the models it trains. This requires more computational resources, particularly for GPU-intensive models like vision models.
</Info>

## Studio integration

The Learned Optimizer can be enabled in Edge Impulse as an option on the training page.

<Frame caption="Enable the Learned Optimizer">
  <img src="https://mintcdn.com/edgeimpulse/gOVZfieUH_bnnc7H/.assets/images/enable-VeLO.png?fit=max&auto=format&n=gOVZfieUH_bnnc7H&q=85&s=aa01c76fe076906dfc99e8046758929a" width="754" height="1000" data-path=".assets/images/enable-VeLO.png" />
</Frame>

## Using VeLO in expert mode

The simplest way to use VeLO in expert mode is to enable the flag for a project and then switch to expert mode. This will pre-fill the needed lines of code in the expert mode.

To use VeLO in expert mode for an existing project:

* Remove any existing optimizer creation, `model.compile`, or `model.fit` calls.
* Replace with the `train_keras_model_with_velo` method.

```python  theme={"system"}
from ei_tensorflow.velo import train_keras_model_with_velo
history = train_keras_model_with_velo(
 keras_model=model,
 training_data=train_dataset,
 validation_data=validation_dataset,
 loss_fn=tf.keras.metrics.categorical_crossentropy, # depending on your model
 num_epochs=num_epochs,
 callbacks=callbacks
)
print("history", history)
```

## How does VeLO compare to Adam?

Consider the following graph which shows several runs of Adam vs VeLO:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZGbvQAs-QNgkltKA/.assets/images/velo-epoch-loss.png?fit=max&auto=format&n=ZGbvQAs-QNgkltKA&q=85&s=b962127492b22e3923872a77ea3c47e0" width="567" height="446" data-path=".assets/images/velo-epoch-loss.png" />
</Frame>

The most influential hyperparameter of Adam is the learning rate.

If the learning rate is too low ( e.g. the red graph "adam\_0.0001" ) then the model takes too long to make progress. If the learning rate is too high (e.g. the blue graph "adam\_0.05") then the optimization becomes unstable.

One of the benefits of VeLO is that it doesn't require a learning rate to do well. In this example we see VeLO (purple graph "velo") doing as well as the best Adam learning rate variant.

As a side note, VeLO was designed for training large models. In this example to get the best result, the batch size was equal to the dataset size.

## Examples

The following projects contain both a learning block with and without the learned optimizer so you can easily see the differences:

* Image classification using transfer learning: [Microscope - VeLO](https://studio.edgeimpulse.com/public/331324/latest)
* Vibration analysis: Coffee Machine Stages - [Multi-label data - VeLO](https://studio.edgeimpulse.com/public/331915/latest)

## Resources

* \[1] [“Adam: A Method for Stochastic Optimization”](https://arxiv.org/abs/1412.6980)
* \[2] [“VeLO: Training Versatile Learned Optimizers by Scaling Up”](https://arxiv.org/abs/2211.09760)


Built with [Mintlify](https://mintlify.com).