# Source: https://docs.startree.ai/corecapabilities/manage-data/deep-store-sync.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep Store Segment Sync

When a user makes changes to a Pinot table configuration or schema and those updates require a segment rebuild, the servers reload the local segments and keep them up to date with the table configuration and schema.

But the deep store segment is not included in the sync and this causes an increase in startup time because a server needs to download the segment from the deep store and rebuild it again locally. To avoid this, the [Alter Table Task](/corecapabilities/manage-data/alter-table-task) has been enhanced to offload the segment reload to minions and to keep the deep store in sync with the latest table configuration and schema, reducing server load.

## How does deep store segment sync work?

When the alter table task is used in the `reloadOnly` mode.

1. The process fetches stale segments on the servers for the table.
2. Generates a minion task that rebuilds the segment with the latest table configuration and schema. Then uploads the segment to the deep store with the same name.
3. This triggers a segment refresh message. After that, all servers hosting the segment will download the segment and load it locally.
4. After the reload through the alter table task, the segment metadata will include a table hash value. This value is used by subsequent task generations to skip these segments.

## Configuration

Add the following configuration parameters to the alter table task:

```json  theme={null}
"task": {
  "taskTypeConfigsMap": {
    "StarTreeAlterTableTask": {
      "reloadOnly": "true",
      "forceReload": "true"
    }
  }
}
```

<Warning>
  Experimental feature, use with caution.
</Warning>

<ParamField path="reloadOnly">
  Set this flag to **true** to use the alter table task for deep store sync.

  General recommendations

* Make sure there is no concurrent server reload operation as that would lead to ATT skipping those segments from reload on deep store.
* Set **skipSegmentPreprocess** on the table so that segments are not reloaded on server restart.
* Run this task periodically to reduce the probability of server side reload through user triggers.
* reloadOnly takes precedence if forceReload is also configured.
</ParamField>

<ParamField path="forceReload">
  This parameter uses the table hash value added by the alter table task in the reloaded segments. The process does not check for segment metadata on servers. Use this flag for the first iteration of deep store sync to bootstrap all the historical segments and to add the table hash. This ensures that all the existing segments are in sync with the table configuration. After the first iteration, this parameter can be removed. Please note that reloadOnly takes precedence if both reloadOnly and forceReload are also configured.
</ParamField>

## Scenarios

The table shows the state of deep store sync and the effect of the configuration parameters for different scenarios:

| ***Scenario***                                |                                                           |                                                                                   |                                                              |                   *Action by the Alter Table Task on the Segment*                   |                                                                                 |
| :-------------------------------------------- | :-------------------------------------------------------- | :-------------------------------------------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------: |
|                                               | **Case**                                                  |                                   **Deep Store**                                  |                       **Local Server**                       |                                     `reloadOnly`                                    |                     `reloadOnly`**with**<br />`forceReload`                     |
| **Existing segment before task introduction** | Table not updated since segment creation                  |      <Icon icon="arrows-rotate" color="#2E6F40" size={30} /><br />*(In Sync)*     |    <Icon icon="arrows-rotate" color="#2E6F40" size={30} />   | <Icon icon="rotate-exclamation" color="#8B0000" size={30} /><br />*(Not Refreshed)* | <Icon icon="arrows-rotate" color="#2E6F40" size={30} /><br />*(Refreshed Once)* |
|                                               | Table updated and segment reloaded on server              | <Icon icon="rotate-exclamation" color="#8B0000" size={30} /><br />*(Not In Sync)* |    <Icon icon="arrows-rotate" color="#2E6F40" size={30} />   |             <Icon icon="rotate-exclamation" color="#8B0000" size={30} />            |             <Icon icon="arrows-rotate" color="#2E6F40" size={30} />             |
|                                               | Table updated but segment not reloaded on server          |            <Icon icon="rotate-exclamation" color="#8B0000" size={30} />           | <Icon icon="rotate-exclamation" color="#8B0000" size={30} /> |               <Icon icon="arrows-rotate" color="#2E6F40" size={30} />               |             <Icon icon="arrows-rotate" color="#2E6F40" size={30} />             |
| **Segment generated post task introduction**  | Table not updated or segment is already processed by task |              <Icon icon="arrows-rotate" color="#2E6F40" size={30} />              |    <Icon icon="arrows-rotate" color="#2E6F40" size={30} />   |             <Icon icon="rotate-exclamation" color="#8B0000" size={30} />            |             <Icon icon="arrows-rotate" color="#2E6F40" size={30} />             |
|                                               | Table updated and segment reloaded on server              |            <Icon icon="rotate-exclamation" color="#8B0000" size={30} />           |    <Icon icon="arrows-rotate" color="#2E6F40" size={30} />   |             <Icon icon="rotate-exclamation" color="#8B0000" size={30} />            |             <Icon icon="arrows-rotate" color="#2E6F40" size={30} />             |
|                                               | Table updated and task is yet to run                      |            <Icon icon="rotate-exclamation" color="#8B0000" size={30} />           | <Icon icon="rotate-exclamation" color="#8B0000" size={30} /> |               <Icon icon="arrows-rotate" color="#2E6F40" size={30} />               |             <Icon icon="arrows-rotate" color="#2E6F40" size={30} />             |

## Limitations

* In the background, the servers still load segments but the loading process is faster.
* The initial run will involve a process overhead to reload all segments. Consecutive runs will be incremental.
* Server-side reloads are not automatically blocked. Maintain a frequent cron on the task to make sure segments are reloaded by the alter table task and to reduce the probability of server side reload through user triggers.

Built with [Mintlify](https://mintlify.com).
