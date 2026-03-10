# on_disk=True and the quantization_config are the areas to focus on
collection_name = "binary-quantization"
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=f"{collection_name}",
        vectors_config=models.VectorParams(
            size=1536,
            distance=models.Distance.DOT,
            on_disk=True,
        ),
        optimizers_config=models.OptimizersConfigDiff(
            default_segment_number=5,
        ),
        hnsw_config=models.HnswConfigDiff(
        m=0,
        ),
        quantization_config=models.BinaryQuantization(
            binary=models.BinaryQuantizationConfig(always_ram=True),
        ),
    )

```

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#what-is-happening-in-the-hnswconfig) What is happening in the HnswConfig?

We’re setting `m` to 0 i.e. disabling the HNSW graph construction. This allows faster uploads of vectors and payloads. We will turn it back on down below, once all the data is loaded.

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#next-we-upload-our-vectors-to-this-and-then-enable-the-graph-construction) Next, we upload our vectors to this and then enable the graph construction:

```python
batch_size = 10000
client.upload_collection(
    collection_name=collection_name,
    ids=range(len(dataset)),
    vectors=dataset["openai"],
    payload=[\
        {"text": x} for x in dataset["text"]\
    ],
    parallel=10, # based on the machine
)

```

Enable HNSW graph construction again:

```python
client.update_collection(
    collection_name=f"{collection_name}",
    hnsw_config=models.HnswConfigDiff(
        m=16,
    ,
)

```

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#configure-the-search-parameters) Configure the search parameters:

When setting search parameters, we specify that we want to use `oversampling` and `rescore`. Here is an example snippet:

```python
client.search(
    collection_name="{collection_name}",
    query_vector=[0.2, 0.1, 0.9, 0.7, ...],
    search_params=models.SearchParams(
        quantization=models.QuantizationSearchParams(
            ignore=False,
            rescore=True,
            oversampling=2.0,
        )
    )
)

```

After Qdrant pulls the oversampled vectors set, the full vectors which will be, say 1536 dimensions for OpenAI will then be pulled up from disk. Qdrant computes the nearest neighbor with the query vector and returns the accurate, rescored order. This method produces much more accurate results. We enabled this by setting `rescore=True`.

These two parameters are how you are going to balance speed versus accuracy. The larger the size of your oversample, the more items you need to read from disk and the more elements you have to search with the relatively slower full vector index. On the other hand, doing this will produce more accurate results.

If you have lower accuracy requirements you can even try doing a small oversample without rescoring. Or maybe, for your data set combined with your accuracy versus speed requirements you can just search the binary index and no rescoring, i.e. leaving those two parameters out of the search query.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#benchmark-results) Benchmark results

We retrieved some early results on the relationship between limit and oversampling using the the DBPedia OpenAI 1M vector dataset. We ran all these experiments on a Qdrant instance where 100K vectors were indexed and used 100 random queries.

We varied the 3 parameters that will affect query time and accuracy: limit, rescore and oversampling. We offer these as an initial exploration of this new feature. You are highly encouraged to reproduce these experiments with your data sets.

> Aside: Since this is a new innovation in vector databases, we are keen to hear feedback and results. [Join our Discord server](https://discord.gg/Qy6HCJK9Dc) for further discussion!

**Oversampling:**
In the figure below, we illustrate the relationship between recall and number of candidates:

![Correct vs candidates](https://qdrant.tech/articles_data/binary-quantization/bq-5.png)

We see that “correct” results i.e. recall increases as the number of potential “candidates” increase (limit x oversampling). To highlight the impact of changing the `limit`, different limit values are broken apart into different curves. For example, we see that the lowest recall for limit 50 is around 94 correct, with 100 candidates. This also implies we used an oversampling of 2.0

As oversampling increases, we see a general improvement in results – but that does not hold in every case.

**Rescore:**
As expected, rescoring increases the time it takes to return a query.
We also repeated the experiment with oversampling except this time we looked at how rescore impacted result accuracy.

![Relationship between limit and rescore on correct](https://qdrant.tech/articles_data/binary-quantization/bq-7.png)

**Limit:**
We experiment with limits from Top 1 to Top 50 and we are able to get to 100% recall at limit 50, with rescore=True, in an index with 100K vectors.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#recommendations) Recommendations

Quantization gives you the option to make tradeoffs against other parameters:
Dimension count/embedding size
Throughput and Latency requirements
Recall requirements

If you’re working with OpenAI or Cohere embeddings, we recommend the following oversampling settings:

| Method | Dimensionality | Test Dataset | Recall | Oversampling |
| --- | --- | --- | --- | --- |
| OpenAI text-embedding-3-large | 3072 | [DBpedia 1M](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-3072-1M) | 0.9966 | 3x |
| OpenAI text-embedding-3-small | 1536 | [DBpedia 100K](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-small-1536-100K) | 0.9847 | 3x |
| OpenAI text-embedding-3-large | 1536 | [DBpedia 1M](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-1536-1M) | 0.9826 | 3x |
| OpenAI text-embedding-ada-002 | 1536 | [DbPedia 1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) | 0.98 | 4x |
| Gemini | 768 | No Open Data | 0.9563 | 3x |
| Mistral Embed | 768 | No Open Data | 0.9445 | 3x |

If you determine that binary quantization is appropriate for your datasets and queries then we suggest the following:

- Binary Quantization with always\_ram=True
- Vectors stored on disk
- Oversampling=2.0 (or more)
- Rescore=True

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#whats-next) What’s next?

Binary quantization is exceptional if you need to work with large volumes of data under high recall expectations. You can try this feature either by spinning up a [Qdrant container image](https://hub.docker.com/r/qdrant/qdrant) locally or, having us create one for you through a [free account](https://cloud.qdrant.io/signup) in our cloud hosted service.

The article gives examples of data sets and configuration you can use to get going. Our documentation covers [adding large datasets to Qdrant](https://qdrant.tech/documentation/tutorials/bulk-upload/) to your Qdrant instance as well as [more quantization methods](https://qdrant.tech/documentation/guides/quantization/).

If you have any feedback, drop us a note on Twitter or LinkedIn to tell us about your results. [Join our lively Discord Server](https://discord.gg/Qy6HCJK9Dc) if you want to discuss BQ with like-minded people!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/binary-quantization.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/binary-quantization.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-135-lllmstxt|>
## monitoring
- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Monitoring & Telemetry