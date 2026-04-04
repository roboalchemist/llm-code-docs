# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/verify-single-connector-credentials.md

# verifySingleConnectorCredentials

Verifies credentials for a specific connector.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation VerifySingleConnectorCredentials($verifyCredentialsInput: VerifyCredentialsInput!) {
  verifySingleConnectorCredentials(verifyCredentialsInput: $verifyCredentialsInput) {
    credentialsAreValid
    noReposFound
    validationMessage
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "verifyCredentialsInput": {
    "connectorID": "2",
    "credentialsID": "example",
    "featureFlags": "example"
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
 "query": "mutation VerifySingleConnectorCredentials($verifyCredentialsInput: VerifyCredentialsInput!) { verifySingleConnectorCredentials(verifyCredentialsInput: $verifyCredentialsInput) { credentialsAreValid noReposFound validationMessage } }",
 "variables": {
    "verifyCredentialsInput": {
      "connectorID": "2",
      "credentialsID": "example",
      "featureFlags": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation VerifySingleConnectorCredentials($verifyCredentialsInput: VerifyCredentialsInput!) { verifySingleConnectorCredentials(verifyCredentialsInput: $verifyCredentialsInput) { credentialsAreValid noReposFound validationMessage } }';

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
      verifyCredentialsInput: {
        connectorID: "2",
        credentialsID: "example",
        featureFlags: "example"
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

query = 'mutation VerifySingleConnectorCredentials($verifyCredentialsInput: VerifyCredentialsInput!) { verifySingleConnectorCredentials(verifyCredentialsInput: $verifyCredentialsInput) { credentialsAreValid noReposFound validationMessage } }'

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
      "verifyCredentialsInput": {
        "connectorID": "2",
        "credentialsID": "example",
        "featureFlags": "example"
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

You can use the following argument(s) to customize your `verifySingleConnectorCredentials` mutation.

| Argument                                                                                                                                                                                                                         | Description | Supported fields                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| verifyCredentialsInput [`VerifyCredentialsInput!`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/verify-credentials-input) <mark style="color:red;background-color:red;">required</mark> |             | <p>connectorID <code>String!</code><br>credentialsID <code>String</code><br>featureFlags <code>JSON</code></p> |

### Fields

Return type: [`VerifySingleCredentialsResponse`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/verify-single-credentials-response)

You can use the following field(s) to specify what information your `verifySingleConnectorCredentials` mutation will return. Please note that some fields may have their own subfields.

| Field                          | Description | Supported fields |
| ------------------------------ | ----------- | ---------------- |
| credentialsAreValid `Boolean!` |             |                  |
| noReposFound `Boolean!`        |             |                  |
| validationMessage `String`     |             |                  |
