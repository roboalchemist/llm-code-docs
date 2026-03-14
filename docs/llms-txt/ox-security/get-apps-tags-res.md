# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/get-apps-tags-res.md

# getAppsTagsRes

Response type containing a list of application tags.

### Examples

```graphql
type GetAppsTagsRes {
  appsTags: [AppTagObject!]!
}
```

### Fields

| Field                                                                                                                          | Description                                          | Supported fields                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appsTags [`[AppTagObject!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/app-tag-object) | List of application tags matching the query criteria | <p>tagType <a href="../../../api--application/types/enums/ox-tag-type"><code>OxTagType!</code></a><br>appId <code>String!</code><br>tagId <code>String!</code><br>appliedBy <code>String</code><br>roles <a href="../../../api--application/types/enums/app-owner-role"><code>\[AppOwnerRole!]</code></a><br>tag <a href="tag-object"><code>TagObject</code></a></p> |

### References

#### Queries using this object

* [\<?> getAppTags](https://docs.ox.security/api-documentation/api-reference/api--tags/queries/get-app-tags)
