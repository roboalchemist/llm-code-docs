# Source: https://docs-v3.activeloop.ai/v3.0.0/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/3.1.0/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/3.1.1/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/getting-started/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/example-code/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/example-code/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/example-code/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/example-code/getting-started/deep-learning/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/examples/dl/guide/visualizing-datasets.md

# Source: https://docs-v3.activeloop.ai/examples/dl/guide/visualizing-datasets.md

# Step 5: Visualizing Datasets

## How to Visualize Datasets in Deep Lake

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

One of Deep Lake's core features is to enable users to visualize and interpret large amounts of data. Let's load the COCO dataset, which is one of the most popular datasets in computer vision.

```python
import deeplake

ds = deeplake.load('hub://activeloop/coco-train')
```

The tensor layout for this dataset can be inspected using:

```python
ds.summary()
```

The dataset can be [visualized in the Activeloop App](https://app.activeloop.ai/activeloop/coco-tour) or using an iframe in a jupyter notebook. If you don't already have flask and ipython installed, make sure to install Deep Lake using `pip install deeplake[visualizer]`.

```python
ds.visualize()
```

{% hint style="info" %}
Visualizing datasets in [Activeloop App](https://app.activeloop.ai/activeloop/coco-tour) will unlock more features and faster performance compared to visualization in Jupyter notebooks.
{% endhint %}

### Visualizing your own datasets

Any Deep Lake dataset can be visualized using the methods above as long as it follows the conventions necessary for the visualization engine to interpret and parse the data. These conventions are explained in the link below:

{% content-ref url="../../../technical-details/visualization" %}
[visualization](https://docs-v3.activeloop.ai/technical-details/visualization)
{% endcontent-ref %}
