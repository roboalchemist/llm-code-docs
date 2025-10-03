# Source: https://developers.notion.com/reference/retrieve-a-database

> ## ❗️
> Deprecated as of version 2025-09-03
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](https://developers.notion.com/docs/upgrade-guide-2025-09-03).
> Refer to the new APIs instead:
>   * [Retrieve a database](https://developers.notion.com/reference/database-retrieve)
>   * [Retrieve a data source](https://developers.notion.com/reference/retrieve-a-data-source)
> 

Retrieves a [database object](https://developers.notion.com/reference/database) — information that describes the structure and columns of a database — for a provided database ID. The response adheres to any limits to an integration’s capabilities.
To fetch database rows rather than columns, use the [Query a database](https://developers.notion.com/reference/post-database-query) endpoint.
To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.
![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)
Notion database ID
Refer to the [Build your first integration guide](https://developers.notion.com/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.
### [](https://developers.notion.com/reference/retrieve-a-database#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
### [](https://developers.notion.com/reference/retrieve-a-database#additional-resources)
  * [How to share a database with your integration](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions)
  * [Working with databases guide](https://developers.notion.com/docs/working-with-databases)


> ## 📘
> Database relations must be shared with your integration
> To retrieve database properties from [database relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.
> ## 🚧
> The Notion API does not support retrieving linked databases.
> To fetch the information in a [linked database](https://www.notion.so/help/guides/using-linked-databases), share the original source database with your Notion integration.
