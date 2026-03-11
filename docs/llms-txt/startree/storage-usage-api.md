# Source: https://docs.startree.ai/corecapabilities/manage-data/recipes/storage-usage-api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Storage Usage API

> Local, Deep Store, and Remote storage breakdown for Pinot tables

## Overview

Unexpected growth in table storage can increase infrastructure and object storage costs. Pinot stores table data across multiple locations, such as server disk, deep store, and remote object stores used by tiered storage. The Table Storage Usage API reports table size with a breakdown by storage location and highlights mismatches between the expected size and the actual size.

This makes it easier to:

* Track total storage footprint across disk, deep store, and remote tier storage
* Detect orphaned segments and stale versions
* Identify deep store deleted segments that are still consuming storage
* Debug discrepancies during rebalances, segment replacement, and tiered storage cleanup

<Callout type="info">
  The APIs mentioned here are available starting StarTree Cloud version 0.12.0
</Callout>

## Key concepts

### Expected size vs Actual size

Pinot reports storage in two ways.

#### Expected size

* Segments that are ONLINE for the table based on Pinot metadata
* Segments found under the deleted segments area in the deep store that are still within the configured retention window

Expected size represents what should exist and is the preferred baseline for monitoring normal growth.

#### Actual size

* Everything included in the expected size
* Unknown segments found in table directories across server disk, deep store, or remote object storage
* Stale versions of remote segments, where older versions exist alongside the latest

## Storage components

Sizes are reported by storage location and component.

### Server disk

* **Local segment directory**: segment index directories stored in the table’s local data directory
* **Remote segment preload index**: local copies of remote tier segments staged for serving
* **Remote segment metadata cache**: local cached metadata for remote tier segments

### Deep store

* **Segment compressed data**: segment tar.gz objects stored in deep store
* **Deleted segments**: segments moved to the deleted directory, including:
  * within retention
  * beyond retention, which is unexpected when cleanup is not running

### Remote object store

* **Remote segment directory (latest)**: the latest version of remote tier segments
* **Remote segment directory (stale versions)**: older versions still present

## API endpoints

### Controller API

The controller endpoint provides a consolidated storage usage view for a table across server instances, deep store, and the remote object store.

`GET /tables/{tableName}/storageUsage?verbose={true|false}`

* `verbose=false` returns a summary suitable for dashboards and alerting
* `verbose=true` returns a detailed breakdown intended for investigating discrepancies

#### Summary response (`verbose=false`)

<Accordion title="Example response">
  ```json  theme={null}
  {
    "tableName": "table_OFFLINE",
    "serverInstances": {
      "server_1": {
        "actualSegments": 4,
        "expectedSegments": 4,
        "totalStaleVersions": 1,
        "actualSizeInBytes": 3072,
        "expectedSizeInBytes": 2560
      }
    },
    "deepStore": {
      "actualSegments": 7,
      "expectedSegments": 6,
      "actualSizeInBytes": 700,
      "expectedSizeInBytes": 600
    },
    "remoteS3": {
      "actualSegments": 2,
      "expectedSegments": 2,
      "totalStaleVersions": 1,
      "actualSizeInBytes": 3072,
      "expectedSizeInBytes": 2048
    }
  }
  ```
</Accordion>

#### Summary response (`verbose=true`)

Verbose adds a breakdown per storage area and lists “unexpected” contributors such as unknown segments and stale versions.

