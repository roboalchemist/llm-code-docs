# Source: https://developers.notion.com/reference/post-page

Creates a new [page](/reference/page) that is a child of an existing page or [data source](/reference/data-source).
If the new page is a child of an existing page,`title` is the only valid property in the `properties` body param.
If the new page is a child of an existing database, the keys of the `properties` object body param must match the parent [data source's properties](/reference/property-object).
This endpoint can be used to create a new page with or without content using the `children` option. To add content to a page after creating it, use the [Append block children](/reference/patch-block-children) endpoint.
Returns a new [page object](/reference/page).
> ##
>
> Some page `properties` are not supported via the API.
>
> A request body that includes `rollup`, `created_by`, `created_time`, `last_edited_by`, or `last_edited_time` values in the properties object returns an error. These Notion-generated values cannot be created or updated via the API. If the `parent` contains any of these properties, then the new page’s corresponding values are automatically created.
> ##
>
> Requirements
>
> Your integration must have [Insert Content capabilities](/reference/capabilities#content-capabilities) on the target parent page or database in order to call this endpoint. To update your integrations capabilities, navigation to the [My integrations](https://www.notion.so/my-integrations) dashboard, select your integration, go to the **Capabilities** tab, and update your settings as needed.
>
> Attempting a query without update content capabilities returns an HTTP response with a 403 status code.
### Errors
Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.