# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/scan-all.md

# scanAll

Trigger a scan of all configured connectors.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation ScanAll($isFullScan: Boolean, $isContainerFullScan: Boolean, $isExternalToolFullScan: Boolean, $useCustomScannerTag: Boolean) {
  scanAll(isFullScan: $isFullScan, isContainerFullScan: $isContainerFullScan, isExternalToolFullScan: $isExternalToolFullScan, useCustomScannerTag: $useCustomScannerTag) {
    scanID
    isFullScan
    isContainerFullScan
    isSingleRepoScan
    isDastFullScan
    isDastSingleTarget
    scannerTag
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "isFullScan": true,
  "isContainerFullScan": true,
  "isExternalToolFullScan": true,
  "useCustomScannerTag": true
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
 "query": "mutation ScanAll($isFullScan: Boolean, $isContainerFullScan: Boolean, $isExternalToolFullScan: Boolean, $useCustomScannerTag: Boolean) { scanAll(isFullScan: $isFullScan, isContainerFullScan: $isContainerFullScan, isExternalToolFullScan: $isExternalToolFullScan, useCustomScannerTag: $useCustomScannerTag) { scanID isFullScan isContainerFullScan isSingleRepoScan isDastFullScan isDastSingleTarget scannerTag } }",
 "variables": {
    "isFullScan": true,
    "isContainerFullScan": true,
    "isExternalToolFullScan": true,
    "useCustomScannerTag": true
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation ScanAll($isFullScan: Boolean, $isContainerFullScan: Boolean, $isExternalToolFullScan: Boolean, $useCustomScannerTag: Boolean) { scanAll(isFullScan: $isFullScan, isContainerFullScan: $isContainerFullScan, isExternalToolFullScan: $isExternalToolFullScan, useCustomScannerTag: $useCustomScannerTag) { scanID isFullScan isContainerFullScan isSingleRepoScan isDastFullScan isDastSingleTarget scannerTag } }';

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
      isFullScan: true,
      isContainerFullScan: true,
      isExternalToolFullScan: true,
      useCustomScannerTag: true
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

query = 'mutation ScanAll($isFullScan: Boolean, $isContainerFullScan: Boolean, $isExternalToolFullScan: Boolean, $useCustomScannerTag: Boolean) { scanAll(isFullScan: $isFullScan, isContainerFullScan: $isContainerFullScan, isExternalToolFullScan: $isExternalToolFullScan, useCustomScannerTag: $useCustomScannerTag) { scanID isFullScan isContainerFullScan isSingleRepoScan isDastFullScan isDastSingleTarget scannerTag } }'

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
      "isFullScan": true,
      "isContainerFullScan": true,
      "isExternalToolFullScan": true,
      "useCustomScannerTag": true
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

You can use the following argument(s) to customize your `scanAll` mutation.

| Argument                         | Description | Supported fields |
| -------------------------------- | ----------- | ---------------- |
| isFullScan `Boolean`             |             |                  |
| isContainerFullScan `Boolean`    |             |                  |
| isExternalToolFullScan `Boolean` |             |                  |
| useCustomScannerTag `Boolean`    |             |                  |

### Fields

Return type: [`ScanResponse`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/objects/scan-response)

You can use the following field(s) to specify what information your `scanAll` mutation will return. Please note that some fields may have their own subfields.

| Field                         | Description                                                                | Supported fields |
| ----------------------------- | -------------------------------------------------------------------------- | ---------------- |
| scanID `String`               | Unique identifier for tracking the scan progress                           |                  |
| isFullScan `Boolean`          | Indicates if this is a full code scan rather than an incremental scan      |                  |
| isContainerFullScan `Boolean` | Indicates if this is a full container scan rather than an incremental scan |                  |
| isSingleRepoScan `Boolean`    | Indicates if this is a scan of a single repository                         |                  |
| isDastFullScan `Boolean`      | Indicates if this is a full DAST scan rather than an incremental scan      |                  |
| isDastSingleTarget `Boolean`  | Indicates if this is a single DAST target scan                             |                  |
| scannerTag `String`           | Scanner image tag                                                          |                  |
