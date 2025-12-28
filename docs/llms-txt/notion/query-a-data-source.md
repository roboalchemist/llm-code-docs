# Notion API

## Objects

### Block
- [Rich text](/reference/rich-text)

### Page
- [Page properties](/reference/page-property-values)
  - [Page property items](/reference/property-item-object)

### Database
- [Database](/reference/database)

### Data source
- [Data source properties](/reference/data-source)

### Comment
- [Comment attachment](/reference/comment-attachment)
- [Comment display name](/reference/comment-display-name)

### File
- [File Upload](/reference/file-upload)

### User
- [User](/reference/user)

### Parent
- [Parent](/reference/parent-object)

### Emoji
- [Emoji](/reference/emoji-object)

### Unfurl attribute (Link Previews)
- [Unfurl attribute (Link Previews)](/reference/unfurl-attribute-object)

## Endpoints

### Authentication
- [Create a token](/reference/create-a-token) (post)
- [Introspect token](/reference/introspect-token) (post)
- [Revoke token](/reference/revoke-token) (post)
- [Refresh a token](/reference/refresh-a-token) (post)

### Blocks
- [Append block children](/reference/append-block-children) (patch)
- [Retrieve a block](/reference/retrieve-a-block) (get)
- [Retrieve block children](/reference/retrieve-block-children) (get)
- [Update a block](/reference/update-a-block) (patch)
- [Delete a block](/reference/delete-a-block) (del)

### Pages
- [Create a page](/reference/create-a-page) (post)
- [Retrieve a page](/reference/retrieve-a-page) (get)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (get)
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (post)
- [List databases](/reference/list-databases) (get)
- [Delete a database](/reference/delete-database) (del)
```

# Query a data source

## Filter data source entries

[See page](/reference/filter-data-source-entries)

## Sort data source entries

[See page](/reference/sort-data-source-entries)

## List data source templates

[See page](/reference/list-data-source-templates)
```

# Query a data source

## Overview

Gets a list of [pages](/reference/page) contained in the data source, filtered and ordered according to the filter conditions and sort criteria provided in the request. The response may contain fewer than `page_size` of results. If the response includes a `next_cursor` value, refer to the [pagination reference](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.

> **Database, data sources, and wikis**
> 
> [Wiki](https://www.notion.so/help/wikis-and-verified-pages) data sources can contain either pages or databases as children. In all other cases, the children can only be pages.
> 
> For wikis, instead of directly returning any [database](/reference/database) results, this API returns all [data sources](/reference/data-source) that are children of _that_ database. Surfacing the data source instead of the direct database child helps make it easier to craft your next API request (for example, retrieving the data source or listing its children.)
> 
> Another tip for wikis is to use the `result_type` filter of `"page"` or `"data_source"` if you're only looking for query results that are one of those two types instead of both.

## Filtering

[**Filters**](/reference/filter-data-source-entries) are similar to the [filters provided in the Notion UI](https://www.notion.so/help/views-filters-and-sorts) where the set of filters and filter groups chained by "And" in the UI is equivalent to having each filter in the array of the compound `"and"` filter. Similar a set of filters chained by "Or" in the UI would be represented as filters in the array of the `"or"` compound filter.  
Filters operate on data source properties and can be combined. If no filter is provided, all the pages in the data source will be returned with pagination.

![1340](https://files.readme.io/6fe4a44-Screen_Shot_2021-12-23_at_11.46.21_AM.png)

The above filters in the UI can be represented as the following filter object

```json
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

```json
{
    "property": "Done",
    "checkbox": {
        "equals": true
   }
 }
```

## Sorting

[**Sorts**](/reference/sort-data-source-entries) are similar to the [sorts provided in the Notion UI](https://notion.so/notion/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e#0eb303043b1742468e5aff2f3f670505). Sorts operate on database properties or page timestamps and can be combined. The order of the sorts in the request matter, with earlier sorts taking precedence over later ones.

Notion doesn't guarantee any particular sort order when no sort parameters are provided.

## Recommendations for performance

Use the `filter_properties` query parameter to filter only the properties of the data source schema you need from the response items. For example:

```http
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title
```

Multiple filter properties can be provided by chaining the `filter_properties` query param. For example:

```http
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title&filter_properties[]=status
```

This parameter accepts property IDs or property names. Property IDs can be determined with the [Retrieve a data source](/reference/retrieve-a-data-source) endpoint.

If you are using the [Notion JavaScript SDK](https://github.com/makenotion/notion-sdk-js), the `filter_properties` endpoint expects an array of strings. For example:

```typescript
notion.dataSources.query({
	data_source_id: id,
	filter_properties: ["title", "status"]
})
```

Using `filter_properties` can make a significant improvement to the speed of the API and size of the JSON objects in the results, especially for databases with lots of properties, some of which might be rollups, relations, or formulas. If you need additional properties from each returned page, you can make subsequent calls to the [Retrieve page property item](/changelog/retrieve-page-property-values) or [Retrieve a page](/reference/retrieve-a-page) APIs.

If you're still running into long query times with this API, other tips include:

- Using more specific filter conditions to reduce the result set, e.g. a more specific title query or a shorter time window.
- Dividing large data sources (ones with more than several dozen thousand pages) into multiple; e.g. splitting a "tasks" database into "Tasks" and "Bugs".
- Pruning data source schemas to remove any complex formulas, rollups, two-way relations, or other properties that are no longer in use.
- Setting up [integration webhooks](/reference/webhooks) to reduce the need for polling this API by instead automatically notifying your system of incremental workspace events.

For more information, visit our [help center article on optimizing database load times](https://www.notion.com/help/optimize-database-load-times-and-performance).

## Other important details and tips

> **Permissions**
> 
> Before an integration can query a data source, its parent database must be shared with the integration. Attempting to query a database that has not been shared will return an HTTP response with a 404 status code.
> 
> To share a database with an integration, click the ••• menu at the top right of a database page, scroll to `Add connections`, and use the search bar to find and select the integration from the dropdown list.

> **Integration capabilities**
> 
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

> **To display the page titles of related pages rather than just the ID:**
> 
> 1. Add a rollup property to the data source which uses a formula to get the related page's title. This works well if you have access to [update](/reference/update-a-data-source) the data source's schema.
> 2. Otherwise, [retrieve the individual related pages](/reference/retrieve-a-page) using each page ID.

> **Formula and rollup limitations**
> 
> - If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
> - Rollups and formulas that depend on multiple layers of relations may not return correct results.
> - Notion recommends individually [retrieving each page property item](/reference/retrieve-a-page-property) to get the most accurate result.

## Errors

Returns a 404 HTTP response if the data source doesn't exist, or if the integration doesn't have access to the data source.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
```