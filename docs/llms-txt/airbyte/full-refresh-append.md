# Source: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-append.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/core-concepts/sync-modes/full-refresh-append.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/core-concepts/sync-modes/full-refresh-append.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/core-concepts/sync-modes/full-refresh-append.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-append.md

# Full Refresh - Append

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

## Overview[​](#overview "Direct link to Overview")

The **Full Refresh** modes are the simplest methods that Airbyte uses to sync data, as they always retrieve all available data requested from the source, regardless of whether it has been synced before. This contrasts with [**Incremental sync**](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md), which does not sync data that has already been synced before.

In the **Append** variant, new syncs will take all data from the sync and append it to the destination table. Therefore, if syncing similar information multiple times, every sync will create duplicates of already existing data.

## Example Behavior[​](#example-behavior "Direct link to Example Behavior")

On the nth sync of a full refresh connection:

## Add new data to the same table. Do not touch existing data.[​](#add-new-data-to-the-same-table-do-not-touch-existing-data "Direct link to Add new data to the same table. Do not touch existing data.")

data in the destination *before* the nth sync:

| Languages |
| --------- |
| Python    |
| Java      |

new data:

| Languages |
| --------- |
| Python    |
| Java      |
| Ruby      |

data in the destination *after* the nth sync:

| Languages |
| --------- |
| Python    |
| Java      |
| Python    |
| Java      |
| Ruby      |

This could be useful when we are interested to know about deletion of data in the source. This is possible if we also consider the date, or the batch id from which the data was written to the destination:

new data at the n+1th sync:

| Languages |
| --------- |
| Python    |
| Ruby      |

data in the destination *after* the n+1th sync:

| Languages | batch id |
| --------- | -------- |
| Python    | 1        |
| Java      | 1        |
| Python    | 2        |
| Java      | 2        |
| Ruby      | 2        |
| Python    | 3        |
| Ruby      | 3        |

## In the future[​](#in-the-future "Direct link to In the future")

We will consider making a better detection of deletions in the source, especially with `Incremental`, and `Change Data Capture` based sync modes for example.

## Related information[​](#related-information "Direct link to Related information")

* [An overview of Airbyte’s replication modes](https://airbyte.com/blog/understanding-data-replication-modes).
* [Explore Airbyte's full refresh data synchronization](https://airbyte.com/tutorials/full-data-synchronization)
