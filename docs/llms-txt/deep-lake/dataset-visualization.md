# Source: https://docs-v3.activeloop.ai/v3.0.0/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/3.1.0/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/3.1.1/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/how-it-works/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/technical-details/dataset-visualization.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/technical-details/dataset-visualization.md

# Dataset Visualization

## How to visualize machine learning datasets

[Deep Lake](https://app.activeloop.ai/) has a web interface for visualizing, versioning, and querying [machine learning datasets](https://datasets.activeloop.ai/). It utilizes the Deep Lake format under-the-hood, and it can be connected to datasets stored in all Deep Lake [storage locations](https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/storage-options).

![](https://content.gitbook.com/content/k6wVYPeYExL0GTAkhW6w/blobs/h9XXGosqy0oiQWcqds6Y/computer_vision_dataset_visualization_coco_dataset.webp)

### Visualization can be performed in 3 ways:

1. **In the** [**Deep Lake UI**](https://app.activeloop.ai/) **(most feature-rich and performant option)**
2. **In the** [**python API**](https://docs-v3.activeloop.ai/v3.8.27/example-code/getting-started/deep-learning/visualizing-datasets) **using `ds.visualize()`**
3. **In your own application using** [**our integration options**](https://docs-v3.activeloop.ai/v3.8.27/technical-details/visualizer-integration)**.**

### Requirements for correctly visualizing your own datasets

Deep Lake makes assumptions about underlying data types and relationships between tensors in order to display the data correctly. Understanding the following concepts is necessary in order to  use the visualizer:&#x20;

1. [Data Types (htypes)](https://docs.deeplake.ai/en/latest/Htypes.html)
2. [Relationships between tensors](https://docs-v3.activeloop.ai/v3.8.27/technical-details/tensor-relationships)

### Visualizer Controls and Modes

{% embed url="<https://youtu.be/N-yvvo2_rrA>" %}

### Downsampling Data for Faster Visualization

For faster visualization of images and masks, tensors can be downsampled during dataset creation. The downsampled data are stored in the dataset and are automatically rendered by the visualizer depending on the zoom level.&#x20;

To add downsampling to your tensors, specify the downsampling factor and the number of downsampling layers during [tensor creation](https://docs.deeplake.ai/en/latest/deeplake.core.dataset.html#deeplake.core.dataset.Dataset.create_tensor):

```python
# 3X downsampling per layer, 2X layers
ds.create_tensor('images', htype = 'image', downsampling = (3,2))
```

{% hint style="warning" %}
Note: since downsampling requires decompression and recompression of data, it will slow down dataset ingestion.
{% endhint %}
