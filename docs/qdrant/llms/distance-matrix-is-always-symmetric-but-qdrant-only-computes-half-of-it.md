# Distance matrix is always symmetric, but qdrant only computes half of it.
matrix = matrix + matrix.T

```

Now we can apply UMAP to the distance matrix:

```python
umap = UMAP(
    metric="precomputed", # We provide ready-made distance matrix
    n_components=2, # output dimension
    n_neighbors=20, # Same as the limit in the search_matrix_offsets
)

vectors_2d = umap.fit_transform(matrix)

```

That’s all that is needed to get the 2d representation of the data.

![UMAP on Midlib](https://qdrant.tech/articles_data/distance-based-exploration/umap-midlib.png)

UMAP applied to Midlib dataset

UMAP isn’t the only algorithm compatible with our distance matrix API. For example, `scikit-learn` also offers:

- [Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html) \- Non-linear dimensionality reduction through Isometric Mapping.
- [SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html) \- Forms an affinity matrix given by the specified function and applies spectral decomposition to the corresponding graph Laplacian.
- [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) \- well-known algorithm for dimensionality reduction.

## [Anchor](https://qdrant.tech/articles/distance-based-exploration/\#clustering) Clustering

Another approach to data structure understanding is clustering–grouping similar items.

_Note that there’s no universally best clustering criterion or algorithm._

![Clustering](https://qdrant.tech/articles_data/distance-based-exploration/clustering.png)

Clustering example, [source](https://scikit-learn.org/)

Many clustering algorithms accept precomputed distance matrix as input, so we can use the same distance matrix we calculated before.

Let’s consider a simple example of clustering the Midlib dataset with **KMeans algorithm**.

From [scikit-learn.cluster documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) we know that `fit()` method of KMeans algorithm prefers as an input:

> `X : {array-like, sparse matrix} of shape (n_samples, n_features)`:
>
> Training instances to cluster. It must be noted that the data will be converted to C ordering, which will cause a memory copy if the given data is not C-contiguous. If a sparse matrix is passed, a copy will be made if it’s not in CSR format.

So we can re-use `matrix` from the previous example:

```python
from sklearn.cluster import KMeans