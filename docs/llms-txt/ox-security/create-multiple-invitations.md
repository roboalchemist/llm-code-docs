# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/create-multiple-invitations.md

# createMultipleInvitations

Will create multiple new invitations to the current organization.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation CreateMultipleInvitations($invitationsInfo: [InvitationInput]!) {
  createMultipleInvitations(invitationsInfo: $invitationsInfo) {
    id
    inviteeEmail
    invitation_url
    created_at
    expires_at
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "invitationsInfo": [
    {
      "inviteeEmail": "user@example.com",
      "inviteeRoles": ["example"],
      "scopes": "example",
      "invitationTTLSec": 42
    }
  ]
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
 "query": "mutation CreateMultipleInvitations($invitationsInfo: [InvitationInput]!) { createMultipleInvitations(invitationsInfo: $invitationsInfo) { id inviteeEmail invitation_url created_at expires_at } }",
 "variables": {
    "invitationsInfo": [
      {
        "inviteeEmail": "user@example.com",
        "inviteeRoles": ["example"],
        "scopes": "example",
        "invitationTTLSec": 42
      }
    ]
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation CreateMultipleInvitations($invitationsInfo: [InvitationInput]!) { createMultipleInvitations(invitationsInfo: $invitationsInfo) { id inviteeEmail invitation_url created_at expires_at } }';

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
      invitationsInfo: [
        {
          inviteeEmail: "user@example.com",
          inviteeRoles: ["example"],
          scopes: "example",
          invitationTTLSec: 42
        }
      ]
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

query = 'mutation CreateMultipleInvitations($invitationsInfo: [InvitationInput]!) { createMultipleInvitations(invitationsInfo: $invitationsInfo) { id inviteeEmail invitation_url created_at expires_at } }'

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
      "invitationsInfo": [
        {
          "inviteeEmail": "user@example.com",
          "inviteeRoles": ["example"],
          "scopes": "example",
          "invitationTTLSec": 42
        }
      ]
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

You can use the following argument(s) to customize your `createMultipleInvitations` mutation.

| Argument                                                                                                                                                                                                       | Description                                                             | Supported fields                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| invitationsInfo [`[InvitationInput]!`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/inputs/invitation-input) <mark style="color:red;background-color:red;">required</mark> | List of invitation information, each containing invitee email and roles | <p>inviteeEmail <code>String!</code><br>inviteeRoles <code>\[String]!</code><br>scopes <code>String</code><br>invitationTTLSec <code>Int</code></p> |

### Fields

Return type: [`[Invitation]`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/invitation)

You can use the following field(s) to specify what information your `createMultipleInvitations` mutation will return. Please note that some fields may have their own subfields.

| Field                    | Description                                                    | Supported fields |
| ------------------------ | -------------------------------------------------------------- | ---------------- |
| id `String`              | Unique identifier for the invitation                           |                  |
| inviteeEmail `String`    | Email address of the person receiving the invitation           |                  |
| invitation\_url `String` | Complete URL that the invitee can use to accept the invitation |                  |
| created\_at `String`     | Timestamp when this invitation was created, in ISO 8601 format |                  |
| expires\_at `String`     | Timestamp when this invitation will expire, in ISO 8601 format |                  |
