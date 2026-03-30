# [SEP]       : 0.047 // Filter out the [SEP] token

```

The resulting formula for the BM42 score would look like this:

score(D,Q)=∑i=1NIDF(qi)×Attention(CLS,qi)

Note that classical transformers have multiple attention heads, so we can get multiple importance vectors for the same document. The simplest way to combine them is to simply average them.

These averaged attention vectors make up the importance information we were looking for.
The best part is, one can get them from any transformer model, without any additional training.
Therefore, BM42 can support any natural language as long as there is a transformer model for it.

In our implementation, we use the `sentence-transformers/all-MiniLM-L6-v2` model, which gives a huge boost in the inference speed compared to the SPLADE models. In practice, any transformer model can be used.
It doesn’t require any additional training, and can be easily adapted to work as BM42 backend.

### [Anchor](https://qdrant.tech/articles/bm42/\#wordpiece-retokenization) WordPiece retokenization

The final piece of the puzzle we need to solve is the tokenization issue. In order to get attention vectors, we need to use native transformer tokenization.
But this tokenization is not suitable for the retrieval tasks. What can we do about it?

Actually, the solution we came up with is quite simple. We reverse the tokenization process after we get the attention vectors.

Transformers use [WordPiece](https://huggingface.co/learn/nlp-course/en/chapter6/6) tokenization.
In case it sees the word, which is not in the vocabulary, it splits it into subwords.

Here is how that looks:

```text
"unbelievable" -> ["un", "##believ", "##able"]

```

What can merge the subwords back into the words. Luckily, the subwords are marked with the `##` prefix, so we can easily detect them.
Since the attention weights are normalized, we can simply sum the attention weights of the subwords to get the attention weight of the word.

After that, we can apply the same traditional NLP techniques, as

- Removing of the stop-words
- Removing of the punctuation
- Lemmatization

In this way, we can significantly reduce the number of tokens, and therefore minimize the memory footprint of the sparse embeddings. We won’t simultaneously compromise the ability to match (almost) exact tokens.

## [Anchor](https://qdrant.tech/articles/bm42/\#practical-examples) Practical examples

| Trait | BM25 | SPLADE | BM42 |
| --- | --- | --- | --- |
| Interpretability | High ✅ | Ok 🆗 | High ✅ |
| Document Inference speed | Very high ✅ | Slow 🐌 | High ✅ |
| Query Inference speed | Very high ✅ | Slow 🐌 | Very high ✅ |
| Memory footprint | Low ✅ | High ❌ | Low ✅ |
| In-domain accuracy | Ok 🆗 | High ✅ | High ✅ |
| Out-of-domain accuracy | Ok 🆗 | Low ❌ | Ok 🆗 |
| Small documents accuracy | Low ❌ | High ✅ | High ✅ |
| Large documents accuracy | High ✅ | Low ❌ | Ok 🆗 |
| Unknown tokens handling | Yes ✅ | Bad ❌ | Yes ✅ |
| Multi-lingual support | Yes ✅ | No ❌ | Yes ✅ |
| Best Match | Yes ✅ | No ❌ | Yes ✅ |

Starting from Qdrant v1.10.0, BM42 can be used in Qdrant via FastEmbed inference.

