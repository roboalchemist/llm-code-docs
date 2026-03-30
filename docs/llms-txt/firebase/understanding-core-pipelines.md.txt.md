# Source: https://firebase.google.com/docs/firestore/pipelines/understanding-core-pipelines.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

This page explains the different interfaces available for accessing data in a
Native mode database.

## Operation interfaces

Native mode supports two interfaces for accessing data:

### Pipeline operations

The newer query interface for Cloud Firestore.
Pipeline operations support a stage-based composable syntax. You construct
an operation by defining a series of sequential stages that are executed in
order. This allows for complex operations, such as filtering on the result of an
aggregation, which was not previously possible in the original interface (Core operations).

Pipeline operations are available only in Firestore Enterprise edition and are in the
[Preview](https://cloud.google.com/products#product-launch-stages) launch stage.

### Core operations

Core operations are the original interface for Cloud Firestore.
Core operations uses a method-chaining syntax (`.where()`, `.orderBy()`, `.get()`)
on document or collection references to retrieve documents.
The ordering of query stages is implied and aggregation support is limited.

Core operations are available in both Enterprise and Standard editions, but
index defaults are very different between editions. See the next section for
details.

## Interface differences between editions

With the introduction of Native mode support in the
Enterprise edition, both Firestore Core and Pipeline operations are available.
When using Core operations in Enterprise edition,
the new index behaviour and pricing model removes many of the restrictions of
Standard edition.

|---|---|---|
| **Feature** | **Standard edition** | **Enterprise edition** |
| **Supported querying operations** | Limited to Firestore Core operations. | Supports Firestore Core and Pipeline operations, and Firestore MongoDB compatibility operations. |
| **Indexing Requirement** | All queries require indexes. | Indexes are not required for queries. |
| **Index creation** | **Automatic indexes** are created for single fields. You can manually create composite indexes. | **No automatic indexes** are created. Indexes need to be manually managed. |
| **Query Performance \& Cost** | Queries are generally **performant** due to index requirements. | Optimize query performance and costs by creating indexes. You can identify missing indexes using Query Explain and Query Insights. Queries without indexes may risk being **non-performant and costly** as the dataset grows, requiring monitoring and tuning. |
| **Indexing Overhead Cost** | No charge for index writes, as indexes are automatic. | Writing index entries **consume write units** when an associated document is written (1 write unit per 1 KiB of index entry size). You save on storage costs by not creating index entries for every field. |
| **Billing Model (Reads/Writes/Deletes)** | Charged per **document read, write, and delete**. | Charged per **read and write** (tranche). Reads are charged in **Read Units** (4 KiB tranches). Writes and deletes are merged into **Write Units** (1 KiB tranches). |
| **Base Pricing (per million) Prices shown are for the *us-central1* region** | Reads: **$0.03 per 100,000 documents** (or $0.30 per million). Writes: **$0.09 per 100,000 documents** (or $0.90 per million). Deletes: **$0.01 per 100,000 documents** (or $0.10 per million) | Read Units: **$0.05 per 1 million** read units. Write Units: **$0.26 per 1 million** write units. Prices are generally **lower if documents are under 4KiB** compared to the Standard Read cost. |
| **Real-time Updates** Prices shown are for the *us-central1* region | Realtime updates are **included billed as Reads at $0.03 per 100,000 documents**. | Realtime updates have a **new separate SKU** (Realtime Update Units), charged per 4 KiB tranche. Realtime updates cost **$0.30 per million read units**. |

## Next steps

- [Learn how to construct Pipeline operations](https://firebase.google.com/docs/firestore/pipelines/get-started-with-pipelines)
- [Get data with Core operations](https://firebase.google.com/docs/firestore/enterprise/get-data-core)