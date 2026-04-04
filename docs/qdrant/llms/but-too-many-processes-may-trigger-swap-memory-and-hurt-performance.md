# But too many processes may trigger swap memory and hurt performance.
client.upload_points("qdrant-sources", points=points, batch_size=64)

```

Internally, `qdrant-client` uses [FastEmbed](https://github.com/qdrant/fastembed) to implicitly convert our documents into their vector representations.
The uploaded points are immediately available for search. Next, query the
collection to find relevant code snippets.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#querying-the-codebase) Querying the codebase

We use one of the models to search the collection. Start with text embeddings.
Run the following query “ _How do I count points in a collection?_”. Review the
results.

```python
query = "How do I count points in a collection?"

hits = client.query_points(
    "qdrant-sources",
    query=models.Document(text=query, model="sentence-transformers/all-MiniLM-L6-v2"),
    using="text",
    limit=5,
).points

```

Now, review the results. The following table lists the module, the file name
and score. Each line includes a link to the signature, as a code block from
the file.

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| toc | point\_ops.rs | 0.59448624 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/storage/src/content_manager/toc/point_ops.rs#L120) |
| operations | types.rs | 0.5493385 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub struct CountRequestInternal`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/operations/types.rs#L831) |
| collection\_manager | segments\_updater.rs | 0.5121002 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub(crate) fn upsert_points<'a, T>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection_manager/segments_updater.rs#L339) |
| collection | point\_ops.rs | 0.5063539 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection/point_ops.rs#L213) |
| map\_index | mod.rs | 0.49973983 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn get_points_with_value_count<Q>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/map_index/mod.rs#L88) |

It seems we were able to find some relevant code structures. Let’s try the same with the code embeddings:

```python
hits = client.query_points(
    "qdrant-sources",
    query=models.Document(text=query, model="jinaai/jina-embeddings-v2-base-code"),
    using="code",
    limit=5,
).points

```

Output:

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| field\_index | geo\_index.rs | 0.73278356 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/geo_index.rs#L612) |
| numeric\_index | mod.rs | 0.7254976 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/numeric_index/mod.rs#L322) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L315) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L429) |
| fixtures | payload\_context\_fixture.rs | 0.706204 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn total_point_count`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/fixtures/payload_context_fixture.rs#L122) |

While the scores retrieved by different models are not comparable, but we can
see that the results are different. Code and text embeddings can capture
different aspects of the codebase. We can use both models to query the collection
and then combine the results to get the most relevant code snippets, from a single batch request.

```python
responses = client.query_batch_points(
    collection_name="qdrant-sources",
    requests=[\
        models.QueryRequest(\
            query=models.Document(\
                text=query, model="sentence-transformers/all-MiniLM-L6-v2"\
            ),\
            using="text",\
            with_payload=True,\
            limit=5,\
        ),\
        models.QueryRequest(\
            query=models.Document(\
                text=query, model="jinaai/jina-embeddings-v2-base-code"\
            ),\
            using="code",\
            with_payload=True,\
            limit=5,\
        ),\
    ],
)

results = [response.points for response in responses]

```

Output:

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| toc | point\_ops.rs | 0.59448624 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/storage/src/content_manager/toc/point_ops.rs#L120) |
| operations | types.rs | 0.5493385 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub struct CountRequestInternal`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/operations/types.rs#L831) |
| collection\_manager | segments\_updater.rs | 0.5121002 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub(crate) fn upsert_points<'a, T>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection_manager/segments_updater.rs#L339) |
| collection | point\_ops.rs | 0.5063539 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`pub async fn count`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/collection/src/collection/point_ops.rs#L213) |
| map\_index | mod.rs | 0.49973983 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn get_points_with_value_count<Q>`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/map_index/mod.rs#L88) |
| field\_index | geo\_index.rs | 0.73278356 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/geo_index.rs#L612) |
| numeric\_index | mod.rs | 0.7254976 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/numeric_index/mod.rs#L322) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L315) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L429) |
| fixtures | payload\_context\_fixture.rs | 0.706204 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn total_point_count`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/fixtures/payload_context_fixture.rs#L122) |

This is one example of how you can use different models and combine the results.
In a real-world scenario, you might run some reranking and deduplication, as
well as additional processing of the results.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#code-search-demo) Code search demo

Our [Code search demo](https://code-search.qdrant.tech/) uses the following process:

1. The user sends a query.
2. Both models vectorize that query simultaneously. We get two different
vectors.
3. Both vectors are used in parallel to find relevant snippets. We expect
5 examples from the NLP search and 20 examples from the code search.
4. Once we retrieve results for both vectors, we merge them in one of the
following scenarios:
1. If both methods return different results, we prefer the results from
      the general usage model (NLP).
2. If there is an overlap between the search results, we merge overlapping
      snippets.

In the screenshot, we search for `flush of wal`. The result
shows relevant code, merged from both models. Note the highlighted
code in lines 621-629. It’s where both models agree.

![Results from both models, with overlap](https://qdrant.tech/documentation/tutorials/code-search/code-search-demo-example.png)

Now you see semantic code intelligence, in action.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#grouping-the-results) Grouping the results

You can improve the search results, by grouping them by payload properties.
In our case, we can group the results by the module. If we use code embeddings,
we can see multiple results from the `map_index` module. Let’s group the
results and assume a single result per module:

```python
results = client.query_points_groups(
    collection_name="qdrant-sources",
    using="code",
    query=models.Document(text=query, model="jinaai/jina-embeddings-v2-base-code"),
    group_by="context.module",
    limit=5,
    group_size=1,
)

```

Output:

| module | file\_name | score | signature |
| --- | --- | --- | --- |
| field\_index | geo\_index.rs | 0.73278356 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/7aa164bd2dda1c0fc9bf3a0da42e656c95c2e52a/lib/segment/src/index/field_index/geo_index.rs#L612) |
| numeric\_index | mod.rs | 0.7254976 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/numeric_index/mod.rs#L322) |
| map\_index | mod.rs | 0.7124739 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn count_indexed_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/field_index/map_index/mod.rs#L315) |
| fixtures | payload\_context\_fixture.rs | 0.706204 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn total_point_count`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/fixtures/payload_context_fixture.rs#L122) |
| hnsw\_index | graph\_links.rs | 0.6998417 | [![](https://qdrant.tech/documentation/tutorials/code-search/github-mark.png)`fn num_points`](https://github.com/qdrant/qdrant/blob/3fbe1cae6cb7f51a0c5bb4b45cfe6749ac76ed59/lib/segment/src/index/hnsw_index/graph_links.rs#L477) |

With the grouping feature, we get more diverse results.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/code-search/\#summary) Summary

This tutorial demonstrates how to use Qdrant to navigate a codebase. For an
end-to-end implementation, review the [code search\\
notebook](https://colab.research.google.com/github/qdrant/examples/blob/master/code-search/code-search.ipynb) and the
[code-search-demo](https://github.com/qdrant/demo-code-search). You can also check out [a running version of the code\\
search demo](https://code-search.qdrant.tech/) which exposes Qdrant codebase for search with a web interface.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/code-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/code-search.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-25-lllmstxt|>
## product-quantization
- [Articles](https://qdrant.tech/articles/)
- Product Quantization in Vector Search \| Qdrant

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)