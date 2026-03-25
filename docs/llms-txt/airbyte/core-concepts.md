# Source: https://docs.airbyte.com/platform/using-airbyte/core-concepts.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/core-concepts.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/core-concepts.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/core-concepts.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/core-concepts.md

# Core Concepts

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte enables you to build data pipelines and replicate data from a source to a destination. You can configure how frequently the data is synced, what data is replicated, and how the data is written to in the destination.

This page describes the concepts you need to know to use Airbyte.

## Source[​](#source "Direct link to Source")

A source is an API, file, database, or data warehouse that you want to ingest data from. The configured source is what you set up when you provide the variables needed for the connector to access records. The exact fields of the configuration depend on the connector, but in most cases, it provides authentication information (username and password, API key) and information about which data to extract, for example, the start date to sync records from, a search query records have to match.

## Destination[​](#destination "Direct link to Destination")

A destination is a data warehouse, data lake, database, or an analytics tool where you want to load your ingested data.

## Connector[​](#connector "Direct link to Connector")

An Airbyte component which pulls data from a source or pushes data to a destination. A connector can be either a source or a destination. Usually, if you’re building a connection, you’re working with a source. The connector defines what’s required to access an API or a database such as protocol, URL paths to access, the way requests need to be structured, and how to extract records from responses.

## Connection[​](#connection "Direct link to Connection")

A connection is an automated data pipeline that replicates data from a source to a destination. It links a configured source (based on a source connector) to a configured destination (based on a destination connector) to perform syncs. It defines things like the replication frequency (e.g. hourly, daily, manually) and which streams to replicate. Setting up a connection enables configuration of the following parameters:

| Concept                                                                                                                           | Description                                                        |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [Stream and Field Selection](/platform/cloud/managing-airbyte-cloud/configuring-connections.md#modify-streams-in-your-connection) | What data should be replicated from the source to the destination? |
| [Sync Mode](/platform/using-airbyte/core-concepts/sync-modes/.md)                                                                 | How should the streams be replicated (read and written)?           |
| [Sync Schedule](/platform/using-airbyte/core-concepts/sync-schedules.md)                                                          | When should a data sync be triggered?                              |
| [Destination Namespace and Stream Prefix](/platform/using-airbyte/core-concepts/namespaces.md)                                    | Where should the replicated data be written?                       |
| [Schema Propagation](/platform/using-airbyte/schema-change-management.md)                                                         | How should Airbyte handle schema drift in sources?                 |

## Stream[​](#stream "Direct link to Stream")

A stream is a group of related records. Depending on the destination, it may be called a table, file, or blob. We use the term `stream` to generalize the flow of data to various destinations.

Examples of streams:

* A table in a relational database
* A resource or API endpoint for a REST API
* The records from a directory containing many files in a filesystem

## Record[​](#record "Direct link to Record")

A record is a single entry or unit of data. This is commonly known as a "row". A record is usually unique and contains information related to a particular entity, like a customer or transaction.

Examples of records:

* A row in the table in a relational database
* A line in a file
* A unit of data returned from an API

## Field[​](#field "Direct link to Field")

A field is an attribute of a record in a stream.

Examples of fields:

* A column in the table in a relational database
* A field in an API response

## Sync Schedule[​](#sync-schedule "Direct link to Sync Schedule")

There are three options for scheduling a sync to run:

* Scheduled (ie. every 24 hours, every 2 hours)
* [CRON schedule](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)
* Manual (i.e: clicking the "Sync Now" button in the UI or through the API)

For more details, see our [Sync Schedules documentation](/platform/using-airbyte/core-concepts/sync-schedules.md).

## Destination Namespace[​](#destination-namespace "Direct link to Destination Namespace")

A namespace defines where the data will be written to your destination. You can use the namespace to group streams in a source or destination. In a relational database system, this is typically known as a schema.

Depending on your destination, you may know this more commonly as the "Dataset", "Schema" or "Bucket Path". The term "Namespace" is used to generalize the concept across various destinations.

For more details, see our [Namespace documentation](/platform/using-airbyte/core-concepts/namespaces.md).

## Delivery Method[​](#delivery-method "Direct link to Delivery Method")

You can move data from a source to a destination in one of two ways, depending on whether your data is structured or unstructured. When you replicate records, you extract and load structured records, allowing for blocking and hashing individual fields, typing, and deduping. You can also copy raw files without processing them, which is appropriate for unstructured data. Read more about the difference in [Delivery methods](/platform/using-airbyte/delivery-methods.md).

## Sync Mode[​](#sync-mode "Direct link to Sync Mode")

A sync mode governs how Airbyte reads from a source and writes to a destination. Airbyte provides several sync modes depending what you want to accomplish. The sync modes define how your data will sync and whether duplicates will exist in the destination.

Read more about each [sync mode](/platform/using-airbyte/core-concepts/sync-modes/.md) and how they differ.

## Resumability[​](#resumability "Direct link to Resumability")

[Resumability](/platform/understanding-airbyte/resumability.md) is an important principle in Airbyte's approach to reliability. To ensure your syncs run smoothly with minimal maintenance, we checkpoint a sync's progress and automatically re-attempt the sync under the hood.

## Typing and Deduping[​](#typing-and-deduping "Direct link to Typing and Deduping")

Typing and deduping ensures the data emitted from sources is written into the correct type-cast relational columns, and if deduplication is selected, only contains unique records. Typing and deduping is only relevant for relational database & warehouse destinations. For more details, see our [Typing & Deduping documentation](/platform/using-airbyte/core-concepts/typing-deduping.md).

## Custom Transformations[​](#custom-transformations "Direct link to Custom Transformations")

Airbyte Cloud integrates natively with dbt to allow you to use dbt for post-sync transformations. This is useful if you would like to trigger dbt models after a sync successfully completes.

Custom transformation is not available for Airbyte Open-Source.

## Workspace[​](#workspace "Direct link to Workspace")

A workspace is a grouping of sources, destinations, connections, and other configurations. It lets you collaborate with team members and share resources across your team under a shared billing account.

## Organization[​](#organization "Direct link to Organization")

Organizations let you collaborate with team members and share workspaces across your team.

## Glossary of Terms[​](#glossary-of-terms "Direct link to Glossary of Terms")

You can find a extended list of [Airbyte specific terms](https://glossary.airbyte.com/term/airbyte-glossary-of-terms/), [data engineering concepts](https://glossary.airbyte.com/term/data-engineering-concepts) or many [other data related terms](https://glossary.airbyte.com/).
