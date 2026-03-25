# Source: https://docs.ox.security/api-documentation/api-reference/api--filters/queries/get-filter-labels.md

# getFilterLabels

Retrieves available filter labels for a specific page with their configuration and capabilities.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetFilterLabels($page: FilterPage!) {
  getFilterLabels(page: $page) {
    id
    label
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "page": "Issues"
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
 "query": "query GetFilterLabels($page: FilterPage!) { getFilterLabels(page: $page) { id label } }",
 "variables": {
    "page": "Issues"
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetFilterLabels($page: FilterPage!) { getFilterLabels(page: $page) { id label } }';

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
      page: "Issues"
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

query = 'query GetFilterLabels($page: FilterPage!) { getFilterLabels(page: $page) { id label } }'

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
      "page": "Issues"
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

You can use the following argument(s) to customize your `getFilterLabels` query.

| Argument                                                                                                                                                                          | Description                                   | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ---------------- |
| page [`FilterPage!`](https://docs.ox.security/api-documentation/api-reference/api--filters/types/enums/filter-page) <mark style="color:red;background-color:red;">required</mark> | The page for which to retrieve filter labels. |                  |

### Fields

Return type: [`[FilterLabelItems]`](https://docs.ox.security/api-documentation/api-reference/api--filters/types/objects/filter-label-items)

You can use the following field(s) to specify what information your `getFilterLabels` query will return. Please note that some fields may have their own subfields.

| Field          | Description                  | Supported fields |
| -------------- | ---------------------------- | ---------------- |
| id `String`    | Filter identifier            |                  |
| label `String` | Display label for the filter |                  |
