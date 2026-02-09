# Source: https://docs.datadoghq.com/api/latest/status-pages.md

---
title: Status Pages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Status Pages
---

# Status Pages

Manage your status pages and communicate service disruptions to stakeholders via Datadog's API. See the [Status Pages documentation](https://docs.datadoghq.com/incident_response/status_pages/) for more information.

## Create status page{% #create-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/statuspages |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/statuspages |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/statuspages      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/statuspages      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/statuspages     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/statuspages |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/statuspages |

### Overview

Creates a new status page. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Query Strings

| Name    | Type   | Description                                                                                             |
| ------- | ------ | ------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                                | Type     | Description                                                                                                                                             |
| ------------ | ------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                                 | object   |
| data         | attributes [*required*]         | object   | The supported attributes for creating a status page.                                                                                                    |
| attributes   | company_logo                         | string   | The base64-encoded image data displayed on the status page.                                                                                             |
| attributes   | components                           | [object] | The components displayed on the status page.                                                                                                            |
| components   | components                           | [object] | If creating a component of type `group`, the components to create within the group.                                                                     |
| components   | id                                   | uuid     | The ID of the grouped component.                                                                                                                        |
| components   | name                                 | string   | The name of the grouped component.                                                                                                                      |
| components   | position                             | int64    | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components   | status                               | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components   | type                                 | enum     | The type of the component. Allowed enum values: `component`                                                                                             |
| components   | id                                   | uuid     | The ID of the component.                                                                                                                                |
| components   | name                                 | string   | The name of the component.                                                                                                                              |
| components   | position                             | int64    | The zero-indexed position of the component.                                                                                                             |
| components   | status                               | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components   | type                                 | enum     | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes   | domain_prefix [*required*]      | string   | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes   | email_header_image                   | string   | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes   | enabled [*required*]            | boolean  | Whether the status page is enabled.                                                                                                                     |
| attributes   | favicon                              | string   | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes   | name [*required*]               | string   | The name of the status page.                                                                                                                            |
| attributes   | subscriptions_enabled                | boolean  | Whether users can subscribe to the status page.                                                                                                         |
| attributes   | type [*required*]               | enum     | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes   | visualization_type [*required*] | enum     | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data         | type [*required*]               | enum     | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "A Status Page",
      "domain_prefix": "5e2fd69be33e79aa",
      "components": [
        {
          "name": "Login",
          "type": "component",
          "position": 0
        },
        {
          "name": "Settings",
          "type": "component",
          "position": 1
        }
      ],
      "enabled": true,
      "type": "internal",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "type": "status_pages"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "company_logo": "string",
      "components": [
        {
          "components": [
            {
              "id": "string",
              "name": "string",
              "position": "integer",
              "status": "string",
              "type": "component"
            }
          ],
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_domain": "string",
      "custom_domain_enabled": false,
      "domain_prefix": "string",
      "email_header_image": "string",
      "enabled": false,
      "favicon": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "page_url": "string",
      "subscriptions_enabled": false,
      "type": "public",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "status_pages"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "A Status Page",
      "domain_prefix": "5e2fd69be33e79aa",
      "components": [
        {
          "name": "Login",
          "type": "component",
          "position": 0
        },
        {
          "name": "Settings",
          "type": "component",
          "position": 1
        }
      ],
      "enabled": true,
      "type": "internal",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "type": "status_pages"
  }
}
EOF
                        
{% /tab %}

