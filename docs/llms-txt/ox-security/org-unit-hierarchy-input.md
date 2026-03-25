# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-input.md

# orgUnitHierarchyInput

### Examples

```graphql
input OrgUnitHierarchyInput {
  orgUnitHierarchy: [OrgUnitHierarchyItemInput!]!
}
```

### Fields

| Field                                                                                                                                                             | Description | Supported fields                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| orgUnitHierarchy [`[OrgUnitHierarchyItemInput!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-item-input) |             | <p>name <code>String!</code><br>tagIds <code>\[ID!]!</code><br>appOwnersEmail <code>\[String!]</code><br>id <code>ID</code><br>parent <code>ID</code><br>children <a href="org-unit-hierarchy-item-input"><code>\[OrgUnitHierarchyItemInput!]!</code></a></p> |

### References

#### Mutations using this object

* [<\~> updateOrgUnitHierarchy.orgUnitHierarchyInput](https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/update-org-unit-hierarchy)
