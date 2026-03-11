# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/org-unit-hierarchy-item.md

# orgUnitHierarchyItem

### Examples

```graphql
type OrgUnitHierarchyItem {
  name: String!
  tagIds: [ID!]!
  appOwnersEmail: [String!]
  id: ID
  parent: ID
  children: [OrgUnitHierarchyItem!]!
}
```

### Fields

| Field                                                                                                                                           | Description | Supported fields                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name `String!`                                                                                                                                  |             |                                                                                                                                                                                                                                                    |
| tagIds `[ID!]!`                                                                                                                                 |             |                                                                                                                                                                                                                                                    |
| appOwnersEmail `[String!]`                                                                                                                      |             |                                                                                                                                                                                                                                                    |
| id `ID`                                                                                                                                         |             |                                                                                                                                                                                                                                                    |
| parent `ID`                                                                                                                                     |             |                                                                                                                                                                                                                                                    |
| children [`[OrgUnitHierarchyItem!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/org-unit-hierarchy-item) |             | <p>name <code>String!</code><br>tagIds <code>\[ID!]!</code><br>appOwnersEmail <code>\[String!]</code><br>id <code>ID</code><br>parent <code>ID</code><br>children <a href="org-unit-hierarchy-item"><code>\[OrgUnitHierarchyItem!]!</code></a></p> |

### References

#### Mutations using this object

* [<\~> updateOrgUnitHierarchy](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/update-org-unit-hierarchy)

#### Fields with this object

* [{} OrgUnitHierarchyItem.children](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/org-unit-hierarchy-item)
