# Source: https://docs.datadoghq.com/api/latest/entity-risk-scores.md

---
title: Entity Risk Scores
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Entity Risk Scores
---

# Entity Risk Scores

Retrieves security risk scores for entities in your organization.

## List Entity Risk Scores{% #list-entity-risk-scores %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/security-entities/risk-scores |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/security-entities/risk-scores |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/security-entities/risk-scores      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/security-entities/risk-scores      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/security-entities/risk-scores     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/security-entities/risk-scores |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/security-entities/risk-scores |

### Overview

Get a list of entity risk scores for your organization. Entity risk scores provide security risk assessment for entities like cloud resources, identities, or services based on detected signals, misconfigurations, and identity risks.

### Arguments

#### Query Strings

| Name          | Type    | Description                                                                                                                                                                            |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from          | integer | Start time for the query in Unix timestamp (milliseconds). Defaults to 2 weeks ago.                                                                                                    |
| to            | integer | End time for the query in Unix timestamp (milliseconds). Defaults to now.                                                                                                              |
| page[size]    | integer | Size of the page to return. Maximum is 1000.                                                                                                                                           |
| page[number]  | integer | Page number to return (1-indexed).                                                                                                                                                     |
| page[queryId] | string  | Query ID for pagination consistency.                                                                                                                                                   |
| filter[sort]  | string  | Sort order for results. Format: `field:direction` where direction is `asc` or `desc`. Supported fields: `riskScore`, `lastDetected`, `firstDetected`, `entityName`, `signalsDetected`. |
| filter[query] | string  | Supports filtering by entity attributes, risk scores, severity, and more. Example: `severity:critical AND entityType:aws_iam_user`                                                     |
| entityType    | array   | Filter by entity type(s). Can specify multiple values.                                                                                                                                 |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of entity risk scores

