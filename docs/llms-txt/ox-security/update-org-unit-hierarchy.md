# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/update-org-unit-hierarchy.md

# updateOrgUnitHierarchy

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation UpdateOrgUnitHierarchy($orgUnitHierarchyInput: OrgUnitHierarchyInput!) {
  updateOrgUnitHierarchy(orgUnitHierarchyInput: $orgUnitHierarchyInput) {
    name
    tagIds
    appOwnersEmail
    id
    parent
    children {
      name
      tagIds
      appOwnersEmail
      id
      parent
      children {
        name
        tagIds
        appOwnersEmail
        id
        parent
      }
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "orgUnitHierarchyInput": {
    "orgUnitHierarchy": [
      {
        "name": "SomeName",
        "tagIds": ["123"],
        "appOwnersEmail": ["example"],
        "id": "123",
        "parent": "123",
        "children": [
          {
            "name": "SomeName",
            "tagIds": [],
            "appOwnersEmail": [],
            "id": "123",
            "parent": "123",
            "children": []
          }
        ]
      }
    ]
  }
}
```

{% endtab %}

{% tab title="cURL" %}

```shell
curl -X POST \
https://api.cloud.ox.security/api/apollo-gateway \
-H 'Content-Type: application/json' \
-H 'Authorization: YOUR_API_TOKEN' \
-d '{
 "query": "mutation UpdateOrgUnitHierarchy($orgUnitHierarchyInput: OrgUnitHierarchyInput!) { updateOrgUnitHierarchy(orgUnitHierarchyInput: $orgUnitHierarchyInput) { name tagIds appOwnersEmail id parent children { name tagIds appOwnersEmail id parent children { name tagIds appOwnersEmail id parent } } } }",
 "variables": {
    "orgUnitHierarchyInput": {
      "orgUnitHierarchy": [
        {
          "name": "SomeName",
          "tagIds": ["123"],
          "appOwnersEmail": ["example"],
          "id": "123",
          "parent": "123",
          "children": [
            {
              "name": "SomeName",
              "tagIds": [],
              "appOwnersEmail": [],
              "id": "123",
              "parent": "123",
              "children": []
            }
          ]
        }
      ]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation UpdateOrgUnitHierarchy($orgUnitHierarchyInput: OrgUnitHierarchyInput!) { updateOrgUnitHierarchy(orgUnitHierarchyInput: $orgUnitHierarchyInput) { name tagIds appOwnersEmail id parent children { name tagIds appOwnersEmail id parent children { name tagIds appOwnersEmail id parent } } } }';

fetch("https://api.cloud.ox.security/api/apollo-gateway", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  body: JSON.stringify({
    query: query,
    // This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    variables: {
      orgUnitHierarchyInput: {
        orgUnitHierarchy: [
          {
            name: "SomeName",
            tagIds: ["123"],
            appOwnersEmail: ["example"],
            id: "123",
            parent: "123",
            children: [
              {
                name: "SomeName",
                tagIds: [],
                appOwnersEmail: [],
                id: "123",
                parent: "123",
                children: []
              }
            ]
          }
        ]
      }
    }
  })
})
.then(response => response.json())
.then(result => console.log(JSON.stringify(result, null, 2)))
.catch(error => console.error('Error:', error));
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

query = 'mutation UpdateOrgUnitHierarchy($orgUnitHierarchyInput: OrgUnitHierarchyInput!) { updateOrgUnitHierarchy(orgUnitHierarchyInput: $orgUnitHierarchyInput) { name tagIds appOwnersEmail id parent children { name tagIds appOwnersEmail id parent children { name tagIds appOwnersEmail id parent } } } }'

response = requests.post(
  "https://api.cloud.ox.security/api/apollo-gateway",
  headers={
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  json={
    "query": query,
    # This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.
    "variables": {
      "orgUnitHierarchyInput": {
        "orgUnitHierarchy": [
          {
            "name": "SomeName",
            "tagIds": ["123"],
            "appOwnersEmail": ["example"],
            "id": "123",
            "parent": "123",
            "children": [
              {
                "name": "SomeName",
                "tagIds": [],
                "appOwnersEmail": [],
                "id": "123",
                "parent": "123",
                "children": []
              }
            ]
          }
        ]
      }
    }
  }
)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

{% endtab %}
{% endtabs %}

### Arguments

You can use the following argument(s) to customize your `updateOrgUnitHierarchy` mutation.

| Argument                                                                                                                                                                                                                 | Description | Supported fields                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| orgUnitHierarchyInput [`OrgUnitHierarchyInput!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-input) <mark style="color:red;background-color:red;">required</mark> |             | orgUnitHierarchy [`[OrgUnitHierarchyItemInput!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/org-unit-hierarchy-item-input) |

### Fields

Return type: [`[OrgUnitHierarchyItem!]`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/org-unit-hierarchy-item)

You can use the following field(s) to specify what information your `updateOrgUnitHierarchy` mutation will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                           | Description | Supported fields                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name `String!`                                                                                                                                  |             |                                                                                                                                                                                                                                                                     |
| tagIds `[ID!]!`                                                                                                                                 |             |                                                                                                                                                                                                                                                                     |
| appOwnersEmail `[String!]`                                                                                                                      |             |                                                                                                                                                                                                                                                                     |
| id `ID`                                                                                                                                         |             |                                                                                                                                                                                                                                                                     |
| parent `ID`                                                                                                                                     |             |                                                                                                                                                                                                                                                                     |
| children [`[OrgUnitHierarchyItem!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/org-unit-hierarchy-item) |             | <p>name <code>String!</code><br>tagIds <code>\[ID!]!</code><br>appOwnersEmail <code>\[String!]</code><br>id <code>ID</code><br>parent <code>ID</code><br>children <a href="../types/objects/org-unit-hierarchy-item"><code>\[OrgUnitHierarchyItem!]!</code></a></p> |
