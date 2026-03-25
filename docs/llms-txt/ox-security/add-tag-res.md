# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/add-tag-res.md

# addTagRes

Response object containing the newly created tags after a tag creation operation.

### Examples

```graphql
type AddTagRes {
  tags: [TagObject!]!
}
```

### Fields

| Field                                                                                                               | Description                        | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tags [`[TagObject!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/tag-object) | Array of newly created tag objects | <p>tagId <code>String!</code><br>name <code>String!</code><br>displayName <code>String!</code><br>tagType <a href="../../../api--application/types/enums/ox-tag-type"><code>OxTagType!</code></a><br>createdBy <code>String!</code><br>createdAt <code>DateTime</code><br>updatedAt <code>DateTime</code><br>tagCategory <code>String</code><br>deploymentModel <code>String</code><br>purpose <code>String</code><br>email <code>String</code></p> |

### References

#### Mutations using this object

* [<\~> addTags](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/add-tags)