## Update status page{% #update-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                     |
| ----------------- | ---------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/statuspages/{page_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/statuspages/{page_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/statuspages/{page_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/statuspages/{page_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/statuspages/{page_id} |

### Overview

Updates an existing status page's attributes. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name               | Type    | Description                                                                                             |
| ------------------ | ------- | ------------------------------------------------------------------------------------------------------- |
| delete_subscribers | boolean | Whether to delete existing subscribers when updating a status page's type.                              |
| include            | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type    | Description                                                                                                                                             |
| ------------ | ---------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object  |
| data         | attributes [*required*] | object  | The supported attributes for updating a status page.                                                                                                    |
| attributes   | company_logo                 | string  | The base64-encoded image data displayed on the status page.                                                                                             |
| attributes   | domain_prefix                | string  | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes   | email_header_image           | string  | The base64-encoded image data displayed in email notifications sent to status page subscribers.                                                         |
| attributes   | enabled                      | boolean | Whether the status page is enabled.                                                                                                                     |
| attributes   | favicon                      | string  | The base64-encoded image data displayed in the browser tab.                                                                                             |
| attributes   | name                         | string  | The name of the status page.                                                                                                                            |
| attributes   | subscriptions_enabled        | boolean | Whether users can subscribe to the status page.                                                                                                         |
| attributes   | type                         | enum    | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes   | visualization_type           | enum    | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data         | id [*required*]         | uuid    | The ID of the status page.                                                                                                                              |
| data         | type [*required*]       | enum    | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "A Status Page in US1"
    },
    "id": "string",
    "type": "status_pages"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "company_logo": "string",
      "components": [
        {
          "components": [
            {
              "id": "string",
              "name": "string",
              "position": "integer",
              "status": "string",
              "type": "component"
            }
          ],
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_domain": "string",
      "custom_domain_enabled": false,
      "domain_prefix": "string",
      "email_header_image": "string",
      "enabled": false,
      "favicon": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "page_url": "string",
      "subscriptions_enabled": false,
      "type": "public",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "status_pages"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "A Status Page in US1"
    },
    "id": "string",
    "type": "status_pages"
  }
}
EOF
                        
{% /tab %}

## List status pages{% #list-status-pages %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages |

### Overview

Lists all status pages for the organization. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Query Strings

| Name         | Type    | Description                                                                                             |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------- |
| page[offset] | integer | Offset to use as the start of the page.                                                                 |
| page[limit]  | integer | The number of status pages to return per page.                                                          |
| include      | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data [*required*] | [object]        |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
|                       | meta                   | object          | Response metadata.                                                                                                                                      |
| meta                  | page                   | object          | Offset-based pagination schema.                                                                                                                         |
| page                  | first_offset           | int64           | Integer representing the offset to fetch the first page of results.                                                                                     |
| page                  | last_offset            | int64           | Integer representing the offset to fetch the last page of results.                                                                                      |
| page                  | limit                  | int64           | Integer representing the number of elements to returned in the results.                                                                                 |
| page                  | next_offset            | int64           | Integer representing the index of the first element in the next page of results. Equal to page size added to the current offset.                        |
| page                  | offset                 | int64           | Integer representing the index of the first element in the results.                                                                                     |
| page                  | prev_offset            | int64           | Integer representing the index of the first element in the previous page of results.                                                                    |
| page                  | total                  | int64           | Integer representing the total number of elements available.                                                                                            |
| page                  | type                   | enum            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "company_logo": "string",
        "components": [
          {
            "components": [
              {
                "id": "string",
                "name": "string",
                "position": "integer",
                "status": "string",
                "type": "component"
              }
            ],
            "id": "string",
            "name": "string",
            "position": "integer",
            "status": "string",
            "type": "component"
          }
        ],
        "created_at": "2019-09-19T10:00:00.000Z",
        "custom_domain": "string",
        "custom_domain_enabled": false,
        "domain_prefix": "string",
        "email_header_image": "string",
        "enabled": false,
        "favicon": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "page_url": "string",
        "subscriptions_enabled": false,
        "type": "public",
        "visualization_type": "bars_and_uptime_percentage"
      },
      "id": "string",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        }
      },
      "type": "status_pages"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ],
  "meta": {
    "page": {
      "first_offset": 0,
      "last_offset": 900,
      "limit": 100,
      "next_offset": 100,
      "offset": 0,
      "prev_offset": 100,
      "total": 1000,
      "type": "offset_limit"
    }
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Get status page{% #get-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                   |
| ----------------- | -------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id} |

### Overview

Retrieves a specific status page by its ID. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name    | Type   | Description                                                                                             |
| ------- | ------ | ------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | Base64-encoded image data displayed on the status page.                                                                                                 |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component. Relative to the other components in the group.                                                              |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| data                  | id                     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | included               | [ <oneOf>] | The included related resources of a status page. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "company_logo": "string",
      "components": [
        {
          "components": [
            {
              "id": "string",
              "name": "string",
              "position": "integer",
              "status": "string",
              "type": "component"
            }
          ],
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "custom_domain": "string",
      "custom_domain_enabled": false,
      "domain_prefix": "string",
      "email_header_image": "string",
      "enabled": false,
      "favicon": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "page_url": "string",
      "subscriptions_enabled": false,
      "type": "public",
      "visualization_type": "bars_and_uptime_percentage"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      }
    },
    "type": "status_pages"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Delete status page{% #delete-status-page %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/statuspages/{page_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/statuspages/{page_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/statuspages/{page_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/statuspages/{page_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/statuspages/{page_id} |

### Overview

Deletes a status page by its ID. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Create component{% #create-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/statuspages/{page_id}/components     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components |

### Overview

Creates a new component. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field  | Field                        | Type     | Description                                                                                       |
| ------------- | ---------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
|               | data                         | object   |
| data          | attributes [*required*] | object   | The supported attributes for creating a component.                                                |
| attributes    | components                   | [object] | If creating a component of type `group`, the components to create within the group.               |
| components    | name [*required*]       | string   | The name of the grouped component.                                                                |
| components    | position [*required*]   | int64    | The zero-indexed position of the grouped component relative to the other components in the group. |
| components    | type [*required*]       | enum     | The type of the component. Allowed enum values: `component`                                       |
| attributes    | name [*required*]       | string   | The name of the component.                                                                        |
| attributes    | position [*required*]   | int64    | The zero-indexed position of the component.                                                       |
| attributes    | type [*required*]       | enum     | The type of the component. Allowed enum values: `component,group`                                 |
| data          | relationships                | object   | The supported relationships for creating a component.                                             |
| relationships | group                        | object   | The group to create the component within.                                                         |
| group         | data [*required*]       | object   |
| data          | id [*required*]         | uuid     | The ID of the group.                                                                              |
| data          | type [*required*]       | enum     | Components resource type. Allowed enum values: `components`                                       |
| data          | type [*required*]       | enum     | Components resource type. Allowed enum values: `components`                                       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Logs",
      "position": 0,
      "type": "component"
    },
    "type": "components"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components": [
        {
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "position": "integer",
      "status": "operational",
      "type": "component"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "group": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "components"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "components"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Logs",
      "position": 0,
      "type": "component"
    },
    "type": "components"
  }
}
EOF
                        
