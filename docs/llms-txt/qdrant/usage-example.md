# Usage example
sorted_tokens = extract_and_map_sparse_vector(vec, tokenizer)
sorted_tokens

```

There will be 102 sorted tokens in total. This has expanded to include tokens that weren’t in the original text. This is the term expansion we will talk about next.

Here are some terms that are added: “Berlin”, and “founder” - despite having no mention of Arthur’s race (which leads to Owen’s Berlin win) and his work as the founder of Arthur Ashe Institute for Urban Health. Here are the top few `sorted_tokens` with a weight of more than 1:

```python
{
    "ashe": 2.95,
    "arthur": 2.61,
    "tennis": 2.22,
    "robert": 1.74,
    "jr": 1.55,
    "he": 1.39,
    "founder": 1.36,
    "doubles": 1.24,
    "won": 1.22,
    "slam": 1.22,
    "died": 1.19,
    "singles": 1.1,
    "was": 1.07,
    "player": 1.06,
    "titles": 0.99,
    ...
}

```

If you’re interested in using the higher-performance approach, check out the following models:

1. [naver/efficient-splade-VI-BT-large-doc](https://huggingface.co/naver/efficient-splade-vi-bt-large-doc)
2. [naver/efficient-splade-VI-BT-large-query](https://huggingface.co/naver/efficient-splade-vi-bt-large-doc)

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#why-splade-works-term-expansion) Why SPLADE works: term expansion

Consider a query “solar energy advantages”. SPLADE might expand this to include terms like “renewable,” “sustainable,” and “photovoltaic,” which are contextually relevant but not explicitly mentioned. This process is called term expansion, and it’s a key component of SPLADE.

SPLADE learns the query/document expansion to include other relevant terms. This is a crucial advantage over other sparse methods which include the exact word, but completely miss the contextually relevant ones.

This expansion has a direct relationship with what we can control when making a SPLADE model: Sparsity via Regularisation. The number of tokens (BERT wordpieces) we use to represent each document. If we use more tokens, we can represent more terms, but the vectors become denser. This number is typically between 20 to 200 per document. As a reference point, the dense BERT vector is 768 dimensions, OpenAI Embedding is 1536 dimensions, and the sparse vector is 30 dimensions.

For example, assume a 1M document corpus. Say, we use 100 sparse token ids + weights per document. Correspondingly, dense BERT vector would be 768M floats, the OpenAI Embedding would be 1.536B floats, and the sparse vector would be a maximum of 100M integers + 100M floats. This could mean a **10x reduction in memory usage**, which is a huge win for large-scale systems:

| Vector Type | Memory (GB) |
| --- | --- |
| Dense BERT Vector | 6.144 |
| OpenAI Embedding | 12.288 |
| Sparse Vector | 1.12 |

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#how-splade-works-leveraging-bert) How SPLADE works: leveraging BERT

SPLADE leverages a transformer architecture to generate sparse representations of documents and queries, enabling efficient retrieval. Let’s dive into the process.

The output logits from the transformer backbone are inputs upon which SPLADE builds. The transformer architecture can be something familiar like BERT. Rather than producing dense probability distributions, SPLADE utilizes these logits to construct sparse vectors—think of them as a distilled essence of tokens, where each dimension corresponds to a term from the vocabulary and its associated weight in the context of the given document or query.

This sparsity is critical; it mirrors the probability distributions from a typical [Masked Language Modeling](http://jalammar.github.io/illustrated-bert/?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors) task but is tuned for retrieval effectiveness, emphasizing terms that are both:

1. Contextually relevant: Terms that represent a document well should be given more weight.
2. Discriminative across documents: Terms that a document has, and other documents don’t, should be given more weight.

The token-level distributions that you’d expect in a standard transformer model are now transformed into token-level importance scores in SPLADE. These scores reflect the significance of each term in the context of the document or query, guiding the model to allocate more weight to terms that are likely to be more meaningful for retrieval purposes.

The resulting sparse vectors are not only memory-efficient but also tailored for precise matching in the high-dimensional space of a search engine like Qdrant.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#interpreting-splade) Interpreting SPLADE

A downside of dense vectors is that they are not interpretable, making it difficult to understand why a document is relevant to a query.

SPLADE importance estimation can provide insights into the ‘why’ behind a document’s relevance to a query. By shedding light on which tokens contribute most to the retrieval score, SPLADE offers some degree of interpretability alongside performance, a rare feat in the realm of neural IR systems. For engineers working on search, this transparency is invaluable.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#known-limitations-of-splade) Known limitations of SPLADE

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#pooling-strategy) Pooling strategy

The switch to max pooling in SPLADE improved its performance on the MS MARCO and TREC datasets. However, this indicates a potential limitation of the baseline SPLADE pooling method, suggesting that SPLADE’s performance is sensitive to the choice of pooling strategy​​.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#document-and-query-eecoder) Document and query Eecoder

The SPLADE model variant that uses a document encoder with max pooling but no query encoder reaches the same performance level as the prior SPLADE model. This suggests a limitation in the necessity of a query encoder, potentially affecting the efficiency of the model​​.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#other-sparse-vector-methods) Other sparse vector methods

SPLADE is not the only method to create sparse vectors.

Essentially, sparse vectors are a superset of TF-IDF and BM25, which are the most popular text retrieval methods.
In other words, you can create a sparse vector using the term frequency and inverse document frequency (TF-IDF) to reproduce the BM25 score exactly.

Additionally, attention weights from Sentence Transformers can be used to create sparse vectors.
This method preserves the ability to query exact words and phrases but avoids the computational overhead of query expansion used in SPLADE.

We will cover these methods in detail in a future article.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#leveraging-sparse-vectors-in-qdrant-for-hybrid-search) Leveraging sparse vectors in Qdrant for hybrid search

Qdrant supports a separate index for Sparse Vectors.
This enables you to use the same collection for both dense and sparse vectors.
Each “Point” in Qdrant can have both dense and sparse vectors.

But let’s first take a look at how you can work with sparse vectors in Qdrant.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#practical-implementation-in-python) Practical implementation in Python

Let’s dive into how Qdrant handles sparse vectors with an example. Here is what we will cover:

1. Setting Up Qdrant Client: Initially, we establish a connection with Qdrant using the QdrantClient. This setup is crucial for subsequent operations.

2. Creating a Collection with Sparse Vector Support: In Qdrant, a collection is a container for your vectors. Here, we create a collection specifically designed to support sparse vectors. This is done using the create\_collection method where we define the parameters for sparse vectors, such as setting the index configuration.

3. Inserting Sparse Vectors: Once the collection is set up, we can insert sparse vectors into it. This involves defining the sparse vector with its indices and values, and then upserting this point into the collection.

4. Querying with Sparse Vectors: To perform a search, we first prepare a query vector. This involves computing the vector from a query text and extracting its indices and values. We then use these details to construct a query against our collection.

5. Retrieving and Interpreting Results: The search operation returns results that include the id of the matching document, its score, and other relevant details. The score is a crucial aspect, reflecting the similarity between the query and the documents in the collection.


### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#1-set-up) 1\. Set up

```python