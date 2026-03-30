# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/metadata-entry.md

# metadataEntry

### Examples

```graphql
type MetadataEntry {
  path: [String!]!
  message: String!
}
```

### Fields

| Field             | Description                                                                          | Supported fields |
| ----------------- | ------------------------------------------------------------------------------------ | ---------------- |
| path `[String!]!` | Path of the metadata entry                                                           |                  |
| message `String!` | Value of the metadata entry, may contain error message in case of validation failure |                  |

### References

#### Fields with this object

* [{} ThirdPartyFile.metadata](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/third-party-file)
