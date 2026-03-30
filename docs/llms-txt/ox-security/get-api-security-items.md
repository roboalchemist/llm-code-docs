# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/queries/get-api-security-items.md

# getApiSecurityItems

Retrieves a list of discovered API endpoints with their security information.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetApiSecurityItems($getApiSecurityInput: GetApiSecurityInput) {
  getApiSecurityItems(getApiSecurityInput: $getApiSecurityInput) {
    apiSecurityItems {
      id
      scanId
      title
      description
      version
      methodDescription
      methodOperationId
      methodSummary
      openapi
      servers
      epName
      methodName
      methodResponses {
        description
        code
      }
      methodTags
      methodParameters {
        description
        in
        name
        required
      }
      appId
      appType
      appName
      fileName
      definitions {
        source
        fileName
        link
        llmTitle
        llmDescription
        functions {
          function
          line
          snippet
          filepath
          link
        }
      }
      framework
      language
      firstSeen
      uuid
      issuesBySeverity {
        info
        low
        medium
        high
        critical
        appox
      }
      codeLocations {
        link
        callBranch
      }
      commits {
        commitInfo {
          authorName
          authorEmail
          committerName
          committerEmail
          commitId
          message
          authorDate
          commitDate
        }
        match
        snippet
        snippetLineNumber
        startLineNumber
        fileName
        link
      }
    }
    total
    totalFiltered
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "getApiSecurityInput": {
    "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
    "offset": 0,
    "limit": 100,
    "owners": ["example"],
    "tagIds": ["example"],
    "search": "/api/v2/",
    "filters": {
      "apps": ["repo-name"],
      "appIds": ["1234567890"],
      "titles": ["Kubernetes"],
      "endpoints": ["/api/v1/some/endpoint"],
      "methods": ["GET"],
      "framework": ["OpenAPI"],
      "languages": ["OpenAPI"],
      "issueIds": ["30966426-oxPolicy_securityCloudScan_100-example"],
      "apiId": ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
      "source": ["OpenAPI"],
      "severities": ["2"],
      "reachability": ["Code"],
      "appTags": ["Private repo"]
    },
    "filterSearch": [
      {
        "fieldName": "example",
        "value": ["example"]
      }
    ],
    "openItems": ["digest"],
    "orderBy": {
      "field": "title",
      "direction": "ASC"
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
 "query": "query GetApiSecurityItems($getApiSecurityInput: GetApiSecurityInput) { getApiSecurityItems(getApiSecurityInput: $getApiSecurityInput) { apiSecurityItems { id scanId title description version methodDescription methodOperationId methodSummary openapi servers epName methodName methodResponses { description code } methodTags methodParameters { description in name required } appId appType appName fileName definitions { source fileName link llmTitle llmDescription functions { function line snippet filepath link } } framework language firstSeen uuid issuesBySeverity { info low medium high critical appox } codeLocations { link callBranch } commits { commitInfo { authorName authorEmail committerName committerEmail commitId message authorDate commitDate } match snippet snippetLineNumber startLineNumber fileName link } } total totalFiltered } }",
 "variables": {
    "getApiSecurityInput": {
      "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
      "offset": 0,
      "limit": 100,
      "owners": ["example"],
      "tagIds": ["example"],
      "search": "/api/v2/",
      "filters": {
        "apps": ["repo-name"],
        "appIds": ["1234567890"],
        "titles": ["Kubernetes"],
        "endpoints": ["/api/v1/some/endpoint"],
        "methods": ["GET"],
        "framework": ["OpenAPI"],
        "languages": ["OpenAPI"],
        "issueIds": ["30966426-oxPolicy_securityCloudScan_100-example"],
        "apiId": ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
        "source": ["OpenAPI"],
        "severities": ["2"],
        "reachability": ["Code"],
        "appTags": ["Private repo"]
      },
      "filterSearch": [
        {
          "fieldName": "example",
          "value": ["example"]
        }
      ],
      "openItems": ["digest"],
      "orderBy": {
        "field": "title",
        "direction": "ASC"
      }
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetApiSecurityItems($getApiSecurityInput: GetApiSecurityInput) { getApiSecurityItems(getApiSecurityInput: $getApiSecurityInput) { apiSecurityItems { id scanId title description version methodDescription methodOperationId methodSummary openapi servers epName methodName methodResponses { description code } methodTags methodParameters { description in name required } appId appType appName fileName definitions { source fileName link llmTitle llmDescription functions { function line snippet filepath link } } framework language firstSeen uuid issuesBySeverity { info low medium high critical appox } codeLocations { link callBranch } commits { commitInfo { authorName authorEmail committerName committerEmail commitId message authorDate commitDate } match snippet snippetLineNumber startLineNumber fileName link } } total totalFiltered } }';

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
      getApiSecurityInput: {
        scanId: "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        offset: 0,
        limit: 100,
        owners: ["example"],
        tagIds: ["example"],
        search: "/api/v2/",
        filters: {
          apps: ["repo-name"],
          appIds: ["1234567890"],
          titles: ["Kubernetes"],
          endpoints: ["/api/v1/some/endpoint"],
          methods: ["GET"],
          framework: ["OpenAPI"],
          languages: ["OpenAPI"],
          issueIds: ["30966426-oxPolicy_securityCloudScan_100-example"],
          apiId: ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
          source: ["OpenAPI"],
          severities: ["2"],
          reachability: ["Code"],
          appTags: ["Private repo"]
        },
        filterSearch: [
          {
            fieldName: "example",
            value: ["example"]
          }
        ],
        openItems: ["digest"],
        orderBy: {
          field: "title",
          direction: "ASC"
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

query = 'query GetApiSecurityItems($getApiSecurityInput: GetApiSecurityInput) { getApiSecurityItems(getApiSecurityInput: $getApiSecurityInput) { apiSecurityItems { id scanId title description version methodDescription methodOperationId methodSummary openapi servers epName methodName methodResponses { description code } methodTags methodParameters { description in name required } appId appType appName fileName definitions { source fileName link llmTitle llmDescription functions { function line snippet filepath link } } framework language firstSeen uuid issuesBySeverity { info low medium high critical appox } codeLocations { link callBranch } commits { commitInfo { authorName authorEmail committerName committerEmail commitId message authorDate commitDate } match snippet snippetLineNumber startLineNumber fileName link } } total totalFiltered } }'

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
      "getApiSecurityInput": {
        "scanId": "c9da693d-8906-4a32-93c9-2ffdb1cebb99",
        "offset": 0,
        "limit": 100,
        "owners": ["example"],
        "tagIds": ["example"],
        "search": "/api/v2/",
        "filters": {
          "apps": ["repo-name"],
          "appIds": ["1234567890"],
          "titles": ["Kubernetes"],
          "endpoints": ["/api/v1/some/endpoint"],
          "methods": ["GET"],
          "framework": ["OpenAPI"],
          "languages": ["OpenAPI"],
          "issueIds": ["30966426-oxPolicy_securityCloudScan_100-example"],
          "apiId": ["ceb76dd8-7c11-448c-9056-17c5b5bfa361"],
          "source": ["OpenAPI"],
          "severities": ["2"],
          "reachability": ["Code"],
          "appTags": ["Private repo"]
        },
        "filterSearch": [
          {
            "fieldName": "example",
            "value": ["example"]
          }
        ],
        "openItems": ["digest"],
        "orderBy": {
          "field": "title",
          "direction": "ASC"
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

You can use the following argument(s) to customize your `getApiSecurityItems` query.

| Argument                                                                                                                                                    | Description                                                     | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| getApiSecurityInput [`GetApiSecurityInput`](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/get-api-security-input) | Parameters for filtering and paginating the API security items. | <p>scanId <code>String</code><br>offset <code>Int</code><br>limit <code>Int</code><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code><br>search <code>String</code><br>filters <a href="../types/inputs/api-sec-filters"><code>ApiSecFilters</code></a><br>filterSearch <a href="../../api--application/types/inputs/auto-complete-search"><code>\[AutoCompleteSearch]</code></a><br>openItems <a href="../../api--application/types/enums/filter-types"><code>\[FilterTypes]</code></a><br>orderBy <a href="../types/inputs/api-security-order-by"><code>ApiSecurityOrderBy</code></a></p> |

### Fields

Return type: [`ApiSecurityItemsResponse`](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-items-response)

You can use the following field(s) to specify what information your `getApiSecurityItems` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                              | Description                                               | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| apiSecurityItems [`[ApiSecurityItem]`](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item) | List of API security items found in the scan              | <p>id <code>String</code><br>scanId <code>String</code><br>title <code>String</code><br>description <code>String</code><br>version <code>String</code><br>methodDescription <code>String</code><br>methodOperationId <code>String</code><br>methodSummary <code>String</code><br>openapi <code>String</code><br>servers <code>\[String]</code><br>epName <code>String</code><br>methodName <code>String</code><br>methodResponses <a href="../types/objects/method-response"><code>\[MethodResponse]</code></a><br>methodTags <code>\[String]</code><br>methodParameters <a href="../types/objects/method-parameter"><code>\[MethodParameter]</code></a><br>appId <code>String</code><br>appType <code>String</code><br>appName <code>String</code><br>fileName <code>\[String]</code><br>definitions <a href="../types/objects/api-definitions"><code>\[APIDefinitions]</code></a><br>framework <code>String</code><br>language <code>String</code><br>firstSeen <code>Date</code><br>uuid <code>String</code><br>issuesBySeverity <a href="../../api--application/types/objects/severities"><code>Severities</code></a><br>codeLocations <a href="../../api--issue/types/objects/code-location"><code>\[CodeLocation]</code></a><br>commits <a href="../types/objects/api-inventory-commit"><code>\[ApiInventoryCommit]</code></a></p> |
| total `Int`                                                                                                                                        | Total number of API security items available              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| totalFiltered `Int`                                                                                                                                | Total number of API security items after applying filters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
