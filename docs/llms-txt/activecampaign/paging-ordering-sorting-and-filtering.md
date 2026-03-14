# Source: https://developers.activecampaign.com/reference/paging-ordering-sorting-and-filtering.md

# Paging, Ordering, Sorting, and Filtering

## Pagination

Endpoints that return collections of resources must limit the number of records returned in a given response. The query parameter `limit` can be used to alter the number of records returned. A typical endpoint will return 20 records by default and will allow a maximum of 100 records to be returned. The query parameter `offset` can be used to offset the result set. These query parameters can be combined to recover all records in a collection through a series of requests by incrementing the `offset` by the value of `limit` with each request.

* `limit`: The number of results to display in each page (default = 20; max = 100).
* `offset`: The starting point for the result set of a page. This is a zero-based index. For example, if there are 39 total records and the `limit` is the default of 20, use `offset=20` to get the second page of results.

The total number of results in a collection can be found in the `meta.total` property of the response.

## Ordering

The `orders` parameter is available to apply multiple sorting criteria to a request. The parameter is set as an array where the key is the field to sort by and the value is the direction of sort, either `ASC` or `DESC`. In the example below the results are first sorted by the schema's label and then sorted by the schema creation timestamp.

```
GET /api/3/customObjects/schemas?orders[labels.singular]=ASC&orders[createdTimestamp]=DESC
```

Please note that in order to sort records by specific field on that record you will have to define what field you want to order by using the field ID. For example, if you have a record `stripe_order` that has a field with an ID of `amount` you would use the following format to order results by that field.

```
GET /api/3/customObjects/records/1111c1f1-a11a-11a1-1111b-c1abc111ab1c?filters[relationships.primary-contact][eq]=14&orders[fields.my-number-field]=DESC
```

## Filtering

* `filters`: All filters will be grouped with **AND** conditions.

### Syntax

Filtering record root level properties

```
?filters[<root_level_property>][<operator>]=<value>
```

Example:

```
?filters[name][contains]=order
```

Filtering Custom Object fields

```
?filters[fields.<field_id>][<operator>]=<value>
```

Example:

```
?filters[fields.amount][gte]=150
```

Filtering Custom Object relationships

```
?filters[relationships.<relationship_name>][<operator>]=<value>
```

Example:

```
?filters[relationships.contacts][eq]=123
```

* The \[\<operator>] section can be omitted in which case the filter will use the default eq operator

### Supported Operators

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Operator
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `eq`
      </td>

      <td>
        Equal
      </td>
    </tr>

    <tr>
      <td>
        `lt`
      </td>

      <td>
        Less than
      </td>
    </tr>

    <tr>
      <td>
        `lte`
      </td>

      <td>
        Less than or equal
      </td>
    </tr>

    <tr>
      <td>
        `gt`
      </td>

      <td>
        Greater than
      </td>
    </tr>

    <tr>
      <td>
        `gte`
      </td>

      <td>
        Greater than or equal
      </td>
    </tr>

    <tr>
      <td>
        `contains`
      </td>

      <td>
        Contains (accepts `*` as a wildcard)
      </td>
    </tr>

    <tr>
      <td>
        `in`
      </td>

      <td>
        In
      </td>
    </tr>

    <tr>
      <td>
        `blank`
      </td>

      <td>
        Mimics "blank" behavior within platform segmentation UI. Below is a list of what `blank` means for each corresponding field type:

        * \*text\*\*: empty string OR no value exists
        * \*text area\*\*: empty string OR no value exists
        * \*drop-down\*\*: no options present
        * \*multi-select\*\*: no options present
        * \*date\*\*: no value exists
        * \*date-time\*\*: no value exists
        * \*number\*\*: no value exists
        * \*currency\*\*: no value exists (for amount)
      </td>
    </tr>

    <tr>
      <td>
        `not_blank`
      </td>

      <td>
        Mimics "not blank" behavior within platform segmentation UI. Below is a list of what `not_blank` means for each corresponding field type:

        * \*text\*\*: value exists AND not empty string
        * \*text area\*\*: value exists AND not empty string
        * \*drop-down\*\*: some sort of option present
        * \*multi-select\*\*: some sort of option present
        * \*date\*\*: some sort of non-null value
        * \*date-time\*\*: some sort of non-null value
        * \*number\*\*: some sort of non-null value
        * \*currency\*\*: some sort of non-null value (for amount)
      </td>
    </tr>
  </tbody>
</Table>