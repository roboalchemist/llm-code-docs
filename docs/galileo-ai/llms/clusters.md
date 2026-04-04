# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/clusters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Clustering

> To help you make sense of your data and your embeddings view, Galileo provides out-of-the-box Clustering and Explainability.

You'll find your *Clusters* on the third tab of your Insights bar, next to *Alerts* and *Metrics*.

<Info>
  Currently, only Text Classification tasks support clustering.
</Info>

Each Cluster contains a number of samples that are semantically similar to one another (i.e. are near each other in the embedding space). We leverage our *Clustering and Custom Tokenization Algorithm* to cluster and explain the commonalities between samples in that cluster.

<Frame>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=95580fc45f22ebddc76983b1d76c79ca" data-og-width="2304" width="2304" data-og-height="1361" height="1361" data-path="images/clustering-1.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=79105270ff38f1456ebc9201f7ad609e 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=86377139322943d772fbb4226cc25de6 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e69e996ac9b931c9e13d8e43eb6c8ef6 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=3a74340c1aaa00b78a571ffc4deaa762 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0576e0a8fb59dafaeb3bdf98f0fa1cfd 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-1.webp?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=92ee591664c744a96dc8bbf1f0a6418a 2500w" />
</Frame>

#### How to make sense of clusters?

For every cluster, the *top common words* are shown in the cluster's card. These are tokens that appear with high frequency in the clustered samples and with low frequency in samples outside of this cluster. You can use these common words to get a sense of what

Average [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep), F1, and size are also shown on the cards. You can also sort your clusters by these metrics and use them to prioritize which clusters you inspect first.

Once you've identified a cluster of interest, you can click on the cluster card to filter the dataset to samples in that cluster. You can see where it is in the embeddings view, or inspect and browse the samples in table form.

#### Advanced: Cluster Summarization

Galileo leverages GPT models to generate a topic description and summary of your clusters. This can further help you get a sense for what the samples in the cluster are about.

<Frame>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=133e9b7706f227b128dd8104fdcc4666" data-og-width="690" width="690" data-og-height="1072" height="1072" data-path="images/clustering-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5b6012ccf88d2e7642ba8272942773a7 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=574e091c559a7cfbaf1003d71ecdf4e5 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=3479466b214159d8c98e4f4d40475b3f 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0c4fe8fa4d17701f783b6ab5e05b1ec9 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0bece5cb948ad07300fa2077bb869968 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/clustering-2.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=fb9ce76b17f0e3c713af6b43dd279e01 2500w" />
</Frame>

To enable this feature, hop over to your [Integrations](/galileo/how-to-and-faq/galileo-product-features/3p-integrations) page and enable your OpenAI integration. Summaries will start showing up on your future runs (i.e. they're not generated retroactively).

Note: We leverage OpenAI's APIs for this. If you enable this feature, some of your samples will be sent to OpenAI to generate the summaries
