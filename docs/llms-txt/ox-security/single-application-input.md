# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/single-application-input.md

# singleApplicationInput

Input type for querying a single application, including optional filters and pagination.

### Examples

```graphql
input SingleApplicationInput {
  applicationId: String!
  limit: Int
  offset: Int
  dateRange: DateRange
  scanId: String
}
```

### Fields

| Field                                                                                                                      | Description                                                                             | Supported fields                                        |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| applicationId `String!`                                                                                                    | Unique identifier of the application to retrieve                                        |                                                         |
| limit `Int`                                                                                                                | Maximum number of flow items to return                                                  |                                                         |
| offset `Int`                                                                                                               | Offset for paginated flow items (default is 0)                                          |                                                         |
| dateRange [`DateRange`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/date-range) | Date range filter for retrieving flow items                                             | <p>from <code>Float</code><br>to <code>Float</code></p> |
| scanId `String`                                                                                                            | Optional scan ID to query a specific scan. If not provided, the latest scan ID is used. |                                                         |

### References

#### Queries using this object

* [\<?> getSingleApplicationInfo.getSingleApplicationInput](https://docs.ox.security/api-documentation/api-reference/api--application/queries/get-single-application-info)
