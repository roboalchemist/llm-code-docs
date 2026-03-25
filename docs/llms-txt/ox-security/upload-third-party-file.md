# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/mutations/upload-third-party-file.md

# uploadThirdPartyFile

Upload a file with third party issues for future processing. Returns a requestId that can be used to track the upload status.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation UploadThirdPartyFile($tool: String!, $file: Upload!) {
  uploadThirdPartyFile(tool: $tool, file: $file) {
    requestId
    success
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "tool": "example",
  "file": "example"
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
 "query": "mutation UploadThirdPartyFile($tool: String!, $file: Upload!) { uploadThirdPartyFile(tool: $tool, file: $file) { requestId success } }",
 "variables": {
    "tool": "example",
    "file": "example"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation UploadThirdPartyFile($tool: String!, $file: Upload!) { uploadThirdPartyFile(tool: $tool, file: $file) { requestId success } }';

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
      tool: "example",
      file: "example"
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

query = 'mutation UploadThirdPartyFile($tool: String!, $file: Upload!) { uploadThirdPartyFile(tool: $tool, file: $file) { requestId success } }'

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
      "tool": "example",
      "file": "example"
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

You can use the following argument(s) to customize your `uploadThirdPartyFile` mutation.

| Argument                                                                     | Description                     | Supported fields |
| ---------------------------------------------------------------------------- | ------------------------------- | ---------------- |
| tool `String!` <mark style="color:red;background-color:red;">required</mark> | Tool name used to generate file |                  |
| file `Upload!` <mark style="color:red;background-color:red;">required</mark> |                                 |                  |

### Fields

Return type: [`UploadFileResponse!`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/upload-file-response)

You can use the following field(s) to specify what information your `uploadThirdPartyFile` mutation will return. Please note that some fields may have their own subfields.

| Field               | Description                                       | Supported fields |
| ------------------- | ------------------------------------------------- | ---------------- |
| requestId `String!` | Unique identifier for tracking the upload request |                  |
| success `Boolean!`  | Indicates whether the file upload was successful  |                  |
