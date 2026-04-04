# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/similarity-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Similarity Search

> Similarity search provides out of the box ability to discover **similar samples** within your datasets.

Given a data sample, similarity search leverages the power of embeddings and similarity search clustering algorithms to surface the most contextually similar samples.

The similarity search feature can be accessed through the "Show similar" action button in both the **Dataset View** and the **Embeddings View .**

### 2 WAYS TO USE SIMILARITY SEARCH

#### 1. Find similar labeled data across splits

This is useful when you find low quality data (mislabeled, garbage, empty, etc) and you want to find other samples similar to it, so that you can take bulk action (remove, relabel, etc). Galileo automatically assigns a smart threshold to give you the most similar data samples.

<iframe src="https://cdn.iframe.ly/H3KR03p" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

While surfacing similar samples, you can easily change the number of similar samples shown within the dataset view and embeddings visualization.

<iframe src="https://cdn.iframe.ly/BJQrikR" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

#### 2. Find similar unlabeled data to train with next

This is useful when you want to search for the right unlabeled data (production data) to train with next. Examples:

a. Find unlabeled data most similar to the highest DEP (hard for the model) samples

b. Find unlabeled data most similar to an under-represented class or data split (eg: a certain gender, zip-code, etc from your meta-data)

<iframe src="https://cdn.iframe.ly/KeLSmhJ" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />
