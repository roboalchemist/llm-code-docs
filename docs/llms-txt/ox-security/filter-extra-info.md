# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-extra-info.md

# filterExtraInfo

Additional metadata for filter information.

### Examples

```graphql
type FilterExtraInfo {
  key: String
  value: String
}
```

### Fields

| Field          | Description    | Supported fields |
| -------------- | -------------- | ---------------- |
| key `String`   | Metadata key   |                  |
| value `String` | Metadata value |                  |

### References

#### Fields with this object

* [{} FilterInfo.extraInfo](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-info)
