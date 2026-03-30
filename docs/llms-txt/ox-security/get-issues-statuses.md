# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-statuses.md

# getIssuesStatuses

Retrieves the status of multiple issues by checking which collection each exists in. Returns an array of objects with issueId and status. Status can be "Active" if found in current issues, "Resolved" if found in fixed issues or null if not found.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetIssuesStatuses($getIssuesStatusesInput: GetIssueStatusInput!) {
  getIssuesStatuses(getIssuesStatusesInput: $getIssuesStatusesInput) {
    issueId
    status
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getIssuesStatusesInput": {
    "issueIds": ["example"]
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
 "query": "query GetIssuesStatuses($getIssuesStatusesInput: GetIssueStatusInput!) { getIssuesStatuses(getIssuesStatusesInput: $getIssuesStatusesInput) { issueId status } }",
 "variables": {
    "getIssuesStatusesInput": {
      "issueIds": ["example"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetIssuesStatuses($getIssuesStatusesInput: GetIssueStatusInput!) { getIssuesStatuses(getIssuesStatusesInput: $getIssuesStatusesInput) { issueId status } }';

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
      getIssuesStatusesInput: {
        issueIds: ["example"]
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

query = 'query GetIssuesStatuses($getIssuesStatusesInput: GetIssueStatusInput!) { getIssuesStatuses(getIssuesStatusesInput: $getIssuesStatusesInput) { issueId status } }'

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
      "getIssuesStatusesInput": {
        "issueIds": ["example"]
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

You can use the following argument(s) to customize your `getIssuesStatuses` query.

| Argument                                                                                                                                                                                                               | Description                                     | Supported fields      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------------- |
| getIssuesStatusesInput [`GetIssueStatusInput!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issue-status-input) <mark style="color:red;background-color:red;">required</mark> | Input containing the array of issue identifiers | issueIds `[String!]!` |

### Fields

Return type: [`[IssueStatusResult!]!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-status-result)

You can use the following field(s) to specify what information your `getIssuesStatuses` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                     | Description                    | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ---------------- |
| issueId `String!`                                                                                                                         | Unique identifier of the issue |                  |
| status [`IssueCollectionStatus`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issue-collection-status) | Status of the issue            |                  |
