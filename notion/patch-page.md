# Source: https://developers.notion.com/reference/patch-page

Updates the `properties` of a page in a database. The `properties` body param of this endpoint can only be used to update the `properties` of a page that is a child of a database. The page’s `properties` schema must match the parent [database’s properties](https://developers.notion.com/reference/property-object).
This endpoint can be used to update any page `icon` or `cover`, and can be used to [`delete`](https://developers.notion.com/reference/archive-a-page) or restore any page.
To add page content instead of page properties, use the [append block children](https://developers.notion.com/reference/patch-block-children) endpoint. The `page_id` can be passed as the `block_id` when adding block children to the page.
Returns the updated [page object](https://developers.notion.com/reference/page).
> ## 📘
> Requirements
> Your integration must have [update content capabilities](https://developers.notion.com/reference/capabilities#content-capabilities) on the target page in order to call this endpoint. To update your integrations capabilities, navigation to the [My integrations](https://www.notion.so/my-integrations) dashboard, select your integration, go to the **Capabilities** tab, and update your settings as needed.
> Attempting a query without update content capabilities returns an HTTP response with a 403 status code.
> ## 🚧
> Limitations
>   * Updating [rollup property values](https://developers.notion.com/reference/property-value-object#rollup-property-values) is not supported. 
>   * A page’s `parent` cannot be changed.
> 

### [](https://developers.notion.com/reference/patch-page#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
