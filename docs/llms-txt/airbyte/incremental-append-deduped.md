# Source: https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/core-concepts/sync-modes/incremental-append-deduped.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/core-concepts/sync-modes/incremental-append-deduped.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/core-concepts/sync-modes/incremental-append-deduped.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append-deduped.md

# Incremental Sync - Append + Deduped

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

## High-Level Context[​](#high-level-context "Direct link to High-Level Context")

This sync mode syncs data **incrementally**, which means that only new or modified data will be synced. In contrast with the [Incremental Append mode](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md), this mode updates rows that have been modified instead of adding a new version of the row with the updated data.

If you've synced a row before and it has since been updated, this sync mode will combine the two rows in the destination and use the most recent data. On the other hand, the [Incremental Append mode](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md) would just add a new row with the updated data.

## Overview[​](#overview "Direct link to Overview")

Airbyte supports syncing data in **Incremental | Append + Deduped** mode:

1. **Incremental** means syncing only replicate *new* or *modified* data. This prevents re-fetching data that you have already replicated from a source. If the sync is running for the first time, it is equivalent to a [Full Refresh](/platform/1.6/using-airbyte/core-concepts/sync-modes/full-refresh-append.md) since all data will be considered as *new*.
2. **Append** means that this incremental data is added to existing tables in your data warehouse.
3. **Deduped** means that data in the final table will be unique per primary key (unlike [Append modes](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md)). This is determined by sorting the data using the cursor field and keeping only the latest de-duplicated data row.

Records in the final destination can potentially be deleted as they are de-duplicated, and if your source supports emitting deleting records (e.g. an CDC database source). You should not find multiple copies of the same primary key as these should be unique in that table.

## Definitions[​](#definitions "Direct link to Definitions")

A `cursor` is the value used to track whether a record should be replicated in an incremental sync. A common example of a `cursor` would be a timestamp from an `updated_at` column in a database table.

A `cursor field` is the *field* or *column* in the data where that cursor can be found. Extending the above example, the `updated_at` column in the database would be the `cursor field`, while the `cursor` is the actual timestamp *value* used to determine if a record should be replicated.

We will refer to the set of records that the source identifies as being new or updated as a `delta`.

A `primary key` is one or multiple (called `composite primary keys`) *fields* or *columns* that is used to identify the unique entities of a table. Only one row per primary key value is permitted in a database table. In the data warehouse, just like in [incremental - Append](/platform/1.6/using-airbyte/core-concepts/sync-modes/incremental-append.md), multiple rows for the same primary key can be found in the history table. The unique records per primary key behavior is mirrored in the final table with **incremental deduped** sync mode. The primary key is then used to refer to the entity which values should be updated.

## Rules[​](#rules "Direct link to Rules")

As mentioned above, the delta from a sync will be *appended* to the existing history data in the data warehouse. In addition, it will update the associated record in the final table. Let's walk through a few examples.

### Newly Created Record[​](#newly-created-record "Direct link to Newly Created Record")

Assume that `updated_at` is our `cursor_field` and `name` is the `primary_key`. Let's say the following data already exists into our data warehouse.

| name             | deceased | updated\_at |
| ---------------- | -------- | ----------- |
| Louis XVI        | false    | 1754        |
| Marie Antoinette | false    | 1755        |

In the next sync, the delta contains the following record:

| name      | deceased | updated\_at |
| --------- | -------- | ----------- |
| Louis XVI | false    | 1785        |

At the end of this incremental sync, the data warehouse would now contain:

| name             | deceased | updated\_at |
| ---------------- | -------- | ----------- |
| Marie Antoinette | false    | 1755        |
| Louis XVI        | false    | 1785        |

### Updating a Record[​](#updating-a-record "Direct link to Updating a Record")

Let's assume that our warehouse contains all the data that it did at the end of the previous section. Now, unfortunately the king and queen lose their heads. Let's see that delta:

| name             | deceased | updated\_at |
| ---------------- | -------- | ----------- |
| Louis XVI        | true     | 1793        |
| Marie Antoinette | true     | 1793        |

In the final de-duplicated table:

| name             | deceased | updated\_at |
| ---------------- | -------- | ----------- |
| Louis XVI        | true     | 1793        |
| Marie Antoinette | true     | 1793        |

## Source-Defined Cursor[​](#source-defined-cursor "Direct link to Source-Defined Cursor")

Some sources are able to determine the cursor that they use without any user input. For example, in the [Exchange Rates source](/integrations/sources/exchange-rates.md), the source already knows that the date field should be used to determine the last record that was synced. In these cases, simply select the incremental sync mode in the UI by navigating to the `Schema` tab for a connection.

You can find a more technical details about the configuration data model [here](/platform/1.6/understanding-airbyte/airbyte-protocol.md#catalog).

## User-Defined Cursor[​](#user-defined-cursor "Direct link to User-Defined Cursor")

Some sources are unable to define the cursor without user input. For example, in the [Postgres source](/integrations/sources/postgres.md), the user needs to choose which column in a database table they want to use as the `cursor`. In these cases, simply select the `cursor` for each stream in the UI by navigating to the `Schema` tab for a connection.

You can find a more technical details about the configuration data model [here](/platform/1.6/understanding-airbyte/airbyte-protocol.md#catalog).

## Source-Defined Primary key[​](#source-defined-primary-key "Direct link to Source-Defined Primary key")

Some sources are able to determine the primary key that they use without any user input. For example, in JDBC database sources, the primary key can be defined in the table's metadata. Most APIs also have pre-determined primary keys.

## User-Defined Primary key[​](#user-defined-primary-key "Direct link to User-Defined Primary key")

Some sources cannot define the primary key without user input or the user may want to specify their own primary key on the destination that is different from the source definition. In these cases, select the field in the stream that should be used as the `primary key`. Multiple primary keys can also be selected to form a `composite primary key`.

## Inclusive Cursors[​](#inclusive-cursors "Direct link to Inclusive Cursors")

When replicating data incrementally, Airbyte provides an at-least-once delivery guarantee. This means that it is acceptable for sources to re-send some data when ran incrementally. One case where this is particularly relevant is when a source's cursor is not very granular. For example, if a cursor field has the granularity of a day (but not hours, seconds, etc), then if that source is run twice in the same day, there is no way for the source to know which records that are that date were already replicated earlier that day. By convention, sources should prefer resending data if the cursor field is ambiguous.

## Known Limitations[​](#known-limitations "Direct link to Known Limitations")

Due to the use of a cursor column, if modifications to the underlying records are made without properly updating the cursor field, then the updated records won't be picked up by the **Incremental** sync as expected since the source connectors extract delta rows using a SQL query looking like:

```
select * from table where cursor_field > 'last_sync_max_cursor_field_value'
```

## Related information[​](#related-information "Direct link to Related information")

* [An overview of Airbyte’s replication modes](https://airbyte.com/blog/understanding-data-replication-modes).
* [Explore Airbyte’s incremental data synchronization](https://airbyte.com/tutorials/incremental-data-synchronization).

***

**Note**:

Previous versions of Airbyte destinations supported SCD tables, which would sore every entry seen for a record. This was removed with Destinations V2 and [Typing and Deduplication](/platform/1.6/using-airbyte/core-concepts/typing-deduping.md).
