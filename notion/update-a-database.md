# Source: https://developers.notion.com/reference/update-a-database

> ##
>
> Deprecated as of version 2025-09-03
>
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
>
> Refer to the new APIs instead:
>
> - [Update a database](/reference/database-update)
> - [Update a data source](/reference/update-a-data-source)
Updates the database object — the title, description, or properties — of a specified database.
Returns the updated [database object](/reference/database).
Database properties represent the columns (or schema) of a database. To update the properties of a database, use the `properties` [body param](/reference/update-property-schema-object) with this endpoint. Learn more about database properties in the [database properties](/reference/property-object) and [Update database properties](/reference/update-property-schema-object) docs.
To update a `relation` database property, share the related database with the integration. Learn more about relations in the [database properties](/reference/property-object#relation) page.
For an overview of how to use the REST API with databases, refer to the [Working with databases](/docs/working-with-databases) guide.
### How database property type changes work
All properties in pages are stored as rich text. Notion will convert that rich text based on the types defined in a database's schema. When a type is changed using the API, the data will continue to be available, it is just presented differently.
For example, a multi select property value is represented as a comma-separated list of strings (eg. "1, 2, 3") and a people property value is represented as a comma-separated list of IDs. These are compatible and the type can be converted.
Note: Not all type changes work. In some cases data will no longer be returned, such as people type → file type.
### Interacting with database rows
This endpoint cannot be used to update database rows.
To update the properties of a database row — rather than a column — use the [Update page properties](/reference/patch-page) endpoint. To add a new row to a database, use the [Create a page](/reference/post-page) endpoint.
### Recommended database schema size limit
Developers are encouraged to keep their database schema size to a maximum of **50KB**. To stay within this schema size limit, the number of properties (or columns) added to a database should be managed.
Database schema updates that are too large will be blocked by the REST API to help developers keep their database queries performant.
### Errors
Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ##
>
> The following database properties cannot be updated via the API:
>
> - `formula`
> - `select`
> - `status`
> - [Synced content](https://www.notion.so/help/guides/synced-databases-bridge-different-tools)
> - A `multi_select` database property’s options values. An option can be removed, but not updated.
> ##
>
> Database relations must be shared with your integration
>
> To update a database [relation](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation) property, the related database must also be shared with your integration.