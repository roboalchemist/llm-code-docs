# Source: https://developers.notion.com/reference/parent-object

[Pages](https://developers.notion.com/reference/page), [databases](https://developers.notion.com/reference/database), [data sources](https://developers.notion.com/reference/data-source), [comments](https://developers.notion.com/reference/comment-object) and [blocks](https://developers.notion.com/reference/block) are either located inside other pages, databases, data sources, and blocks, or are located at the top level of a workspace. This location is known as the "parent". Parent information is represented by a consistent `parent` object throughout the API.
General parenting rules:
  * Pages can be parented by other pages, data sources, blocks, or by the whole workspace. 
    * _Prior to[API version 2025-09-03](https://developers.notion.com/docs/upgrade-guide-2025-09-03), page parents were databases, not data sources._
  * Blocks can be parented by pages, data sources, or blocks.
  * Databases can be parented by pages, blocks, or by the whole workspace. 
    * _For wikis, databases can also have a data source parent._
  * Data sources are parented by databases. 
    * _Linked or externally synced external data sources may have data source parents, but aren't thoroughly supported in Notion's API._


> ## 🚧
> Exceptions apply
> These parenting rules reflect the possible response you may receive when retrieving information about pages, databases, and blocks via Notion’s REST API in the latest APIversion.
> If you are creating new pages, databases, or blocks via Notion’s public REST API, the parenting rules may vary. For example, the parent of a database currently must be a page if it is [created](https://developers.notion.com/reference/create-a-database) via the API.
> Refer to the API reference documentation for creating [pages](https://developers.notion.com/reference/post-page), [databases](https://developers.notion.com/reference/database-create), [data sources](https://developers.notion.com/reference/create-a-data-source), and [blocks](https://developers.notion.com/reference/patch-block-children) for more information on current parenting rules.
### [](https://developers.notion.com/reference/parent-object#database-parent)
Database parents most commonly show up for [Data source](https://developers.notion.com/reference/data-source) objects.
Property | Type | Description | Example values  
---|---|---|---  
`type` | `string` | Always `"database_id"`. | `"database_id"`  
`database_id` |  `string` (UUIDv4) | The ID of the [database](https://developers.notion.com/reference/database) that this page belongs to. | `"b8595b75-abd1-4cad-8dfe-f935a8ef57cb"`  
Database parent example
```
{
  "type": "database_id",
  "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
}

```

### [](https://developers.notion.com/reference/parent-object#data-source-parent)
Data source parents most commonly show up for [Page](https://developers.notion.com/reference/page) objects.
Property | Type | Description | Example values  
---|---|---|---  
`type` | `string` | Always `"data_source_id"`. | `"data_source_id"`  
`data_source_id` |  `string` (UUIDv4) | The ID of the [data source](https://developers.notion.com/reference/data-source) that this page belongs to. | `"1a44be12-0953-4631-b498-9e5817518db8"`  
`database_id` |  `string` (UUIDv4) | The ID of the [database](https://developers.notion.com/reference/database) that the data source belongs to, provided in the API response for convenience. | `"b8595b75-abd1-4cad-8dfe-f935a8ef57cb"`  
Data source parent example
```
{
  "type": "data_source_id",
  "data_source_id": "1a44be12-0953-4631-b498-9e5817518db8",
  "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
}

```

### [](https://developers.notion.com/reference/parent-object#page-parent)
Property | Type | Description | Example values  
---|---|---|---  
`type` | `string` | Always `"page_id"`. | `"page_id"`  
`page_id` |  `string` (UUIDv4) | The ID of the [page](https://developers.notion.com/reference/page) that this page belongs to. | `"59833787-2cf9-4fdf-8782-e53db20768a5"`  
Page parent example
```
{
  "type": "page_id",
  "page_id": "59833787-2cf9-4fdf-8782-e53db20768a5"
}

```

### [](https://developers.notion.com/reference/parent-object#workspace-parent)
A page or database with a workspace parent is a top-level page within a Notion workspace. Team-level pages are also currently represented as having a workspace parent in the API.
The workspace `parent` object contains the following keys:
Property | Type | Description | Example values  
---|---|---|---  
`type` | `type` | Always `"workspace"`. | `"workspace"`  
`workspace` | `boolean` | Always `true`. | `true`  
Workspace parent example
```
{
  "type": "workspace",
  "workspace": true
}

```

### [](https://developers.notion.com/reference/parent-object#block-parent)
A page may have a block parent if it is created inline in a chunk of text, or is located beneath another block like a toggle or bullet block. The `parent` property is an object containing the following keys:
Property | Type | Description | Example values  
---|---|---|---  
`type` | `type` | Always `"block_id"`. | `"block_id"`  
`block_id` |  `string` (UUIDv4) | The ID of the [page](https://developers.notion.com/reference/page) that this page belongs to. | `"ea29285f-7282-4b00-b80c-32bdbab50261"`  
Block parent example
```
{
  "type": "block_id",
  "block_id": "7d50a184-5bbe-4d90-8f29-6bec57ed817b"
}

```

