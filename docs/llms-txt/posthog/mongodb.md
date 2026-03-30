# Source: https://posthog.com/docs/data-warehouse/sources/mongodb.md

# Source: https://posthog.com/docs/cdp/sources/mongodb.md

# Linking MongoDB as a source - Docs

The MongoDB connector can link your MongoDB collections to PostHog.

To link MongoDB:

1.  Go to the [Data pipeline page](https://app.posthog.com/data-management/sources) and the sources tab in PostHog
2.  Click **New source** and select MongoDB
3.  Enter your MongoDB connection string
4.  Click **Next**, select the collections you want to sync, as well as the [sync method](/docs/cdp/sources.md#incremental-vs-full-table), and then press **Import**

Once the syncs are complete, you can start using MongoDB data in PostHog.

> **Note:** MongoDB data is unstructured so the returned columns are an `_id` field and a `data` column that contain the entire document contents. Data fields can be selected with dot notation (e.g. `data.field1`)

### Incremental and append-only syncing

MongoDB supports incremental and append-only sync methods. For a field to be available for these sync methods, it must:

1.  **Have an index** — only indexed fields are eligible.
2.  **Be a supported type** — the following BSON types work:
    -   `date` or `timestamp`
    -   `int` or `long`
    -   `double` or `decimal`
    -   `objectId` (only for the `_id` field)

PostHog infers field types from the first 10,000 documents in the collection, so fields with mixed types may resolve to an unsupported type.

#### Inbound IP addresses

We use a set of IP addresses to access your instance. To ensure this connector works, add these IPs to your inbound security rules:

| US | EU |
| --- | --- |
| 44.205.89.55 | 3.75.65.221 |
| 44.208.188.173 | 18.197.246.42 |
| 52.4.194.122 | 3.120.223.253 |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better