Let’s see how you can setup a collection for hybrid search with BM42 and [jina.ai](https://jina.ai/embeddings/) dense embeddings.

httppython

```http
PUT collections/my-hybrid-collection
{
  "vectors": {
    "jina": {
      "size": 768,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "bm42": {
      "modifier": "idf" // <--- This parameter enables the IDF calculation
    }
  }
}

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient()

client.create_collection(
    collection_name="my-hybrid-collection",
    vectors_config={
        "jina": models.VectorParams(
            size=768,
            distance=models.Distance.COSINE,
        )
    },
    sparse_vectors_config={
        "bm42": models.SparseVectorParams(
            modifier=models.Modifier.IDF,
        )
    }
)

```

The search query will retrieve the documents with both dense and sparse embeddings and combine the scores
using the Reciprocal Rank Fusion (RRF) algorithm.

```python
from fastembed import SparseTextEmbedding, TextEmbedding

query_text = "best programming language for beginners?"

model_bm42 = SparseTextEmbedding(model_name="Qdrant/bm42-all-minilm-l6-v2-attentions")
model_jina = TextEmbedding(model_name="jinaai/jina-embeddings-v2-base-en")

sparse_embedding = list(model_bm42.query_embed(query_text))[0]
dense_embedding = list(model_jina.query_embed(query_text))[0]

client.query_points(
  collection_name="my-hybrid-collection",
  prefetch=[\
      models.Prefetch(query=sparse_embedding.as_object(), using="bm42", limit=10),\
      models.Prefetch(query=dense_embedding.tolist(),  using="jina", limit=10),\
  ],
  query=models.FusionQuery(fusion=models.Fusion.RRF), # <--- Combine the scores
  limit=10
)

```

### [Anchor](https://qdrant.tech/articles/bm42/\#benchmarks) Benchmarks

To prove the point further we have conducted some benchmarks to highlight the cases where BM42 outperforms BM25.
Please note, that we didn’t intend to make an exhaustive evaluation, as we are presenting a new approach, not a new model.

For out experiments we choose [quora](https://huggingface.co/datasets/BeIR/quora) dataset, which represents a question-deduplication task ~~the Question-Answering task~~.

The typical example of the dataset is the following:

```text
{"_id": "109", "text": "How GST affects the CAs and tax officers?"}
{"_id": "110", "text": "Why can't I do my homework?"}
{"_id": "111", "text": "How difficult is it get into RSI?"}

```

As you can see, it has pretty short texts, there are not much of the statistics to rely on.

After encoding with BM42, the average vector size is only **5.6 elements per document**.

With `datatype: uint8` available in Qdrant, the total size of the sparse vector index is about **13MB** for ~530k documents.

As a reference point, we use:

- BM25 with tantivy
- the [sparse vector BM25 implementation](https://github.com/qdrant/bm42_eval/blob/master/index_bm25_qdrant.py) with the same preprocessing pipeline like for BM42: tokenization, stop-words removal, and lemmatization

|  | BM25 (tantivy) | BM25 (Sparse) | BM42 |
| --- | --- | --- | --- |
| ~~Precision @ 10~~ \* | ~~0.45~~ | ~~0.45~~ | ~~0.49~~ |
| Recall @ 10 | ~~0.71~~ **0.89** | 0.83 | 0.85 |

\\* \- values were corrected after the publication due to a mistake in the evaluation script.

To make our benchmarks transparent, we have published scripts we used for the evaluation: see [github repo](https://github.com/qdrant/bm42_eval).

Please note, that both BM25 and BM42 won’t work well on their own in a production environment.
Best results are achieved with a combination of sparse and dense embeddings in a hybrid approach.
In this scenario, the two models are complementary to each other.
The sparse model is responsible for exact token matching, while the dense model is responsible for semantic matching.

Some more advanced models might outperform default `sentence-transformers/all-MiniLM-L6-v2` model we were using.
We encourage developers involved in training embedding models to include a way to extract attention weights and contribute to the BM42 backend.

## [Anchor](https://qdrant.tech/articles/bm42/\#fostering-curiosity-and-experimentation) Fostering curiosity and experimentation

Despite all of its advantages, BM42 is not always a silver bullet.
For large documents without chunks, BM25 might still be a better choice.

There might be a smarter way to extract the importance information from the transformer. There could be a better method to weigh IDF against attention scores.

Qdrant does not specialize in model training. Our core project is the search engine itself. However, we understand that we are not operating in a vacuum. By introducing BM42, we are stepping up to empower our community with novel tools for experimentation.

We truly believe that the sparse vectors method is at exact level of abstraction to yield both powerful and flexible results.

Many of you are sharing your recent Qdrant projects in our [Discord channel](https://discord.com/invite/qdrant). Feel free to try out BM42 and let us know what you come up with.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/bm42.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/bm42.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-140-lllmstxt|>
## memory-consumption
- [Articles](https://qdrant.tech/articles/)
- Minimal RAM you need to serve a million vectors

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)