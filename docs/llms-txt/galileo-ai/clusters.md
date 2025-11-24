# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/clusters.md

# Clustering

> To help you make sense of your data and your embeddings view, Galileo provides out-of-the-box Clustering and Explainability.

You'll find your *Clusters* on the third tab of your Insights bar, next to *Alerts* and *Metrics*.

<Info>
  Currently, only Text Classification tasks support clustering.
</Info>

Each Cluster contains a number of samples that are semantically similar to one another (i.e. are near each other in the embedding space). We leverage our *Clustering and Custom Tokenization Algorithm* to cluster and explain the commonalities between samples in that cluster.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/clustering-1.webp" />
</Frame>

#### How to make sense of clusters?

For every cluster, the *top common words* are shown in the cluster's card. These are tokens that appear with high frequency in the clustered samples and with low frequency in samples outside of this cluster. You can use these common words to get a sense of what

Average [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep), F1, and size are also shown on the cards. You can also sort your clusters by these metrics and use them to prioritize which clusters you inspect first.

Once you've identified a cluster of interest, you can click on the cluster card to filter the dataset to samples in that cluster. You can see where it is in the embeddings view, or inspect and browse the samples in table form.

#### Advanced: Cluster Summarization

Galileo leverages GPT models to generate a topic description and summary of your clusters. This can further help you get a sense for what the samples in the cluster are about.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/clustering-2.png" />
</Frame>

To enable this feature, hop over to your [Integrations](/galileo/how-to-and-faq/galileo-product-features/3p-integrations) page and enable your OpenAI integration. Summaries will start showing up on your future runs (i.e. they're not generated retroactively).

Note: We leverage OpenAI's APIs for this. If you enable this feature, some of your samples will be sent to OpenAI to generate the summaries
