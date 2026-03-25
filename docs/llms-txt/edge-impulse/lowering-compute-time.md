# Source: https://docs.edgeimpulse.com/knowledge/guides/lowering-compute-time.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lowering compute time

## Why lower compute time?

Developer accounts on Edge Impulse have limits on their compute time per job. Below are some tips to help you stay within these compute limits.

## Reduce dataset size

The dataset size has a direct impact on the training time. If you're reaching the limit, you can reduce decrease your dataset size.

To easily reduce your dataset, go to **Data acquisition**, click on the **Filter** and **Select** icons. You can either delete your samples or disable them:

<Frame caption="Reduce your dataset size in data acquisition view">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-reduce-dataset-size.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=1b7b187e2f057be03dad5f0fffa2fa12" width="1415" height="1000" data-path=".assets/images/studio-reduce-dataset-size.png" />
</Frame>

*Note: Reducing your dataset size will have an impact on your accuracy. Try first with a small dataset and increase it over time until you reach the limit.*

## Reduce your number of epochs

An epoch (or training cycle) means one complete pass of the training dataset through the algorithm. Reducing this hyper parameter will reduce the number of times you perform a complete pass through your dataset, thus, lower your training time.

To reduce the number of epochs, just lower the **Number of training cycles** value:

<Frame caption="Reduce the number of training cycles">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-reduce-epochs.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=6e6bd6b16bf8d4b23e9c395603b00f96" width="1479" height="1000" data-path=".assets/images/studio-reduce-epochs.png" />
</Frame>

## Apply Early Stopping

Early Stopping is a technique that helps prevent overfitting by halting the training process at the right time. This approach allows your model to stop training as soon as it starts overfitting, or if further training doesn't lead to better performance, making your training process more efficient and potentially leading to better model performance.

See how to apply [Early Stopping in Expert Mode](/knowledge/concepts/machine-learning/neural-networks/epochs#apply-early-stopping-in-expert-mode).

## Increase your batch size

The batch size is a hyperparameter that defines the number of samples to work through before updating the internal model parameters. A training dataset can be divided into one or more batches. The bigger your batch is, the less iterations will be performed.

To increase the batch size, on the **NN Classifier** view, switch to **expert mode** and change the `BATCH_SIZE` hyper parameter:

<Frame caption="Increase batch size">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-increase-batch-size.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=4b7d1224d08aacc48ebe22264318b6d7" width="1413" height="1000" data-path=".assets/images/studio-increase-batch-size.png" />
</Frame>

*Note: This also have an impact on the memory, the bigger the batch size is, the more memory your training will use.*

## Reduce the complexity of your neural network architecture

A simple neural network architecture will train faster than a very complex. To reduce the complexity of your NN architecture, remove some of the layers, reduce the number of neurons and kernel size:

<Frame caption="Decrease neural network complexity">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-decrease-nn-complexity.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=ab92f2d9da9ce7144e32b2be329727c1" width="1414" height="1000" data-path=".assets/images/studio-decrease-nn-complexity.png" />
</Frame>

## Still need more compute time?

If you still need more compute time for your project, you can check our [pricing page](https://edgeimpulse.com/pricing) and [contact us](https://edgeimpulse.com/contact)


Built with [Mintlify](https://mintlify.com).