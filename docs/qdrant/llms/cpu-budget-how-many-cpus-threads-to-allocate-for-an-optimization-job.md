# CPU budget, how many CPUs (threads) to allocate for an optimization job.
optimizer_cpu_budget: 0

```

- If left at 0, Qdrant will keep 1 or more CPUs unallocated - depending on CPU size.
- If the setting is positive, Qdrant will use this exact number of CPUs for indexing.
- If the setting is negative, Qdrant will subtract this number of CPUs from the available CPUs for indexing.

For most users, the default `optimizer_cpu_budget` setting will work well. We only recommend you use this if your indexing load is significant.

Our backend leverages dynamic CPU saturation to increase indexing speed. For that reason, the impact on search query performance ends up being minimal. Ultimately, you will be able to strike the best possible balance between indexing times and search performance.

This configuration can be done at any time, but it requires a restart of Qdrant. Changing it affects both existing and new collections.

> **Note:** This feature is not configurable on [Qdrant Cloud](https://qdrant.to/cloud).

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#better-indexing-for-text-data) Better indexing for text data

In order to [minimize your RAM expenditure](https://qdrant.tech/articles/memory-consumption/), we have developed a new way to index specific types of data. Please keep in mind that this is a backend improvement, and you won’t need to configure anything.

> Going forward, if you are indexing immutable text fields, we estimate a 10% reduction in RAM loads. Our benchmark result is based on a system that uses 64GB of RAM. If you are using less RAM, this reduction might be higher than 10%.

Immutable text fields are static and do not change once they are added to Qdrant. These entries usually represent some type of attribute, description or tag. Vectors associated with them can be indexed more efficiently, since you don’t need to re-index them anymore. Conversely, mutable fields are dynamic and can be modified after their initial creation. Please keep in mind that they will continue to require additional RAM.

This approach ensures stability in the [vector search](https://qdrant.tech/documentation/overview/vector-search/) index, with faster and more consistent operations. We achieved this by setting up a field index which helps minimize what is stored. To improve search performance we have also optimized the way we load documents for searches with a text field index. Now our backend loads documents mostly sequentially and in increasing order.

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#minor-improvements-and-new-features) Minor improvements and new features

Beyond these enhancements, [Qdrant v1.8.0](https://github.com/qdrant/qdrant/releases/tag/v1.8.0) adds and improves on several smaller features:

1. **Order points by payload:** In addition to searching for semantic results, you might want to retrieve results by specific metadata (such as price). You can now use Scroll API to [order points by payload key](https://qdrant.tech/documentation/concepts/points/#order-points-by-payload-key).
2. **Datetime support:** We have implemented [datetime support for the payload index](https://qdrant.tech/documentation/concepts/filtering/#datetime-range). Prior to this, if you wanted to search for a specific datetime range, you would have had to convert dates to UNIX timestamps. ( [PR#3320](https://github.com/qdrant/qdrant/issues/3320))
3. **Check collection existence:** You can check whether a collection exists via the `/exists` endpoint to the `/collections/{collection_name}`. You will get a true/false response. ( [PR#3472](https://github.com/qdrant/qdrant/pull/3472)).
4. **Find points** whose payloads match more than the minimal amount of conditions. We included the `min_should` match feature for a condition to be `true` ( [PR#3331](https://github.com/qdrant/qdrant/pull/3466/)).
5. **Modify nested fields:** We have improved the `set_payload` API, adding the ability to update nested fields ( [PR#3548](https://github.com/qdrant/qdrant/pull/3548)).

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#experience-the-power-of-qdrant-180) Experience the Power of Qdrant 1.8.0

Ready to experience the enhanced performance of Qdrant 1.8.0? Upgrade now and explore the major improvements, from faster sparse vectors to optimized CPU resource management and better indexing for text data. Take your search capabilities to the next level with Qdrant’s latest version. [Try a demo today](https://qdrant.tech/demo/) and see the difference firsthand!

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#release-notes) Release notes

For more information, see [our release notes](https://github.com/qdrant/qdrant/releases/tag/v1.8.0).
Qdrant is an open-source project. We welcome your contributions; raise [issues](https://github.com/qdrant/qdrant/issues), or contribute via [pull requests](https://github.com/qdrant/qdrant/pulls)!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.8.x.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.8.x.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-35-lllmstxt|>
## what-is-a-vector-database
- [Articles](https://qdrant.tech/articles/)
- What is a Vector Database?

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)