# Source: https://docs.datadoghq.com/api/latest/integrations.md

---
title: Integrations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Integrations
---

# Integrations

The Integrations API is used to list available integrations and retrieve information about their installation status.

## List Integrations{% #list-integrations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integrations |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integrations |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integrations      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integrations      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integrations     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integrations |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integrations |

### Overview

### Response

{% tab title="200" %}
Successful Response.
{% tab title="Model" %}
Response containing information about multiple integrations.

| Parent field | Field                         | Type     | Description                                                   |
| ------------ | ----------------------------- | -------- | ------------------------------------------------------------- |
|              | data [*required*]        | [object] | Array of integration objects.                                 |
| data         | attributes [*required*]  | object   | Attributes for an integration.                                |
| attributes   | categories [*required*]  | [string] | List of categories associated with the integration.           |
| attributes   | description [*required*] | string   | A description of the integration.                             |
| attributes   | installed [*required*]   | boolean  | Whether the integration is installed.                         |
| attributes   | title [*required*]       | string   | The name of the integration.                                  |
| data         | id [*required*]          | string   | The unique identifier of the integration.                     |
| data         | links                         | object   | Links for the integration resource.                           |
| links        | self                          | string   | Link to the integration resource.                             |
| data         | type [*required*]        | enum     | Integration resource type. Allowed enum values: `integration` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "categories": [
          "Category::Kubernetes",
          "Category::Log Collection"
        ],
        "description": "Calico is a networking and network security solution for containers.",
        "installed": true,
        "title": "calico"
      },
      "id": "calico",
      "links": {
        "self": "/integrations?integrationId=calico"
      },
      "type": "integration"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integrations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}
