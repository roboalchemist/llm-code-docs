# Source: https://docs.fiddler.ai/observability/platform/embedding-visualization-with-umap.md

# Source: https://docs.fiddler.ai/observability/llm/embedding-visualization-with-umap.md

# Embedding Visualizations

Discover how embedding visualization enhances LLM monitoring and analysis by simplifying complex data relationships and delivering actionable insights. This guide explains how to implement Fiddler’s LLM visualization techniques, such as UMAP, to uncover patterns, clusters, and anomalies in high-dimensional data.

![Charts: UMAP embedding visualization](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-47ab334388907ccbba0d279e88acc864040e7123%2Fb874b1a-umap%20\(2\).gif?alt=media)

### What is Embedding Visualization and Why It Matters for LLM Monitoring

Embedding visualization is a powerful technique for understanding and interpreting complex relationships in high-dimensional data. By reducing the dimensionality of custom features into a 2D or 3D space, patterns, clusters, and outliers become easier to identify, offering valuable insights for LLM embedding analysis and vector embedding visualization.

In Fiddler, high-dimensional data like embeddings and vectors are ingested as a [Custom Feature](https://docs.fiddler.ai/platform/vector-monitoring-platform#defining-custom-features).

This approach allows you to visualize embeddings and perform vector embedding visualization effectively, enabling detailed analysis and uncovering hidden patterns in your data.

### Using UMAP for LLM Embedding Visualization in High-Dimensional Data

We use the [UMAP](https://umap-learn.readthedocs.io/en/latest/) (Uniform Manifold Approximation and Projection) technique to embed visualizations. UMAP is a dimensionality reduction method particularly effective at preserving the local structure of data, making it ideal for visualizing embeddings, including those from embedded LLM models. Reducing high-dimensional embeddings to a 3D space allows for easier interpretation and analysis.

UMAP supports both text embedding visualization and image embedding as a [Custom Feature](https://docs.fiddler.ai/platform/vector-monitoring-platform#defining-custom-features). Our [guide](#creating-an-embedding-visualization-chart) teaches you how to apply UMAP visualizations to your application data, unlocking deeper insights into your embedded LLM data.

### How UMAP Embedding Visualization Enhances Generative Applications

UMAP embedding visualizations are extremely helpful in understanding common themes and topics in the data corpus for generative AI applications. When evaluating prompts and responses, it is paramount to see which concept clusters emerge and which exhibit the most problems. Users can identify the clusters with the most issues by coloring them with various LLM and GenAI correctness and safety metrics.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-a4b1c5675855fbb859da33348d884c107c1d434f%2Fumap-cluster.png?alt=media" alt="Identifying a cluster of prompts with Jailbreak attempts via UMAP"><figcaption><p>Identifying a cluster of prompts with Jailbreak attempts via UMAP</p></figcaption></figure>

{% hint style="info" %}
To create an embedding visualization chart, follow the Guide [here](#creating-an-embedding-visualization-chart).
{% endhint %}

***

:question: Questions? [Talk](https://www.fiddler.ai/contact-sales) to a product expert or [request](https://www.fiddler.ai/demo) a demo.

:bulb: Need help? Contact us at <support@fiddler.ai>.
