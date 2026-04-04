# Source: https://docs.ox.security/api-documentation/api-reference/api--application/mutations/set-priority.md

# setPriority

Sets the business priority level for specified applications.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation SetPriority($priorityInput: PriorityInput!) {
  setPriority(priorityInput: $priorityInput) {
    hasModifiedPriority
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "priorityInput": {
    "priority": 100,
    "appId": ["30966426"]
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
 "query": "mutation SetPriority($priorityInput: PriorityInput!) { setPriority(priorityInput: $priorityInput) { hasModifiedPriority } }",
 "variables": {
    "priorityInput": {
      "priority": 100,
      "appId": ["30966426"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation SetPriority($priorityInput: PriorityInput!) { setPriority(priorityInput: $priorityInput) { hasModifiedPriority } }';

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
      priorityInput: {
        priority: 100,
        appId: ["30966426"]
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

query = 'mutation SetPriority($priorityInput: PriorityInput!) { setPriority(priorityInput: $priorityInput) { hasModifiedPriority } }'

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
      "priorityInput": {
        "priority": 100,
        "appId": ["30966426"]
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

You can use the following argument(s) to customize your `setPriority` mutation.

| Argument                                                                                                                                                                                              | Description                                         | Supported fields                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------ |
| priorityInput [`PriorityInput!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/priority-input) <mark style="color:red;background-color:red;">required</mark> | Input containing priority level and application IDs | <p>priority <code>Int!</code><br>appId <code>\[String]!</code></p> |

### Fields

Return type: [`SetPriorityResponse!`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/set-priority-response)

You can use the following field(s) to specify what information your `setPriority` mutation will return. Please note that some fields may have their own subfields.

| Field                         | Description                                  | Supported fields |
| ----------------------------- | -------------------------------------------- | ---------------- |
| hasModifiedPriority `Boolean` | Whether any priority modifications were made |                  |
