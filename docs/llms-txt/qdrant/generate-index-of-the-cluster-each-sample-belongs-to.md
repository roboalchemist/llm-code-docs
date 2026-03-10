# Generate index of the cluster each sample belongs to
cluster_labels = kmeans.fit_predict(matrix)

```

With this simple code, we have clustered the data into 10 clusters, while the main CPU-intensive part of the process was done by Qdrant.

![Clustering on Midlib](https://qdrant.tech/articles_data/distance-based-exploration/clustering-midlib.png)

Clustering applied to Midlib dataset

How to plot this chart

```python
sns.scatterplot(
    # Coordinates obtained from UMAP
    x=vectors_2d[:, 0], y=vectors_2d[:, 1],
    # Color datapoints by cluster
    hue=cluster_labels,
    palette=sns.color_palette("pastel", 10),
    legend="full",
)

```

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#graphs) Graphs

Clustering and dimensionality reduction both aim to provide a more transparent overview of the data.
However, they share a common characteristic - they require a training step before the results can be visualized.

This also implies that introducing new data points necessitates re-running the training step, which may be computationally expensive.

Graphs offer an alternative approach to data exploration, enabling direct, interactive visualization of relationships between data points.
In a graph representation, each data point is a node, and similarities between data points are represented as edges connecting the nodes.

Such a graph can be rendered in real-time using [force-directed layout](https://en.wikipedia.org/wiki/Force-directed_graph_drawing) algorithms, which aim to minimize the system’s energy by repositioning nodes dynamically–the more similar the data points are, the stronger the edges between them.

Adding new data points to the graph is as straightforward as inserting new nodes and edges without the need to re-run any training steps.

In practice, rendering a graph for an entire dataset at once may be computationally expensive and overwhelming for the user. Therefore, let’s explore a few strategies to address this issue.

### [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#expanding-from-a-single-node) Expanding from a single node

This is the simplest approach, where we start with a single node and expand the graph by adding the most similar nodes to the graph.

![Graph](https://qdrant.tech/articles_data/distance-based-exploration/graph.gif)

Graph representation of the data

### [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#sampling-from-a-collection) Sampling from a collection

Expanding a single node works well if you want to explore neighbors of a single point, but what if you want to explore the whole dataset?
If your dataset is small enough, you can render relations for all the data points at once. But it is a rare case in practice.

Instead, we can sample a subset of the data and render the graph for this subset.
This way, we can get a good overview of the data without overwhelming the user with too much information.

Let’s try to do so in [Qdrant’s Graph Exploration Tool](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool):

```json
{
  "limit": 5, # node neighbors to consider
  "sample": 100 # nodes
}

```

![Graph](https://qdrant.tech/articles_data/distance-based-exploration/graph-sampled.png)

Graph representation of the data ( [Qdrant’s Graph Exploration Tool](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool))

This graph captures some high-level structure of the data, but as you might have noticed, it is quite noisy.
This is because the differences in similarities are relatively small, and they might be overwhelmed by the stretches and compressions of the force-directed layout algorithm.

To make the graph more readable, let’s concentrate on the most important similarities and build a so called [Minimum/Maximum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree).

```json
{
  "limit": 5,
  "sample": 100,
  "tree": true
}

```

![Graph](https://qdrant.tech/articles_data/distance-based-exploration/spanning-tree.png)

Spanning tree of the graph ( [Qdrant’s Graph Exploration Tool](https://qdrant.tech/blog/qdrant-1.11.x/#web-ui-graph-exploration-tool))

This algorithm will only keep the most important edges and remove the rest while keeping the graph connected.
By doing so, we can reveal clusters of the data and the most important relations between them.

In some sense, this is similar to hierarchical clustering, but with the ability to interactively explore the data.
Another analogy might be a dynamically constructed mind map.

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#conclusion) Conclusion

Vector similarity goes beyond looking up the nearest neighbors–it provides a powerful tool for data exploration.
Many algorithms can construct human-readable data representations, and Qdrant makes using them easy.

Several data exploration instruments are available in the Qdrant Web UI ( [Visualization and Graph Exploration Tools](https://qdrant.tech/articles/web-ui-gsoc/)), and for more advanced use cases, you could directly utilise our distance matrix API.

Try it with your data and see what hidden structures you can reveal!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/distance-based-exploration.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/distance-based-exploration.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-142-lllmstxt|>
## role-management
- [Documentation](https://qdrant.tech/documentation/)
- [Cloud rbac](https://qdrant.tech/documentation/cloud-rbac/)
- Role Management