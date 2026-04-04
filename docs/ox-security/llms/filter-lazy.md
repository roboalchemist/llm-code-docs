# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy.md

# filterLazy

Lazy-loaded filter category with its items.

### Examples

```graphql
type FilterLazy {
  type: FilterTypes
  items: [FilterInfo]
}
```

### Fields

| Field                                                                                                                       | Description                           | Supported fields                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type [`FilterTypes`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/filter-types)    | Type of filter category               |                                                                                                                                                                                                                                                                                                  |
| items [`[FilterInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-info) | List of filter items in this category | <p>id <code>String</code><br>filterId <code>String</code><br>label <code>String</code><br>count <code>Int</code><br>percent <code>Int</code><br>changeNumber <code>Float</code><br>policyId <code>String</code><br>extraInfo <a href="filter-extra-info"><code>\[FilterExtraInfo]</code></a></p> |

### References

#### Fields with this object

* [{} FilterLazyResponse.filters](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy-response)
