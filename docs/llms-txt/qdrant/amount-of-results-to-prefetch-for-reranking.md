# Amount of results to prefetch for reranking
prefetch_limit = 100

response = client.query_points(
    collection_name=collection_name,
    query=query_embedding,
    prefetch=[\
        models.Prefetch(\
            query=query_embedding,\
            limit=prefetch_limit,\
            using="mean_pooling_columns"\
        ),\
        models.Prefetch(\
            query=query_embedding,\
            limit=prefetch_limit,\
            using="mean_pooling_rows"\
        ),\
    ],
    limit=search_limit,
    with_payload=True,
    with_vector=False,
    using="original"
)

```

And check the top retrieved result to our query _“Lee Harvey Oswald’s involvement in the JFK assassination”_.

```python
dataset[response.points[0].payload['index']]['image']

```

![Results, ColPali](https://qdrant.tech/documentation/tutorials/pdf-retrieval-at-scale/result-VLLMs.png)

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#conclusion) Conclusion

In this tutorial, we demonstrated an optimized approach using **Qdrant for PDF retrieval at scale** with VLLMs producing **heavy multivector representations** like **ColPali** and **ColQwen2**.

Without such optimization, the performance of retrieval systems can degrade severely, both in terms of indexing time and query latency, especially as the dataset size grows.

We **strongly recommend** implementing this approach in your workflows to ensure efficient and scalable PDF retrieval. Neglecting to optimize the retrieval process could result in unacceptably slow performance, hindering the usability of your system.

Start scaling your PDF retrieval today!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/pdf-retrieval-at-scale.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/pdf-retrieval-at-scale.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-160-lllmstxt|>
## fastembed-semantic-search
- [Documentation](https://qdrant.tech/documentation/)
- [Fastembed](https://qdrant.tech/documentation/fastembed/)
- FastEmbed & Qdrant