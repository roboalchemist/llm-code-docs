# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/modify-apps-tags.md

# modifyAppsTags

Modify tags associated with applications by adding and/or removing tags.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation ModifyAppsTags($input: ModifyAppsTagsInput!) {
  modifyAppsTags(input: $input) {
    acknowledge
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "appIds": ["30966426"],
    "addedTagsIds": ["example"],
    "removedTagsIds": ["example"]
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
 "query": "mutation ModifyAppsTags($input: ModifyAppsTagsInput!) { modifyAppsTags(input: $input) { acknowledge } }",
 "variables": {
    "input": {
      "appIds": ["30966426"],
      "addedTagsIds": ["example"],
      "removedTagsIds": ["example"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation ModifyAppsTags($input: ModifyAppsTagsInput!) { modifyAppsTags(input: $input) { acknowledge } }';

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
        appIds: ["30966426"],
        addedTagsIds: ["example"],
        removedTagsIds: ["example"]
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

query = 'mutation ModifyAppsTags($input: ModifyAppsTagsInput!) { modifyAppsTags(input: $input) { acknowledge } }'

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
        "appIds": ["30966426"],
        "addedTagsIds": ["example"],
        "removedTagsIds": ["example"]
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

You can use the following argument(s) to customize your `modifyAppsTags` mutation.

| Argument                                                                                                                                                                                             | Description                                                   | Supported fields                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| input [`ModifyAppsTagsInput!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/modify-apps-tags-input) <mark style="color:red;background-color:red;">required</mark> | Input specifying applications and tags to be added or removed | <p>appIds <code>\[String!]!</code><br>addedTagsIds <code>\[String!]!</code><br>removedTagsIds <code>\[String!]!</code></p> |

### Fields

Return type: [`Acknowledge!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/acknowledge)

You can use the following field(s) to specify what information your `modifyAppsTags` mutation will return. Please note that some fields may have their own subfields.

| Field                  | Description                                        | Supported fields |
| ---------------------- | -------------------------------------------------- | ---------------- |
| acknowledge `Boolean!` | Boolean indicating if the operation was successful |                  |
