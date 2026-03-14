# Source: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/core-concepts/sync-modes.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/core-concepts/sync-modes.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/core-concepts/sync-modes.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/core-concepts/sync-modes.md

# Sync Modes

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

A sync mode governs how Airbyte reads from a source and writes to a destination. Airbyte provides different sync modes to account for various use cases. To minimize confusion, a mode's behavior is reflected in its name. The easiest way to understand Airbyte's sync modes is to understand how the modes are named.

1. The first part of the name denotes how the source connector reads data from the source:

   <!-- -->

   1. Incremental: Read records added to the source since the last sync job. (The first sync using Incremental is equivalent to a Full Refresh)

      <!-- -->

      * Method 1: Using a cursor. Generally supported by all connectors whose data source allows extracting records incrementally.
      * Method 2: Using change data capture. Only supported by some sources. See [CDC](/platform/1.6/understanding-airbyte/cdc.md) for more info.

   2. Full Refresh: Read everything in the source.

2. The second part of the sync mode name denotes how the destination connector writes data. This is not affected by how the source connector produced the data:

   <!-- -->

   1. Overwrite: Overwrite by replacing pre-existing data in the destination.
   2. Append: Write by adding data to existing tables in the destination.
   3. Append Deduped: Write by first adding data to existing tables in the destination to keep a history of changes. The final table is produced by de-duplicating the intermediate ones using a primary key.
   4. Overwrite Deduped: Overwrite by replacing pre-existing data in the destination and deduplicate the final data using a primary key.

A sync mode is a combination of a source and destination mode together. The UI exposes the following options, whenever both source and destination connectors are capable to support it for the corresponding stream:

* [Incremental Append](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md): Sync new records from stream and append data in destination.
* [Incremental Append + Deduped](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append-deduped.md): Sync new records from stream and append data in destination, also provides a de-duplicated view mirroring the state of the stream in the source.
* [Full Refresh Append](/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-append.md): Sync the whole stream and append data in destination.
* [Full Refresh Overwrite](/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite.md): Sync the whole stream and replace data in destination by overwriting it.
* [Full Refresh Overwrite + Deduped](/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped.md): Sync the whole stream and replace data in destination by overwriting it, also de-duplicate the data.
