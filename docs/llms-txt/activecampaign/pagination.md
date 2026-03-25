# Source: https://developers.activecampaign.com/reference/pagination.md

# Pagination, Ordering, and Filtering

## Pagination

Endpoints that return collections of resources must limit the number of records returned in a given response. The query parameter `limit` can be used to alter the number of records returned. A typical endpoint will return 20 records by default and will allow a maximum of 100 records to be returned. The query parameter `offset` can be used to offset the result set. These query parameters can be combined to recover all records in a collection through a series of requests by incrementing the `offset` by the value of `limit` with each request.

| Parameter | Description                                                                                                                                                                                                      |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`   | The number of results to display in each page (default = 20; max = 100).                                                                                                                                         |
| `offset`  | The starting point for the result set of a page. This is a zero-based index. For example, if there are 39 total records and the `limit` is the default of 20, use `offset=20` to get the second page of results. |

The total number of results in a collection can be found in the `meta.total` property of the response.

> ❗️ Performance Tip for Pagination and Contacts
>
> When using the [List, Search, and Filter Contacts endpoint (`GET /3/contacts`)](https://developers.activecampaign.com/reference/list-all-contacts), accounts with many Contacts may encounter slower responses when using the `offset` parameter to paginate. For best performance, sort using `orders[id]=ASC` and use the `id_greater` parameter to paginate. `id_greater` is currently only available with the Contacts endpoint.
>
> This is especially important when calling `GET /3/contacts` frequently, such as when retrieving many or all Contacts from an account.

## Ordering

The `orders` parameter is available to apply multiple sorting criteria to a request. The parameter is set as an array where the key is the field to be sorted by and the value is the direction of sort, either `ASC` or `DESC`. Not all fields are available for ordering. The order in which sorting criteria is applied reflects the order in which the parameters are set in the query string. In the example below the results are first sorted by the contacts last name, and then sorted by the contacts email address.

```
GET api/3/contacts?orders[lastName]=ASC&orders[email]=DESC

{
   "contacts": [
       {
           "email": "janderson@example.com",
           "firstName": "John",
           "lastName": "Anderson"
       },
       {
           "email": "banderson@example.com",
           "firstName": "Brian",
           "lastName": "Anderson"
       },
       {
           "email": "alice@example.com",
           "firstName": "Alice",
           "lastName": "Jones"
       }
 ]
}
```

## Filtering

The `filters` query parameter is available to apply multiple, convention oriented filters to a request. The parameter is set as an array where the key is the field to be filtered by and the value is the value to filter by. Not all fields are available for filtering in this way. Field filters will match on “equals” or “contains” on a case by case basis, as configured in the API endpoint. In the example below the results are filtered to goals in automation 5 with a name that contains “ecom”.

```
GET api/3/goals?filters[seriesid]=5&filters[name]=ecom

{
   "goals": [
       {
           "name": "Recommended to Friend",
           "automation": "5"
       },
       {
           "name": "Power Ecom User",
           "automation": "5"
       }
   ]
}
```

## Meta

Metadata can be represented as a top-level member named “meta”. Any information may be provided in the metadata. Its most common use is to return the total number of records when requesting a collection of resources.

```
GET api/3/contacts?limit=2

{
   "contacts": [
       {
           "id": 1,
           "email": "jsmith@example.com",
           "firstName": "John",
           "lastName": "Smith"
       },
       {
           "id": 2,
           "email": "alice@example.com",
           "firstName": "Alice",
           "lastName": "Jones"
       }
 ],
 "meta": {
    "total": 36
  }
}
```