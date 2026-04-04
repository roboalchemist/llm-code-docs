# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/queries/fetch-list-of-third-party-issue-files.md

# fetchListOfThirdPartyIssueFiles

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query FetchListOfThirdPartyIssueFiles($requestId: String, $tool: String) {
  fetchListOfThirdPartyIssueFiles(requestId: $requestId, tool: $tool) {
    files {
      requestId
      tool
      status
      metadata {
        path
        message
      }
    }
    error
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "requestId": "example",
  "tool": "example"
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
 "query": "query FetchListOfThirdPartyIssueFiles($requestId: String, $tool: String) { fetchListOfThirdPartyIssueFiles(requestId: $requestId, tool: $tool) { files { requestId tool status metadata { path message } } error } }",
 "variables": {
    "requestId": "example",
    "tool": "example"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query FetchListOfThirdPartyIssueFiles($requestId: String, $tool: String) { fetchListOfThirdPartyIssueFiles(requestId: $requestId, tool: $tool) { files { requestId tool status metadata { path message } } error } }';

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
      requestId: "example",
      tool: "example"
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

query = 'query FetchListOfThirdPartyIssueFiles($requestId: String, $tool: String) { fetchListOfThirdPartyIssueFiles(requestId: $requestId, tool: $tool) { files { requestId tool status metadata { path message } } error } }'

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
      "requestId": "example",
      "tool": "example"
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

You can use the following argument(s) to customize your `fetchListOfThirdPartyIssueFiles` query.

| Argument           | Description                              | Supported fields |
| ------------------ | ---------------------------------------- | ---------------- |
| requestId `String` | Unique identifier for the file request   |                  |
| tool `String`      | Tool name which was used for file upload |                  |

### Fields

Return type: [`FetchThirdPartyFileListResponse!`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/fetch-third-party-file-list-response)

You can use the following field(s) to specify what information your `fetchListOfThirdPartyIssueFiles` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                   | Description            | Supported fields                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| files [`[ThirdPartyFile!]`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/third-party-file) | List of uploaded files | <p>requestId <code>String!</code><br>tool <code>String!</code><br>status <code>String!</code><br>metadata <a href="../types/objects/metadata-entry"><code>\[MetadataEntry!]</code></a></p> |
| error `Boolean`                                                                                                                         |                        |                                                                                                                                                                                            |
