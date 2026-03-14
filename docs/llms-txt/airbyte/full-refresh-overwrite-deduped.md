# Source: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped.md

# Full Refresh - Overwrite + Deduped

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

## Overview[​](#overview "Direct link to Overview")

The **Full Refresh** modes are the simplest methods that Airbyte uses to sync data, as they always retrieve all available information requested from the source, regardless of whether it has been synced before. This contrasts with [**Incremental sync**](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md), which does not sync data that has already been synced before.

In the **Overwrite + Deduped** variant, new syncs will replace all data in the existing destination table and then pull the new data in. Therefore, data that has been removed from the source after an old sync will be deleted in the destination table. The **deduped** variant also means that the data in the final table will be unique per primary key (unlike [Full Refresh Overwrite](/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite.md)). This is determined by sorting the data using the cursor field and keeping only the latest de-duplicated data row.

Full Refresh syncs may be [resumed](/platform/understanding-airbyte/resumability.md) (to recover from transient errors for example), when this happens, duplicate may happen. If avoiding duplicate is a strong requirement, we recommend using **Overwrite + Deduped** over **Overwrite**. Bear in mind that deduplication incurs additional warehouse costs.

## Example Behavior[​](#example-behavior "Direct link to Example Behavior")

On the nth sync of a full refresh connection:

## *Replace* existing data with new data. The connection does not create any new tables.[​](#replace-existing-data-with-new-data-the-connection-does-not-create-any-new-tables "Direct link to replace-existing-data-with-new-data-the-connection-does-not-create-any-new-tables")

data in the destination *before* the sync:

| Languages |
| --------- |
| Python    |
| Java      |
| Bash      |

new data in the source:

| Languages |
| --------- |
| Python    |
| Java      |
| Ruby      |

data in the destination *after* the sync (note how the old value of "bash" is no longer present):

| Languages |
| --------- |
| Python    |
| Java      |
| Ruby      |

## Destination-specific mechanism for full refresh[​](#destination-specific-mechanism-for-full-refresh "Direct link to Destination-specific mechanism for full refresh")

The mechanism by which a destination connector accomplishes the full refresh will vary wildly from destination to destination. For our certified database and data warehouse destinations, we will be recreating the final table each sync. This allows us leave the previous sync's data viewable by writing to a "final-table-tmp" location as the sync is running, and at the end dropping the old "final" table, and renaming the new one into place. That said, this may not possible for all destinations, and we may need to erase the existing data at the start of each full-refresh sync.

## Related information[​](#related-information "Direct link to Related information")

* [An overview of Airbyte’s replication modes](https://airbyte.com/blog/understanding-data-replication-modes).
* [Explore Airbyte's full refresh data synchronization](https://airbyte.com/tutorials/full-data-synchronization).
