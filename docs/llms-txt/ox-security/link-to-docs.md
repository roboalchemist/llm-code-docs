# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/link-to-docs.md

# linkToDocs

Documentation link with title.

### Examples

```graphql
type LinkToDocs {
  href: String!
  title: String!
}
```

### Fields

| Field           | Description                             | Supported fields |
| --------------- | --------------------------------------- | ---------------- |
| href `String!`  | URL of the documentation                |                  |
| title `String!` | Display text for the documentation link |                  |

### References

#### Fields with this object

* [{} ConnectionInstructions.linksToDocs](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connection-instructions)
