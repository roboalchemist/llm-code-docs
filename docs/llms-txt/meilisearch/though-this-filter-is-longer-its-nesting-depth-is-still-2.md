# Though this filter is longer, its nesting depth is still 2
user = 1 OR (user = 2 AND user = 3) OR (user = 4 AND user = 5) OR user = 6
```

## Size of integer fields

**Limitation:** Meilisearch can only exactly represent integers between -2⁵³ and 2⁵³.

**Explanation:** Meilisearch stores numeric values as double-precision floating-point numbers. This allows for greater precision and increases the range of magnitudes that Meilisearch can represent, but leads to inaccuracies in [values beyond certain thresholds](https://en.wikipedia.org/wiki/Double-precision_floating-point_format#Precision_limitations_on_integer_values).

## Maximum number of results per search

**Limitation:** By default, Meilisearch returns up to 1000 documents per search.

**Explanation:** Meilisearch limits the maximum amount of returned search results to protect your database from malicious scraping. You may change this by using the `maxTotalHits` property of the [pagination index settings](/reference/api/settings#pagination-object). `maxTotalHits` only applies to the [search route](/reference/api/search) and has no effect on the [get documents with POST](/reference/api/documents#get-documents-with-post) and [get documents with GET](/reference/api/documents#get-documents-with-get) endpoints.

## Large datasets and internal errors

**Limitation:** Meilisearch might throw an internal error when indexing large batches of documents.

**Explanation:** Indexing a large batch of documents, such as a JSON file over 3.5GB in size, can result in Meilisearch opening too many file descriptors. Depending on your machine, this might reach your system's default resource usage limits and trigger an internal error. Use [`ulimit`](https://www.ibm.com/docs/en/aix/7.1?topic=u-ulimit-command) or a similar tool to increase resource consumption limits before running Meilisearch. For example, call `ulimit -Sn 3000` in a UNIX environment to raise the number of allowed open file descriptors to 3000.

## Maximum database size

**Limitation:** Meilisearch supports a maximum index size of around 80TiB on Linux environments. For performance reasons, Meilisearch recommends keeping indexes under 2TiB.

**Explanation:** Meilisearch can accommodate indexes of any size as long the combined size of active databases is below the maximum virtual address space the OS devotes to a single process. On 64-bit Linux, this limit is approximately 80TiB.

## Maximum task database size

**Limitation:** Meilisearch supports a maximum task database size of 10GiB.

**Explanation:** Depending on your setup, 10GiB should correspond to 5M to 15M tasks. Once the task database contains over 1M entries (roughly 1GiB on average), Meilisearch tries to automatically delete finished tasks while continuing to enqueue new tasks as usual. This ensures the task database does not use an excessive amount of resources. If your database reaches the 10GiB limit, Meilisearch will log a warning indicating the engine is not working properly and refuse to enqueue new tasks.

## Maximum number of indexes in an instance

**Limitation:** Meilisearch can accommodate an arbitrary number of indexes as long as their size does not exceed 2TiB. When dealing with larger indexes, Meilisearch can accommodate up to 20 indexes as long as their combined size does not exceed the OS's virtual address space limit.

**Explanation:** While Meilisearch supports an arbitrary number of indexes under 2TiB, accessing hundreds of different databases in short periods of time might lead to decreased performance and should be avoided when possible.

## Facet Search limitation

**Limitation:** When [searching for facet values](/reference/api/facet_search), Meilisearch returns a maximum of 100 facets.

**Explanation:** the limit to the maximum number of returned facets has been implemented to offer a good balance between usability and comprehensive results. Facet search allows users to filter a large list of facets so they may quickly find categories relevant to their query. This is different from searching through an index of documents. Faceting index settings such as the `maxValuesPerFacet` limit do not impact facet search and only affect queries searching through documents.