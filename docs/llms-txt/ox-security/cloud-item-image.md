# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item-image.md

# cloudItemImage

Represents container image information associated with cloud resources.

### Examples

```graphql
type CloudItemImage {
  name: String
  hashes: [CloudItemImageHash]
  tags: [String]
}
```

### Fields

| Field                                                                                                                                             | Description                                    | Supported fields                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------- |
| name `String`                                                                                                                                     | Name of the container image                    |                                                                        |
| hashes [`[CloudItemImageHash]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item-image-hash) | List of image hashes with registry information | <p>hash <code>String</code><br>isFromRegistry <code>Boolean</code></p> |
| tags `[String]`                                                                                                                                   | Tags associated with the container image       |                                                                        |

### References

#### Fields with this object

* [{} CloudItem.images](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
