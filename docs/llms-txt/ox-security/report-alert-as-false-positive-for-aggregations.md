# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/mutations/report-alert-as-false-positive-for-aggregations.md

# reportAlertAsFalsePositiveForAggregations

Report an alert as a false positive for aggregations.

### Examples

{% tabs %}
{% tab title="GraphQL" %}

```graphql
mutation ReportAlertAsFalsePositiveForAggregations($input: ReportFalsePositiveInput!) {
  reportAlertAsFalsePositiveForAggregations(input: $input) {
    exclusionInfo {
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
    aggregationsStatus
  }
}
```

**Variables**

This is an example input showing all available input fields. Only fields marked as required in the schema are mandatory.

```json
{
  "input": {
    "reportedAlertInput": {
      "oxIssueId": "example",
      "rule": {
        "oxRuleId": "issue",
        "aggIds": [],
        "cvesAndLibs": []
      },
      "comment": "some comment",
      "exclusionMode": "fullScan",
      "expiredAt": "example"
    },
    "isExclude": true
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
 "query": "mutation ReportAlertAsFalsePositiveForAggregations($input: ReportFalsePositiveInput!) { reportAlertAsFalsePositiveForAggregations(input: $input) { exclusionInfo { exclusions { exclusionType exclusionId modifiedIssues modifiedBy createdAt exclusionAppliedOn exclusionTypeLabel exclusionMatch { key value } appName policyName appId policyId policyCategory appType comment exclusionScope oxIssueId issueName exclusionMode expiredAt isActive inDayExpired inWeekExpired status fp exclusionSubType } totalExclusions totalFilteredExclusions } aggregationsStatus } }",
 "variables": {
    "input": {
      "reportedAlertInput": {
        "oxIssueId": "example",
        "rule": {
          "oxRuleId": "issue",
          "aggIds": [],
          "cvesAndLibs": []
        },
        "comment": "some comment",
        "exclusionMode": "fullScan",
        "expiredAt": "example"
      },
      "isExclude": true
    }
  }
}'
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const query = 'mutation ReportAlertAsFalsePositiveForAggregations($input: ReportFalsePositiveInput!) { reportAlertAsFalsePositiveForAggregations(input: $input) { exclusionInfo { exclusions { exclusionType exclusionId modifiedIssues modifiedBy createdAt exclusionAppliedOn exclusionTypeLabel exclusionMatch { key value } appName policyName appId policyId policyCategory appType comment exclusionScope oxIssueId issueName exclusionMode expiredAt isActive inDayExpired inWeekExpired status fp exclusionSubType } totalExclusions totalFilteredExclusions } aggregationsStatus } }';

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
        reportedAlertInput: {
          oxIssueId: "example",
          rule: {
            oxRuleId: "issue",
            aggIds: [],
            cvesAndLibs: []
          },
          comment: "some comment",
          exclusionMode: "fullScan",
          expiredAt: "example"
        },
        isExclude: true
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

query = 'mutation ReportAlertAsFalsePositiveForAggregations($input: ReportFalsePositiveInput!) { reportAlertAsFalsePositiveForAggregations(input: $input) { exclusionInfo { exclusions { exclusionType exclusionId modifiedIssues modifiedBy createdAt exclusionAppliedOn exclusionTypeLabel exclusionMatch { key value } appName policyName appId policyId policyCategory appType comment exclusionScope oxIssueId issueName exclusionMode expiredAt isActive inDayExpired inWeekExpired status fp exclusionSubType } totalExclusions totalFilteredExclusions } aggregationsStatus } }'

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
        "reportedAlertInput": {
          "oxIssueId": "example",
          "rule": {
            "oxRuleId": "issue",
            "aggIds": [],
            "cvesAndLibs": []
          },
          "comment": "some comment",
          "exclusionMode": "fullScan",
          "expiredAt": "example"
        },
        "isExclude": true
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

You can use the following argument(s) to customize your `reportAlertAsFalsePositiveForAggregations` mutation.

| Argument                                                                                                                                                                                                             | Description                                           | Supported fields                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| input [`ReportFalsePositiveInput!`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/report-false-positive-input) <mark style="color:red;background-color:red;">required</mark> | Details of the false positive report for aggregations | <p>reportedAlertInput <a href="../types/inputs/exclude-alert-input"><code>ExcludeAlertInput!</code></a><br>isExclude <code>Boolean!</code></p> |

### Fields

Return type: [`ReportFalsePositiveAlertRes`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/report-false-positive-alert-res)

You can use the following field(s) to specify what information your `reportAlertAsFalsePositiveForAggregations` mutation will return. Please note that some fields may have their own subfields.

| Field                                                                                                                                         | Description                                                               | Supported fields                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exclusionInfo [`GetExclusionsRes`](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/get-exclusions-res) | Information about the created exclusion if one was created                | <p>exclusions <a href="../types/objects/exclusion"><code>\[Exclusion!]!</code></a><br>totalExclusions <code>Float</code><br>totalFilteredExclusions <code>Float</code></p> |
| aggregationsStatus `String`                                                                                                                   | Status of aggregations for display in UI based on enum AggregationsStatus |                                                                                                                                                                            |
