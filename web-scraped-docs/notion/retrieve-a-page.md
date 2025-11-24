# Source: https://developers.notion.com/reference/retrieve-a-page

> ## 🚧
> This endpoint will not accurately return properties that exceed 25 references
> Do **not** use this endpoint if a page property includes more than 25 references to receive the full list of references. Instead, use the [Retrieve a page property endpoint](https://developers.notion.com/reference/retrieve-a-page-property) for the specific property to get its complete reference list.
Retrieves a [Page object](https://developers.notion.com/reference/page) using the ID specified.
Responses contains page **properties** , not page content. To fetch page content, use the [Retrieve block children](https://developers.notion.com/reference/get-block-children) endpoint.
Page properties are limited to up to **25 references** per page property. To retrieve data related to properties that have more than 25 references, use the [Retrieve a page property](https://developers.notion.com/reference/retrieve-a-page-property#rollup-properties) endpoint. (See [Limits](https://developers.notion.com/reference/retrieve-a-page#limits) below for additional information.)
### [](https://developers.notion.com/reference/retrieve-a-page#parent-objects-pages-vs-databases)
If a page’s [Parent object](https://developers.notion.com/reference/parent-object) is a database, then the property values will conform to the [database property schema](https://developers.notion.com/reference/property-object). 
If a page object is not part of a database, then the only property value available for that page is its `title`.
### [](https://developers.notion.com/reference/retrieve-a-page#limits)
The endpoint returns a maximum of 25 page or person references per [page property](https://developers.notion.com/reference/property-value-object). If a page property includes more than 25 references, then the 26th reference and beyond might be returned as `Untitled`, `Anonymous`, or not be returned at all. 
This limit affects the following properties: 
  * [`people`](https://developers.notion.com/reference/property-value-object#people-property-values): response object can’t be guaranteed to return more than 25 people.
  * [`relation`](https://developers.notion.com/reference/property-value-object#relation-property-values): the `has_more` value of the `relation` in the response object is `true` if a `relation` contains more than 25 related pages. Otherwise, `has_more` is false.
  * [`rich_text`](https://developers.notion.com/reference/property-value-object#rich-text-property-values): response object includes a maximum of 25 populated inline page or person mentions.
  * [`title`](https://developers.notion.com/reference/property-value-object#title-property-values): response object includes a maximum of 25 inline page or person mentions.


> ## 📘
> Integration capabilities
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
### [](https://developers.notion.com/reference/retrieve-a-page#errors)
Returns a 404 HTTP response if the page doesn't exist, or if the integration doesn't have access to the page.
Returns a 400 or 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
_Note: Each Public API endpoint can return several possible error codes. See the Error codes section of the Status codes documentation for more information._