{% /tab %}

## Update component{% #update-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |

### Overview

Updates an existing component's attributes. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                |
| ------------------------------ | ------ | -------------------------- |
| page_id [*required*]      | string | The ID of the status page. |
| component_id [*required*] | string | The ID of the component.   |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                        |
| ------------ | ---------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
|              | data                         | object |
| data         | attributes [*required*] | object | The supported attributes for updating a component.                                                                                 |
| attributes   | name                         | string | The name of the component.                                                                                                         |
| attributes   | position                     | int64  | The position of the component. If the component belongs to a group, the position is relative to the other components in the group. |
| data         | id [*required*]         | uuid   | The ID of the component.                                                                                                           |
| data         | type [*required*]       | enum   | Components resource type. Allowed enum values: `components`                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "name": "Logs Indexing"
    },
    "id": "c34e5b83-90fe-4de2-087b-ea1f64387277",
    "type": "components"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components": [
        {
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "position": "integer",
      "status": "operational",
      "type": "component"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "group": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "components"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "components"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export component_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components/${component_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "name": "Logs Indexing"
    },
    "id": "c34e5b83-90fe-4de2-087b-ea1f64387277",
    "type": "components"
  }
}
EOF
                        
{% /tab %}

## List components{% #list-components %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}/components     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components |

### Overview

