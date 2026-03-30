# Known limitations
Source: https://www.meilisearch.com/docs/learn/resources/known_limitations

Meilisearch has a number of known limitations. These are hard limits you cannot change and should take into account when designing your application.

Meilisearch has a number of known limitations. Some of these limitations are the result of intentional design trade-offs, while others can be attributed to [LMDB](/learn/engine/storage), the key-value store that Meilisearch uses under the hood.

This article covers hard limits that cannot be altered. Meilisearch also has some default limits that *can* be changed, such as a [default payload limit of 100MB](/learn/self_hosted/configure_meilisearch_at_launch#payload-limit-size) and a [default search limit of 20 hits](/reference/api/search#limit).

## Maximum Meilisearch Cloud upload size

**Limitation:** The maximum file upload size when using the Meilisearch Cloud interface is 20mb.

**Explanation:** Handling large files may result in degraded user experience and performance issues. To add datasets larger than 20mb to a Meilisearch Cloud project, use the [add documents endpoint](/reference/api/documents#add-or-replace-documents) or [`meilisearch-importer`](https://github.com/meilisearch/meilisearch-importer).

## Maximum number of query words

**Limitation:** The maximum number of terms taken into account for each [search query](/reference/api/search#query-q) is 10. If a search query includes more than 10 words, all words after the 10th will be ignored.

**Explanation:** Queries with many search terms can lead to long response times. This goes against our goal of providing a fast search-as-you-type experience.

## Maximum number of words per attribute

**Limitation:** Meilisearch can index a maximum of 65535 positions per attribute. Any words exceeding the 65535 position limit will be silently ignored.

**Explanation:** This limit is enforced for relevancy reasons. The more words there are in a given attribute, the less relevant the search queries will be.

### Example

Suppose you have three similar queries: `Hello World`, `Hello, World`, and `Hello - World`. Due to how our tokenizer works, each one of them will be processed differently and take up a different number of "positions" in our internal database.

If your query is `Hello World`:

* `Hello` takes the position `0` of the attribute
* `World` takes the position `1` of the attribute

If your query is `Hello, World`:

* `Hello` takes the position `0` of the attribute
* `,` takes the position `8` of the attribute
* `World` takes the position `9` of the attribute

<Note>
  `,` takes 8 positions as it is a hard separator. You can read more about word separators in our [article about data types](/learn/engine/datatypes#string).
</Note>

If your query is `Hello - World`:

* `Hello` takes the position `0` of the attribute
* `-` takes the position `1` of the attribute
* `World` takes the position `2` of the attribute

<Note>
  `-` takes 1 position as it is a soft separator. You can read more about word separators in our [article about data types](/learn/engine/datatypes#string).
</Note>

## Maximum number of attributes per document

**Limitation:** Meilisearch can index a maximum of **65,536 attributes per document**. If a document contains more than 65,536 attributes, an error will be thrown.

**Explanation:** This limit is enforced for performance and storage reasons. Overly large internal data structures—resulting from documents with too many fields—lead to overly large databases on disk, and slower search performance.

## Maximum number of documents in an index

**Limitation:** An index can contain no more than 4,294,967,296 documents.

**Explanation:** This is the largest possible value for a 32-bit unsigned integer. Since Meilisearch's engine uses unsigned integers to identify documents internally, this is the maximum number of documents that can be stored in an index.

## Maximum number of concurrent search requests

**Limitation:** Meilisearch handles a maximum of 1000 concurrent search requests.

**Explanation:** This limit exists to prevent Meilisearch from queueing an unlimited number of requests and potentially consuming an unbounded amount of memory. If Meilisearch receives a new request when the queue is already full, it drops a random search request and returns a 503 `too_many_search_requests` error with a `Retry-After` header set to 10 seconds. Configure this limit with [`--experimental-search-queue-size`](/learn/self_hosted/configure_meilisearch_at_launch).

## Length of primary key values

**Limitation:** Primary key values are limited to 511 bytes.

**Explanation:** Meilisearch stores primary key values as LMDB keys, a data type whose size is limited to 511 bytes. If a primary key value exceeds 511 bytes, the task containing these documents will fail.

## Length of individual `filterableAttributes` values

**Limitation:** Individual `filterableAttributes` values are limited to 468 bytes.

**Explanation:** Meilisearch stores `filterableAttributes` values as keys in LMDB, a data type whose size is limited to 511 bytes, to which Meilisearch adds a margin of 44 bytes. Note that this only applies to individual values—for example, a `genres` attribute can contain any number of values such as `horror`, `comedy`, or `cyberpunk` as long as each one of them is smaller than 468 bytes.

## Maximum filter depth

**Limitation:** searches using the [`filter` search parameter](/reference/api/search#filter) may have a maximum filtering depth of 2000.

**Explanation:** mixing and alternating `AND` and `OR` operators filters creates nested logic structures. Excessive nesting can lead to stack overflow.

### Example

The following filter is composed of a number of filter expressions. Since these statements are all chained with `OR` operators, there is no nesting:

```sql theme={null}
genre = "romance" OR genre = "horror" OR genre = "adventure"
```

Replacing `OR` with `AND` does not change the filter structure. The following filter's nesting level remains 1:

```sql theme={null}
genre = "romance" AND genre = "horror" AND genre = "adventure"
```

Nesting only occurs when alternating `AND` and `OR` operators. The following example fetches documents that either belong only to `user` `1`, or belong to users `2` and `3`:

```sql theme={null}