# Source: https://docs.wandb.ai/models/integrations/tensorflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# TensorFlow

> Integrate W&B with TensorFlow for logging custom metrics, using estimator hooks, and TensorBoard log synchronization.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/drive/1JCpAbjkCFhYMT7LCQ399y35TS3jlMpvM" />

## Get started

If you're already using TensorBoard, it's easy to integrate with wandb.

```python  theme={null}
import tensorflow as tf
import wandb
```

## Log custom metrics

If you need to log additional custom metrics that aren't being logged to TensorBoard, you can call `run.log()` in your code `run.log({"custom": 0.8}) `

Setting the step argument in `run.log()` is turned off when syncing Tensorboard. If you'd like to set a different step count, you can log the metrics with a step metric as:

```python  theme={null}
with wandb.init(config=tf.flags.FLAGS, sync_tensorboard=True) as run:
    run.log({"custom": 0.8, "global_step":global_step}, step=global_step)
```

## TensorFlow estimators hook

If you want more control over what gets logged, wandb also provides a hook for TensorFlow estimators. It will log all `tf.summary` values in the graph.

```python  theme={null}
import tensorflow as tf
import wandb

run = wandb.init(config=tf.FLAGS)

estimator.train(hooks=[wandb.tensorflow.WandbHook(steps_per_log=1000)])
run.finish()
```

## Log manually

The simplest way to log metrics in TensorFlow is by logging `tf.summary` with the TensorFlow logger:

```python  theme={null}
import wandb
run = wandb.init(config=tf.flags.FLAGS, sync_tensorboard=True)
with tf.Session() as sess:
    # ...
    wandb.tensorflow.log(tf.summary.merge_all())
```

With TensorFlow 2, the recommended way of training a model with a custom loop is via using `tf.GradientTape`. You can read more in the [TensorFlow custom training walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough). If you want to incorporate `wandb` to log metrics in your custom TensorFlow training loops you can follow this snippet:

```python  theme={null}
    with tf.GradientTape() as tape:
        # Get the probabilities
        predictions = model(features)
        # Calculate the loss
        loss = loss_func(labels, predictions)

    # Log your metrics
    run.log("loss": loss.numpy())
    # Get the gradients
    gradients = tape.gradient(loss, model.trainable_variables)
    # Update the weights
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

A [full example of customizing training loops in TensorFlow 2](https://www.wandb.com/articles/wandb-customizing-training-loops-in-tensorflow-2) is available.

## How is W\&B different from TensorBoard?

When the cofounders started working on W\&B, they were inspired to build a tool for the frustrated TensorBoard users at OpenAI. Here are a few things we've focused on improving:

1. **Reproduce models**: W\&B is good for experimentation, exploration, and reproducing models later. We capture not just the metrics, but also the hyperparameters and version of the code, and we can save your version-control status and model checkpoints for you so your project is reproducible.
2. **Automatic organization**: Whether you're picking up a project from a collaborator, coming back from a vacation, or dusting off an old project, W\&B makes it easy to see all the models that have been tried so no one wastes hours, GPU cycles, or carbon re-running experiments.
3. **Fast, flexible integration**: Add W\&B to your project in 5 minutes. Install our free open-source Python package and add a couple of lines to your code, and every time you run your model you'll have nice logged metrics and records.
4. **Persistent, centralized dashboard**: No matter where you train your models, whether on your local machine, in a shared lab cluster, or on spot instances in the cloud, your results are shared to the same centralized dashboard. You don't need to spend your time copying and organizing TensorBoard files from different machines.
5. **Powerful tables**: Search, filter, sort, and group results from different models. It's easy to look over thousands of model versions and find the best performing models for different tasks. TensorBoard isn't built to work well on large projects.
6. **Tools for collaboration**: Use W\&B to organize complex machine learning projects. It's easy to share a link to W\&B, and you can use private teams to have everyone sending results to a shared project. We also support collaboration via reports— add interactive visualizations and describe your work in markdown. This is a great way to keep a work log, share findings with your supervisor, or present findings to your lab or team.

Get started with a [free account](https://wandb.ai)

## Examples

We've created a few examples for you to see how the integration works:

* [Example on Github](https://github.com/wandb/examples/blob/master/examples/tensorflow/tf-estimator-mnist/mnist.py): MNIST example Using TensorFlow Estimators
* [Example on Github](https://github.com/wandb/examples/blob/master/examples/tensorflow/tf-cnn-fashion/train.py): Fashion MNIST example Using Raw TensorFlow
* [Wandb Dashboard](https://app.wandb.ai/l2k2/examples-tf-estimator-mnist/runs/p0ifowcb): View result on W\&B
* Customizing Training Loops in TensorFlow 2 - [Article](https://www.wandb.com/articles/wandb-customizing-training-loops-in-tensorflow-2) | [Dashboard](https://app.wandb.ai/sayakpaul/custom_training_loops_tf)
