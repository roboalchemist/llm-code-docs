# Document Service API: Sorting and paginating results

The [Document Service API](/cms/api/document-service) offers the ability to sort and paginate query results.

## Sort

To sort results returned by the Document Service API, include the `sort` parameter with queries.

### Sort on a single field

To sort results based on a single field:

</ApiCall>

### Sort on multiple fields

To sort on multiple fields, pass them all in an array:

</ApiCall>

## Pagination

To paginate results, pass the `limit` and `start` parameters:

</ApiCall>