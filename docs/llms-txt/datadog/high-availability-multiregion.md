# Source: https://docs.datadoghq.com/api/latest/high-availability-multiregion.md

---
title: High Availability MultiRegion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > High Availability MultiRegion
---

# High Availability MultiRegion

Configure High Availability Multi-Region (HAMR) connections between Datadog organizations. HAMR provides disaster recovery capabilities by maintaining synchronized data between primary and secondary organizations across different datacenters.

## Create or update HAMR organization connection{% #create-or-update-hamr-organization-connection %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                   |
| ----------------- | ---------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/hamr |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/hamr |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/hamr      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/hamr      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/hamr     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/hamr |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/hamr |

### Overview

Create or update the High Availability Multi-Region (HAMR) organization connection. This endpoint allows you to configure the HAMR connection between the authenticated organization and a target organization, including setting the connection status (ONBOARDING, PASSIVE, FAILOVER, ACTIVE, RECOVERY)

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                                   | Type    | Description                                                                                                                                                                               |
| ------------ | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object  |
| data         | attributes [*required*]            | object  |
| attributes   | hamr_status [*required*]           | enum    | Status of the HAMR connection:                                                                                                                                                            |
| attributes   | is_primary [*required*]            | boolean | Indicates whether this organization is the primary organization in the HAMR relationship. If true, this is the primary organization. If false, this is the secondary/backup organization. |
| attributes   | modified_by [*required*]           | string  | Username or identifier of the user who last modified this HAMR connection.                                                                                                                |
| attributes   | target_org_datacenter [*required*] | string  | Datacenter location of the target organization (e.g., us1, eu1, us5).                                                                                                                     |
| attributes   | target_org_name [*required*]       | string  | Name of the target organization in the HAMR relationship.                                                                                                                                 |
| attributes   | target_org_uuid [*required*]       | string  | UUID of the target organization in the HAMR relationship.                                                                                                                                 |
| data         | id [*required*]                    | string  | The organization UUID for this HAMR connection. Must match the authenticated organization's UUID.                                                                                         |
| data         | type [*required*]                  | enum    | Type of the HAMR organization connection resource. Allowed enum values: `hamr_org_connections`                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                                   | Type    | Description                                                                                                                                                                               |
| ------------ | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object  |
| data         | attributes [*required*]            | object  |
| attributes   | hamr_status [*required*]           | enum    | Status of the HAMR connection:                                                                                                                                                            |
| attributes   | is_primary [*required*]            | boolean | Indicates whether this organization is the primary organization in the HAMR relationship. If true, this is the primary organization. If false, this is the secondary/backup organization. |
| attributes   | modified_at [*required*]           | string  | Timestamp of when this HAMR connection was last modified (RFC3339 format).                                                                                                                |
| attributes   | modified_by [*required*]           | string  | Username or identifier of the user who last modified this HAMR connection.                                                                                                                |
| attributes   | target_org_datacenter [*required*] | string  | Datacenter location of the target organization (e.g., us1, eu1, us5).                                                                                                                     |
| attributes   | target_org_name [*required*]       | string  | Name of the target organization in the HAMR relationship.                                                                                                                                 |
| attributes   | target_org_uuid [*required*]       | string  | UUID of the target organization in the HAMR relationship.                                                                                                                                 |
| data         | id [*required*]                    | string  | The organization UUID for this HAMR connection.                                                                                                                                           |
| data         | type [*required*]                  | enum    | Type of the HAMR organization connection resource. Allowed enum values: `hamr_org_connections`                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_at": "2026-01-13T17:26:48.830968Z",
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
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

{% tab title="500" %}
Internal Server Error
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

### Code Example

##### 
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/hamr" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
  }
}
EOF
                
{% /tab %}

## Get HAMR organization connection{% #get-hamr-organization-connection %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                  |
| ----------------- | --------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/hamr |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/hamr |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/hamr      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/hamr      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/hamr     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/hamr |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/hamr |

### Overview

Retrieve the High Availability Multi-Region (HAMR) organization connection details for the authenticated organization. This endpoint returns information about the HAMR connection configuration, including the target organization, datacenter, status, and whether this is the primary or secondary organization in the HAMR relationship.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field                                   | Type    | Description                                                                                                                                                                               |
| ------------ | --------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object  |
| data         | attributes [*required*]            | object  |
| attributes   | hamr_status [*required*]           | enum    | Status of the HAMR connection:                                                                                                                                                            |
| attributes   | is_primary [*required*]            | boolean | Indicates whether this organization is the primary organization in the HAMR relationship. If true, this is the primary organization. If false, this is the secondary/backup organization. |
| attributes   | modified_at [*required*]           | string  | Timestamp of when this HAMR connection was last modified (RFC3339 format).                                                                                                                |
| attributes   | modified_by [*required*]           | string  | Username or identifier of the user who last modified this HAMR connection.                                                                                                                |
| attributes   | target_org_datacenter [*required*] | string  | Datacenter location of the target organization (e.g., us1, eu1, us5).                                                                                                                     |
| attributes   | target_org_name [*required*]       | string  | Name of the target organization in the HAMR relationship.                                                                                                                                 |
| attributes   | target_org_uuid [*required*]       | string  | UUID of the target organization in the HAMR relationship.                                                                                                                                 |
| data         | id [*required*]                    | string  | The organization UUID for this HAMR connection.                                                                                                                                           |
| data         | type [*required*]                  | enum    | Type of the HAMR organization connection resource. Allowed enum values: `hamr_org_connections`                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "hamr_status": 4,
      "is_primary": true,
      "modified_at": "2026-01-13T17:26:48.830968Z",
      "modified_by": "admin@example.com",
      "target_org_datacenter": "us1",
      "target_org_name": "Production Backup Org",
      "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"
    },
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "type": "hamr_org_connections"
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

{% tab title="404" %}
Not Found
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/hamr" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}
