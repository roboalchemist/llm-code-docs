# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-item-input.md

# orgUnitHierarchyItemInput

### Examples

```graphql
input OrgUnitHierarchyItemInput {
  name: String!
  tagIds: [ID!]!
  appOwnersEmail: [String!]
  id: ID
  parent: ID
  children: [OrgUnitHierarchyItemInput!]!
}
```

### Fields

| Field                                                                                                                                                     | Description | Supported fields                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name `String!`                                                                                                                                            |             |                                                                                                                                                                                                                                                               |
| tagIds `[ID!]!`                                                                                                                                           |             |                                                                                                                                                                                                                                                               |
| appOwnersEmail `[String!]`                                                                                                                                |             |                                                                                                                                                                                                                                                               |
| id `ID`                                                                                                                                                   |             |                                                                                                                                                                                                                                                               |
| parent `ID`                                                                                                                                               |             |                                                                                                                                                                                                                                                               |
| children [`[OrgUnitHierarchyItemInput!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-item-input) |             | <p>name <code>String!</code><br>tagIds <code>\[ID!]!</code><br>appOwnersEmail <code>\[String!]</code><br>id <code>ID</code><br>parent <code>ID</code><br>children <a href="org-unit-hierarchy-item-input"><code>\[OrgUnitHierarchyItemInput!]!</code></a></p> |

### References

#### Fields with this object

* [{} OrgUnitHierarchyInput.orgUnitHierarchy](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-input)
* [{} OrgUnitHierarchyItemInput.children](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-item-input)
