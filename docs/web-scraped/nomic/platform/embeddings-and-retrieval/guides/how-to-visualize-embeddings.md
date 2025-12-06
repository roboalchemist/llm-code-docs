# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/guides/how-to-visualize-embeddings

Neural networks transform data (e.g. text, images, audio) into numerical vectors called embeddings. These vectors capture semantic or structural relationships within the data, allowing models to perform tasks like recommendation, classification, and clustering. However, embeddings typically live in high-dimensional spaces (e.g., 128, 512, or 1024 dimensions), making them hard to interpret directly without the right tools.

This guide explores three leading methods for embedding visualization:

- t-SNE (t-Distributed Stochastic Neighbor Embedding)
- UMAP (Uniform Manifold Approximation and Projection)
- Nomic Atlas (Cloud-based, Interactive Visualization)
By the end, you will understand how each technique works, their pros and cons, and when to use each one for debugging models, analyzing clustering, and refining vector search performance.

## What Are Embeddings?​

In machine learning, embeddings are dense vector representations of data. For example:

- Text Embeddings: Words or sentences mapped into high-dimensional vectors where similar meanings cluster together.
- Image Embeddings: Visual features extracted by a convolutional and transformer network.
Visualization techniques like t-SNE, UMAP, and Nomic Atlas help you project these high-dimensional embeddings into 2D space for easy exploration on a flat canvas.

## Why Visualize Embeddings?​

- Identify Clusters: See if your data forms distinct groups, which can be crucial for classification or recommendation tasks.
- Debug Model Failures: Spot misclassified or outlier points where a model's assumptions break down.
- Refine Vector Search: Understand how embeddings are distributed, which can improve search accuracy and performance.
- Explainability: Provide stakeholders with a tangible view of how a model "sees" the data.
## Visualizing Embeddings with t-SNE​

t-SNE is a non-linear dimensionality reduction method that emphasizes local relationships among data points.

### Key Characteristics​

- Local Structure: Excels at forming tight clusters of similar points.
- Complexity: Can be computationally expensive (often O(N² log N) for naive implementations).
- Best For: Small or medium-sized datasets (a few thousand to tens of thousands of points).
### Pros & Cons​

Pros

- Captures local relationships well
- Effective at visually separating small, distinct clusters
Cons

- Slow for large datasets
- May distort global distances; clusters might appear artificially separated
- Requires careful hyperparameter tuning (perplexity, learning rate)
- Python
```
import numpy as npfrom sklearn.manifold import TSNEimport matplotlib.pyplot as plt# Sample high-dimensional data (1,000 points, 128-dimensional)X = np.random.rand(1000, 128)# Reduce to 2D using t-SNEtsne = TSNE(n_components=2, perplexity=30, random_state=42)X_embedded = tsne.fit_transform(X)# Plot resultsplt.scatter(X_embedded[:, 0], X_embedded[:, 1], s=5)plt.title("t-SNE Visualization")plt.show()
```

## Visualizing Embeddings with UMAP​

UMAP (Uniform Manifold Approximation and Projection) is a faster alternative to t-SNE that also aims to preserve some global structure.

### Key Characteristics​

- Speed: Typically much faster than t-SNE, often utilizing approximate nearest neighbor search.
- Structure: Balances local and global neighborhood preservation.
- Best For: Medium to large datasets, where you need quicker computation than t-SNE.
### Pros & Cons​

Pros

- Faster than t-SNE, scales better
- Preserves both local and global relationships (less likely to split single clusters)
Cons

- Results can vary based on hyperparameters (n_neighbors, min_dist)
- Some interpretability challenges remain for very large datasets
- Python
```
import numpy as npimport umapimport matplotlib.pyplot as plt# Sample high-dimensional data (1,000 points, 128-dimensional)X = np.random.rand(1000, 128)# Reduce to 2D using UMAPumap_model = umap.UMAP(n_neighbors=15, min_dist=0.1, metric='cosine', random_state=42)X_embedded = umap_model.fit_transform(X)# Plot resultsplt.scatter(X_embedded[:, 0], X_embedded[:, 1], s=5)plt.title("UMAP Visualization")plt.show()
```

