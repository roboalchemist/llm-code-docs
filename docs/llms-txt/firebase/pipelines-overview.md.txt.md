# Source: https://firebase.google.com/docs/firestore/enterprise/pipelines-overview.md.txt

<br />

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

The Firestore in Native mode consists of two sets of operations - Firestore Core operations
and Firestore Pipeline operations.

The Firestore Core operations provide the standard document Create, Read, Update,
and Delete (CRUD) functionality, along with built-in support for real-time
listen queries and offline persistence. A distinct operational difference in
this edition is that indexes are optional and are not automatically created for
single fields. While this allows queries to execute without upfront index
configuration, unindexed queries will default to scanning the entire collection.
This can lead to increased latency and costs as the dataset grows.

The Firestore Pipeline operations is a central feature of the Firestore Enterprise
edition, built on an advanced query engine to significantly expand the range of
possible queries. Pipeline operations employ a flexible query
syntax and a distinct indexing method where indexes are optional and not
automatically created, enabling advanced data retrieval operations for
applications.

## Features of Firestore Core operations

The Core operations allow standard CRUD operations and real-time
listen queries. However, when using these operations on the Enterprise edition,
the underlying behavior regarding indexing and billing changes significantly
compared to the Standard edition.

### Functionality and Continuity

Core operations retain the familiar method-chaining syntax (for
example, `.where()`, `.orderBy()`) used in the Standard edition. These
operations support real-time listen queries and offline persistence for mobile
and web clients. It is recommended to use these operations for standard
transactional workloads, simple lookups, and existing application code
migration.

### Custom Indexing

Unlike the Standard edition, Core operations in the Enterprise
edition does not automatically create single-field indexes. Indexes are optional
and not required to execute a query. If a specific index is missing, the query
performs a full collection scan. While unindexed queries allow for rapid
prototyping, they may perform slower and cost more as the dataset grows.
Developers must manually create indexes to optimize query performance and reduce
the Read Unit consumption.

### Billing Model (Unit-Based)

Read Units are charged in 4KB tranches rather than per document count. An
unindexed query scanning a large collection will consume Read Units based on the
total bytes scanned across all documents. Write Units are charged in 1KB
tranches. Writing a document consumes units for the data plus additional units
for every index entry updated. Unlike in the Standard edition, which enforces
automatic single-field indexing, you can now choose specific fields to index to
optimize write costs and performance.

## Features of Firestore Pipeline operations

The Firestore Enterprise edition with Pipeline operations utilizes an
advanced query engine that removes many existing limitations of the Firestore
Standard edition. Pipeline operations provides hundreds of
additional query features. The Pipeline operations has the
following capabilities:

### Stage-Based Composable Syntax

Pipeline queries are constructed by defining a series of sequential
[stages](https://firebase.google.com/docs/firestore/pipelines/get-started-with-pipelines#stages) that are
executed in order. This allows for complex operations, such as filtering on the
result of an aggregation, which was not previously possible.

The following example shows a pipeline query that finds the number of unique
product IDs viewed in the last month:

    guard let cutoffDate = Calendar.current.date(byAdding: .month, value: -1, to: Date()) else {
      return
    }
    let snapshot = try await db.pipeline()
      .collection("productViews")
      .where(Field("viewedAt").greaterThan(cutoffDate.timeIntervalSince1970))
      .aggregate([Field("productId").countDistinct().as("uniqueProductViews")])
      .execute()

### Expanded Capabilities

The Pipeline query introduces a vast number of new capabilities, including:

- Aggregations: Support for new aggregation functions (like `sum(...)`, `min(...)`, and `count_distinct(...)`) combined with arbitrary grouping fields.
- Complex Filtering: Support for hundreds of additional functions to express arbitrarily complex `where(...)` statements, including `regex_match(...)`, `add(...)` and `str_contains(...)`, all without hard index requirements.
- Partial Reads / Projections: Retrieve dynamic subsets of documents using `select(...)`, `remove_fields(...)`, and many other document manipulation stages.

To learn more about these capabilities, see [Query data with Pipeline
operations](https://firebase.google.com/docs/firestore/pipelines/get-started-with-pipelines).

### Realtime and Offline Support

To utilize Realtime and Offline, developers can use the Firestore Core operations
in the Firestore Enterprise edition.

### Client and Tooling Integration

The Enterprise edition includes specialized features to interact
with and manage Pipeline queries:

- **Query explaining and profiling:** You can use Query Explain results to understand how many read or write units a query consumes and analyze its execution.
- **Query insights:**The Enterprise edition supports Query Insights which helps you determine where indexes could be created to improve performance and cost by providing visibility into top queries that are run on your database and their performance characteristics
- **New index types:**You can create specialized indexes for Enterprise edition, including index types like sparse, non-sparse, and unique indexes. It also supports creating and editing vector search indexes for Enterprise databases.

<br />

## Differences between Firestore Standard and Firestore Enterprise

The major operational difference between the Core and Pipeline operations lies
in the management of indexing, which directly affects performance and cost.

|---|---|---|
|   | **Standard edition - Core operations** | **Enterprise edition - Core and Pipeline operations** |
| **Indexing requirement** | Indexes are required for queries. Indexes for individual fields are created automatically, while more complex queries rely on composite indexes or collection group indexes that must be manually configured. | Indexes are not required, and therefore optional for queries. You define indexes as-needed. Enterprise edition also supports a broader range of index types, including non-sparse/sparse, and unique indexes. |
| **Performance** | **Indexed queries:** Performance and cost scales with the size of your result set. | **Unindexed queries:** Performance and cost scales with the size of your dataset. **Indexed queries:** Performance and cost scales with the size of your result set. We recommend using the Query Explain and Query Insights tools to create indexes and improve the performance and cost of your queries. |
| **Storage Cost Implication** | You incur storage overhead from automatic indexes, and composite indexes. | You save on storage costs because indexes are not automatically created for every field. |
| **Cost Basis** | Charged per document **read** , **write** , and **delete** operation. | Charged per **Read Unit** (4KB tranches) and **Write Unit** (1KB tranches). Writing index entries consume Write Units. Learn about the new pricing with some [examples](https://firebase.google.com/docs/firestore/pipelines/pricing-examples). |
| **Security Rules** | [Security Rules](https://firebase.google.com/docs/firestore/security/overview) protect collections by verifying read/write permissions. | [Security Rules](https://firebase.google.com/docs/firestore/enterprise/security/overview) protect collections by verifying read/write permissions. Learn how to model your data to support Pipeline queries in the [Data Model](https://firebase.google.com/docs/firestore/data-model) guide. |