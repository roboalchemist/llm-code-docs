# query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)

```

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#run-a-test-query) Run a test query

Now you can ask questions and receive answers based on the data:

**Question**

```python
result = query_engine.query("What temperature should I use for my laundry?")
print(result.response)

```

**Answer**

```text
The water temperature is set to 70 ˚C during the Eco Drum Clean cycle. You cannot change the water temperature. However, the temperature for other cycles is not specified in the context.

```

And that’s it! Feel free to scale this up to as many documents and complex PDFs as you like.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/hybrid-search-llamaindex-jinaai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/hybrid-search-llamaindex-jinaai.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-20-lllmstxt|>
## fastembed-rerankers
- [Documentation](https://qdrant.tech/documentation/)
- [Fastembed](https://qdrant.tech/documentation/fastembed/)
- Reranking with FastEmbed