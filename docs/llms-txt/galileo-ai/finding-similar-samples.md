# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/finding-similar-samples.md

# Finding Similar Samples

> Similarity search allows you to discover **similar samples** within your datasets

. Given a data sample, similarity search leverages the power of embeddings and similarity search clustering algorithms to surface the most contextually similar samples.

The similarity search feature can be accessed through the "Find Similar From" action button in both the **Table View** and the **Embeddings View.** You can change the split name to choose which split (training, validation, test or inference) you want to find similar samples in.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finding-similar-samples.gif)

This is useful when you find low-quality data (mislabeled, garbage, empty, etc) and you want to find other samples similar to it so that you can take bulk action (e.g. remove, etc). Galileo automatically assigns a smart threshold to give you the most similar data samples.
