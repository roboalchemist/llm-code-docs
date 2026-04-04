# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/visualizing-and-understanding-your-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Visualizing And Understanding Your Data

> Finetuning an LLM often requires large datasets.

Analyzing these datasets to uncover meaningful patterns, compositions, and the overall nature of the text is a critical step in model development and data understanding. Galileo helps you understand your dataset better.

### Embedding Visualization

The Embeddings View provides a visual playground for you to interact with your datasets. To visualize your datasets, we leverage your model's embeddings logged during training, validation, testing, or inference. Given these embeddings, we plot the data points on the 2D plane using the techniques [here](/galileo/how-to-and-faq/galileo-product-features/embeddings-view).

Your samples are visualized as dots in the embedding space. Dots that are near each other are *semantically* similar to each other. Finding groups of dots near each other and hovering over them to see their text values is a good way to understand your dataset.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-embedding-zoom.gif?s=8632dd1ebbc5a9c32ec231ddc6f82f1b" alt="" data-og-width="600" width="600" data-og-height="380" height="380" data-path="images/finetune-embedding-zoom.gif" data-optimize="true" data-opv="3" />

### Out-of-the-box Clustering

To help you make sense of your data and your embeddings view, Galileo provides out-of-the-box Clustering and Explainability. You'll find your *Clusters* on the third tab of your Insights bar, next to *Alerts* and *Metrics*.

Each Cluster contains a number of samples that are semantically similar to one another (i.e. are near each other in the embedding space). We leverage our *Clustering and Custom Tokenization Algorithm* to cluster and explain the commonalities between samples in that cluster.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=870fb6173baaca812b1fb0ed41deb276" alt="" data-og-width="2952" width="2952" data-og-height="1656" height="1656" data-path="images/finetune-understanding-clustering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=9b82ee05928a1665ecc27069737f5332 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=21fb966926f76c0b9efc8a331b011f43 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6f6db74b0d384e8889387e0a0e89f896 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=ec5d1db5892dc26104d11f3bc266659b 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=beeca3c1886947d50a9fee26f0994731 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-understanding-clustering.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=a29d155700b478ed1fee288513573f3e 2500w" />

#### How to make sense of clusters?

For every cluster, the *top common words* are shown in the cluster's card. These are tokens that appear with high frequency in the clustered samples and with low frequency in samples outside of this cluster. You can use these common words to get a sense of what

Average [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) and size are also shown on the cards. You can also sort your clusters by these metrics and use them to prioritize which clusters you inspect first.

Once you've identified a cluster of interest, you can click on the cluster card to filter the dataset to samples in that cluster. You can see where it is in the embeddings view, or inspect and browse the samples in table form.

#### Advanced: Cluster Summarization

Galileo leverages GPT models to generate a topic description and summary of your clusters. This can further help you get a sense of what the samples in the cluster are about.

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=466086e89b44ddc695d46f295e554e4c" width="400" data-og-width="690" data-og-height="1072" data-path="images/finetune-cluster-summaries.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f8cf44710cb084c7bcd8afd4e7cde761 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=da81024b536ccec7ecdb45591403948b 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e96137347685f4c0fc6d265a8e754eb5 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=1e5b03341e8004a69f2a76b28a8b41a6 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f54910eff5be935bd3ffc298bbe0a29d 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-cluster-summaries.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=bbc4b7ff781fd9c8ac1552f7c5f917fd 2500w" />
</Frame>

To enable this feature, hop over to your [Integrations](/galileo/how-to-and-faq/galileo-product-features/3p-integrations) page and enable your OpenAI integration. Summaries will start showing up on your future runs (i.e. they're not generated retroactively).

Note: We leverage OpenAI's APIs for the summarization feature. If you enable this feature, some of your samples will be sent to OpenAI to generate the summaries
