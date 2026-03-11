# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/mutations/update-issue-severity.md

# updateIssueSeverity

Updates the severity level of a specific security issue. Allows manual adjustment of issue severity based on additional context or analysis.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation UpdateIssueSeverity($input: UpdateIssueSeverityInput!) {
  updateIssueSeverity(input: $input)
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
    "severity": 2
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
 "query": "mutation UpdateIssueSeverity($input: UpdateIssueSeverityInput!) { updateIssueSeverity(input: $input) }",
 "variables": {
    "input": {
      "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
      "severity": 2
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation UpdateIssueSeverity($input: UpdateIssueSeverityInput!) { updateIssueSeverity(input: $input) }';

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
        issueId: "30966426-oxPolicy_securityCloudScan_100-example",
        severity: 2
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

query = 'mutation UpdateIssueSeverity($input: UpdateIssueSeverityInput!) { updateIssueSeverity(input: $input) }'

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
        "issueId": "30966426-oxPolicy_securityCloudScan_100-example",
        "severity": 2
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

You can use the following argument(s) to customize your `updateIssueSeverity` mutation.

| Argument                                                                                                                                                                                                        | Description                                                      | Supported fields                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------- |
| input [`UpdateIssueSeverityInput!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/update-issue-severity-input) <mark style="color:red;background-color:red;">required</mark> | Input containing the issue identifier and the new severity level | <p>issueId <code>String!</code><br>severity <code>Int!</code></p> |

### Fields

Return type: `Boolean`
