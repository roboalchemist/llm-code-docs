# Source: https://docs.datadoghq.com/api/latest/cloud-authentication.md

---
title: Cloud Authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Cloud Authentication
---

# Cloud Authentication

Configure AWS cloud authentication mappings for persona and intake authentication through the Datadog API.

## List AWS cloud authentication persona mappings{% #list-aws-cloud-authentication-persona-mappings %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/cloud_auth/aws/persona_mapping |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/cloud_auth/aws/persona_mapping |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/cloud_auth/aws/persona_mapping      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/cloud_auth/aws/persona_mapping      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/cloud_auth/aws/persona_mapping     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/cloud_auth/aws/persona_mapping |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/cloud_auth/aws/persona_mapping |

### Overview

List all AWS cloud authentication persona mappings. This endpoint retrieves all configured persona mappings that associate AWS IAM principals with Datadog users.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a list of AWS cloud authentication persona mappings

| Parent field | Field                                | Type     | Description                                                                                               |
| ------------ | ------------------------------------ | -------- | --------------------------------------------------------------------------------------------------------- |
|              | data [*required*]               | [object] | List of AWS cloud authentication persona mappings                                                         |
| data         | attributes [*required*]         | object   | Attributes for AWS cloud authentication persona mapping response                                          |
| attributes   | account_identifier [*required*] | string   | Datadog account identifier (email or handle) mapped to the AWS principal                                  |
| attributes   | account_uuid [*required*]       | string   | Datadog account UUID                                                                                      |
| attributes   | arn_pattern [*required*]        | string   | AWS IAM ARN pattern to match for authentication                                                           |
| data         | id [*required*]                 | string   | Unique identifier for the persona mapping                                                                 |
| data         | type [*required*]               | enum     | Type identifier for AWS cloud authentication persona mapping Allowed enum values: `aws_cloud_auth_config` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [{
      "attributes": {
        "account_identifier": "test@test.com",
        "account_uuid": "12bbdc5c-5966-47e0-8733-285f9e44bcf4",
        "arn_pattern": "arn:aws:iam::123456789012:user/testuser"
      },
      "id": "c5c758c6-18c2-4484-ae3f-46b84128404a",
      "type": "aws_cloud_auth_config"
    }]
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
  "errors": [{
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }]
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
  "errors": [{
      "detail": "Missing required attribute in body",
      "meta": {},
      "source": {
        "header": "Authorization",
        "parameter": "limit",
        "pointer": "/data/attributes/title"
      },
      "status": "400",
      "title": "Bad Request"
    }]
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
  "errors": ["Bad Request"]
}

```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/cloud_auth/aws/persona_mapping" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}
