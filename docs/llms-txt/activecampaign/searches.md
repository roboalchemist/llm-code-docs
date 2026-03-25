# Source: https://developers.activecampaign.com/reference/searches.md

# Searches

The ActiveCampaign Ecommerce GraphQL API contains search operations for its various object types.

A search request has two components: pagination info and filters.

## Pagination

The pagination object is in the following format:

| Attribute Name | Description                                                                                                                                                               |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| offset(`Int`)  | The offset of the page. For example, an offset of 10 will cause the page to start at the 10th object returned for the result set. Must be `&gt;= 0`. **Default Value**: 0 |
| limit(`Int`)   | The number of objects to return. Must be `&gt;0` and `&lt;=100` **Default Value**: 20                                                                                     |

## Filters

By default, all results for an object (for example, all orders) will be returned by a search request. To return specific results, apply filters. Filters are applied based on the fields in the object being searched. For a full list of searchable fields per object type, check the search request documentation for that object type. For example, OrderSearchRequest.

When multiple filters are applied, the result is a logical intersection (also known as `AND`) of the filter results.

All filters follow the format:

| Name                   | Description                                                                                                                                                                                          |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filterOperator(`Enum`) | The operator to be applied to the value. Must be one of:  `EQ, LT, LTE, GT, GTE, CONTAINS, IN`                                                                                                       |
| value (`Object`)       | A value to perform the filterOperator on. This is strongly typed. The type of this value will match [the type of the filter](https://developers.activecampaign.com/reference/searches#filter-types). |
| sort(`enum`)           | How results should be sorted. Must be one of: `ASC, DESC`. **Default Value**: ASC                                                                                                                    |

If a filter has a `value` populated, it requires a `filterOperator`.

A `sort` may be applied to a field without a `value` or `filterOperator`.

### Search Request Examples

This order search request will find the first 20 orders (the default page size) for `legacyConnectionId` 21. Note that `value` on the `legacyConnectionId` filter is an integer.

```json
{  
  searchOrder (filter: {
     legacyConnectionId: {
         value: 21
         filterOperator: EQ
     }
  })
  {
    id
  }
}
```

This order search request will find 20 orders placed by email addresses containing the string "gmail". It will sort the results by email in ascending order. Note that `value` on the `email` filter is a string.

```json
{  
  searchOrder (filter: {  
    email: {
        value: "gmail"
        filterOperator: CONTAINS
        sort: ASC
    }
  })  
  {  
    id  
  }  
}
```

This order search request will return the 50th through 60th orders sorted by orderNumber in descending order. It will exclude test orders.

```json
{  
  searchOrder (filter: {
    pagination: {
      offset: 50
      limit: 10
    }
    orderNumber: {
      sort: DESC
    }
    isTestOrder: {
      value: false
      filterOperator: EQ
    }
  })  
  {  
    orderNumber
  }  
}
```

### Filter Types

Depending on field types, the following filter type objects are available. All are identical except for the type of the `value` field.

Depending on the type, only certain filterOperators are valid, as specified below:

| Filter Object Type | Type of `value` field                                                                              | Available `filterOperators` |
| :----------------- | :------------------------------------------------------------------------------------------------- | :-------------------------- |
| BooleanFieldFilter | Boolean                                                                                            | EQ                          |
| StringFieldFilter  | String                                                                                             | EQ, CONTAINS                |
| NumberFieldFilter  | Decimal                                                                                            | EQ, LT, LTE, GT, GTE        |
| IntFieldFilter     | Integer                                                                                            | EQ, LT, LTE, GT, GTE        |
| Enum               | Corresponding Enum type                                                                            | EQ                          |
| AddressFilter      | See: [AddressFilter](https://developers.activecampaign.com/reference/shared-objects#addressfilter) |                             |