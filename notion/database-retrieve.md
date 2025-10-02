# Source: https://developers.notion.com/reference/database-retrieve

Retrieves a [database object](/reference/database) — a container for one or more [data sources](/reference/data-source) — for a provided database ID. The response adheres to any limits to an integration’s capabilities.
The most important fields in the database object response to highlight:
- `data_sources`: An array of JSON objects with the `id` and `name` of every data source under the database
  - These data source IDs can be used with the [Retrieve a data source](/reference/retrieve-a-data-source), [Update a data source](/reference/update-a-data-source), and [Query a data source](/reference/query-a-data-source) APIs
- `parent`: The direct parent of the database; generally a `page_id` or `workspace: true`
To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.
<img src="https://files.readme.io/64967fd-small-62e5027-notion_database_id.png" alt="Notion database ID" />
<figcaption><p>Notion database ID</p></figcaption>
Refer to the [Build your first integration guide](/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.
### Errors
Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
### Additional resources
- [How to share a database with your integration](/docs/create-a-notion-integration#give-your-integration-page-permissions)
- [Working with databases guide](/docs/working-with-databases)