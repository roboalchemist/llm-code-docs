# Source: https://developers.notion.com/reference/post-search

Searches all parent or child pages and data_sources that have been shared with an integration.
Returns all [pages](https://developers.notion.com/reference/page) or [data_sources](https://developers.notion.com/reference/data-source) , excluding duplicated linked databases, that have titles that include the `query` param. If no `query` param is provided, then the response contains all pages or data_sources that have been shared with the integration. The results adhere to any limitations related to an [integration’s capabilities](https://developers.notion.com/reference/capabilities).
To limit the request to search only pages or to search only data_source, use the `filter` param.
### [](https://developers.notion.com/reference/post-search#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ## 📘
> The Search endpoint supports pagination. To learn more about working with [paginated](https://developers.notion.com/reference/intro#pagination) responses, see the pagination section of the Notion API Introduction.
> ## 🚧
> To search a specific data_source — not all sources shared with the integration — use the [Query a data_source](https://developers.notion.com/reference/query-a-data-source) endpoint instead.