Lists all components for a status page. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data [*required*] | [object]        |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "components": [
          {
            "id": "string",
            "name": "string",
            "position": "integer",
            "status": "string",
            "type": "component"
          }
        ],
        "created_at": "2019-09-19T10:00:00.000Z",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "position": "integer",
        "status": "operational",
        "type": "component"
      },
      "id": "string",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "group": {
          "data": {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "type": "components"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "status_page": {
          "data": {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "type": "status_pages"
          }
        }
      },
      "type": "components"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Get component{% #get-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |

### Overview

Retrieves a specific component by its ID. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                |
| ------------------------------ | ------ | -------------------------- |
| page_id [*required*]      | string | The ID of the status page. |
| component_id [*required*] | string | The ID of the component.   |

#### Query Strings

| Name    | Type   | Description                                                                                                                 |
| ------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page, group. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                  | Type            | Description                                                                                                                                             |
| --------------------- | ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                   | object          |
| data                  | attributes             | object          | The attributes of a component.                                                                                                                          |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            |
| components            | name                   | string          |
| components            | position               | int64           |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| data                  | id                     | uuid            | The ID of the component.                                                                                                                                |
| data                  | relationships          | object          | The relationships of a component.                                                                                                                       |
| relationships         | created_by_user        | object          | The Datadog user who created the component.                                                                                                             |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component.                                                                                                   |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component belongs to.                                                                                                                     |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the group the component belongs to.                                                                                                           |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component.                                                                                                       |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component belongs to.                                                                                                               |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page the component belongs to.                                                                                                     |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
|                       | included               | [ <oneOf>] | The included related resources of a component. Client must explicitly request these resources by name in the `include` query parameter.                 |
| included              | Option 1               | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes             | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                  | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                 | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                   | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                   | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                   | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                     | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2               | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes             | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo           | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components             | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components             | [object]        |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                     | uuid            | The ID of the component.                                                                                                                                |
| components            | name                   | string          | The name of the component.                                                                                                                              |
| components            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at             | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain          | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled  | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix          | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image     | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at            | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                   | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url               | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled  | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                   | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type     | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                     | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships          | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user        | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| included              | Option 3               | object          | The included component group resource.                                                                                                                  |
| Option 3              | attributes             | object          | The attributes of a component group.                                                                                                                    |
| attributes            | components             | [object]        | If the component is of type `group`, the components within the group.                                                                                   |
| components            | id                     | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                   | string          | The name of the grouped component.                                                                                                                      |
| components            | position               | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                   | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| attributes            | created_at             | date-time       | Timestamp of when the component was created.                                                                                                            |
| attributes            | modified_at            | date-time       | Timestamp of when the component was last modified.                                                                                                      |
| attributes            | name                   | string          | The name of the component.                                                                                                                              |
| attributes            | position               | int64           | The zero-indexed position of the component.                                                                                                             |
| attributes            | status                 | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | type [*required*] | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| Option 3              | id                     | uuid            | The ID of the component.                                                                                                                                |
| Option 3              | relationships          | object          | The relationships of a component group.                                                                                                                 |
| relationships         | created_by_user        | object          | The Datadog user who created the component group.                                                                                                       |
| created_by_user       | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who created the component group.                                                                                             |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | group                  | object          | The group the component group belongs to.                                                                                                               |
| group                 | data [*required*] | object          |
| data                  | id [*required*]   | uuid            |
| data                  | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |
| relationships         | last_modified_by_user  | object          | The Datadog user who last modified the component group.                                                                                                 |
| last_modified_by_user | data [*required*] | object          |
| data                  | id [*required*]   | string          | The ID of the Datadog user who last modified the component group.                                                                                       |
| data                  | type [*required*] | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page            | object          | The status page the component group belongs to.                                                                                                         |
| status_page           | data [*required*] | object          |
| data                  | id [*required*]   | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*] | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| Option 3              | type [*required*] | enum            | Components resource type. Allowed enum values: `components`                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components": [
        {
          "id": "string",
          "name": "string",
          "position": "integer",
          "status": "string",
          "type": "component"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "string",
      "position": "integer",
      "status": "operational",
      "type": "component"
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "group": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "components"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "components"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export component_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components/${component_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Delete component{% #delete-component %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/statuspages/{page_id}/components/{component_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/components/{component_id} |

### Overview

Deletes a component by its ID. This endpoint requires the `status_pages_settings_write` permission.

### Arguments

#### Path Parameters

| Name                           | Type   | Description                |
| ------------------------------ | ------ | -------------------------- |
| page_id [*required*]      | string | The ID of the status page. |
| component_id [*required*] | string | The ID of the component.   |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export component_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/components/${component_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Create degradation{% #create-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                 |
| ----------------- | ---------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations |

### Overview

Creates a new degradation. This endpoint requires the `status_pages_incident_write` permission.

### Arguments

#### Path Parameters

| Name                      | Type   | Description                |
| ------------------------- | ------ | -------------------------- |
| page_id [*required*] | string | The ID of the status page. |

#### Query Strings

| Name               | Type    | Description                                                                                                          |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------- |
| notify_subscribers | boolean | Whether to notify page subscribers of the degradation.                                                               |
| include            | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field        | Field                                 | Type     | Description                                                                                          |
| ------------------- | ------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
|                     | data                                  | object   |
| data                | attributes [*required*]          | object   | The supported attributes for creating a degradation.                                                 |
| attributes          | components_affected [*required*] | [object] | The components affected by the degradation.                                                          |
| components_affected | id [*required*]                  | uuid     | The ID of the component. Must be a component of type `component`.                                    |
| components_affected | name                                  | string   |
| components_affected | status [*required*]              | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage` |
| attributes          | description                           | string   | The description of the degradation.                                                                  |
| attributes          | status [*required*]              | enum     | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`   |
| attributes          | title [*required*]               | string   | The title of the degradation.                                                                        |
| data                | type [*required*]                | enum     | Degradations resource type. Allowed enum values: `degradations`                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "4e9d3726-bdd7-0079-613c-e9aaba89eb01",
          "status": "major_outage"
        }
      ],
      "description": "Our API is experiencing elevated latency. We are investigating the issue.",
      "status": "investigating",
      "title": "Elevated API Latency"
    },
    "type": "degradations"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                     | object          |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "name": "string",
          "status": "operational"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "status": "investigating",
      "title": "string",
      "updates": [
        {
          "components_affected": [
            {
              "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
              "name": "string",
              "status": "operational"
            }
          ],
          "created_at": "2019-09-19T10:00:00.000Z",
          "description": "string",
          "id": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "status": "investigating"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "degradations"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "4e9d3726-bdd7-0079-613c-e9aaba89eb01",
          "status": "major_outage"
        }
      ],
      "description": "Our API is experiencing elevated latency. We are investigating the issue.",
      "status": "investigating",
      "title": "Elevated API Latency"
    },
    "type": "degradations"
  }
}
EOF
                        
