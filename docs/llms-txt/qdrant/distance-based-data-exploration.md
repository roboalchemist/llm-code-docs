# Distance-based data exploration

Andrey Vasnetsov

·

March 11, 2025

![Distance-based data exploration](https://qdrant.tech/articles_data/distance-based-exploration/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#hidden-structure) Hidden Structure

When working with large collections of documents, images, or other arrays of unstructured data, it often becomes useful to understand the big picture.
Examining data points individually is not always the best way to grasp the structure of the data.

![Data visualization](https://qdrant.tech/articles_data/distance-based-exploration/no-context-data.png)

Datapoints without context, pretty much useless

As numbers in a table obtain meaning when plotted on a graph, visualising distances (similar/dissimilar) between unstructured data items can reveal hidden structures and patterns.

![Data visualization](https://qdrant.tech/articles_data/distance-based-exploration/data-on-chart.png)

Vizualized chart, very intuitive

There are many tools to investigate data similarity, and Qdrant’s [1.12 release](https://qdrant.tech/blog/qdrant-1.12.x/) made it much easier to start this investigation. With the new [Distance Matrix API](https://qdrant.tech/documentation/concepts/explore/#distance-matrix), Qdrant handles the most computationally expensive part of the process—calculating the distances between data points.

In many implementations, the distance matrix calculation was part of the clustering or visualization processes, requiring either brute-force computation or building a temporary index. With Qdrant, however, the data is already indexed, and the distance matrix can be computed relatively cheaply.

In this article, we will explore several methods for data exploration using the Distance Matrix API.

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#dimensionality-reduction) Dimensionality Reduction

Initially, we might want to visualize an entire dataset, or at least a large portion of it, at a glance. However, high-dimensional data cannot be directly visualized. We must apply dimensionality reduction techniques to convert data into a lower-dimensional representation while preserving important data properties.

In this article, we will use [UMAP](https://github.com/lmcinnes/umap) as our dimensionality reduction algorithm.

Here is a **very** simplified but intuitive explanation of UMAP:

1. _Randomly generate points in 2D space_: Assign a random 2D point to each high-dimensional point.
2. _Compute distance matrix for high-dimensional points_: Calculate distances between all pairs of points.
3. _Compute distance matrix for 2D points_: Perform similarly to step 2.
4. _Match both distance matrices_: Adjust 2D points to minimize differences.

![UMAP](https://qdrant.tech/articles_data/distance-based-exploration/umap.png)

Canonical example of UMAP results, [source](https://github.com/lmcinnes/umap?tab=readme-ov-file#performance-and-examples)

UMAP preserves the relative distances between high-dimensional points; the actual coordinates are not essential. If we already have the distance matrix, step 2 can be skipped entirely.

Let’s use Qdrant to calculate the distance matrix and apply UMAP.
We will use one of the default datasets perfect for experimenting in Qdrant– [Midjourney Styles dataset](https://midlibrary.io/).

Use this command to download and import the dataset into Qdrant:

```http
PUT /collections/midlib/snapshots/recover
{
  "location": "http://snapshots.qdrant.io/midlib.snapshot"
}

```

We also need to prepare our python enviroment:

```bash
pip install umap-learn seaborn matplotlib qdrant-client

```

Import the necessary libraries:

```python