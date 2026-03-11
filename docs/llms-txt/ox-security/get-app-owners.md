# Source: https://docs.ox.security/api-documentation/api-reference/api--applications-owners/queries/get-app-owners.md

# getAppOwners

Retrieves a list of application owners and their roles within the organization. Useful for managing access control and responsibility assignments.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetAppOwners($getAppOwnersInput: GetAppOwnersInput) {
  getAppOwners(getAppOwnersInput: $getAppOwnersInput) {
    name
    email
    roles
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getAppOwnersInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
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
 "query": "query GetAppOwners($getAppOwnersInput: GetAppOwnersInput) { getAppOwners(getAppOwnersInput: $getAppOwnersInput) { name email roles } }",
 "variables": {
    "getAppOwnersInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetAppOwners($getAppOwnersInput: GetAppOwnersInput) { getAppOwners(getAppOwnersInput: $getAppOwnersInput) { name email roles } }';

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
      getAppOwnersInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
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

query = 'query GetAppOwners($getAppOwnersInput: GetAppOwnersInput) { getAppOwners(getAppOwnersInput: $getAppOwnersInput) { name email roles } }'

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
      "getAppOwnersInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99"
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

You can use the following argument(s) to customize your `getAppOwners` query.

| Argument                                                                                                                                                     | Description                                                                 | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ---------------- |
| getAppOwnersInput [`GetAppOwnersInput`](https://docs.ox.security/api-documentation/api-reference/api--applications-owners/types/inputs/get-app-owners-input) | Parameters to filter the list of application owners, optionally by scan ID. | scanId `String`  |

### Fields

Return type: [`[OwnerInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/owner-info)

You can use the following field(s) to specify what information your `getAppOwners` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                          | Description                  | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ---------------- |
| name `String`                                                                                                                  | Name of the owner            |                  |
| email `String`                                                                                                                 | Email address of the owner   |                  |
| roles [`[AppOwnerRole]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-owner-role) | Roles assigned to this owner |                  |
