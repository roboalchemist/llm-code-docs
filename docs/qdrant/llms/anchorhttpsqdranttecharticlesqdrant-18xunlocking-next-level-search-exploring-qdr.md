# [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#unlocking-next-level-search-exploring-qdrant-180s-advanced-search-capabilities) Unlocking Next-Level Search: Exploring Qdrant 1.8.0’s Advanced Search Capabilities

[Qdrant 1.8.0 is out!](https://github.com/qdrant/qdrant/releases/tag/v1.8.0).
This time around, we have focused on Qdrant’s internals. Our goal was to optimize performance so that your existing setup can run faster and save on compute. Here is what we’ve been up to:

- **Faster [sparse vectors](https://qdrant.tech/articles/sparse-vectors/):** [Hybrid search](https://qdrant.tech/articles/hybrid-search/) is up to 16x faster now!
- **CPU resource management:** You can allocate CPU threads for faster indexing.
- **Better indexing performance:** We optimized text [indexing](https://qdrant.tech/documentation/concepts/indexing/) on the backend.

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#faster-search-with-sparse-vectors) Faster search with sparse vectors

Search throughput is now up to 16 times faster for sparse vectors. If you are [using Qdrant for hybrid search](https://qdrant.tech/articles/sparse-vectors/), this means that you can now handle up to sixteen times as many queries. This improvement comes from extensive backend optimizations aimed at increasing efficiency and capacity.

What this means for your setup:

- **Query speed:** The time it takes to run a search query has been significantly reduced.
- **Search capacity:** Qdrant can now handle a much larger volume of search requests.
- **User experience:** Results will appear faster, leading to a smoother experience for the user.
- **Scalability:** You can easily accommodate rapidly growing users or an expanding dataset.

### [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#sparse-vectors-benchmark) Sparse vectors benchmark

Performance results are publicly available for you to test. Qdrant’s R&D developed a dedicated [open-source benchmarking tool](https://github.com/qdrant/sparse-vectors-benchmark) just to test sparse vector performance.

A real-life simulation of sparse vector queries was run against the [NeurIPS 2023 dataset](https://big-ann-benchmarks.com/neurips23.html). All tests were done on an 8 CPU machine on Azure.

Latency (y-axis) has dropped significantly for queries. You can see the before/after here:

![dropping latency](https://qdrant.tech/articles_data/qdrant-1.8.x/benchmark.png)**Figure 1:** Dropping latency in sparse vector search queries across versions 1.7-1.8.

The colors within both scatter plots show the frequency of results. The red dots show that the highest concentration is around 2200ms (before) and 135ms (after). This tells us that latency for sparse vector queries dropped by about a factor of 16. Therefore, the time it takes to retrieve an answer with Qdrant is that much shorter.

This performance increase can have a dramatic effect on hybrid search implementations. [Read more about how to set this up.](https://qdrant.tech/articles/sparse-vectors/)

FYI, sparse vectors were released in [Qdrant v.1.7.0](https://qdrant.tech/articles/qdrant-1.7.x/#sparse-vectors). They are stored using a different index, so first [check out the documentation](https://qdrant.tech/documentation/concepts/indexing/#sparse-vector-index) if you want to try an implementation.

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#cpu-resource-management) CPU resource management

Indexing is Qdrant’s most resource-intensive process. Now you can account for this by allocating compute use specifically to indexing. You can assign a number CPU resources towards indexing and leave the rest for search. As a result, indexes will build faster, and search quality will remain unaffected.

This isn’t mandatory, as Qdrant is by default tuned to strike the right balance between indexing and search. However, if you wish to define specific CPU usage, you will need to do so from `config.yaml`.

This version introduces a `optimizer_cpu_budget` parameter to control the maximum number of CPUs used for indexing.

> Read more about `config.yaml` in the [configuration file](https://qdrant.tech/documentation/guides/configuration/).

```yaml