# Source: https://docs.vespa.ai/en/writing/reads-and-writes.html.md

# Reads and writes

 

This guide covers the aspects of accessing [documents](../schemas/documents.html) in Vespa. Documents are stored in _content_ clusters. Writes (PUT, UPDATE, DELETE) and reads (GET) pass through a _container_ cluster. Find a more detailed flow at the end of this article.

 ![Vespa Overview](/assets/img/vespa-overview.svg)

Highlights:

- Vespa's indexing structures are built for high-rate field updates. Refer to the [feed sizing guide](../performance/sizing-feeding.html) for write performance, in particular [partial updates](partial-updates.html) for partial updates.
- Vespa supports [parent/child](../schemas/parent-child.html) for de-normalized data. This can be used to simplify the code to update application data, as one write will update all children documents.
- Applications can add custom feed [document processors](../applications/document-processors.html) and multiple container clusters - see [indexing](indexing.html) for details.
- Writes in Vespa are _consistent_ in a stable cluster, but Vespa will prioritize availability over consistency when there is a conflict. See the [elasticity](../content/elasticity.html#consistency) documentation and the [Vespa consistency model](../content/consistency). It is recommended to use the same client instance for updating a given document when possible - for data consistency, but also [performance](../performance/sizing-feeding.html#concurrent-mutations) (see _concurrent mutations_). Read more on write operation [ordering](../content/content-nodes.html#ordering). For performance, group field updates to the same document into [one update operation](../performance/sizing-feeding.html#client-roundtrips).
- Applications can [auto-expire documents](../schemas/documents.html#document-expiry). This feature also blocks PUTs to documents that are already expired - see [indexing](document-routing.html#document-selection) and [document selection](../reference/applications/services/content.html#documents). This is a common problem when feeding test data with timestamps, and the writes a silently dropped.

Also see [troubleshooting](../operations/self-managed/admin-procedures.html#troubleshooting).

## Operations

| Operation | Description |
| --- | --- |
| Get | 

Get a document by ID.

 |
| Put | 

Write a document by ID - a document is overwritten if a document with the same document ID exists.

Puts can have [conditions](document-v1-api-guide.html#conditional-writes) for test-and-set use cases. Conditions can be combined with [create if nonexistent](document-v1-api-guide.html#create-if-nonexistent), which causes the condition to be ignored if the document does not already exist.

 |
| Remove | 

Remove a document by ID. If the document to be removed is not found, it is not considered a failure. Read more about [data-retention](../operations/self-managed/admin-procedures.html#data-retention-vs-size). Also see [batch deletes](batch-delete.html).

Removes can have [conditions](document-v1-api-guide.html#conditional-writes) for test-and-set use cases.

A removed document is written as a tombstone, and later garbage collected - see [removed-db / prune / age](../reference/applications/services/content.html#removed-db-prune-age). Vespa does not retain, nor return, the document data of removed documents.

 |
| Update | 

Also referred to as [partial updates](partial-updates.html), as it updates one or more fields of a document by ID - the [document v1 API](document-v1-api-guide.html#put) can be used to perform [updates in the JSON Document format](../reference/schemas/document-json-format.html#update). If the document to update is not found, it is not considered a failure.

Updates support [create if nonexistent](document-v1-api-guide.html#create-if-nonexistent) (upsert).

Updates can have [conditions](document-v1-api-guide.html#conditional-writes) for test-and-set use cases.

All data structures ([attribute](../content/attributes.html), [index](../content/proton.html#index) and [summary](../querying/document-summaries.html)) are updatable. Note that only _assign_ and _remove_ are idempotent - message re-sending can apply updates more than once. Use _conditional writes_ for stronger consistency.

| **All field types** | 
- [assign](../reference/schemas/document-json-format.html#assign) (may also be used to clear fields)

 |
| **Numeric field types** | 
- [increment](../reference/schemas/document-json-format.html#arithmetic). Also see [auto-generate weightedset keys](../reference/schemas/schemas.html#weightedset)
- [decrement](../reference/schemas/document-json-format.html#arithmetic)
- [multiply](../reference/schemas/document-json-format.html#arithmetic)
- [divide](../reference/schemas/document-json-format.html#arithmetic)

 |
| **Composite types** | 
- [add](../reference/schemas/document-json-format.html#add) For _array_ and _weighted set_. To put into a _map_, see the [assign](../reference/schemas/document-json-format.html#assign) section
- [remove](../reference/schemas/document-json-format.html#composite-remove)
- [match](../reference/schemas/document-json-format.html#match) Pick element from collection, then apply given operation to matched element
- [accessing elements within a composite field using fieldpaths](../reference/schemas/document-json-format.html#fieldpath)

 |
| **Tensor types** | 
- [modify](../reference/schemas/document-json-format.html#tensor-modify) Modify individual cells in a tensor - can replace, add or multiply cell values
- [add](../reference/schemas/document-json-format.html#tensor-add) Add cells to mapped or mixed tensors
- [remove](../reference/schemas/document-json-format.html#tensor-remove) Remove cells from mapped or mixed tensors

 |

 |

## API and utilities

Also see the [JSON Document format](../reference/schemas/document-json-format.html):

| API / util | Description |
| --- | --- |
| [Vespa CLI](../clients/vespa-cli.html) | Command-line tool to `get`, `put`, `remove`, `update`, `feed`, `visit`. |
| [/document/v1/](../reference/api/document-v1.html) | API for `get`, `put`, `remove`, `update`, `visit`. |
| [Java Document API](document-api-guide.html) | Provides direct read-and write access to Vespa documents using Vespa's internal communication layer. Use this when accessing documents from Java components in Vespa such as [searchers](../applications/searchers.html) and [document processors](../applications/document-processors.html). See the [Document](https://github.com/vespa-engine/vespa/blob/master/document/src/main/java/com/yahoo/document/Document.java) class. |
| [pyvespa](https://vespa-engine.github.io/pyvespa/reads-writes.html) | Python client library for reading and writing documents to Vespa. Provides convenient methods for feeding, querying, and visiting documents. Expect less performance than Vespa CLI and vespa-feed-client for heavy batch feed operations. |

Advanced / debugging tools:

- [vespa-feed-client](../clients/vespa-feed-client.html): Java library and command line client for feeding document operations using [/document/v1/](../reference/api/document-v1.html). 
- [vespa-feeder](../reference/operations/self-managed/tools.html#vespa-feeder) is a utility for feeding over the [Message Bus](document-routing.html). 
- [vespa-get](../reference/operations/self-managed/tools.html#vespa-get) gets single documents over the [Message Bus](document-routing.html). 
- [vespa-visit](../reference/operations/self-managed/tools.html#vespa-visit) gets multiple documents over the [Message Bus](document-routing.html). 

## Feed flow

Use the [Vespa CLI](../clients/vespa-cli.html), [vespa-feed-client](../clients/vespa-feed-client.html), [pyvespa python client](https://vespa-engine.github.io/pyvespa/reads-writes.html) or [/document/v1/ API](../reference/api/document-v1.html) to read and write documents:

 ![Feed with feed client](/assets/img/elastic-feed-container.svg)

Alternatively, use [vespa-feeder](../reference/operations/self-managed/tools.html#vespa-feeder) to feed files or the [Java Document API](document-api-guide.html).

 ![Feed with vespafeeder](/assets/img/elastic-feed-vespafeeder.svg)

[Indexing](document-routing.html#routing-for-indexing) and/or [document processing](../applications/document-processors.html) is a chain of processors that manipulate documents before they are stored. Document processors can be user defined. When using indexed search, the final step in the chain prepares documents for indexing.

The [Document API](document-api-guide.html) forwards requests to distributors on content nodes. For more information, read about [content nodes](../content/content-nodes.html) and the [search core](../content/proton.html).

## Further reading

- [Visiting](visiting.html)
- [/document/v1/ API guide](document-v1-api-guide.html)
- [/document/v1/ API reference](../reference/api/document-v1.html)

 Copyright © 2025 - [Cookie Preferences](#)

