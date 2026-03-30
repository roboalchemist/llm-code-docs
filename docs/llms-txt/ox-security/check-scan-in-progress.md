# Source: https://docs.ox.security/api-documentation/api-reference/api--scan/queries/check-scan-in-progress.md

# checkScanInProgress

Check if a scan is currently in progress and get its status.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query CheckScanInProgress {
  checkScanInProgress {
    scanID
    isInProgress
    scanStage
    isFullScan
    isContainerFullScan
    isSingleRepoScan
    isDastFullScan
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
 "query": "query CheckScanInProgress { checkScanInProgress { scanID isInProgress scanStage isFullScan isContainerFullScan isSingleRepoScan isDastFullScan } }"
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query CheckScanInProgress { checkScanInProgress { scanID isInProgress scanStage isFullScan isContainerFullScan isSingleRepoScan isDastFullScan } }';

fetch("https://api.cloud.ox.security/api/apollo-gateway", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  body: JSON.stringify({
    query: query
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

query = 'query CheckScanInProgress { checkScanInProgress { scanID isInProgress scanStage isFullScan isContainerFullScan isSingleRepoScan isDastFullScan } }'

response = requests.post(
  "https://api.cloud.ox.security/api/apollo-gateway",
  headers={
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_TOKEN"
  },
  json={
    "query": query
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

### Fields

Return type: [`ScanInProgressResponse`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/objects/scan-in-progress-response)

You can use the following field(s) to specify what information your `checkScanInProgress` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                              | Description                                                                | Supported fields |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------- |
| scanID `String`                                                                                                    | Unique identifier of the scan                                              |                  |
| isInProgress `Boolean`                                                                                             | Indicates if a scan is currently running                                   |                  |
| scanStage [`ScanStage`](https://docs.ox.security/api-documentation/api-reference/api--scan/types/enums/scan-stage) | Current stage of the scan process                                          |                  |
| isFullScan `Boolean`                                                                                               | Indicates if this is a full code scan rather than an incremental scan      |                  |
| isContainerFullScan `Boolean`                                                                                      | Indicates if this is a full container scan rather than an incremental scan |                  |
| isSingleRepoScan `Boolean`                                                                                         | Indicates if this is a scan of a single repository                         |                  |
| isDastFullScan `Boolean`                                                                                           | Indicates if this is a full DAST scan rather than an incremental scan      |                  |
