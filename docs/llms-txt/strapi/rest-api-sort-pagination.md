# REST API: Sort & Pagination

Entries that are returned by queries to the [REST API](/cms/api/rest) can be sorted and paginated.

:::tip

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>

### Example: Sort using 2 fields and set the order

Using the `sort` parameter and defining `:asc` or  `:desc` on sorted fields, you can get results sorted in a particular order.

<br />

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>

## Pagination

Queries can accept `pagination` parameters. Results can be paginated:

- either by [page](#pagination-by-page) (i.e., specifying a page number and the number of entries per page)
- or by [offset](#pagination-by-offset) (i.e., specifying how many entries to skip and to return)

:::note
Pagination methods can not be mixed. Always use either `page` with `pageSize` **or** `start` with `limit`.
:::

### Pagination by page

To paginate results by page, use the following parameters:

| Parameter               | Type    | Description                                                               | Default |
| ----------------------- | ------- | ------------------------------------------------------------------------- | ------- |
| `pagination[page]`      | Integer | Page number                                                               | 1       |
| `pagination[pageSize]`  | Integer | Page size                                                                 | 25      |
| `pagination[withCount]` | Boolean | Adds the total numbers of entries and the number of pages to the response | True    |

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>

### Pagination by offset

To paginate results by offset, use the following parameters:

| Parameter               | Type    | Description                                                    | Default |
| ----------------------- | ------- | -------------------------------------------------------------- | ------- |
| `pagination[start]`     | Integer | Start value (i.e. first entry to return)                      | 0       |
| `pagination[limit]`     | Integer | Number of entries to return                                    | 25      |
| `pagination[withCount]` | Boolean | Toggles displaying the total number of entries to the response | `true`  |

:::tip
The default and maximum values for `pagination[limit]` can be [configured in the `./config/api.js`](/cms/configurations/api) file with the `api.rest.defaultLimit` and `api.rest.maxLimit` keys.
:::

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>