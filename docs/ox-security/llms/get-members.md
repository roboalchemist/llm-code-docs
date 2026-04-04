# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/queries/get-members.md

# getMembers

Will return all members listed for the current org.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetMembers {
  getMembers {
    user_id
    picture
    name
    email
    roles {
      id
      name
      description
      displayName
    }
    scopes
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
 "query": "query GetMembers { getMembers { user_id picture name email roles { id name description displayName } scopes } }"
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetMembers { getMembers { user_id picture name email roles { id name description displayName } scopes } }';

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

query = 'query GetMembers { getMembers { user_id picture name email roles { id name description displayName } scopes } }'

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

Return type: [`[Member]`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/member)

You can use the following field(s) to specify what information your `getMembers` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                           | Description                                                     | Supported fields                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| user\_id `String`                                                                                               | Unique identifier of the user                                   |                                                                                                                                   |
| picture `String`                                                                                                | URL to the user's profile picture                               |                                                                                                                                   |
| name `String`                                                                                                   | Full display name of the user                                   |                                                                                                                                   |
| email `String`                                                                                                  | Email address of the user                                       |                                                                                                                                   |
| roles [`[Role]`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/role) | List of roles assigned to this user within the organization     | <p>id <code>String!</code><br>name <code>String!</code><br>description <code>String</code><br>displayName <code>String</code></p> |
| scopes `String`                                                                                                 | Permission scopes assigned to this user within the organization |                                                                                                                                   |
