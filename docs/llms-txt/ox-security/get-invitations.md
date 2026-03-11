# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/queries/get-invitations.md

# getInvitations

Will return all Invitation listed for the current Organization.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetInvitations {
  getInvitations {
    id
    inviteeEmail
    invitation_url
    created_at
    expires_at
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
 "query": "query GetInvitations { getInvitations { id inviteeEmail invitation_url created_at expires_at } }"
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetInvitations { getInvitations { id inviteeEmail invitation_url created_at expires_at } }';

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

query = 'query GetInvitations { getInvitations { id inviteeEmail invitation_url created_at expires_at } }'

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

Return type: [`[Invitation]`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/invitation)

You can use the following field(s) to specify what information your `getInvitations` query will return. Please note that some fields may have their own subfields.

| Field                    | Description                                                    | Supported fields |
| ------------------------ | -------------------------------------------------------------- | ---------------- |
| id `String`              | Unique identifier for the invitation                           |                  |
| inviteeEmail `String`    | Email address of the person receiving the invitation           |                  |
| invitation\_url `String` | Complete URL that the invitee can use to accept the invitation |                  |
| created\_at `String`     | Timestamp when this invitation was created, in ISO 8601 format |                  |
| expires\_at `String`     | Timestamp when this invitation will expire, in ISO 8601 format |                  |
