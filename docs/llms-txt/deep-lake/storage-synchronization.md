# Source: https://docs-v3.activeloop.ai/v3.0.0/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/3.1.0/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/3.1.1/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/how-it-works/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/how-it-works/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/technical-details/best-practices/storage-synchronization.md

# Source: https://docs-v3.activeloop.ai/technical-details/best-practices/storage-synchronization.md

# Storage Synchronization and "with" Context

## How Deep Lake Datasets are Synchronized with Long-Term Storage

{% hint style="danger" %}
**Using `with` context when updating Deep Lake datasets is critical for achieving rapid write performance.**
{% endhint %}

### BAD PRACTICE - Code without `with` context

Any standalone update to a Deep Lake dataset is immediately pushed to the dataset's long-term storage location. Due to the high number of write operations, there may be a significant increase in runtime when the data is stored in the cloud. In the example below, an update is pushed to storage for every call to the `.append()` command.

```python
for i in range(10):
    ds.my_tensor.append(i)
```

### Code using `with` context

To increase write speeds when using Deep Lake, the `with` syntax significantly improves performance because it only pushes updates to long-term storage after the code block inside the `with` statement has been executed, or when the local cache is full. This significantly reduces the number of discreet write operations, thereby increasing the speed by up to 100X.&#x20;

```python
with ds:
    for i in range(10):
        ds.my_tensor.append(i)
```
