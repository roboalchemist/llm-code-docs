# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/mutations/reset-issue-owner.md

# resetIssueOwner

Resets the issue owner back to the original automatically calculated owner, removing any manual override.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation ResetIssueOwner($input: ResetIssueOwnerInput!) {
  resetIssueOwner(input: $input)
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "issueId": "30966426-oxPolicy_securityCloudScan_100-example"
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
 "query": "mutation ResetIssueOwner($input: ResetIssueOwnerInput!) { resetIssueOwner(input: $input) }",
 "variables": {
    "input": {
      "issueId": "30966426-oxPolicy_securityCloudScan_100-example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation ResetIssueOwner($input: ResetIssueOwnerInput!) { resetIssueOwner(input: $input) }';

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
        issueId: "30966426-oxPolicy_securityCloudScan_100-example"
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

query = 'mutation ResetIssueOwner($input: ResetIssueOwnerInput!) { resetIssueOwner(input: $input) }'

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
        "issueId": "30966426-oxPolicy_securityCloudScan_100-example"
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

You can use the following argument(s) to customize your `resetIssueOwner` mutation.

| Argument                                                                                                                                                                                                | Description                                                  | Supported fields  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------- |
| input [`ResetIssueOwnerInput!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/reset-issue-owner-input) <mark style="color:red;background-color:red;">required</mark> | Input containing the issue identifier to reset the owner for | issueId `String!` |

### Fields

Return type: `Boolean`
