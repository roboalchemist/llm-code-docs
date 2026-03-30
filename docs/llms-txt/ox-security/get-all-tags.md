# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/queries/get-all-tags.md

# getAllTags

Retrieve all tags in the system including both user-defined and system (ox) tags.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetAllTags($input: GetTagsInput) {
  getAllTags(input: $input) {
    tags {
      tagId
      name
      displayName
      tagType
      createdBy
      createdAt
      updatedAt
      tagCategory
      deploymentModel
      purpose
      email
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "filters": {
      "tagType": ["simple"],
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
 "query": "query GetAllTags($input: GetTagsInput) { getAllTags(input: $input) { tags { tagId name displayName tagType createdBy createdAt updatedAt tagCategory deploymentModel purpose email } } }",
 "variables": {
    "input": {
      "filters": {
        "tagType": ["simple"],
        "tagId": ["ox_tag_1"]
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetAllTags($input: GetTagsInput) { getAllTags(input: $input) { tags { tagId name displayName tagType createdBy createdAt updatedAt tagCategory deploymentModel purpose email } } }';

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
        filters: {
          tagType: ["simple"],
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

query = 'query GetAllTags($input: GetTagsInput) { getAllTags(input: $input) { tags { tagId name displayName tagType createdBy createdAt updatedAt tagCategory deploymentModel purpose email } } }'

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
        "filters": {
          "tagType": ["simple"],
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

You can use the following argument(s) to customize your `getAllTags` query.

| Argument                                                                                                               | Description                                                         | Supported fields                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| input [`GetTagsInput`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-input) | Input parameters for filtering tags by type, ID, and other criteria | filters [`GetTagsFilters`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-tags-filters) |

### Fields

Return type: [`GetAllTagsResponse!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/get-all-tags-response)

You can use the following field(s) to specify what information your `getAllTags` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                               | Description                               | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| tags [`[TagObject!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/tag-object) | Array of tags matching the query criteria | <p>tagId <code>String!</code><br>name <code>String!</code><br>displayName <code>String!</code><br>tagType <a href="../../api--application/types/enums/ox-tag-type"><code>OxTagType!</code></a><br>createdBy <code>String!</code><br>createdAt <code>DateTime</code><br>updatedAt <code>DateTime</code><br>tagCategory <code>String</code><br>deploymentModel <code>String</code><br>purpose <code>String</code><br>email <code>String</code></p> |