| Parent field   | Field                                  | Type     | Description                                                                             |
| -------------- | -------------------------------------- | -------- | --------------------------------------------------------------------------------------- |
|                | data [*required*]                 | [object] |
| data           | attributes [*required*]           | object   | Attributes of an entity risk score                                                      |
| attributes     | configRisks [*required*]          | object   | Configuration risks associated with the entity                                          |
| configRisks    | hasIdentityRisk [*required*]      | boolean  | Whether the entity has identity risks                                                   |
| configRisks    | hasMisconfiguration [*required*]  | boolean  | Whether the entity has misconfigurations                                                |
| configRisks    | hasPrivilegedRole [*required*]    | boolean  | Whether the entity has privileged roles                                                 |
| configRisks    | isPrivileged [*required*]         | boolean  | Whether the entity has privileged access                                                |
| configRisks    | isProduction [*required*]         | boolean  | Whether the entity is in a production environment                                       |
| configRisks    | isPubliclyAccessible [*required*] | boolean  | Whether the entity is publicly accessible                                               |
| attributes     | entityID [*required*]             | string   | Unique identifier for the entity                                                        |
| attributes     | entityMetadata [*required*]       | object   | Metadata about the entity from cloud providers                                          |
| entityMetadata | accountID                              | string   | Cloud account ID (AWS)                                                                  |
| entityMetadata | environments [*required*]         | [string] | Environment tags associated with the entity                                             |
| entityMetadata | mitreTactics [*required*]         | [string] | MITRE ATT&CK tactics detected                                                           |
| entityMetadata | mitreTechniques [*required*]      | [string] | MITRE ATT&CK techniques detected                                                        |
| entityMetadata | projectID                              | string   | Cloud project ID (GCP)                                                                  |
| entityMetadata | services [*required*]             | [string] | Services associated with the entity                                                     |
| entityMetadata | sources [*required*]              | [string] | Data sources that detected this entity                                                  |
| entityMetadata | subscriptionID                         | string   | Cloud subscription ID (Azure)                                                           |
| attributes     | entityName                             | string   | Human-readable name of the entity                                                       |
| attributes     | entityProviders [*required*]      | [string] | Cloud providers associated with the entity                                              |
| attributes     | entityRoles                            | [string] | Roles associated with the entity                                                        |
| attributes     | entityType [*required*]           | string   | Type of the entity (e.g., aws_iam_user, aws_ec2_instance)                               |
| attributes     | firstDetected [*required*]        | int64    | Timestamp when the entity was first detected (Unix milliseconds)                        |
| attributes     | lastActivityTitle [*required*]    | string   | Title of the most recent signal detected for this entity                                |
| attributes     | lastDetected [*required*]         | int64    | Timestamp when the entity was last detected (Unix milliseconds)                         |
| attributes     | riskScore [*required*]            | double   | Current risk score for the entity                                                       |
| attributes     | riskScoreEvolution [*required*]   | double   | Change in risk score compared to previous period                                        |
| attributes     | severity [*required*]             | enum     | Severity level based on risk score Allowed enum values: `critical,high,medium,low,info` |
| attributes     | signalsDetected [*required*]      | int64    | Number of security signals detected for this entity                                     |
| data           | id [*required*]                   | string   | Unique identifier for the entity                                                        |
| data           | type [*required*]                 | enum     | Resource type Allowed enum values: `security_entity_risk_score`                         |
|                | meta [*required*]                 | object   | Metadata for pagination                                                                 |
| meta           | pageNumber [*required*]           | int64    | Current page number (1-indexed)                                                         |
| meta           | pageSize [*required*]             | int64    | Number of items per page                                                                |
| meta           | queryId [*required*]              | string   | Query ID for pagination consistency                                                     |
| meta           | totalRowCount [*required*]        | int64    | Total number of entities matching the query                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "configRisks": {
          "hasIdentityRisk": false,
          "hasMisconfiguration": true,
          "hasPrivilegedRole": true,
          "isPrivileged": false,
          "isProduction": true,
          "isPubliclyAccessible": true
        },
        "entityID": "arn:aws:iam::123456789012:user/john.doe",
        "entityMetadata": {
          "accountID": "123456789012",
          "environments": [
            "production",
            "us-east-1"
          ],
          "mitreTactics": [
            "Credential Access",
            "Privilege Escalation"
          ],
          "mitreTechniques": [
            "T1078",
            "T1098"
          ],
          "projectID": "my-gcp-project",
          "services": [
            "api-gateway",
            "lambda"
          ],
          "sources": [
            "cloudtrail",
            "cloud-security-posture-management"
          ],
          "subscriptionID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        },
        "entityName": "john.doe",
        "entityProviders": [
          "aws"
        ],
        "entityRoles": [
          "Admin",
          "Developer"
        ],
        "entityType": "aws_iam_user",
        "firstDetected": 1704067200000,
        "lastActivityTitle": "Suspicious API call detected",
        "lastDetected": 1705276800000,
        "riskScore": 85.5,
        "riskScoreEvolution": 12.3,
        "severity": "critical",
        "signalsDetected": 15
      },
      "id": "arn:aws:iam::123456789012:user/john.doe",
      "type": "security_entity_risk_score"
    }
  ],
  "meta": {
    "pageNumber": 1,
    "pageSize": 10,
    "queryId": "abc123def456",
    "totalRowCount": 150
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Parent field | Field                    | Type     | Description                                                                     |
| ------------ | ------------------------ | -------- | ------------------------------------------------------------------------------- |
|              | errors [*required*] | [object] | A list of errors.                                                               |
| errors       | detail                   | string   | A human-readable explanation specific to this occurrence of the error.          |
| errors       | meta                     | object   | Non-standard meta-information about the error                                   |
| errors       | source                   | object   | References to the source of the error.                                          |
| source       | header                   | string   | A string indicating the name of a single request header which caused the error. |
| source       | parameter                | string   | A string indicating which URI query parameter caused the error.                 |
| source       | pointer                  | string   | A JSON pointer to the value in the request document that caused the error.      |
| errors       | status                   | string   | Status code of the response.                                                    |
| errors       | title                    | string   | Short human-readable summary of the error.                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/security-entities/risk-scores" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}
