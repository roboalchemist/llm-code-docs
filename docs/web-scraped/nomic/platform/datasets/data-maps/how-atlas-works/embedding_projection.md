# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/how-atlas-works/embedding_projection

Embeddings are vector representations of real-world objects, and embedding projection preserves the semantic neighborhood information embeddings capture in two dimensions.

Despite their mathematical utility, high-dimensional embeddings cannot be easily interpreted because humans do not have a good point of reference for understanding what a 768-dimensional vector "looks" like.

Atlas augments your dataset using embedding projection to build a contextual two-dimensional data map from high-dimensional embeddings. This map preserves high-dimensional relationships present between embeddings in a two-dimensional, human interpretable view.

## Embedding​

Atlas uses a contrastively trained deep neural network, similar to Neelakantan et al., to vectorize text. Users may also upload their own embeddings to build Atlas maps. Image, audio, video, and multimodal embeddings are on the way to Atlas.

## Projection​

Nomic Atlas takes high-dimensional embeddings and generates a low-dimensional set of vectors for mapping. Nomic’s layout optimizer performs dimensionality reduction on embeddings, and decides on parameters for the high dimensional kernel, low dimensional kernel, and optimizer that enable optimized projection speed, size, and quality.

- Embedding
- Projection
