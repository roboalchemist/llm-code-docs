# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/get-app-owners-input.md

# getAppOwnersInput

Input for retrieving application owners, optionally filtered by scan.

### Examples

```graphql
input GetAppOwnersInput {
  scanId: String
}
```

### Fields

| Field           | Description                                               | Supported fields |
| --------------- | --------------------------------------------------------- | ---------------- |
| scanId `String` | Optional scan identifier to filter owners by scan context |                  |

### References

#### Queries using this object

* [\<?> getAppOwners.getAppOwnersInput](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/queries/get-app-owners)