{% /tab %}

## Update degradation{% #update-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |

### Overview

Updates an existing degradation's attributes. This endpoint requires the `status_pages_incident_write` permission.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| page_id [*required*]        | string | The ID of the status page. |
| degradation_id [*required*] | string | The ID of the degradation. |

#### Query Strings

| Name               | Type    | Description                                                                                                          |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------- |
| notify_subscribers | boolean | Whether to notify page subscribers of the degradation.                                                               |
| include            | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field        | Field                        | Type     | Description                                                                                          |
| ------------------- | ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
|                     | data                         | object   |
| data                | attributes [*required*] | object   | The supported attributes for updating a degradation.                                                 |
| attributes          | components_affected          | [object] | The components affected by the degradation.                                                          |
| components_affected | id [*required*]         | uuid     | The ID of the component. Must be a component of type `component`.                                    |
| components_affected | name                         | string   |
| components_affected | status [*required*]     | enum     | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage` |
| attributes          | description                  | string   | The description of the degradation.                                                                  |
| attributes          | status                       | enum     | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`   |
| attributes          | title                        | string   | The title of the degradation.                                                                        |
| data                | id [*required*]         | uuid     | The ID of the degradation.                                                                           |
| data                | type [*required*]       | enum     | Degradations resource type. Allowed enum values: `degradations`                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "title": "Elevated API Latency in US1"
    },
    "id": "81335836-b858-2e64-43d6-5b27ba1e6d8e",
    "type": "degradations"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                     | object          |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "name": "string",
          "status": "operational"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "status": "investigating",
      "title": "string",
      "updates": [
        {
          "components_affected": [
            {
              "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
              "name": "string",
              "status": "operational"
            }
          ],
          "created_at": "2019-09-19T10:00:00.000Z",
          "description": "string",
          "id": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "status": "investigating"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "degradations"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                          \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export degradation_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations/${degradation_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "title": "Elevated API Latency in US1"
    },
    "id": "81335836-b858-2e64-43d6-5b27ba1e6d8e",
    "type": "degradations"
  }
}
EOF
                        
