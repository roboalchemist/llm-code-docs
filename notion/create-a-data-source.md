# Source: https://developers.notion.com/reference/create-a-data-source

Use this API to add an additional [data source](https://developers.notion.com/reference/data-source) to an existing [database](https://developers.notion.com/reference/database). The `properties` follow the [same structure](https://developers.notion.com/reference/property-object) as the initial schema passed to `initial_data_source[properties]` in the [Create a database](https://developers.notion.com/reference/database-create6ee911d9) API, but can be managed independently of the `properties` of any sibling data sources.
A standard "table" view is created alongside the new data source. To customize database views, use the Notion app. Managing views is not currently supported in the API.