<Accordion title="Example response">
  ```json  theme={null}
  {
    "tableName": "fake_table_SRT_Compaction_REALTIME",
    "serverInstances": {
      "Server_pinot-server-server-0-1": {
        "unexpectedSizeInBytes": 253932,
        "actualSizeInBytes": 1119418454,
        "actualItemsCount": 1305,
        "totalStaleVersions": 0,
        "unexpectedItemsCount": 38,
        "breakdown": {
          "localSegmentsDirectory": {
            "unexpectedSizeInBytes": 253932,
            "actualSizeInBytes": 1119418454,
            "actualItemsCount": 1305,
            "unexpected": {
              "unknownItems": {
                "items": [
                  "fake_table_SRT_Compaction__0__14199__20251222T2339Z.tar.compressed",
                  "..."
                ],
                "sizeInBytes": 253932,
                "count": 38
              }
            }
          }
        }
      }
    },
    "deepStore": {
      "unexpectedSizeInBytes": 14193,
      "actualSizeInBytes": 21805648,
      "actualItemsCount": 2890,
      "unexpectedItemsCount": 3,
      "breakdown": {
        "onlineSegments": {
          "unexpectedSizeInBytes": 14193,
          "actualSizeInBytes": 19301473,
          "unexpectedItemsCount": 2,
          "unexpected": {
            "unknownItems": {
              "items": [
                "fake_table_SRT_Compaction__1__162105__20260107T1819Z.tmp",
                "fake_table_SRT_Compaction__0__144799__20260107T1819Z.tmp"
              ],
              "sizeInBytes": 14193,
              "count": 2
            }
          }
        },
        "deletedSegments": {
          "unexpectedSizeInBytes": 1201,
          "actualSizeInBytes": 1201,
          "actualItemsCount": 1,
          "unexpectedItemsCount": 1,
          "unexpected": {
            "beyondRetentionSegments": {
              "items": [
                "fake_table_SRT_Compaction__1__10702__20251222T1506Z"
              ],
              "sizeInBytes": 1201,
              "count": 1
            }
          }
        }
      }
    },
   "remoteS3": {
      "s3Tier": {
        "unexpectedItemsCount": 0,
        "unexpectedSizeInBytes": 1006228697,
        "actualItemsCount": 5,
        "totalStaleVersions": 3,
        "actualSizeInBytes": 1331507185,
        "breakdown": {
          "segmentDirectory": {
            "unexpectedItemsCount": 0,
            "unexpectedSizeInBytes": 1006228697,
            "actualItemsCount": 5,
            "totalStaleVersions": 3,
            "actualSizeInBytes": 1331507185,
            "unexpected": {
              "staleVersions": {
                "sizeInBytes": 1006228697,
                "items": [
                  "3769746207_-1890732847",
                  "3811220169_-1890732847",
                  "3118351592_-1890732847"
                ],
                "count": 3
              }
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

### Response Schema

The response is hierarchical. To maintain clarity, the data structure is defined in three parts below:

1. [Root Response](#1-root-response-fields)
2. [The StorageStats Object](#2-the-storagestats-object) (Reused recursively)
3. [Breakdown Contexts](#3-breakdown-definitions) (Specifics for Servers vs. Deep Store)

### 1. Root Response Fields

| Field                 | Type     | Description                                                                                                                                                         |
| :-------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`tableName`**       | `string` | The name of the table being analyzed.                                                                                                                               |
| **`serverInstances`** | `map`    | A map of Server Instance IDs (e.g., `Server_pinot-server-0`) to a [StorageStats Object](#2-the-storagestats-object). Represents storage on the actual server nodes. |
| **`deepStore`**       | `object` | A [StorageStats Object](#2-the-storagestats-object) representing the storage of the Deep Store (PinotFS/S3).                                                        |
| **`remoteS3`**        | `object` | A [StorageStats Object](#2-the-storagestats-object) representing the storage on the Remote S3 for a tier table.                                                     |

### 2. The `StorageStats` Object

This object structure is used for `serverInstances`, `deepStore`, `remoteS3`, and all nested `breakdown` objects.

| Field                       | Type      | Description                                                                                                                                     |
| :-------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **`actualItemsCount`**      | `integer` | The total count of unique items (segments/files) physically found in the storage location.                                                      |
| **`actualSizeInBytes`**     | `long`    | The total physical size (in bytes) of all items found.                                                                                          |
| **`unexpectedItemsCount`**  | `integer` | The count of items found physically that were **not** expected (e.g., orphaned segments, temp files).                                           |
| **`unexpectedSizeInBytes`** | `long`    | The total size (in bytes) of the unexpected items.                                                                                              |
| **`totalStaleVersions`**    | `integer` | *(Tiered tables only)* Number of unique versions found that differ from the version calculated via table config and segment CRC.                |
| **`breakdown`**             | `map`     | A granular breakdown of storage by sub-directory. See [Breakdown Definitions](#3-breakdown-definitions) below. Only present when `verbose=true` |
| **`unexpected`**            | `object`  | Details on why items were flagged as unexpected. Contains keys like `unknownItems` or `beyondRetentionSegments`.                                |

### 3. Breakdown Definitions

The keys inside the `breakdown` object change depending on the context (Server vs. Deep Store).

#### Context: Server Instance

When inspecting `serverInstances`, the breakdown contains:

| Key                               | Description                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| **`localSegmentsDirectory`**      | Stats derived from the physical local disk. This is the segment directories for local segments                            |
| **`remoteSegmentsPreloadIndex`**  | Stats derived from the physical local disk. This is the preload indexes for remote segments of a tier table if configured |
| **`remoteSegmentsMetadataCache`** | Stats derived from the physical local disk. This is the metadata cache for remote segments of a tier table if configured  |

#### Context: Deep Store

When inspecting `deepStore`, the breakdown contains:

| Key                   | Description                                                                          |
| :-------------------- | :----------------------------------------------------------------------------------- |
| **`onlineSegments`**  | Segments found in `<data.dir>/<tableNameWithType>`.                                  |
| **`deletedSegments`** | Segments found in the retention queue: `<data.dir>/Deleted_Segments/<rawTableName>`. |
| **`upsertSnapshots`** | Snapshot files for Upsert tables.                                                    |
| **`dedupSnapshots`**  | Snapshot files for Dedup tables.                                                     |

#### Context: Remote S3

When inspecting `remoteS3`, the breakdown contains:

| Key                    | Description                                                    |
| :--------------------- | :------------------------------------------------------------- |
| **`segmentDirectory`** | Segments found under the configured prefix for the tier table. |

## Interpreting results

If `unexpectedSizeInBytes` is not zero, it could mean:

* Stale remote segment versions
* Segments present in storage but not referenced by Pinot metadata
* Deleted segments beyond retention that still exist in deep store

Use `verbose=true` to identify the specific storage component contributing to the difference.

### Stale versions

A version is considered **stale** when it is not the latest expected version for a segment. In remote object storage and local caches for remote tiers, stale versions may remain if cleanup is disabled or delayed.

## Replication considerations

Replication increases server disk usage because segment directories exist per replica. Deep store and remote object store sizes are reported independently of replica placement.

## Operational notes

Listing large deep store or S3 prefixes can be slow and may incur additional object store request costs. Use `verbose=false` for routine monitoring and `verbose=true` for investigation.

## Limitations

During cluster transitions such as rebalances or segment updates, `actualSizeInBytes` can temporarily exceed `expectedSizeInBytes` due to overlapping placement and intermediate artifacts.

Built with [Mintlify](https://mintlify.com).
