# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/get-all-tags-response.md

# getAllTagsResponse

Response object containing an array of tags returned from a query.

### Examples

```graphql
type GetAllTagsResponse {
  tags: [TagObject!]!
}
```

### Fields

| Field                                                                                                               | Description                               | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tags [`[TagObject!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/tag-object) | Array of tags matching the query criteria | <p>tagId <code>String!</code><br>name <code>String!</code><br>displayName <code>String!</code><br>tagType <a href="../../../api--application/types/enums/ox-tag-type"><code>OxTagType!</code></a><br>createdBy <code>String!</code><br>createdAt <code>DateTime</code><br>updatedAt <code>DateTime</code><br>tagCategory <code>String</code><br>deploymentModel <code>String</code><br>purpose <code>String</code><br>email <code>String</code></p> |

### References

#### Queries using this object

* [\<?> getAllTags](https://docs.ox.security/api-documentation/api-reference/api--tags/queries/get-all-tags)