## Visualizing Embeddings with Atlas​

Nomic Atlas is a cloud-based platform for scalable, interactive embedding visualization. Unlike standalone local methods (t-SNE, UMAP), it:

- Handles millions of embeddings with real-time interactivity
- Provides collaborative, web-based interactive maps you can share
- Allows filtering and annotation by metadata
### When to Use Nomic Atlas​

- Very Large Datasets: Seamlessly upload and visualize millions of embeddings.
- Collaboration: Share interactive maps and analysis with team members or stakeholders.
- Exploration: Filter, zoom in on clusters, and annotate specific points.
- Data Workflows: Building data workflows like embedding power model improvements and data curation.
### Projection in Atlas​

Atlas automatically selects the optimal projection algorithm based on your dataset size:

- For datasets with fewer than 50,000 points, Atlas uses algorithms optimized for smaller datasets
- For datasets with 50,000 or more points, Atlas uses advanced proprietary algorithms designed for large-scale visualization
You can configure projection parameters when creating your maps:

```
from nomic import AtlasDatasetfrom nomic.data_inference import ProjectionOptions# Create a map with custom projection parametersdataset = AtlasDataset("your-dataset-name")dataset.add_data(your_data)atlas_map = dataset.create_index(    indexed_field='your_text_field',    projection=ProjectionOptions(        n_neighbors=15,        min_dist=0.1,        n_epochs=20    ))
```

Learn more about configuring projection algorithms in the Atlas Dataset Documentation

### Example: Uploading Embeddings to Atlas​

- Python
```
from nomic import AtlasDatasetimport numpy as np# Suppose we have text embeddings for 100,000 documents (512-dimensional)embeddings = np.random.rand(100000, 512)metadata = [{'id': str(i), 'category': 'demo'} for i in range(100000)]# Create an interactive mapdataset = AtlasDataset('my-first-embedding-map')dataset.add_data(embeddings=embeddings, data=metadata)atlas_map = dataset.create_index()
```

- Install the Nomic Atlas Python SDK:
pip install nomic
```
pip install nomic
```

- Run the above script to upload embeddings and metadata.
- Log in to Nomic Atlas to explore and share the interactive map.
## Comparison of t-SNE, UMAP, and Nomic Atlas​

Below is a quick reference to help you decide which method best fits your needs:

Nomic Atlas automatically selects the most appropriate projection algorithm based on your dataset size, while still allowing customization of projection parameters through the Python SDK.

## Best Practices for Embedding Visualization​

- Pick the Right Method:

t-SNE for smaller datasets where local detail is paramount.
UMAP for medium-large datasets and a better global picture.
Nomic Atlas for collaborative, interactive visualization of datasets of any size.
Pick the Right Method:

- t-SNE for smaller datasets where local detail is paramount.
- UMAP for medium-large datasets and a better global picture.
- Nomic Atlas for collaborative, interactive visualization of datasets of any size.
- Tune Hyperparameters:

t-SNE: Experiment with perplexity (often 5–50) and learning_rate.
UMAP: Adjust n_neighbors (5–50), min_dist.
Nomic Atlas: Configure projection parameters and metadata columns to visualize.
Tune Hyperparameters:

- t-SNE: Experiment with perplexity (often 5–50) and learning_rate.
```
perplexity
```

```
learning_rate
```

- UMAP: Adjust n_neighbors (5–50), min_dist.
```
n_neighbors
```

```
min_dist
```

- Nomic Atlas: Configure projection parameters and metadata columns to visualize.
- Use Metadata:

Always color or label points by known categories, class labels, or other relevant metadata.
Use Metadata:

- Always color or label points by known categories, class labels, or other relevant metadata.
- Compare Multiple Methods:

If suspicious clusters appear, try a second technique (e.g., UMAP after t-SNE) to confirm.
Compare Multiple Methods:

