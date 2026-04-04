# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issue-graph.md

# getIssueGraph

Retrieves a graph representation of an issue showing its relationships with various entities, dependencies, and related components.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetIssueGraph($issueId: String!) {
  getIssueGraph(issueId: $issueId) {
    nodes {
      id
      type
      metaData
    }
    edges {
      id
      type
      metaData
      target
      source
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "issueId": "30966426-oxPolicy_securityCloudScan_100-example"
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
 "query": "query GetIssueGraph($issueId: String!) { getIssueGraph(issueId: $issueId) { nodes { id type metaData } edges { id type metaData target source } } }",
 "variables": {
    "issueId": "30966426-oxPolicy_securityCloudScan_100-example"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetIssueGraph($issueId: String!) { getIssueGraph(issueId: $issueId) { nodes { id type metaData } edges { id type metaData target source } } }';

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
      issueId: "30966426-oxPolicy_securityCloudScan_100-example"
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

query = 'query GetIssueGraph($issueId: String!) { getIssueGraph(issueId: $issueId) { nodes { id type metaData } edges { id type metaData target source } } }'

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
      "issueId": "30966426-oxPolicy_securityCloudScan_100-example"
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

You can use the following argument(s) to customize your `getIssueGraph` query.

| Argument                                                                        | Description                                              | Supported fields |
| ------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------- |
| issueId `String!` <mark style="color:red;background-color:red;">required</mark> | Unique identifier of the issue to generate the graph for |                  |

### Fields

Return type: [`IssueGraph!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-graph)

You can use the following field(s) to specify what information your `getIssueGraph` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                      | Description                                                             | Supported fields                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nodes [`[Node!]!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/node) | List of nodes representing various entities in the issue graph          | <p>id <code>Float!</code><br>type <a href="../types/enums/node-type"><code>NodeType!</code></a><br>metaData <code>JSON!</code></p>                                                            |
| edges [`[Edge!]!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/edge) | List of edges representing connections between nodes in the issue graph | <p>id <code>Float!</code><br>type <a href="../types/enums/edge-type"><code>EdgeType!</code></a><br>metaData <code>JSON</code><br>target <code>Float!</code><br>source <code>Float!</code></p> |
