# Source: https://docs-v3.activeloop.ai/v3.0.0/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/3.1.0/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/3.1.1/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/enterprise-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/enterprise-features/compute-engine/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/performance-features/performant-dataloader.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/performance-features/performant-dataloader.md

# Performant Dataloader

## How to use Deep Lake's performant Dataloader built and optimized in C++

Deep Lake offers an optimized dataloader implementation built in C++, [which is 1.5-3X faster than the pure-python implementation](https://docs-v3.activeloop.ai/v3.8.27/technical-details/best-practices/training-models-at-scale), and it supports distributed training. The C++ and Python dataloaders can be used interchangeably, and their syntax varies as shown below.&#x20;

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

{% content-ref url="../example-code/tutorials/deep-learning/training-models" %}
[training-models](https://docs-v3.activeloop.ai/v3.8.27/example-code/tutorials/deep-learning/training-models)
{% endcontent-ref %}

{% content-ref url="../example-code/playbooks/training-reproducibility-with-wandb" %}
[training-reproducibility-with-wandb](https://docs-v3.activeloop.ai/v3.8.27/example-code/playbooks/training-reproducibility-with-wandb)
{% endcontent-ref %}
