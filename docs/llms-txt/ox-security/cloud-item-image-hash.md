# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item-image-hash.md

# cloudItemImageHash

Defines hash information for container images.

### Examples

```graphql
type CloudItemImageHash {
  hash: String
  isFromRegistry: Boolean
}
```

### Fields

| Field                    | Description                                   | Supported fields |
| ------------------------ | --------------------------------------------- | ---------------- |
| hash `String`            | SHA hash of the container image               |                  |
| isFromRegistry `Boolean` | Whether the hash is from a container registry |                  |

### References

#### Fields with this object

* [{} CloudItemImage.hashes](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item-image)
