# Source: https://developers.notion.com/reference/update-a-data-source

Updates the [data source](/reference/data-source) object — the properties, title, description, or whether it's in the trash — of a specified data source under a database.
Returns the updated data source object.
Use the `parent` parameter to move the data source to a different `database_id`. If you do so, any existing views that refer to the data source in the current database continue to exist, but become *linked* views. A new standard "table" view for the moved data source is created under the new (destination) database. Use the Notion app to make any further changes to the views; managing views using the API is not currently supported.
Data source properties represent the columns (or schema) of a data source. To update the properties of a data source, use the `properties` [body param](/reference/update-data-source-properties) with this endpoint. Learn more about data source properties in the [data source properties](/reference/property-object) and [Update data source properties](/reference/update-data-source-properties) docs.
To update a `relation` data source property, share the related database with the integration. Learn more about relations in the [data source properties](/reference/property-object#relation) page.
For an overview of how to use the REST API with databases, refer to the [Working with databases](/docs/working-with-databases) guide.
### How data sources property type changes work
All properties in pages are stored as rich text. Notion will convert that rich text based on the types defined in a data source's schema. When a type is changed using the API, the data will continue to be available, it is just presented differently.
For example, a multi select property value is represented as a comma-separated list of strings (eg. "1, 2, 3") and a people property value is represented as a comma-separated list of IDs. These are compatible and the type can be converted.
Note: Not all type changes work. In some cases data will no longer be returned, such as people type → file type.
### Interacting with data source rows
This endpoint cannot be used to update data source rows.
To update the properties of a data source row — rather than a column — use the [Update page properties](/reference/patch-page) endpoint. To add a new row to a database, use the [Create a page](/reference/post-page) endpoint.
### Recommended data source schema size limit
Developers are encouraged to keep their data source schema size to a maximum of **50KB**. To stay within this schema size limit, the number of properties (or columns) added to a data source should be managed.
Data source schema updates that are too large will be blocked by the REST API to help developers keep their data source queries performant.
### Errors
Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ##
>
> The following data source properties cannot be updated via the API:
>
> - `formula`
> - `status`
> - [Synced content](https://www.notion.so/help/guides/synced-databases-bridge-different-tools)
> - `place`
> ##
>
> Data source relations must be shared with your integration
>
> To update a data source [relation](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation) property, the related database must also be shared with your integration.