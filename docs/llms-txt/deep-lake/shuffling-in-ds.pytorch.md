# Source: https://docs-v3.activeloop.ai/v3.0.0/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/3.1.0/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/3.1.1/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/how-it-works/shuffling-in-ds.pytorch.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/how-it-works/shuffling-in-ds.pytorch.md

# Shuffling in ds.pytorch()

{% hint style="warning" %}
It is important to understand the shuffling methodology in Deep Lake's `.pytorch()` dataloader because it is not fully random, which in some cases may affect model performance.
{% endhint %}

## How Shuffling Works in Deep Lake's PyTorch DataLoader

The Deep Lake shuffling algorithm is based upon a shuffle buffer that preloads a specified amount of data (in MB) determined by the `buffer_size` parameter in `ds.pytorch(buffer_size = 2048)`. First, the dataloader randomly selects chunks of from the applicable tensors until the shuffle buffer is full. Next, the indices that are available in shuffle buffer are randomly sampled to construct the batches that are returned by the dataloader. As the data in the shuffle buffer is consumed, new chunks are randomly selected and added to the buffer.

As a consequence, if many chunks in the buffer contain data from the same class, which may occur if data was uploaded in non-random order, the shuffle buffer may contain fewer unique classes than if the samples were chosen fully randomly based on index. The most extreme case of reduced randomness occurs when datasets are much larger than the shuffle buffer, when they have many classes, and when those classes occur in sequence within the dataset indices.&#x20;

One example dataset is Imagenet, which has 1000 classes, 1.2M images, 140GB of data, and approximately 140 images per 16MB chunk. For the case when the images are uploaded in sequence, the plot below shows how many unique classes are returned by the loader vs the number of images that have been returned in total. It is evident that randomly sampling by index returns many more unique values than the Deep Lake's dataloader.&#x20;

![](https://529890529-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FeJ8QNopXnp0zfN3131sJ%2Fuploads%2Fb5FGELnhlhVW4POSdi4Z%2FShuffling_Sweep_New.png?alt=media\&token=b765c263-4a2a-4320-8b0e-d27ba368159c)

{% hint style="warning" %}
If this reduced randomness has an impact on model performance in your workflows, the recommended countermeasures are:

* Store the dataset in a shuffled fashion such that the data does not appear in order by class. This completely mitigates the randomness concerns at the output of the data loader.
* Store the dataset with a smaller chunk size. This increases randomness because the shuffle buffer selects more discreet chunks before filling up. The current default size is 16MB, and reducing chunk size to 4MB significantly increases randomness (see plot above) with only a modest slowdown in data transfer speed. Reducing chunk size below 4MB is not recommended.
* Increase the size of the shuffle buffer. This mitigates the randomness concerns but may not completely alleviate them.
  {% endhint %}
