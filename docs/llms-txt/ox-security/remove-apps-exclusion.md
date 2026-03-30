# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/remove-apps-exclusion.md

# removeAppsExclusion

Remove multiple application exclusions.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation RemoveAppsExclusion($input: RemoveAppsExclusionInput!) {
  removeAppsExclusion(input: $input) {
    removeAppsExclusion {
      isSucceeded
      exclusionId
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "relevance": "Irrelevant",
    "exclusionIds": ["example"]
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
 "query": "mutation RemoveAppsExclusion($input: RemoveAppsExclusionInput!) { removeAppsExclusion(input: $input) { removeAppsExclusion { isSucceeded exclusionId } } }",
 "variables": {
    "input": {
      "relevance": "Irrelevant",
      "exclusionIds": ["example"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation RemoveAppsExclusion($input: RemoveAppsExclusionInput!) { removeAppsExclusion(input: $input) { removeAppsExclusion { isSucceeded exclusionId } } }';

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
      input: {
        relevance: "Irrelevant",
        exclusionIds: ["example"]
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

query = 'mutation RemoveAppsExclusion($input: RemoveAppsExclusionInput!) { removeAppsExclusion(input: $input) { removeAppsExclusion { isSucceeded exclusionId } } }'

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
      "input": {
        "relevance": "Irrelevant",
        "exclusionIds": ["example"]
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

You can use the following argument(s) to customize your `removeAppsExclusion` mutation.

| Argument                                                                                                                                                                                                             | Description                         | Supported fields                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`RemoveAppsExclusionInput!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/remove-apps-exclusion-input) <mark style="color:red;background-color:red;">required</mark> | Details of the exclusions to remove | <p>relevance <a href="../types/enums/exclusion-relevance"><code>ExclusionRelevance!</code></a><br>exclusionIds <code>\[String!]!</code></p> |

### Fields

Return type: [`RemoveAppsExclusionRes`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/remove-apps-exclusion-res)

You can use the following field(s) to specify what information your `removeAppsExclusion` mutation will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                         | Description | Supported fields                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------- |
| removeAppsExclusion [`[RemoveAppSingleExclusionRes]`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/remove-app-single-exclusion-res) |             | <p>isSucceeded <code>Boolean!</code><br>exclusionId <code>String</code></p> |
