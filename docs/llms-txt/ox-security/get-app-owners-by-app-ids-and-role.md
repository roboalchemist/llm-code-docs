# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/queries/get-app-owners-by-app-ids-and-role.md

# getAppOwnersByAppIdsAndRole

Retrieve application owners filtered by application IDs and roles.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetAppOwnersByAppIdsAndRole($input: GetAppOwnersByAppIdsAndRoleInput) {
  getAppOwnersByAppIdsAndRole(input: $input) {
    role
    owners {
      name
      email
      appIds
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "appIds": ["30966426"],
    "roles": ["Dev"]
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
 "query": "query GetAppOwnersByAppIdsAndRole($input: GetAppOwnersByAppIdsAndRoleInput) { getAppOwnersByAppIdsAndRole(input: $input) { role owners { name email appIds } } }",
 "variables": {
    "input": {
      "appIds": ["30966426"],
      "roles": ["Dev"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetAppOwnersByAppIdsAndRole($input: GetAppOwnersByAppIdsAndRoleInput) { getAppOwnersByAppIdsAndRole(input: $input) { role owners { name email appIds } } }';

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
      input: {
        appIds: ["30966426"],
        roles: ["Dev"]
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

query = 'query GetAppOwnersByAppIdsAndRole($input: GetAppOwnersByAppIdsAndRoleInput) { getAppOwnersByAppIdsAndRole(input: $input) { role owners { name email appIds } } }'

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
      "input": {
        "appIds": ["30966426"],
        "roles": ["Dev"]
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

You can use the following argument(s) to customize your `getAppOwnersByAppIdsAndRole` query.

| Argument                                                                                                                                                                            | Description                                                            | Supported fields                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`GetAppOwnersByAppIdsAndRoleInput`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/get-app-owners-by-app-ids-and-role-input) | Input parameters specifying application IDs and roles to filter owners | <p>appIds <code>\[String!]!</code><br>roles <a href="../../api--application/types/enums/app-owner-role"><code>\[AppOwnerRole!]!</code></a></p> |

### Fields

Return type: [`[GetAppOwnersByAppIdsAndRoleRes!]`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/get-app-owners-by-app-ids-and-role-res)

You can use the following field(s) to specify what information your `getAppOwnersByAppIdsAndRole` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                              | Description                                | Supported fields                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| role [`AppOwnerRole!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role)       | Role for which owners were retrieved       |                                                                                                   |
| owners [`[AppOwner!]!`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/objects/app-owner) | List of app owners with the specified role | <p>name <code>String!</code><br>email <code>String!</code><br>appIds <code>\[String!]!</code></p> |
