# Source: https://docs.ox.security/api-documentation/api-reference/api--organization/mutations/update-member.md

# updateMember

Will update an existing org member.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation UpdateMember($updateMemberInput: UpdateMemberInput) {
  updateMember(updateMemberInput: $updateMemberInput) {
    userId
    roleIDs
    scopes
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "updateMemberInput": {
    "userId": "example",
    "roleIDs": ["example"],
    "scopes": "example"
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
 "query": "mutation UpdateMember($updateMemberInput: UpdateMemberInput) { updateMember(updateMemberInput: $updateMemberInput) { userId roleIDs scopes } }",
 "variables": {
    "updateMemberInput": {
      "userId": "example",
      "roleIDs": ["example"],
      "scopes": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation UpdateMember($updateMemberInput: UpdateMemberInput) { updateMember(updateMemberInput: $updateMemberInput) { userId roleIDs scopes } }';

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
      updateMemberInput: {
        userId: "example",
        roleIDs: ["example"],
        scopes: "example"
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

query = 'mutation UpdateMember($updateMemberInput: UpdateMemberInput) { updateMember(updateMemberInput: $updateMemberInput) { userId roleIDs scopes } }'

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
      "updateMemberInput": {
        "userId": "example",
        "roleIDs": ["example"],
        "scopes": "example"
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

You can use the following argument(s) to customize your `updateMember` mutation.

| Argument                                                                                                                                             | Description | Supported fields                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------- |
| updateMemberInput [`UpdateMemberInput`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/inputs/update-member-input) |             | <p>userId <code>String!</code><br>roleIDs <code>\[String]</code><br>scopes <code>String</code></p> |

### Fields

Return type: [`UpdateMemberResponse`](https://docs.ox.security/api-documentation/api-reference/api--organization/types/objects/update-member-response)

You can use the following field(s) to specify what information your `updateMember` mutation will return. Please note that some fields may have their own subfields.

| Field              | Description                                    | Supported fields |
| ------------------ | ---------------------------------------------- | ---------------- |
| userId `String!`   | user ID                                        |                  |
| roleIDs `[String]` | list of roles assigned for the user            |                  |
| scopes `String`    | list of scopes assigned for the user as string |                  |
