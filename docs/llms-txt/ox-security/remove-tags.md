# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/mutations/remove-tags.md

# removeTags

Remove tags from the system with optional repository tag updates.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation RemoveTags($deleteTagsInput: DeleteTagsInput!) {
  removeTags(deleteTagsInput: $deleteTagsInput) {
    acknowledge
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "deleteTagsInput": {
    "filters": {
      "tagId": ["ox_tag_1"]
    }
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
 "query": "mutation RemoveTags($deleteTagsInput: DeleteTagsInput!) { removeTags(deleteTagsInput: $deleteTagsInput) { acknowledge } }",
 "variables": {
    "deleteTagsInput": {
      "filters": {
        "tagId": ["ox_tag_1"]
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation RemoveTags($deleteTagsInput: DeleteTagsInput!) { removeTags(deleteTagsInput: $deleteTagsInput) { acknowledge } }';

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
      deleteTagsInput: {
        filters: {
          tagId: ["ox_tag_1"]
        }
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

query = 'mutation RemoveTags($deleteTagsInput: DeleteTagsInput!) { removeTags(deleteTagsInput: $deleteTagsInput) { acknowledge } }'

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
      "deleteTagsInput": {
        "filters": {
          "tagId": ["ox_tag_1"]
        }
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

You can use the following argument(s) to customize your `removeTags` mutation.

| Argument                                                                                                                                                                                              | Description                                                                 | Supported fields                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| deleteTagsInput [`DeleteTagsInput!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/delete-tags-input) <mark style="color:red;background-color:red;">required</mark> | Input specifying which tags to delete and whether to update repository tags | filters [`DeleteTagsFilter!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/delete-tags-filter) |

### Fields

Return type: [`Acknowledge`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/acknowledge)

You can use the following field(s) to specify what information your `removeTags` mutation will return. Please note that some fields may have their own subfields.

| Field                  | Description                                        | Supported fields |
| ---------------------- | -------------------------------------------------- | ---------------- |
| acknowledge `Boolean!` | Boolean indicating if the operation was successful |                  |
