# Source: https://docs.pinot.apache.org/release-1.0.0/basics/data-import/segment-reload.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/data-import/segment-reload.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/data-import/segment-reload.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/data-import/segment-reload.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/tutorials/segment-reload.md

# Source: https://docs.pinot.apache.org/operators/tutorials/segment-reload.md

# Reload a table segment

When Pinot writes data to segments in a table, it saves those segments to a deep store location specified in your [table configuration](https://docs.pinot.apache.org/configuration-reference/table), such as a storage drive or Amazon S3 bucket.

{% hint style="info" %}
If a **new column is added to your table or schema configuration during ingestion**, incorrect data may appear in the consuming segment(s). To ensure accurate values are reloaded, see how to [add a new column during ingestion](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations#add-a-new-column-during-ingestion).&#x20;
{% endhint %}

## Use the Pinot Controller API to reload segments

To reload all segments from a table, use:

```
POST /segments/{tableName}/reload
```

To reload a specific segment from a table, use:

```
POST /segments/{tableName}/{segmentName}/reload
```

A successful API call returns the following response:

```json
{
    "status": "200"
}
```

## Use the Pinot Admin Console to reload segments

To use the Pinot Admin Console, do the following:

1. From the left navigation menu, select **Cluster Manager**.
2. Under **TENANTS**, select the **Tenant Name**.
3. From the list of tables in the tenant, select the **Table Name**.
4. Do one of the following:
   * To reload all segments, under **OPERATIONS**, click **Reload All Segments**.
   * To reload a specific segment, under **SEGMENTS**, select the **Segment Name**, and then in the new **OPERATIONS** section, select **Reload Segment**.
