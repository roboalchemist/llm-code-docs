# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/queries/get-sbom-vulnerable-libraries.md

# getSbomVulnerableLibraries

Gets statistics about libraries with known vulnerabilities grouped by severity.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
query GetSbomVulnerableLibraries($input: SbomVulnerableLibrariesInput) {
  getSbomVulnerableLibraries(input: $input) {
    data {
      name
      count
    }
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "search": "example",
    "filters": {
      "libForSearch": ["example"],
      "libraryNames": ["example"],
      "libraryVersions": ["example"],
      "apps": ["example"],
      "appIds": ["30966426"],
      "source": ["example"],
      "dependencyTypes": ["example"],
      "licenses": ["example"],
      "packageNames": ["example"],
      "copyrights": ["example"],
      "severities": ["example"],
      "packageInfos": ["example"],
      "malicious": ["example"],
      "packageManagers": ["example"],
      "cve": ["example"],
      "languages": ["example"],
      "os": ["example"],
      "registryName": ["example"],
      "baseImage": ["example"],
      "image": ["example"],
      "reachability": ["example"],
      "tags": ["example"],
      "imageSource": ["example"],
      "licenseIssue": [true],
      "sbomImageTags": ["example"],
      "runtimeStatus": ["example"]
    },
    "owners": ["example"],
    "tagIds": ["example"]
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
 "query": "query GetSbomVulnerableLibraries($input: SbomVulnerableLibrariesInput) { getSbomVulnerableLibraries(input: $input) { data { name count } } }",
 "variables": {
    "input": {
      "search": "example",
      "filters": {
        "libForSearch": ["example"],
        "libraryNames": ["example"],
        "libraryVersions": ["example"],
        "apps": ["example"],
        "appIds": ["30966426"],
        "source": ["example"],
        "dependencyTypes": ["example"],
        "licenses": ["example"],
        "packageNames": ["example"],
        "copyrights": ["example"],
        "severities": ["example"],
        "packageInfos": ["example"],
        "malicious": ["example"],
        "packageManagers": ["example"],
        "cve": ["example"],
        "languages": ["example"],
        "os": ["example"],
        "registryName": ["example"],
        "baseImage": ["example"],
        "image": ["example"],
        "reachability": ["example"],
        "tags": ["example"],
        "imageSource": ["example"],
        "licenseIssue": [true],
        "sbomImageTags": ["example"],
        "runtimeStatus": ["example"]
      },
      "owners": ["example"],
      "tagIds": ["example"]
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'query GetSbomVulnerableLibraries($input: SbomVulnerableLibrariesInput) { getSbomVulnerableLibraries(input: $input) { data { name count } } }';

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
        search: "example",
        filters: {
          libForSearch: ["example"],
          libraryNames: ["example"],
          libraryVersions: ["example"],
          apps: ["example"],
          appIds: ["30966426"],
          source: ["example"],
          dependencyTypes: ["example"],
          licenses: ["example"],
          packageNames: ["example"],
          copyrights: ["example"],
          severities: ["example"],
          packageInfos: ["example"],
          malicious: ["example"],
          packageManagers: ["example"],
          cve: ["example"],
          languages: ["example"],
          os: ["example"],
          registryName: ["example"],
          baseImage: ["example"],
          image: ["example"],
          reachability: ["example"],
          tags: ["example"],
          imageSource: ["example"],
          licenseIssue: [true],
          sbomImageTags: ["example"],
          runtimeStatus: ["example"]
        },
        owners: ["example"],
        tagIds: ["example"]
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

query = 'query GetSbomVulnerableLibraries($input: SbomVulnerableLibrariesInput) { getSbomVulnerableLibraries(input: $input) { data { name count } } }'

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
        "search": "example",
        "filters": {
          "libForSearch": ["example"],
          "libraryNames": ["example"],
          "libraryVersions": ["example"],
          "apps": ["example"],
          "appIds": ["30966426"],
          "source": ["example"],
          "dependencyTypes": ["example"],
          "licenses": ["example"],
          "packageNames": ["example"],
          "copyrights": ["example"],
          "severities": ["example"],
          "packageInfos": ["example"],
          "malicious": ["example"],
          "packageManagers": ["example"],
          "cve": ["example"],
          "languages": ["example"],
          "os": ["example"],
          "registryName": ["example"],
          "baseImage": ["example"],
          "image": ["example"],
          "reachability": ["example"],
          "tags": ["example"],
          "imageSource": ["example"],
          "licenseIssue": [true],
          "sbomImageTags": ["example"],
          "runtimeStatus": ["example"]
        },
        "owners": ["example"],
        "tagIds": ["example"]
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

You can use the following argument(s) to customize your `getSbomVulnerableLibraries` query.

| Argument                                                                                                                                                | Description                                                                       | Supported fields                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`SbomVulnerableLibrariesInput`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/sbom-vulnerable-libraries-input) | Parameters for filtering which libraries to include in the vulnerability analysis | <p>search <code>String</code><br>filters <a href="../types/inputs/sbom-lib-filters"><code>SBOMLibFilters</code></a><br>owners <code>\[String]</code><br>tagIds <code>\[String]</code></p> |

### Fields

Return type: [`SbomVulnerableLibrariesResponse`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response)

You can use the following field(s) to specify what information your `getSbomVulnerableLibraries` query will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                                                     | Description                                            | Supported fields                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| data [`[SbomVulnerableLibrariesResponseItem]!`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response-item) | List of vulnerability counts grouped by severity level | <p>name <a href="../types/enums/severity-risk"><code>SeverityRisk!</code></a><br>count <code>Int!</code></p> |
