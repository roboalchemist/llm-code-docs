# Source: https://docs.squared.ai/guides/data-modelling/sync-modes/full-refresh.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Full Refresh

> Full Refresh syncs replace existing data with new data.

### Overview

The Full Refresh mode in AI Squared is a straightforward method used to sync data to a destination. It retrieves all available information from the source, regardless of whether it has been synced before. This mode is ideal for scenarios where you want to completely replace existing data in the destination with fresh data from the source.

In the Full Refresh mode, new syncs will replace all existing data in the destination table with the new data from the source. This ensures that the destination contains the most up-to-date information available from the source.

### Example Behavior

Consider the following scenario where we have a database table named `Users` in the destination:

#### Before Sync

| **id** | **name** | **email**                                     |
| ------ | -------- | --------------------------------------------- |
| 1      | Alice    | [alice@example.com](mailto:alice@example.com) |
| 2      | Bob      | [bob@example.com](mailto:bob@example.com)     |

#### New Data in Source

| **id** | **name** | **email**                                     |
| ------ | -------- | --------------------------------------------- |
| 1      | Alice    | [alice@example.com](mailto:alice@example.com) |
| 3      | Carol    | [carol@example.com](mailto:carol@example.com) |
| 4      | Dave     | [dave@example.com](mailto:dave@example.com)   |

#### After Sync

| **id** | **name** | **email**                                     |
| ------ | -------- | --------------------------------------------- |
| 1      | Alice    | [alice@example.com](mailto:alice@example.com) |
| 3      | Carol    | [carol@example.com](mailto:carol@example.com) |
| 4      | Dave     | [dave@example.com](mailto:dave@example.com)   |

In this example, notice how the previous user "Bob" is no longer present in the destination after the sync, and new users "Carol" and "Dave" have been added.
