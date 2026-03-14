# Source: https://docs.startree.ai/corecapabilities/manage-data/schema-evolution.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Schema Evolution

Apache Pinot provides great support for evolving a schema after the table has been created. This is frequently needed as business requirements evolve, and data formats or structures need to change.

At a high level schema evolution works as follows:

1. Create the new schema based on the existing schema.
2. Update the schema using the Controller API
3. Invoker the Table Reload operation to ensure the new schema is picked up by all Pinot segments and hence in the query results.

Details of each of these steps can be found in the Apache Pinot docs: [Schema Evolution](https://docs.pinot.apache.org/users/tutorials/schema-evolution)

**Segment reload** is the primary mechanism that enables schema evolution in Pinot by applying new schema changes to existing segments. When you update a schema with backwards compatible changes, the segments need to be reloaded to incorporate these changes into the queryable data.

### **Schema Update and Reload Integration**

When a schema is updated, Pinot provides two options for applying the changes to existing segments

1. **Immediate reload** (`reload=true`) - Triggers `reloadAllSegments()` for all tables using the schema
2. **Deferred reload - default** (`reload=false`) - Sends schema refresh messages to servers without immediate reload

By default, Pinot does not do a full reload operation but instead only instructs the servers to refresh the schema.

### **Backwards compatible changes**

Following changes are considered backwards compatible:

* **Adding new columns** - You can add new fields to the schema
* **Changing default values** - Modifying default values for existing columns is allowed
* **Time column granularity changes** - Modifications to time field granularity specifications are permitted
* **DateTime column format changes** - Changes to datetime field formats are backwards compatible

### **Incompatible Changes**

Generally speaking, following changes are deemed as incompatible:

* Removing existing columns
* Changing column data types

<Note>
  In StarTree Cloud, you can still make such incompatible changes by running the SegmentRefreshTask (SRT). Note that queries may not succeed until the SRT task has finished.
</Note>

### **Query Semantics**

It is important to ensure that queries don't fail in the midst of a schema evolution operation. In order to make this easier, Pinot supports the notion of a virtual column which is used in lieu of the actual newly added column. Queries touching this virtual column will pick up the default values instead of failing (which was the old behavior). Here is the general guidance:

| **Scenario**                                  | **Before**                               | **After**                                                                      |
| :-------------------------------------------- | :--------------------------------------- | :----------------------------------------------------------------------------- |
| Rolling addition of a new column (newCol)     | Queries fail with schema mismatch        | Queries succeed; newCol is exposed as a virtual column                         |
| Add a new column without segment reload       | Empty results due to server‑side pruning | Queries succeed and return all columns, with newCol filled with default values |
| Queries over existing columns only            | No change                                | No change                                                                      |
| Queries referencing a partially loaded column | Merge errors or empty responses          | Queries succeed with consistent results, including the new virtual column      |

Full details of this new functionality can be found [in this PR](https://github.com/apache/pinot/pull/15350).

### **Data Backfill**

Once a new column is added, often times we need to populate it with real values - typically from a batch data source like data lake. StarTree cloud provides a convenient way to accomplish this using the SegmentBackfillTask. For more details, please refer to: [https://docs.startree.ai/corecapabilities/manage-data/segment-backfill-task](https://docs.startree.ai/corecapabilities/manage-data/segment-backfill-task)

Built with [Mintlify](https://mintlify.com).
