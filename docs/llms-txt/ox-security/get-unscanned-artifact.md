# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-unscanned-artifact.md

# getUnscannedArtifact

Retrieves detailed information about a specific unscanned artifact.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetUnscannedArtifact($getUnscannedArtifactInput: GetUnscannedArtifactInput) {
  getUnscannedArtifact(getUnscannedArtifactInput: $getUnscannedArtifactInput) {
    id
    artifactId
    registryType
    registryName
    registryLink
    imageName
    imageTags
    imageCreationDate
    imageDigest
    reason
    error
    scanId
    cloudData {
      cloudIdentifier
      link
      lastExecutionTime
      lastModifiedTime
      account
      zone
      cluster
      cloudDescription {
        type
        subType
        cloudEntityAttributes {
          ... on ECS {
            os
            cpu
            memory
            containers
            registeredAt
            registeredBy
            account
            zone
          }
        }
      }
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getUnscannedArtifactInput": {
    "artifactId": "example"
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
 "query": "query GetUnscannedArtifact($getUnscannedArtifactInput: GetUnscannedArtifactInput) { getUnscannedArtifact(getUnscannedArtifactInput: $getUnscannedArtifactInput) { id artifactId registryType registryName registryLink imageName imageTags imageCreationDate imageDigest reason error scanId cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } } }",
 "variables": {
    "getUnscannedArtifactInput": {
      "artifactId": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetUnscannedArtifact($getUnscannedArtifactInput: GetUnscannedArtifactInput) { getUnscannedArtifact(getUnscannedArtifactInput: $getUnscannedArtifactInput) { id artifactId registryType registryName registryLink imageName imageTags imageCreationDate imageDigest reason error scanId cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } } }';

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
      getUnscannedArtifactInput: {
        artifactId: "example"
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

query = 'query GetUnscannedArtifact($getUnscannedArtifactInput: GetUnscannedArtifactInput) { getUnscannedArtifact(getUnscannedArtifactInput: $getUnscannedArtifactInput) { id artifactId registryType registryName registryLink imageName imageTags imageCreationDate imageDigest reason error scanId cloudData { cloudIdentifier link lastExecutionTime lastModifiedTime account zone cluster cloudDescription { type subType cloudEntityAttributes { ... on ECS { os cpu memory containers registeredAt registeredBy account zone } } } } } }'

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
      "getUnscannedArtifactInput": {
        "artifactId": "example"
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

You can use the following argument(s) to customize your `getUnscannedArtifact` query.

| Argument                                                                                                                                                                  | Description                                     | Supported fields    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------- |
| getUnscannedArtifactInput [`GetUnscannedArtifactInput`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifact-input) | Input to retrieve a specific unscanned artifact | artifactId `String` |

### Fields

Return type: [`UnscannedArtifact`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifact)

You can use the following field(s) to specify what information your `getUnscannedArtifact` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                       | Description                                 | Supported fields                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id `String`                                                                                                                                 | Unique identifier of the unscanned artifact |                                                                                                                                                                                                                                                                                                                                                    |
| artifactId `String`                                                                                                                         | Unique identifier of the artifact           |                                                                                                                                                                                                                                                                                                                                                    |
| registryType `String`                                                                                                                       | Type of the registry                        |                                                                                                                                                                                                                                                                                                                                                    |
| registryName `String`                                                                                                                       | Name of the registry                        |                                                                                                                                                                                                                                                                                                                                                    |
| registryLink `String`                                                                                                                       | Link to the registry                        |                                                                                                                                                                                                                                                                                                                                                    |
| imageName `String`                                                                                                                          | Name of the image                           |                                                                                                                                                                                                                                                                                                                                                    |
| imageTags `[String]`                                                                                                                        | Tags of the image                           |                                                                                                                                                                                                                                                                                                                                                    |
| imageCreationDate `String`                                                                                                                  | Creation date of the image                  |                                                                                                                                                                                                                                                                                                                                                    |
| imageDigest `String`                                                                                                                        | Digest of the image                         |                                                                                                                                                                                                                                                                                                                                                    |
| reason `String`                                                                                                                             | Reason for the unscanned artifact           |                                                                                                                                                                                                                                                                                                                                                    |
| error `String`                                                                                                                              | Error message for the unscanned artifact    |                                                                                                                                                                                                                                                                                                                                                    |
| scanId `String`                                                                                                                             | Scan identifier                             |                                                                                                                                                                                                                                                                                                                                                    |
| cloudData [`[CloudArtifactData]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-artifact-data) | Cloud data for the unscanned artifact       | <p>cloudIdentifier <code>String</code><br>link <code>String</code><br>lastExecutionTime <code>Float</code><br>lastModifiedTime <code>Float</code><br>account <code>String</code><br>zone <code>String</code><br>cluster <code>String</code><br>cloudDescription <a href="../types/objects/cloud-description"><code>CloudDescription</code></a></p> |
