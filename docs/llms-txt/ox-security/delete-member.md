# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/delete-member.md

# deleteMember

Will delete the existing member for the organization.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation DeleteMember($userId: String!, $userEmail: String) {
  deleteMember(userId: $userId, userEmail: $userEmail)
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "userId": "example",
  "userEmail": "example"
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
 "query": "mutation DeleteMember($userId: String!, $userEmail: String) { deleteMember(userId: $userId, userEmail: $userEmail) }",
 "variables": {
    "userId": "example",
    "userEmail": "example"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation DeleteMember($userId: String!, $userEmail: String) { deleteMember(userId: $userId, userEmail: $userEmail) }';

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
      userId: "example",
      userEmail: "example"
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

query = 'mutation DeleteMember($userId: String!, $userEmail: String) { deleteMember(userId: $userId, userEmail: $userEmail) }'

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
      "userId": "example",
      "userEmail": "example"
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

You can use the following argument(s) to customize your `deleteMember` mutation.

| Argument                                                                       | Description | Supported fields |
| ------------------------------------------------------------------------------ | ----------- | ---------------- |
| userId `String!` <mark style="color:red;background-color:red;">required</mark> |             |                  |
| userEmail `String`                                                             |             |                  |

### Fields

Return type: `Boolean`
