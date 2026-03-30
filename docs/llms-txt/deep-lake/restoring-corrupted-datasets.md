# Source: https://docs-v3.activeloop.ai/v3.2.20/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/how-it-works/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/technical-details/best-practices/restoring-corrupted-datasets.md

# Source: https://docs-v3.activeloop.ai/technical-details/best-practices/restoring-corrupted-datasets.md

# Restoring Corrupted Datasets

## How to restore a corrupted Deep Lake dataset

**Deliberate of accidental interruption of code may make a Deep Lake dataset or some of its tensors unreadable. At scale, code interruption is more likely to occur, and Deep Lake's version control is the primary tool for recovery.**

### How to Use Version Control to Retrieve Data

When manipulating Deep Lake datasets, it is recommended to commit periodically in order to create snapshots of the dataset that can be accessed later. This can be done automatically when [creating datasets with `deeplake.compute`](https://docs-v3.activeloop.ai/technical-details/best-practices/creating-datasets-at-scale), or manually using [our version control API.](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-version-control)

If a dataset becomes corrupted, when loading the dataset, you may see an error like:

```markup
DatasetCorruptError: Exception occured (see Traceback). The dataset maybe corrupted. Try using `reset=True` to reset HEAD changes and load the previous commit. This will delete all uncommitted changes on the branch you are trying to load.
```

To reset the uncommitted corrupted changes, `load` the dataset with the `reset = True` flag:

```python
ds = deeplake.load(<dataset_path>, reset = True)
```

{% hint style="danger" %}
Note: this operation deletes *all* uncommitted changes.
{% endhint %}
