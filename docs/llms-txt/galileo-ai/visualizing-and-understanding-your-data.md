# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/visualizing-and-understanding-your-data.md

# Visualizing And Understanding Your Data

> Finetuning an LLM often requires large datasets.

Analyzing these datasets to uncover meaningful patterns, compositions, and the overall nature of the text is a critical step in model development and data understanding. Galileo helps you understand your dataset better.

### Embedding Visualization

The Embeddings View provides a visual playground for you to interact with your datasets. To visualize your datasets, we leverage your model's embeddings logged during training, validation, testing, or inference. Given these embeddings, we plot the data points on the 2D plane using the techniques [here](/galileo/how-to-and-faq/galileo-product-features/embeddings-view).

Your samples are visualized as dots in the embedding space. Dots that are near each other are *semantically* similar to each other. Finding groups of dots near each other and hovering over them to see their text values is a good way to understand your dataset.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-embedding-zoom.gif)

### Out-of-the-box Clustering

To help you make sense of your data and your embeddings view, Galileo provides out-of-the-box Clustering and Explainability. You'll find your *Clusters* on the third tab of your Insights bar, next to *Alerts* and *Metrics*.

Each Cluster contains a number of samples that are semantically similar to one another (i.e. are near each other in the embedding space). We leverage our *Clustering and Custom Tokenization Algorithm* to cluster and explain the commonalities between samples in that cluster.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-understanding-clustering.png)

#### How to make sense of clusters?

For every cluster, the *top common words* are shown in the cluster's card. These are tokens that appear with high frequency in the clustered samples and with low frequency in samples outside of this cluster. You can use these common words to get a sense of what

Average [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) and size are also shown on the cards. You can also sort your clusters by these metrics and use them to prioritize which clusters you inspect first.

Once you've identified a cluster of interest, you can click on the cluster card to filter the dataset to samples in that cluster. You can see where it is in the embeddings view, or inspect and browse the samples in table form.

#### Advanced: Cluster Summarization

Galileo leverages GPT models to generate a topic description and summary of your clusters. This can further help you get a sense of what the samples in the cluster are about.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-cluster-summaries.png" width="400" />
</Frame>

To enable this feature, hop over to your [Integrations](/galileo/how-to-and-faq/galileo-product-features/3p-integrations) page and enable your OpenAI integration. Summaries will start showing up on your future runs (i.e. they're not generated retroactively).

Note: We leverage OpenAI's APIs for the summarization feature. If you enable this feature, some of your samples will be sent to OpenAI to generate the summaries
