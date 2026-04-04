# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/finding-similar-samples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Finding Similar Samples

> Similarity search allows you to discover **similar samples** within your datasets

. Given a data sample, similarity search leverages the power of embeddings and similarity search clustering algorithms to surface the most contextually similar samples.

The similarity search feature can be accessed through the "Find Similar From" action button in both the **Table View** and the **Embeddings View.** You can change the split name to choose which split (training, validation, test or inference) you want to find similar samples in.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finding-similar-samples.gif?s=96d3cb6791ee56d1252483ddf675fe1d" alt="" data-og-width="600" width="600" data-og-height="175" height="175" data-path="images/finding-similar-samples.gif" data-optimize="true" data-opv="3" />

This is useful when you find low-quality data (mislabeled, garbage, empty, etc) and you want to find other samples similar to it so that you can take bulk action (e.g. remove, etc). Galileo automatically assigns a smart threshold to give you the most similar data samples.
