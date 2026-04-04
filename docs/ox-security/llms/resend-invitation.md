# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/resend-invitation.md

# resendInvitation

Will revoke existing invitation and create a new invitation for the user to the current Organization.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation ResendInvitation($invitationId: String!) {
  resendInvitation(invitationId: $invitationId) {
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
  "invitationId": "example"
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
 "query": "mutation ResendInvitation($invitationId: String!) { resendInvitation(invitationId: $invitationId) { id inviteeEmail invitation_url created_at expires_at } }",
 "variables": {
    "invitationId": "example"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation ResendInvitation($invitationId: String!) { resendInvitation(invitationId: $invitationId) { id inviteeEmail invitation_url created_at expires_at } }';

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
      invitationId: "example"
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

query = 'mutation ResendInvitation($invitationId: String!) { resendInvitation(invitationId: $invitationId) { id inviteeEmail invitation_url created_at expires_at } }'

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
      "invitationId": "example"
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

You can use the following argument(s) to customize your `resendInvitation` mutation.

| Argument                                                                             | Description                    | Supported fields |
| ------------------------------------------------------------------------------------ | ------------------------------ | ---------------- |
| invitationId `String!` <mark style="color:red;background-color:red;">required</mark> | ID of the invitation to resend |                  |

### Fields

Return type: [`Invitation`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/invitation)

You can use the following field(s) to specify what information your `resendInvitation` mutation will return. Please note that some fields may have their own subfields.

| Field                    | Description                                                    | Supported fields |
| ------------------------ | -------------------------------------------------------------- | ---------------- |
| id `String`              | Unique identifier for the invitation                           |                  |
| inviteeEmail `String`    | Email address of the person receiving the invitation           |                  |
| invitation\_url `String` | Complete URL that the invitee can use to accept the invitation |                  |
| created\_at `String`     | Timestamp when this invitation was created, in ISO 8601 format |                  |
| expires\_at `String`     | Timestamp when this invitation will expire, in ISO 8601 format |                  |
