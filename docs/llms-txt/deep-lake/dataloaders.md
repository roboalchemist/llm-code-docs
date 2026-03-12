# Source: https://docs-v3.activeloop.ai/v3.9.0/examples/dl/dataloaders.md

# Source: https://docs-v3.activeloop.ai/examples/dl/dataloaders.md

# Deep Lake Dataloaders

## How to use Deep Lake's Dataloaders for Training Models

Deep Lake offers an optimized dataloader implementation built in C++, [which is 1.5-3X faster than the pure-python implementation](https://docs-v3.activeloop.ai/technical-details/best-practices/training-models-at-scale), and it supports distributed training. The C++ and Python dataloaders can be used interchangeably, and their syntax varies as shown below.&#x20;

The Deep Lake Compute Engine is only accessible to registered and authenticated users, and it applies usage restrictions based on your Deep Lake Plan.

### Pure-Python Dataloader

```python
train_loader = ds_train.pytorch(num_workers = 8,
                                transform = transform, 
                                batch_size = 32,
                                tensors=['images', 'labels'],
                                shuffle = True)
```

### C++ Dataloader

{% hint style="danger" %}
The C++ dataloader is only accessible to registered and authenticated users.
{% endhint %}

The Deep Lake query engine is only accessible to registered and authenticated users, and it applies usage restrictions based on your Deep Lake Plan.

#### PyTorch (returns PyTorch Dataloader)

<pre class="language-python"><code class="lang-python"><strong>train_loader = ds.dataloader()\
</strong>                 .transform(transform)\
                 .batch(32)\
                 .shuffle(True)\
                 .offset(10000)\
                 .pytorch(tensors=['images', 'labels'], num_workers = 8)
</code></pre>

#### TensorFlow

```
train_loader = ds.dataloader()\
                 .transform(transform)\
                 .batch(32)\
                 .shuffle(True)\
                 .offset(10000)\
                 .tensorflow(tensors=['images', 'labels'], num_workers = 8)
```

### Further Information

{% content-ref url="tutorials/training-models" %}
[training-models](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models)
{% endcontent-ref %}

{% content-ref url="playbooks/training-reproducibility-wandb" %}
[training-reproducibility-wandb](https://docs-v3.activeloop.ai/examples/dl/playbooks/training-reproducibility-wandb)
{% endcontent-ref %}
