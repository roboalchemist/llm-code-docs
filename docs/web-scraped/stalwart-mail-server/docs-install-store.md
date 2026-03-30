# Source: https://stalw.art/docs/install/store

Title: Choosing a database | Stalwart Labs

URL Source: https://stalw.art/docs/install/store

Markdown Content:
Stalwart employs a modular storage architecture that separates different types of data into four distinct stores. This design provides flexibility and allows each storage component to be optimized independently, depending on the scale and needs of the deployment.

*   The [Data Store](https://stalw.art/docs/storage/data) is responsible for storing structured metadata such as email headers, folder hierarchies, calendar, contacts, user settings, and other non-binary information. Essentially, it holds everything except large binary objects.
*   The [Blob Store](https://stalw.art/docs/storage/blob) is where large binary files—such as the actual email content, sieve scripts, and attachments—are stored. 
*   To support efficient search operations, Stalwart also utilizes a [Search Store](https://stalw.art/docs/storage/fts), which maintains indexes to speed up text-based queries across message content. 
*   Finally, the [In-memory Store](https://stalw.art/docs/storage/in-memory) handles ephemeral key-value data used by security, clustering, and anti-spam components, including rate limiting, distributed locks and message interaction tracking.

In simple or single-node setups, it is entirely feasible to consolidate these roles into a single storage backend. For example, databases such as **RocksDB** or **PostgreSQL** can be configured to serve as the data store, blob store, search store, and even in-memory store. It is common to see lightweight deployments where RocksDB is used exclusively for all four functions, simplifying management and reducing infrastructure complexity.

However, for larger deployments—particularly those running in [distributed environments](https://stalw.art/docs/cluster/overview)—it is advisable to assign each storage role to a backend that is specifically designed for that purpose. A more scalable and robust configuration might involve **FoundationDB** as the data store, an **S3-compatible service** for blob storage, **Redis** for handling volatile in-memory data, and a dedicated search engine such as **Elasticsearch** or **Meilisearch** for full-text indexing.

Selecting the right combination of databases will depend on the performance requirements, fault tolerance expectations, and operational constraints of the deployment. Stalwart’s flexible architecture ensures that it can scale from compact single-server setups to complex multi-node clusters with specialized infrastructure for each storage layer.

The following table summarizes the supported backends available for each store type:

|  | Data store | Blob store | Search store | In-memory store |
| --- | --- | --- | --- | --- |
| RocksDB | ✅ | ✅ | ✅ | ✅ |
| FoundationDB | ✅ | ✅ | ✅ | ✅ |
| PostgreSQL | ✅ | ✅ | ✅ | ✅ |
| MySQL / MariaDB | ✅ | ✅ | ✅ | ✅ |
| SQLite | ✅ | ✅ | ✅ | ✅ |
| S3/MinIO |  | ✅ |  |  |
| Azure Blob Storage |  | ✅ |  |  |
| Filesystem |  | ✅ |  |  |
| ElasticSearch |  |  | ✅ |  |
| Meilisearch |  |  | ✅ |  |
| Redis / Valkey |  |  |  | ✅ |

Note

Be aware that changing the database backend at a later time will require migrating your data.
