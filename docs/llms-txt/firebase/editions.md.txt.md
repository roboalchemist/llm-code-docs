# Source: https://firebase.google.com/docs/firestore/editions.md.txt

This page describes Cloud Firestore editions and its key features.
Cloud Firestore is available in the following editions:

- **Firestore Standard edition** provides a broad suite of capabilities as a
  document database including fluent SDKs for a large number of programming
  languages, real-time and offline support, high availability in single and
  multi-region configurations, and a convenient serverless operation model
  with seamless autoscaling. This edition supports Firestore in Native mode using
  Firestore Core operations (basic reads, writes, and queries).

- **Firestore Enterprise edition** provides a broad suite of capabilities and
  controls for developers as a document database. It features an advanced
  query engine supporting exhaustive query capabilities, and all queries on
  Enterprise edition can now be executed, with the presence of
  indexes being optional. As a result, indexing is fully customizable, and
  single field indexes are no longer created automatically. This edition
  supports two modes of operation that you select when creating a database:

  - **Firestore in Native mode (Preview)** with Core and Pipeline operations. The
    Firestore Core operations provide the standard document Create, Read,
    Update, and Delete (CRUD) functionality, along with built-in support for
    real-time listen queries and offline persistence. Firestore Pipeline
    operations provide hundreds of additional query capabilities. Examples
    include support for additional operators for aggregations, string
    matching, and refined filtering capabilities.

  - **Firestore with MongoDB compatibility** with MongoDB compatible operations. This mode
    enables developers to use existing MongoDB application code, drivers,
    tools, and the open-source ecosystem of MongoDB integrations with
    Cloud Firestore.

  All operations in both modes run on a more advanced query engine, maximizing
  developer control by making indexing an optional step for applications
  trying to improve the performance of their queries.

## Editions features

The following table summarizes the features available for each edition:

|---|---|---|
| **Features** | **Standard edition** | **Enterprise edition** |
| Query Engine | Standard - querying support only using Core operations. | Advanced - querying support using [Core](https://firebase.google.com/docs/firestore/enterprise/get-data-core) and [Pipelines](https://firebase.google.com/docs/firestore/pipelines/get-started-with-pipelines) or [MongoDB compatible operations](https://firebase.google.com/docs/firestore/enterprise/supported-data-types-drivers). |
| Supports Cloud Firestore in Native mode server-side, web, and mobile SDKs | Yes. Supported by [Core operations](https://firebase.google.com/docs/firestore/compare-editions-for-native-mode). | Yes. Supported by [Core and Pipeline operations](https://firebase.google.com/docs/firestore/compare-editions-for-native-mode). |
| Supports real-time and offline capabilities | Yes. Supported by [Core operations](https://firebase.google.com/docs/firestore/query-data/listen). | Yes. Supported by [Core operations](https://firebase.google.com/docs/firestore/query-data/listen) only. |
| Supports Firestore with MongoDB compatibility | No | Yes |
| Indexing | Indexes are required for queries. Indexes for individual fields are created automatically, while more complex queries rely on composite indexes or collection group indexes that must be manually configured. For aggregation queries like count(), sum(), and avg(), the cost is determined by the number of index entries read, with a minimum charge of one document read applied if zero index entries are scanned. | Indexes are not required, and therefore optional for queries. You define indexes as-needed. Enterprise edition also supports a broader range of index types, including non-sparse/sparse, and unique indexes. With Query Explain and Query Insights, you are able to identify queries that can benefit from an index, as indexes are no longer required. |
| Query and write performance and costs | With Query Explain, you can optimize queries with range and inequality filters on multiple fields in a single query. There are metrics available in [Query Insights](https://firebase.google.com/docs/firestore/enterprise/query-insights), [Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain), and Cloud Monitoring to provide deep insight into query execution. <br /> <br /> | You're in full control of query and write performance, and can optimize performance using customizable indexing, enhanced monitoring, diagnostic tools, and new execution controls called Query Hints. There are metrics available in [Query Insights](https://firebase.google.com/docs/firestore/enterprise/query-insights), [Query Explain](https://firebase.google.com/docs/firestore/enterprise/query-explain), and Cloud Monitoring to provide deep insight into query execution. |
| Pricing | [Refer to pricing details](https://cloud.google.com/firestore/pricing) | [Refer to pricing details](https://cloud.google.com/firestore/enterprise/pricing) |
| Observability | - Key Visualizer - Query Explain - Query Insights | - Query Explain - Query Insights |
| Data protection | - Scheduled backups - Point-in-time recovery | - Scheduled backups - Point-in-time recovery |
| Encryption | - Google-managed encryption key - Customer-managed encryption keys | - Google-managed encryption key - Customer-managed encryption keys |
| Storage | Hybrid storage (SSD \& HDD) | SSD |
| Committed Use Discounts | 20% for 1 year; 40% for 3 years | 20% for 1 year; 40% for 3 years |

## What you need to do

If you haven't selected an edition for your Cloud Firestore database, it's
automatically classified as a Standard edition with no changes
required on your part. If you want to create a new Firestore Enterprise edition
database, follow the steps outlined in [Native
mode](https://firebase.google.com/docs/firestore/enterprise/create-databases) or [MongoDB compatibility
mode](https://firebase.google.com/docs/firestore/enterprise/create-databases-mongodb).

## Pricing

For information about Cloud Firestore editions pricing, see pricing pages for
[Enterprise edition](https://cloud.google.com/firestore/enterprise/pricing)
and [Standard edition](https://cloud.google.com/firestore/pricing).