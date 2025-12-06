# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/analyze-text-data

This guide will walk you through how Atlas helps you quickly find the main takeaways from text data. You'll need:

1) An Atlas account

If you don't have an Atlas account yet, you can create one for free at atlas.nomic.ai

2) Text data

We will use reviews of Singapore Airlines as demo data. You can download this dataset of reviews in spreadsheet form as a CSV file here:

Here's what the first few rows of the dataset look like:

If you have your own text data you already want to explore trends from, feel free to follow along with the steps in this guide on your data.

## Upload Text Data to Atlas​

### Visit Platform Dashboard​

You Platform Dashboard is at atlas.nomic.ai/data.

### Create New Dataset​

If you have no datasets yet, visiting your dashboard will prompt you to create one.

If you have existing datasets,
click  to create a new dataset.

You can upload text to Atlas via dataset connectors, via Python, or by uploading your own file directly.

Take a look at the auto-inferred Name,
Embedding Field,
and dataset settings (e.g., whether to use a multilingual model when embedding, which we deactivate in the above video) before clicking . Your map will take a few minutes to load, requiring more time the more data you upload.

## Explore Your Text Data​

Atlas shows your data in an interactive map with controls for searching and filtering over text, as well as recoloring the data by other fields in your data.

For example, on the dataset of reviews of an airline, if you recolor the points by the rating field, you'll see a distinct cluster of low-rating reviews that all discuss the need for better customer service during travel.

```
rating
```

On the data map, reviews discussing similar topics or themes naturally cluster together in the map, because vector embedding models are trained to arrange similar texts nearby in vector space. This is why embeddings are particularly useful for semantic analysis of reviews.

As you explore the map, you'll notice labels that come from an automatically generated hierarchical topic model. These labels provide both broad themes and more specific subthemes, helping you understand the major topics and subtle variations in your data at different levels of granularity.

One of Atlas's most powerful features is vector search, which can uncover patterns that traditional keyword searches would miss. Because it uses nearest-embeddings search, vector search can find conceptually similar content even when the exact words differ. This makes it an excellent tool for flexible sentiment analysis - for example, you can search for abstract concepts like "who had a great experience?" to find relevant reviews regardless of the specific language used.

## Share Your Analysis​

To share the specific view of the data map you capture with others, click  to generate a URL you can copy/paste.

- Upload Text Data to AtlasVisit Platform DashboardCreate New Dataset
- Visit Platform Dashboard
- Create New Dataset
- Explore Your Text Data
- Share Your Analysis
