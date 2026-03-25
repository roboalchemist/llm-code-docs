# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/queries/get-global-roles.md

# getGlobalRoles

Retrieves all available roles that can be assigned to users in the organization.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetGlobalRoles {
  getGlobalRoles {
    id
    name
    description
    displayName
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
 "query": "query GetGlobalRoles { getGlobalRoles { id name description displayName } }"
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetGlobalRoles { getGlobalRoles { id name description displayName } }';

fetch("https://api.cloud.ox.security/api/apollo-gateway", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  body: JSON.stringify({
    query: query
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

query = 'query GetGlobalRoles { getGlobalRoles { id name description displayName } }'

response = requests.post(
  "https://api.cloud.ox.security/api/apollo-gateway",
  headers={
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  json={
    "query": query
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

### Fields

Return type: [`[Role]`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/role)

You can use the following field(s) to specify what information your `getGlobalRoles` query will return. Please note that some fields may have their own subfields.

| Field                | Description                                                | Supported fields |
| -------------------- | ---------------------------------------------------------- | ---------------- |
| id `String!`         | Unique identifier of the role                              |                  |
| name `String!`       | Auth0 name of the role                                     |                  |
| description `String` | Detailed description of the role's purpose and permissions |                  |
| displayName `String` | Human-readable name of the role                            |                  |
