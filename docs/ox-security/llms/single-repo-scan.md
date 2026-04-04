# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/mutations/single-repo-scan.md

# singleRepoScan

Trigger a scan for specific repositories.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation SingleRepoScan($singleRepoScanInput: SingleRepoScanInput) {
  singleRepoScan(singleRepoScanInput: $singleRepoScanInput) {
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
  "singleRepoScanInput": {
    "applications": [
      {
        "appId": "30966426",
        "appName": "My Application",
        "connectorId": "2",
        "credentialsId": "example"
      }
    ]
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
 "query": "mutation SingleRepoScan($singleRepoScanInput: SingleRepoScanInput) { singleRepoScan(singleRepoScanInput: $singleRepoScanInput) { scanID isFullScan isContainerFullScan isSingleRepoScan isDastFullScan isDastSingleTarget scannerTag } }",
 "variables": {
    "singleRepoScanInput": {
      "applications": [
        {
          "appId": "30966426",
          "appName": "My Application",
          "connectorId": "2",
          "credentialsId": "example"
        }
      ]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation SingleRepoScan($singleRepoScanInput: SingleRepoScanInput) { singleRepoScan(singleRepoScanInput: $singleRepoScanInput) { scanID isFullScan isContainerFullScan isSingleRepoScan isDastFullScan isDastSingleTarget scannerTag } }';

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
      singleRepoScanInput: {
        applications: [
          {
            appId: "30966426",
            appName: "My Application",
            connectorId: "2",
            credentialsId: "example"
          }
        ]
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

query = 'mutation SingleRepoScan($singleRepoScanInput: SingleRepoScanInput) { singleRepoScan(singleRepoScanInput: $singleRepoScanInput) { scanID isFullScan isContainerFullScan isSingleRepoScan isDastFullScan isDastSingleTarget scannerTag } }'

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
      "singleRepoScanInput": {
        "applications": [
          {
            "appId": "30966426",
            "appName": "My Application",
            "connectorId": "2",
            "credentialsId": "example"
          }
        ]
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

You can use the following argument(s) to customize your `singleRepoScan` mutation.

| Argument                                                                                                                                            | Description | Supported fields                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| singleRepoScanInput [`SingleRepoScanInput`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/single-repo-scan-input) |             | applications [`[ApplicationToScanInput]!`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/inputs/application-to-scan-input) |

### Fields

Return type: [`ScanResponse`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/objects/scan-response)

You can use the following field(s) to specify what information your `singleRepoScan` mutation will return. Please note that some fields may have their own subfields.

| Field                         | Description                                                                | Supported fields |
| ----------------------------- | -------------------------------------------------------------------------- | ---------------- |
| scanID `String`               | Unique identifier for tracking the scan progress                           |                  |
| isFullScan `Boolean`          | Indicates if this is a full code scan rather than an incremental scan      |                  |
| isContainerFullScan `Boolean` | Indicates if this is a full container scan rather than an incremental scan |                  |
| isSingleRepoScan `Boolean`    | Indicates if this is a scan of a single repository                         |                  |
| isDastFullScan `Boolean`      | Indicates if this is a full DAST scan rather than an incremental scan      |                  |
| isDastSingleTarget `Boolean`  | Indicates if this is a single DAST target scan                             |                  |
| scannerTag `String`           | Scanner image tag                                                          |                  |
