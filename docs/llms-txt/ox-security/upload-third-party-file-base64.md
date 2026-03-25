# Source: https://docs.ox.security/api-documentation/api-reference/api--file-download/mutations/upload-third-party-file-base64.md

# uploadThirdPartyFileBase64

Upload a file with third party issues for future processing. Returns a requestId that can be used to track the upload status.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation UploadThirdPartyFileBase64($data: String!, $tool: String!, $fileType: ThirdPartyUploadDataType) {
  uploadThirdPartyFileBase64(data: $data, tool: $tool, fileType: $fileType) {
    requestId
    success
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "data": "example",
  "tool": "example",
  "fileType": "JSON"
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
 "query": "mutation UploadThirdPartyFileBase64($data: String!, $tool: String!, $fileType: ThirdPartyUploadDataType) { uploadThirdPartyFileBase64(data: $data, tool: $tool, fileType: $fileType) { requestId success } }",
 "variables": {
    "data": "example",
    "tool": "example",
    "fileType": "JSON"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation UploadThirdPartyFileBase64($data: String!, $tool: String!, $fileType: ThirdPartyUploadDataType) { uploadThirdPartyFileBase64(data: $data, tool: $tool, fileType: $fileType) { requestId success } }';

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
      data: "example",
      tool: "example",
      fileType: "JSON"
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

query = 'mutation UploadThirdPartyFileBase64($data: String!, $tool: String!, $fileType: ThirdPartyUploadDataType) { uploadThirdPartyFileBase64(data: $data, tool: $tool, fileType: $fileType) { requestId success } }'

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
      "data": "example",
      "tool": "example",
      "fileType": "JSON"
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

You can use the following argument(s) to customize your `uploadThirdPartyFileBase64` mutation.

| Argument                                                                                                                                                    | Description                                                            | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------- |
| data `String!` <mark style="color:red;background-color:red;">required</mark>                                                                                | File content to upload, must be encoded as base64                      |                  |
| tool `String!` <mark style="color:red;background-color:red;">required</mark>                                                                                | Tool Name                                                              |                  |
| fileType [`ThirdPartyUploadDataType`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/enums/third-party-upload-data-type) | Type of file being uploaded. If not specified, defaults to Policy file |                  |

### Fields

Return type: [`UploadFileResponse!`](https://docs.ox.security/api-documentation/api-reference/api--file-download/types/objects/upload-file-response)

You can use the following field(s) to specify what information your `uploadThirdPartyFileBase64` mutation will return. Please note that some fields may have their own subfields.

| Field               | Description                                       | Supported fields |
| ------------------- | ------------------------------------------------- | ---------------- |
| requestId `String!` | Unique identifier for tracking the upload request |                  |
| success `Boolean!`  | Indicates whether the file upload was successful  |                  |
