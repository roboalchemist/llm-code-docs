# Source: https://docs.ox.security/api-documentation/api-reference/api--tags/queries/get-app-tags.md

# getAppTags

Retrieve tags associated with applications with optional filtering and pagination.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetAppTags($getAppsTagsInput: GetAppsTagsInput) {
  getAppTags(getAppsTagsInput: $getAppsTagsInput) {
    appsTags {
      tagType
      appId
      tagId
      appliedBy
      roles
      tag {
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
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getAppsTagsInput": {
    "filters": {
      "appId": ["30966426"],
      "tagId": ["ox_tag_1"],
      "tagType": ["simple"]
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
 "query": "query GetAppTags($getAppsTagsInput: GetAppsTagsInput) { getAppTags(getAppsTagsInput: $getAppsTagsInput) { appsTags { tagType appId tagId appliedBy roles tag { tagId name displayName tagType createdBy createdAt updatedAt tagCategory deploymentModel purpose email } } } }",
 "variables": {
    "getAppsTagsInput": {
      "filters": {
        "appId": ["30966426"],
        "tagId": ["ox_tag_1"],
        "tagType": ["simple"]
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetAppTags($getAppsTagsInput: GetAppsTagsInput) { getAppTags(getAppsTagsInput: $getAppsTagsInput) { appsTags { tagType appId tagId appliedBy roles tag { tagId name displayName tagType createdBy createdAt updatedAt tagCategory deploymentModel purpose email } } } }';

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
      getAppsTagsInput: {
        filters: {
          appId: ["30966426"],
          tagId: ["ox_tag_1"],
          tagType: ["simple"]
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

query = 'query GetAppTags($getAppsTagsInput: GetAppsTagsInput) { getAppTags(getAppsTagsInput: $getAppsTagsInput) { appsTags { tagType appId tagId appliedBy roles tag { tagId name displayName tagType createdBy createdAt updatedAt tagCategory deploymentModel purpose email } } } }'

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
      "getAppsTagsInput": {
        "filters": {
          "appId": ["30966426"],
          "tagId": ["ox_tag_1"],
          "tagType": ["simple"]
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

You can use the following argument(s) to customize your `getAppTags` query.

| Argument                                                                                                                                   | Description                                                    | Supported fields                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| getAppsTagsInput [`GetAppsTagsInput`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input) | Input parameters for filtering and paginating application tags | filters [`GetAppsTagsInputFilter`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/inputs/get-apps-tags-input-filter) |

### Fields

Return type: [`GetAppsTagsRes!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/get-apps-tags-res)

You can use the following field(s) to specify what information your `getAppTags` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                          | Description                                          | Supported fields                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appsTags [`[AppTagObject!]!`](https://docs.ox.security/api-documentation/api-reference/api--tags/types/objects/app-tag-object) | List of application tags matching the query criteria | <p>tagType <a href="../../api--application/types/enums/ox-tag-type"><code>OxTagType!</code></a><br>appId <code>String!</code><br>tagId <code>String!</code><br>appliedBy <code>String</code><br>roles <a href="../../api--application/types/enums/app-owner-role"><code>\[AppOwnerRole!]</code></a><br>tag <a href="../types/objects/tag-object"><code>TagObject</code></a></p> |
