# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/mutations/set-app-owners.md

# setAppOwners

Set or update application owners with their respective roles.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation SetAppOwners($input: SetApplicationsOwnersByRoleInput!) {
  setAppOwners(input: $input) {
    acknowledge
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "ownersByRoleInput": [
      {
        "role": "Dev",
        "owners": [
          {
            "name": "SomeName",
            "email": "user@example.com",
            "appIds": ["30966426"]
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
 "query": "mutation SetAppOwners($input: SetApplicationsOwnersByRoleInput!) { setAppOwners(input: $input) { acknowledge } }",
 "variables": {
    "input": {
      "ownersByRoleInput": [
        {
          "role": "Dev",
          "owners": [
            {
              "name": "SomeName",
              "email": "user@example.com",
              "appIds": ["30966426"]
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
const query = 'mutation SetAppOwners($input: SetApplicationsOwnersByRoleInput!) { setAppOwners(input: $input) { acknowledge } }';

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
        ownersByRoleInput: [
          {
            role: "Dev",
            owners: [
              {
                name: "SomeName",
                email: "user@example.com",
                appIds: ["30966426"]
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

query = 'mutation SetAppOwners($input: SetApplicationsOwnersByRoleInput!) { setAppOwners(input: $input) { acknowledge } }'

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
        "ownersByRoleInput": [
          {
            "role": "Dev",
            "owners": [
              {
                "name": "SomeName",
                "email": "user@example.com",
                "appIds": ["30966426"]
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

You can use the following argument(s) to customize your `setAppOwners` mutation.

| Argument                                                                                                                                                                                                                                        | Description                                                          | Supported fields                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`SetApplicationsOwnersByRoleInput!`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/set-applications-owners-by-role-input) <mark style="color:red;background-color:red;">required</mark> | Input containing owner assignments with their roles for applications | ownersByRoleInput [`[OwnersByRoleInput!]!`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/owners-by-role-input) |

### Fields

Return type: [`Acknowledge!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/acknowledge)

You can use the following field(s) to specify what information your `setAppOwners` mutation will return. Please note that some fields may have their own subfields.

| Field                  | Description                                        | Supported fields |
| ---------------------- | -------------------------------------------------- | ---------------- |
| acknowledge `Boolean!` | Boolean indicating if the operation was successful |                  |
