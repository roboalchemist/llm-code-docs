# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/exclude-alert.md

# excludeAlert

Create an exclusion for an alert.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation ExcludeAlert($input: ExcludeAlertInput!) {
  excludeAlert(input: $input) {
    exclusions {
      exclusionType
      exclusionId
      modifiedIssues
      modifiedBy
      createdAt
      exclusionAppliedOn
      exclusionTypeLabel
      exclusionMatch {
        key
        value
      }
      appName
      policyName
      appId
      policyId
      policyCategory
      appType
      comment
      exclusionScope
      oxIssueId
      issueName
      exclusionMode
      expiredAt
      isActive
      inDayExpired
      inWeekExpired
      status
      fp
      exclusionSubType
    }
    totalExclusions
    totalFilteredExclusions
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "oxIssueId": "example",
    "rule": {
      "oxRuleId": "issue",
      "aggIds": ["example"],
      "cvesAndLibs": [
        {
          "cve": "example",
          "libName": "example",
          "libVersion": "example"
        }
      ]
    },
    "comment": "some comment",
    "exclusionMode": "fullScan",
    "expiredAt": "example"
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
 "query": "mutation ExcludeAlert($input: ExcludeAlertInput!) { excludeAlert(input: $input) { exclusions { exclusionType exclusionId modifiedIssues modifiedBy createdAt exclusionAppliedOn exclusionTypeLabel exclusionMatch { key value } appName policyName appId policyId policyCategory appType comment exclusionScope oxIssueId issueName exclusionMode expiredAt isActive inDayExpired inWeekExpired status fp exclusionSubType } totalExclusions totalFilteredExclusions } }",
 "variables": {
    "input": {
      "oxIssueId": "example",
      "rule": {
        "oxRuleId": "issue",
        "aggIds": ["example"],
        "cvesAndLibs": [
          {
            "cve": "example",
            "libName": "example",
            "libVersion": "example"
          }
        ]
      },
      "comment": "some comment",
      "exclusionMode": "fullScan",
      "expiredAt": "example"
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation ExcludeAlert($input: ExcludeAlertInput!) { excludeAlert(input: $input) { exclusions { exclusionType exclusionId modifiedIssues modifiedBy createdAt exclusionAppliedOn exclusionTypeLabel exclusionMatch { key value } appName policyName appId policyId policyCategory appType comment exclusionScope oxIssueId issueName exclusionMode expiredAt isActive inDayExpired inWeekExpired status fp exclusionSubType } totalExclusions totalFilteredExclusions } }';

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
        oxIssueId: "example",
        rule: {
          oxRuleId: "issue",
          aggIds: ["example"],
          cvesAndLibs: [
            {
              cve: "example",
              libName: "example",
              libVersion: "example"
            }
          ]
        },
        comment: "some comment",
        exclusionMode: "fullScan",
        expiredAt: "example"
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

query = 'mutation ExcludeAlert($input: ExcludeAlertInput!) { excludeAlert(input: $input) { exclusions { exclusionType exclusionId modifiedIssues modifiedBy createdAt exclusionAppliedOn exclusionTypeLabel exclusionMatch { key value } appName policyName appId policyId policyCategory appType comment exclusionScope oxIssueId issueName exclusionMode expiredAt isActive inDayExpired inWeekExpired status fp exclusionSubType } totalExclusions totalFilteredExclusions } }'

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
        "oxIssueId": "example",
        "rule": {
          "oxRuleId": "issue",
          "aggIds": ["example"],
          "cvesAndLibs": [
            {
              "cve": "example",
              "libName": "example",
              "libVersion": "example"
            }
          ]
        },
        "comment": "some comment",
        "exclusionMode": "fullScan",
        "expiredAt": "example"
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

You can use the following argument(s) to customize your `excludeAlert` mutation.

| Argument                                                                                                                                                                                              | Description                     | Supported fields                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| input [`ExcludeAlertInput!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-alert-input) <mark style="color:red;background-color:red;">required</mark> | Details of the alert to exclude | <p>oxIssueId <code>String!</code><br>rule <a href="../types/inputs/exclusion-rule-input"><code>ExclusionRuleInput</code></a><br>comment <code>String</code><br>exclusionMode <a href="../types/enums/exclusion-mode"><code>ExclusionMode</code></a><br>expiredAt <code>DateTime</code></p> |

### Fields

Return type: [`GetExclusionsRes`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/get-exclusions-res)

You can use the following field(s) to specify what information your `excludeAlert` mutation will return. Please note that some fields may have their own subfields.

| Field                                                                                                                          | Description                                       | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exclusions [`[Exclusion!]!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion) | List of exclusions matching the query             | <p>exclusionType <a href="../types/enums/exclusion-type"><code>ExclusionType!</code></a><br>exclusionId <code>String!</code><br>modifiedIssues <code>Float</code><br>modifiedBy <code>String!</code><br>createdAt <code>DateTime!</code><br>exclusionAppliedOn <code>String!</code><br>exclusionTypeLabel <code>String!</code><br>exclusionMatch <a href="../types/objects/exclusion-match"><code>\[ExclusionMatch!]!</code></a><br>appName <code>String</code><br>policyName <code>String</code><br>appId <code>String</code><br>policyId <code>String</code><br>policyCategory <code>String</code><br>appType <code>String</code><br>comment <code>String</code><br>exclusionScope <a href="../types/enums/exclusion-scope"><code>ExclusionScope</code></a><br>oxIssueId <code>String</code><br>issueName <code>String</code><br>exclusionMode <a href="../types/enums/exclusion-mode"><code>ExclusionMode</code></a><br>expiredAt <code>DateTime</code><br>isActive <code>Boolean!</code><br>inDayExpired <code>Boolean</code><br>inWeekExpired <code>Boolean</code><br>status <a href="../types/enums/status-mode"><code>StatusMode</code></a><br>fp <code>Boolean</code><br>exclusionSubType <a href="../types/enums/ox-exclusion-sub-type"><code>OxExclusionSubType</code></a></p> |
| totalExclusions `Float`                                                                                                        | Total number of exclusions in the system          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| totalFilteredExclusions `Float`                                                                                                | Number of exclusions matching the current filters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
