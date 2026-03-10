# Compute sparse and dense vectors
query_indices, query_values = compute_sparse_vector(query_text)
query_dense_vector = compute_dense_vector(query_text)

client.search_batch(
    collection_name=COLLECTION_NAME,
    requests=[\
        models.SearchRequest(\
            vector=models.NamedVector(\
                name="text-dense",\
                vector=query_dense_vector,\
            ),\
            limit=10,\
        ),\
        models.SearchRequest(\
            vector=models.NamedSparseVector(\
                name="text-sparse",\
                vector=models.SparseVector(\
                    indices=query_indices,\
                    values=query_values,\
                ),\
            ),\
            limit=10,\
        ),\
    ],
)

```

The result will be a pair of result lists, one for dense and one for sparse vectors.

Having those results, there are several ways to combine them:

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#mixing-or-fusion) Mixing or fusion

You can mix the results from both dense and sparse vectors, based purely on their relative scores. This is a simple and effective approach, but it doesn’t take into account the semantic similarity between the results. Among the [popular mixing methods](https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18) are:

```
- Reciprocal Ranked Fusion (RRF)
- Relative Score Fusion (RSF)
- Distribution-Based Score Fusion (DBSF)

```

![Relative Score Fusion](https://qdrant.tech/articles_data/sparse-vectors/mixture.png)

Relative Score Fusion

[Ranx](https://github.com/AmenRa/ranx) is a great library for mixing results from different sources.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#re-ranking) Re-ranking

You can use obtained results as a first stage of a two-stage retrieval process. In the second stage, you can re-rank the results from the first stage using a more complex model, such as [Cross-Encoders](https://www.sbert.net/examples/applications/cross-encoder/README.html) or services like [Cohere Rerank](https://txt.cohere.com/rerank/).

And that’s it! You’ve successfully achieved hybrid search with Qdrant!

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#additional-resources) Additional resources

For those who want to dive deeper, here are the top papers on the topic most of which have code available:

1. Problem Motivation: [Sparse Overcomplete Word Vector Representations](https://ar5iv.org/abs/1506.02004?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors)
2. [SPLADE v2: Sparse Lexical and Expansion Model for Information Retrieval](https://ar5iv.org/abs/2109.10086?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors)
3. [SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking](https://ar5iv.org/abs/2107.05720?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors)
4. Late Interaction - [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://ar5iv.org/abs/2112.01488?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors)
5. [SparseEmbed: Learning Sparse Lexical Representations with Contextual Embeddings for Retrieval](https://research.google/pubs/pub52289/?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors)

**Why just read when you can try it out?**

We’ve packed an easy-to-use Colab for you on how to make a Sparse Vector: [Sparse Vectors Single Encoder Demo](https://colab.research.google.com/drive/1wa2Yr5BCOgV0MTOFFTude99BOXCLHXky?usp=sharing). Run it, tinker with it, and start seeing the magic unfold in your projects. We can’t wait to hear how you use it!

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#conclusion) Conclusion

Alright, folks, let’s wrap it up. Better search isn’t a ’nice-to-have,’ it’s a game-changer, and Qdrant can get you there.

Got questions? Our [Discord community](https://qdrant.to/discord?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors) is teeming with answers.

If you enjoyed reading this, why not sign up for our [newsletter](https://qdrant.tech/subscribe/?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors) to stay ahead of the curve.

And, of course, a big thanks to you, our readers, for pushing us to make ranking better for everyone.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/sparse-vectors.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/sparse-vectors.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-14-lllmstxt|>
## rag-chatbot-red-hat-openshift-haystack
- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Private Chatbot for Interactive Learning