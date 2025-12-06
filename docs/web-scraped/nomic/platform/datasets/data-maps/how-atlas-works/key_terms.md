# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/how-atlas-works/key_terms

Atlas is a platform for visually and programmatically interacting with massive unstructured datasets of text documents, images and embeddings.

Atlas augments your unstructured dataset with four key steps: Vectorization, 2D Layout Optimization, Annotation, and Presentation.

- Vectorization is the transformation of data into high dimensional vector space. Atlas uses a contrastively trained deep neural network, similar to Neelakantan et al., to vectorize text. Users may also upload their own embeddings for Atlas.
- 2D Layout Optimization is the arrangement of data points into two dimensions for human interpretability. Nomic’s layout optimizer performs dimensionality reduction, and decides on parameters for the high dimensional kernel, low dimensional kernel, and optimizer that enable better projection speed, size, and quality.
- Annotation colors and labels the map using user- and Atlas-generated metadata (like topic labels and duplicate detection).
- Presentation in the Atlas system is done with Deepscatter, a library developed by the Nomic Team which can efficiently visualize billions of datapoints in the browser using custom WebGL and Apache Arrow feather files in a custom quadtree format.
```
feather
```

## Unstructured Data​

Unstructured data is characterized by its lack of conventional tabular structure, and is typically challenging to organize and analyze using traditional spreadsheet tools or databases.

Nomic Atlas excels in managing and visualizing unstructured data, which encompasses diverse formats such as text documents, image galleries, audio files, videos, and AI model datasets.

To address this, Nomic Atlas introduces an AI-powered interface known as "the map." This innovative tool spatially organizes unstructured datapoints, grouping similar items together to facilitate intuitive understanding and interaction. Whether it's exploring large collections of multimedia content or collaborating on complex datasets, Nomic Atlas makes it possible to visualize and work with unstructured data seamlessly. Users can share insights and collaborate through a simple browser link, while developers gain programmatic access to the map's data and functionalities, enhancing the overall experience of unstructured data analysis.

## Embeddings​

Embeddings are the core of understanding and processing unstructured data in Nomic Atlas. They are numerical vectors representing real-world data, converting various forms of unstructured data into a format that computers can understand and process. These embeddings encapsulate the semantics and contextual relationships of data, whether it's text, images, or other media. Nomic Atlas automatically assigns embeddings to uploaded data, organizing it meaningfully. This process involves advanced AI and embedding models, transforming data into vector representations that capture their underlying meaning and relationships.

## Projection​

Projection in Nomic Atlas involves compressing high-dimensional data (like embeddings) into lower-dimensional spaces, primarily 2-D, for visualization and analysis. Techniques like UMAP, t-SNE, and PCA are employed to ensure that relative distances and relationships in high-dimensional space are preserved in the projected lower-dimensional space. This feature allows users to view and interact with complex datasets in a more comprehensible 2-D format on their screens, facilitating better understanding and manipulation of the data.

## Semantic Space​

Semantic space refers to an abstract space where data with semantic attributes in common are situated as nearby coordinates in space.

For example, in a semantic space of thousands of words, "cat" and "kitten" would be positioned near each other in a cluster, along with all the other words they share context and meaning with cats. Unrelated words like "calculator" would be be arranged in a different cluster of words that have similar a meaning to calculators.

In Nomic Atlas, semantic spaces are created when you upload data. Our embedding models produce an embedding vector for each data point, and our projection models then let you interact with the data on a map arranged as it is approximately situated in the semantic space (since vector spaces of embeddings are typically much higher-dimensional than 2D, and therefore only approximately representable in 2D).

## Topic Modeling​

Topic modeling is an advanced technique used in Nomic Atlas to automatically discover and categorize abstract themes within large text collections. By analyzing patterns of keywords and themes across documents, this method effectively groups texts into clusters based on shared topics. For instance, articles about health, finance, and technology can be automatically categorized into distinct clusters, each characterized by relevant sets of keywords. This automated categorization aids in sifting through vast amounts of unstructured text data to uncover underlying thematic structures without manual intervention.

- Unstructured Data
- Embeddings
- Projection
- Semantic Space
- Topic Modeling
