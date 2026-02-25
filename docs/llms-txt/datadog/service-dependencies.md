# Source: https://docs.datadoghq.com/api/latest/service-dependencies.md

---
title: Service Dependencies
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Service Dependencies
---

# Service Dependencies

APM Service Map API. For more information, visit the [Service Map page](https://docs.datadoghq.com/tracing/visualization/services_map/).

## Get all APM service dependencies{% #get-all-apm-service-dependencies %}

{% tab title="v1" %}
**Note: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/service_dependencies |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/service_dependencies |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/service_dependencies      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/service_dependencies      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/service_dependencies     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/service_dependencies |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/service_dependencies |

### Overview

Get a list of services from APM and their dependencies. The services retrieved are filtered by environment and a primary tag, if one is defined.

### Arguments

#### Query Strings

| Name                  | Type    | Description                                                                                                 |
| --------------------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| env [*required*] | string  | Specify what APM environment to query service dependencies by.                                              |
| primary_tag           | string  | Specify what primary tag to query service dependencies by.                                                  |
| start                 | integer | Specify the start of the timeframe in epoch seconds to query for. (defaults to 1 hour before end parameter) |
| end                   | integer | Specify the end of the timeframe in epoch seconds to query for. (defaults to current time)                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An object containing a list of APM services and their dependencies.

| Parent field | Field                   | Type     | Description                                         |
| ------------ | ----------------------- | -------- | --------------------------------------------------- |
|              | <any-key>               | object   | An object containing an APM service's dependencies. |
| <any-key>    | calls [*required*] | [string] | A list of dependencies.                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "servica_a": {
    "calls": [
      "service_b",
      "service_c"
    ]
  },
  "service_b": {
    "calls": [
      "service_o"
    ]
  },
  "service_c": {
    "calls": [
      "service_o"
    ]
  },
  "service_o": {
    "calls": []
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Required query argumentsexport env="prod"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/service_dependencies?env=${env}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}

## Get one APM service's dependencies{% #get-one-apm-services-dependencies %}

{% tab title="v1" %}
**Note: This endpoint is in public beta. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).**
| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/service_dependencies/{service} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/service_dependencies/{service} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/service_dependencies/{service}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/service_dependencies/{service}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/service_dependencies/{service}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/service_dependencies/{service} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/service_dependencies/{service} |

### Overview

Get a specific service's immediate upstream and downstream services. The services retrieved are filtered by environment and a primary tag, if one is defined.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                                      |
| ------------------------- | ------ | ------------------------------------------------ |
| service [*required*] | string | The name of the service go get dependencies for. |

#### Query Strings

| Name                  | Type    | Description                                                                                                 |
| --------------------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| env [*required*] | string  | Specify what APM environment to query service dependencies by.                                              |
| primary_tag           | string  | Specify what primary tag to query service dependencies by.                                                  |
| start                 | integer | Specify the start of the timeframe in epoch seconds to query for. (defaults to 1 hour before end parameter) |
| end                   | integer | Specify the end of the timeframe in epoch seconds to query for. (defaults to current time)                  |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
An object with information on APM services that call, and are called by a given service.

| Field     | Type     | Description                                        |
| --------- | -------- | -------------------------------------------------- |
| called_by | [string] | List of service names that call the given service. |
| calls     | [string] | List of service names called by the given service. |
| name      | string   | Name of the APM service being searched for.        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "called_by": [
    "service-a",
    "service-b"
  ],
  "calls": [
    "service-d",
    "service-e"
  ],
  "name": "service-c"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="403" %}
Authentication Error
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

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
                  \# Path parametersexport service="service-c"\# Required query argumentsexport env="prod"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/service_dependencies/${service}?env=${env}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}