- If suspicious clusters appear, try a second technique (e.g., UMAP after t-SNE) to confirm.
## Common Pitfalls and How to Avoid Them​

- Misinterpreting Distances: 2D projections can distort high-dimensional distances. Validate with metadata or alternative projections.
- Not Tuning Hyperparameters: Default perplexity in t-SNE or default n_neighbors in UMAP might not reveal the best structure.
```
n_neighbors
```

- Overlooking Global Structure: t-SNE, in particular, can overemphasize local clusters. Use UMAP or a larger perplexity to see global relationships.
- Using Local Tools for Huge Datasets: For datasets over 100k embeddings, local methods might become too slow or memory-intensive. Consider Nomic Atlas for large-scale visualization.
## Frequently Asked Questions (FAQ)​

1. How do I choose perplexity for t-SNE?
A good rule of thumb is to try values between 5 and 50. Larger datasets often work better with a higher perplexity. Experiment with different values and visually inspect the results.

2. What about GPU acceleration for t-SNE, UMAP and Nomic Atlas?
Libraries like OpenTSNE and Rapids UMAP leverage GPU acceleration, speeding up t-SNE and UMAP dramatically on compatible hardware.
Nomic Atlas will automatically select the fastest hardware to generate your embedding visualization.

3. Which embedding distances work best for UMAP?
Cosine is a popular choice for text data (e.g., NLP embeddings). Euclidean might work well for image embeddings. Always pick a distance metric aligned with how embeddings were generated.

## Further Reading and References​

- t-SNE Paper: Maaten & Hinton, 2008
- UMAP Documentation: UMAP-Learn Docs
- Getting started with Atlas: Nomic Atlas
## Conclusion and Next Steps​

### Which Method Should You Use?​

- t-SNE for smaller datasets and detailed cluster separation.
- UMAP for larger datasets where speed and partial global structure matter.
- Nomic Atlas for scaling to millions of points, collaborative features, and interactive exploration with automatic projection algorithm selection.
Whether you choose t-SNE, UMAP, or Nomic Atlas, visualizing embeddings is a crucial step in understanding, debugging, and refining your machine learning models.

### Get Started with Nomic Atlas:​

- Install Nomic Atlas:
pip install nomic
Install Nomic Atlas:

```
pip install nomic
```

- Upload and Explore:
from nomic import AtlasDatasetimport numpy as npembeddings = np.random.rand(100000, 128)dataset = AtlasDataset('my-embedding-visualization')dataset.add_data(embeddings=embeddings)atlas_map = dataset.create_index()
Upload and Explore:

```
from nomic import AtlasDatasetimport numpy as npembeddings = np.random.rand(100000, 128)dataset = AtlasDataset('my-embedding-visualization')dataset.add_data(embeddings=embeddings)atlas_map = dataset.create_index()
```

- Visualize: Log in to Nomic Atlas, open your project, and start exploring your embeddings interactively.
Visualize: Log in to Nomic Atlas, open your project, and start exploring your embeddings interactively.

- What Are Embeddings?
- Why Visualize Embeddings?
- Visualizing Embeddings with t-SNEKey CharacteristicsPros & Cons
- Key Characteristics
- Pros & Cons
- Visualizing Embeddings with UMAPKey CharacteristicsPros & Cons
- Key Characteristics
- Pros & Cons
- Visualizing Embeddings with AtlasWhen to Use Nomic AtlasProjection in AtlasExample: Uploading Embeddings to Atlas
- When to Use Nomic Atlas
- Projection in Atlas
- Example: Uploading Embeddings to Atlas
- Comparison of t-SNE, UMAP, and Nomic Atlas
- Best Practices for Embedding Visualization
- Common Pitfalls and How to Avoid Them
- Frequently Asked Questions (FAQ)
- Further Reading and References
- Conclusion and Next StepsWhich Method Should You Use?Get Started with Nomic Atlas:
- Which Method Should You Use?
- Get Started with Nomic Atlas:
