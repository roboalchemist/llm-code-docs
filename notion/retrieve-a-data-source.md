# Source: https://developers.notion.com/reference/retrieve-a-data-source

Retrieves a [data source](https://developers.notion.com/reference/data-source) object — information that describes the structure and columns of a data source — for a provided data source ID. The response adheres to any limits to an integration’s capabilities and the permissions of the `parent` database.
To fetch data source _rows_ (i.e. the child pages of a data source) rather than columns, use the [Query a data source](https://developers.notion.com/reference/query-a-data-source) endpoint.
### [](https://developers.notion.com/reference/retrieve-a-data-source#finding-a-data-source-id)
Navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.
![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)
Notion database ID
Then, use the [Retrieve a database](https://developers.notion.com/reference/retrieve-a-database-1-6ee911d9) API to get a list of `data_sources` for that database. There is often only one data source, but when there are multiple, you may have the ID or name of the one you want to retrieve in mind (or you can retrieve each of them). Use that data source ID with this endpoint to get its `properties`.
To get a data source ID from the Notion app directly, the settings menu for a database includes a "Copy data source ID" button under "Manage data sources":
![Screenshot of the "Manage data sources" menu for a database in Notion, with "Copy data source ID" button.](https://files.readme.io/30ed6ac31d8c25eb2ff653dd3b11bfd2e30e8af4df6a6d5e0670b4ad7a96cf73-image.png)
Screenshot of the "Manage data sources" menu for a database in Notion, with "Copy data source ID" button.
Refer to the [Build your first integration guide](https://developers.notion.com/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.
### [](https://developers.notion.com/reference/retrieve-a-data-source#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
### [](https://developers.notion.com/reference/retrieve-a-data-source#additional-resources)
  * [How to share a database with your integration](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions)
  * [Working with databases guide](https://developers.notion.com/docs/working-with-databases)


> ## 📘
> Data source relations must be shared with your integration
> To retrieve data source properties from [database relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.
> ## 🚧
> The Notion API does not support retrieving linked data sources
> To fetch the information in a [linked data source](https://www.notion.so/help/guides/using-linked-databases), share the original source database with your Notion integration.
