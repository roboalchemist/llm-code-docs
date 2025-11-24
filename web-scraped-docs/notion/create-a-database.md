# Source: https://developers.notion.com/reference/create-a-database

> ## ❗️
> Deprecated as of version 2025-09-03
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](https://developers.notion.com/docs/upgrade-guide-2025-09-03).
> Refer to the new APIs instead:
>   * [Create a database](https://developers.notion.com/reference/database-create)
>   * [Create a data source](https://developers.notion.com/reference/create-a-data-source)
> 

Creates a database as a subpage in the specified parent page, with the specified `properties` schema. Currently, the parent of a new database must be a Notion page or a [wiki database](https://www.notion.so/help/wikis-and-verified-pages).
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have insert content capabilities. Attempting to call this API without insert content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
> ## 🚧
> Limitations
> Creating new `status` database properties is currently not supported.
### [](https://developers.notion.com/reference/create-a-database#errors)
Returns a 404 if the specified parent page does not exist, or if the integration does not have access to the parent page.
Returns a 400 if the request is incorrectly formatted, or a 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
_Note: Each Public API endpoint can return several possible error codes. See the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information._
