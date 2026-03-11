# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/queries/fetch-third-party-issues-file.md

# fetchThirdPartyIssuesFile

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query FetchThirdPartyIssuesFile($requestId: String!) {
  fetchThirdPartyIssuesFile(requestId: $requestId) {
    downloadLink
    isFileReady
    error
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "requestId": "example"
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
 "query": "query FetchThirdPartyIssuesFile($requestId: String!) { fetchThirdPartyIssuesFile(requestId: $requestId) { downloadLink isFileReady error } }",
 "variables": {
    "requestId": "example"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query FetchThirdPartyIssuesFile($requestId: String!) { fetchThirdPartyIssuesFile(requestId: $requestId) { downloadLink isFileReady error } }';

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
      requestId: "example"
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

query = 'query FetchThirdPartyIssuesFile($requestId: String!) { fetchThirdPartyIssuesFile(requestId: $requestId) { downloadLink isFileReady error } }'

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
      "requestId": "example"
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

You can use the following argument(s) to customize your `fetchThirdPartyIssuesFile` query.

| Argument                                                                          | Description                                               | Supported fields |
| --------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------- |
| requestId `String!` <mark style="color:red;background-color:red;">required</mark> | Unique identifier of the file request to check status for |                  |

### Fields

Return type: [`FetchReadyFileResponse!`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/fetch-ready-file-response)

You can use the following field(s) to specify what information your `fetchThirdPartyIssuesFile` query will return. Please note that some fields may have their own subfields.

| Field                  | Description                                                                                          | Supported fields |
| ---------------------- | ---------------------------------------------------------------------------------------------------- | ---------------- |
| downloadLink `String`  | Pre-signed URL for downloading the file. Will be null if the file is not ready or there was an error |                  |
| isFileReady `Boolean!` | Indicates whether the requested file is ready for download                                           |                  |
| error `Boolean`        | Indicates whether an error occurred while checking file status                                       |                  |
