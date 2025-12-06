# Nomic Documentation

Source: https://docs.nomic.ai/reference/getting-started/rate-limits

To ensure consistent service quality across our growing user base, we implement limits on API usage. These limits help us maintain platform stability while serving all users effectively.

## Embedding Inference API​

We enforce a rate limit of 1200 requests per 5-minute rolling window per IP address for the Embedding Inference API.

If your use case requires higher throughput than our standard rate limits allow, we offer two recommended solutions:

### Atlas Datasets​

You can upload your dataset into Atlas and then download the embeddings we generate.

The Atlas Platform prioritizes embedding generation for Atlas Datasets and does not apply rate limits. This solution offers you an efficient way to generate embeddings at scale, coupled with the ability to visualize and explore your data in the Atlas UI in your browser.

You can get started generating embeddings for your data via Atlas by visiting our Atlas Documentation quickstart guide.

### Amazon SageMaker​

Our text embedding and image models are available for inference on Amazon SageMaker, giving you ability to configure settings for throughput and processing power. This solution is well-suited for teams already working within the AWS ecosystem who need high-volume embedding generation.

You can get started generating text and image embeddings via Amazon SageMaker with these example notebooks from our GitHub repository.

- Embedding Inference APIAtlas DatasetsAmazon SageMaker
- Atlas Datasets
- Amazon SageMaker
