# Source: https://developers.notion.com/reference/query-a-data-source

Gets a list of [Pages](/reference/page) and/or [Data Sources](/reference/data-source) contained in the data source, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.
> ##
>
> Databases, data sources, and wikis
>
> [Wiki](https://www.notion.so/help/wikis-and-verified-pages) data sources can contain both pages and databases as children. In all other cases, the children can only be pages.
>
> When there's a [database](/reference/database) result, this API returns all data sources that are children of *that* database, instead of surfacing the database directly. Surfacing the data source instead of the direct database child helps make it easier to craft your next API request (for example, retrieving the data source).
[**Filters**](/reference/filter-data-source-entries) are similar to the [filters provided in the Notion UI](https://www.notion.so/help/views-filters-and-sorts) where the set of filters and filter groups chained by "And" in the UI is equivalent to having each filter in the array of the compound `"and"` filter. Similar a set of filters chained by "Or" in the UI would be represented as filters in the array of the `"or"` compound filter.
Filters operate on data source properties and can be combined. If no filter is provided, all the pages in the data source will be returned with pagination.
<img src="https://files.readme.io/6fe4a44-Screen_Shot_2021-12-23_at_11.46.21_AM.png" title="Screen Shot 2021-12-23 at 11.46.21 AM.png" alt="1340" />
<figcaption><p>The above filters in the UI can be represented as the following filter object</p></figcaption>
```
{
  "and": [
    {
      "property": "Done",
      "checkbox": {
        "equals": true
      }
    },
    {
      "or": [
        {
          "property": "Tags",
          "contains": "A"
        },
        {
          "property": "Tags",
          "contains": "B"
        }
      ]
    }
  ]
}
```
In addition to chained filters, data sources can be queried with single filters.
    {
        "property": "Done",
        "checkbox": {
            "equals": true
       }
     }
[**Sorts**](/reference/sort-data-source-entries) are similar to the [sorts provided in the Notion UI](https://notion.so/notion/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e#0eb303043b1742468e5aff2f3f670505). Sorts operate on database properties or page timestamps and can be combined. The order of the sorts in the request matter, with earlier sorts taking precedence over later ones.
The properties of the data source schema returned in the response body can be filtered with the `filter_properties` query parameter.
    https://api.notion.com/v1/data_sources/[data_source_id]/query?filter_properties=[property_id_1]
Multiple filter properties can be provided by chaining the `filter_properties` query param.
    https://api.notion.com/v1/data_sources/[data_source_id]/query?filter_properties=[property_id_1]&filter_properties=[property_id_2]
Property IDs can be determined with the [Retrieve a data source](/reference/retrieve-a-data-source) endpoint.
If you are using the [Notion JavaScript SDK](https://github.com/makenotion/notion-sdk-js), the `filter_properties` endpoint expects an array of property ID strings.
    notion.dataSources.query({
        data_source_id: id,
        filter_properties: ["propertyID1", "propertyID2"]
    })
> ##
>
> Permissions
>
> Before an integration can query a data source, its parent database must be shared with the integration. Attempting to query a database that has not been shared will return an HTTP response with a 404 status code.
>
> To share a database with an integration, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the integration from the dropdown list.
> ##
>
> Integration capabilities
>
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).
> ##
>
> To display the page titles of related pages rather than just the ID:
>
> 1.  Add a rollup property to the data source which uses a formula to get the related page's title. This works well if you have access to [update](/reference/update-a-data-source) the data source's schema.
>
> 2.  Otherwise, [retrieve the individual related pages](/reference/retrieve-a-page) using each page ID.
> ##
>
> Formula and rollup limitations
>
> - If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
> - Rollups and formulas that depend on multiple layers of relations may not return correct results.
> - Notion recommends individually [retrieving each page property item](/reference/retrieve-a-page-property) to get the most accurate result.
### Errors
Returns a 404 HTTP response if the data source doesn't exist, or if the integration doesn't have access to the data source.
Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*