{% /tab %}

## List degradations{% #list-degradations %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/degradations |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/degradations |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/degradations      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/degradations      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/degradations     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/degradations |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/degradations |

### Overview

Lists all degradations for the organization. Optionally filter by status and page. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Query Strings

| Name            | Type    | Description                                                                                                          |
| --------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| filter[page_id] | string  | Optional page id filter.                                                                                             |
| page[offset]    | integer | Offset to use as the start of the page.                                                                              |
| page[limit]     | integer | The number of degradations to return per page.                                                                       |
| include         | string  | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |
| filter[status]  | string  | Optional degradation status filter. Supported values: investigating, identified, monitoring, resolved.               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data [*required*]   | [object]        |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
|                       | meta                     | object          | Response metadata.                                                                                                                                      |
| meta                  | page                     | object          | Offset-based pagination schema.                                                                                                                         |
| page                  | first_offset             | int64           | Integer representing the offset to fetch the first page of results.                                                                                     |
| page                  | last_offset              | int64           | Integer representing the offset to fetch the last page of results.                                                                                      |
| page                  | limit                    | int64           | Integer representing the number of elements to returned in the results.                                                                                 |
| page                  | next_offset              | int64           | Integer representing the index of the first element in the next page of results. Equal to page size added to the current offset.                        |
| page                  | offset                   | int64           | Integer representing the index of the first element in the results.                                                                                     |
| page                  | prev_offset              | int64           | Integer representing the index of the first element in the previous page of results.                                                                    |
| page                  | total                    | int64           | Integer representing the total number of elements available.                                                                                            |
| page                  | type                     | enum            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "components_affected": [
          {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "name": "string",
            "status": "operational"
          }
        ],
        "created_at": "2019-09-19T10:00:00.000Z",
        "description": "string",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "status": "investigating",
        "title": "string",
        "updates": [
          {
            "components_affected": [
              {
                "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
                "name": "string",
                "status": "operational"
              }
            ],
            "created_at": "2019-09-19T10:00:00.000Z",
            "description": "string",
            "id": "string",
            "modified_at": "2019-09-19T10:00:00.000Z",
            "status": "investigating"
          }
        ]
      },
      "id": "string",
      "relationships": {
        "created_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "last_modified_by_user": {
          "data": {
            "id": "",
            "type": "users"
          }
        },
        "status_page": {
          "data": {
            "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
            "type": "status_pages"
          }
        }
      },
      "type": "degradations"
    }
  ],
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
    }
  ],
  "meta": {
    "page": {
      "first_offset": 0,
      "last_offset": 900,
      "limit": 100,
      "next_offset": 100,
      "offset": 0,
      "prev_offset": 100,
      "total": 1000,
      "type": "offset_limit"
    }
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/degradations" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Get degradation{% #get-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |

### Overview

Retrieves a specific degradation by its ID. This endpoint requires the `status_pages_settings_read` permission.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| page_id [*required*]        | string | The ID of the status page. |
| degradation_id [*required*] | string | The ID of the degradation. |

#### Query Strings

| Name    | Type   | Description                                                                                                          |
| ------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| include | string | Comma-separated list of resources to include. Supported values: created_by_user, last_modified_by_user, status_page. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field          | Field                    | Type            | Description                                                                                                                                             |
| --------------------- | ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       | data                     | object          |
| data                  | attributes               | object          | The attributes of a degradation.                                                                                                                        |
| attributes            | components_affected      | [object]        | Components affected by the degradation.                                                                                                                 |
| components_affected   | id [*required*]     | uuid            | The ID of the component.                                                                                                                                |
| components_affected   | name                     | string          | The name of the component.                                                                                                                              |
| components_affected   | status [*required*] | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| attributes            | created_at               | date-time       | Timestamp of when the degradation was created.                                                                                                          |
| attributes            | description              | string          | Description of the degradation.                                                                                                                         |
| attributes            | modified_at              | date-time       | Timestamp of when the degradation was last modified.                                                                                                    |
| attributes            | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| attributes            | title                    | string          | Title of the degradation.                                                                                                                               |
| attributes            | updates                  | [object]        | Past updates made to the degradation.                                                                                                                   |
| updates               | components_affected      | [object]        | The components affected at the time of the update.                                                                                                      |
| components_affected   | id [*required*]     | uuid            | Identifier of the component affected at the time of the update.                                                                                         |
| components_affected   | name                     | string          | The name of the component affected at the time of the update.                                                                                           |
| components_affected   | status [*required*] | enum            | The status of the component affected at the time of the update. Allowed enum values: `operational,degraded,partial_outage,major_outage`                 |
| updates               | created_at               | date-time       | Timestamp of when the update was created.                                                                                                               |
| updates               | description              | string          | Description of the update.                                                                                                                              |
| updates               | id                       | uuid            | Identifier of the update.                                                                                                                               |
| updates               | modified_at              | date-time       | Timestamp of when the update was last modified.                                                                                                         |
| updates               | status                   | enum            | The status of the degradation. Allowed enum values: `investigating,identified,monitoring,resolved`                                                      |
| data                  | id                       | uuid            | The ID of the degradation.                                                                                                                              |
| data                  | relationships            | object          | The relationships of a degradation.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the degradation.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the degradation.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the degradation.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the degradation.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | status_page              | object          | The status page the degradation belongs to.                                                                                                             |
| status_page           | data [*required*]   | object          |
| data                  | id [*required*]     | uuid            | The ID of the status page.                                                                                                                              |
| data                  | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |
| data                  | type [*required*]   | enum            | Degradations resource type. Allowed enum values: `degradations`                                                                                         |
|                       | included                 | [ <oneOf>] | The included related resources of a degradation. Client must explicitly request these resources by name in the `include` query parameter.               |
| included              | Option 1                 | object          | The included Datadog user resource.                                                                                                                     |
| Option 1              | attributes               | object          | Attributes of the Datadog user.                                                                                                                         |
| attributes            | email                    | string          | The email of the Datadog user.                                                                                                                          |
| attributes            | handle                   | string          | The handle of the Datadog user.                                                                                                                         |
| attributes            | icon                     | string          | The icon of the Datadog user.                                                                                                                           |
| attributes            | name                     | string          | The name of the Datadog user.                                                                                                                           |
| attributes            | uuid                     | string          | The UUID of the Datadog user.                                                                                                                           |
| Option 1              | id                       | uuid            | The ID of the Datadog user.                                                                                                                             |
| Option 1              | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| included              | Option 2                 | object          | The included status page resource.                                                                                                                      |
| Option 2              | attributes               | object          | The attributes of a status page.                                                                                                                        |
| attributes            | company_logo             | string          | The base64-encoded image data displayed in the company logo.                                                                                            |
| attributes            | components               | [object]        | Components displayed on the status page.                                                                                                                |
| components            | components               | [object]        |
| components            | id                       | uuid            | The ID of the grouped component.                                                                                                                        |
| components            | name                     | string          | The name of the grouped component.                                                                                                                      |
| components            | position                 | int64           | The zero-indexed position of the grouped component. Relative to the other components in the group.                                                      |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component`                                                                                             |
| components            | id                       | uuid            | The ID of the component.                                                                                                                                |
| components            | name                     | string          | The name of the component.                                                                                                                              |
| components            | position                 | int64           | The zero-indexed position of the component.                                                                                                             |
| components            | status                   | enum            | The status of the component. Allowed enum values: `operational,degraded,partial_outage,major_outage`                                                    |
| components            | type                     | enum            | The type of the component. Allowed enum values: `component,group`                                                                                       |
| attributes            | created_at               | date-time       | Timestamp of when the status page was created.                                                                                                          |
| attributes            | custom_domain            | string          | If configured, the url that the status page is accessible at.                                                                                           |
| attributes            | custom_domain_enabled    | boolean         | Whether the custom domain is configured.                                                                                                                |
| attributes            | domain_prefix            | string          | The subdomain of the status page's url taking the form `https://{domain_prefix}.statuspage.datadoghq.com`. Globally unique across Datadog Status Pages. |
| attributes            | email_header_image       | string          | Base64-encoded image data included in email notifications sent to status page subscribers.                                                              |
| attributes            | enabled                  | boolean         | Whether the status page is enabled.                                                                                                                     |
| attributes            | favicon                  | string          | Base64-encoded image data displayed in the browser tab.                                                                                                 |
| attributes            | modified_at              | date-time       | Timestamp of when the status page was last modified.                                                                                                    |
| attributes            | name                     | string          | The name of the status page.                                                                                                                            |
| attributes            | page_url                 | string          | The url that the status page is accessible at.                                                                                                          |
| attributes            | subscriptions_enabled    | boolean         | Whether users can subscribe to the status page.                                                                                                         |
| attributes            | type                     | enum            | The type of the status page controlling how the status page is accessed. Allowed enum values: `public,internal`                                         |
| attributes            | visualization_type       | enum            | The visualization type of the status page. Allowed enum values: `bars_and_uptime_percentage,bars_only,component_name_only`                              |
| Option 2              | id                       | uuid            | The ID of the status page.                                                                                                                              |
| Option 2              | relationships            | object          | The relationships of a status page.                                                                                                                     |
| relationships         | created_by_user          | object          | The Datadog user who created the status page.                                                                                                           |
| created_by_user       | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who created the status page.                                                                                                 |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| relationships         | last_modified_by_user    | object          | The Datadog user who last modified the status page.                                                                                                     |
| last_modified_by_user | data [*required*]   | object          |
| data                  | id [*required*]     | string          | The ID of the Datadog user who last modified the status page.                                                                                           |
| data                  | type [*required*]   | enum            | Users resource type. Allowed enum values: `users`                                                                                                       |
| Option 2              | type [*required*]   | enum            | Status pages resource type. Allowed enum values: `status_pages`                                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "components_affected": [
        {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "name": "string",
          "status": "operational"
        }
      ],
      "created_at": "2019-09-19T10:00:00.000Z",
      "description": "string",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "status": "investigating",
      "title": "string",
      "updates": [
        {
          "components_affected": [
            {
              "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
              "name": "string",
              "status": "operational"
            }
          ],
          "created_at": "2019-09-19T10:00:00.000Z",
          "description": "string",
          "id": "string",
          "modified_at": "2019-09-19T10:00:00.000Z",
          "status": "investigating"
        }
      ]
    },
    "id": "string",
    "relationships": {
      "created_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "last_modified_by_user": {
        "data": {
          "id": "",
          "type": "users"
        }
      },
      "status_page": {
        "data": {
          "id": "1234abcd-12ab-34cd-56ef-123456abcdef",
          "type": "status_pages"
        }
      }
    },
    "type": "degradations"
  },
  "included": [
    {
      "attributes": {
        "email": "string",
        "handle": "string",
        "icon": "string",
        "name": "string",
        "uuid": "string"
      },
      "id": "string",
      "type": "users"
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export degradation_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations/${degradation_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Delete degradation{% #delete-degradation %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/statuspages/{page_id}/degradations/{degradation_id} |

### Overview

Deletes a degradation by its ID. This endpoint requires the `status_pages_incident_write` permission.

### Arguments

#### Path Parameters

| Name                             | Type   | Description                |
| -------------------------------- | ------ | -------------------------- |
| page_id [*required*]        | string | The ID of the status page. |
| degradation_id [*required*] | string | The ID of the degradation. |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport page_id="1234abcd-12ab-34cd-56ef-123456abcdef"export degradation_id="1234abcd-12ab-34cd-56ef-123456abcdef"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/statuspages/${page_id}/degradations/${degradation_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}
