# Source: https://docs.datadoghq.com/api/latest/jira-integration.md

---
title: Jira Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Jira Integration
---

# Jira Integration

Manage your Jira Integration. Atlassian Jira is a project management and issue tracking tool for teams to coordinate work and handle tasks efficiently.

## Delete Jira issue template{% #delete-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |

### Overview

Delete a Jira issue template by ID.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                 |
| ----------------------------------- | ------ | ------------------------------------------- |
| issue_template_id [*required*] | string | The ID of the Jira issue template to delete |

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
                  \# Path parametersexport issue_template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/${issue_template_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Update Jira issue template{% #update-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |

### Overview

Update a Jira issue template by ID.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                 |
| ----------------------------------- | ------ | ------------------------------------------- |
| issue_template_id [*required*] | string | The ID of the Jira issue template to update |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                  |
| ------------ | ---------------------------- | ------ | -------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | Data object for updating a Jira issue template                                               |
| data         | attributes [*required*] | object | Attributes for updating a Jira issue template                                                |
| attributes   | fields                       | object | Custom fields for the Jira issue template                                                    |
| attributes   | name                         | string | The name of the issue template                                                               |
| data         | type [*required*]       | enum   | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Updated Description",
          "type": "json"
        }
      },
      "name": "test_template_updated"
    },
    "type": "jira-issue-template"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single Jira issue template

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object    | Data object for a Jira issue template                                                        |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test Description",
          "type": "json"
        }
      },
      "issue_type_id": "456",
      "name": "Test Template",
      "project_id": "123"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "relationships": {
      "jira-account": {
        "data": {
          "attributes": {
            "consumer_key": "consumer-key-1",
            "instance_url": "https://example.atlassian.net",
            "last_webhook_timestamp": "2024-01-15T10:30:00Z"
          },
          "id": "account-1",
          "type": "jira-account"
        }
      }
    },
    "type": "jira-issue-template"
  },
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
    }
  ]
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
                  \# Path parametersexport issue_template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/${issue_template_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {},
    "type": "jira-issue-template"
  }
}
EOF
                
{% /tab %}

## Get Jira issue template{% #get-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/jira/issue-templates/{issue_template_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/{issue_template_id} |

### Overview

Get a Jira issue template by ID.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                   |
| ----------------------------------- | ------ | --------------------------------------------- |
| issue_template_id [*required*] | string | The ID of the Jira issue template to retrieve |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single Jira issue template

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object    | Data object for a Jira issue template                                                        |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test Description",
          "type": "json"
        }
      },
      "issue_type_id": "456",
      "name": "Test Template",
      "project_id": "123"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "relationships": {
      "jira-account": {
        "data": {
          "attributes": {
            "consumer_key": "consumer-key-1",
            "instance_url": "https://example.atlassian.net",
            "last_webhook_timestamp": "2024-01-15T10:30:00Z"
          },
          "id": "account-1",
          "type": "jira-account"
        }
      }
    },
    "type": "jira-issue-template"
  },
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
    }
  ]
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
                  \# Path parametersexport issue_template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates/${issue_template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Create Jira issue template{% #create-jira-issue-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/jira/issue-templates      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/jira/issue-templates      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/jira/issue-templates     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates |

### Overview

Create a new Jira issue template.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                | Type   | Description                                                                                  |
| ------------ | -------------------- | ------ | -------------------------------------------------------------------------------------------- |
|              | data                 | object | Data object for creating a Jira issue template                                               |
| data         | attributes           | object | Attributes for creating a Jira issue template                                                |
| attributes   | fields               | object | Custom fields for the Jira issue template                                                    |
| attributes   | issue_type_id        | string | The ID of the Jira issue type                                                                |
| attributes   | jira-account         | object | Reference to the Jira account                                                                |
| jira-account | id [*required*] | uuid   | The ID of the Jira account                                                                   |
| attributes   | name                 | string | The name of the issue template                                                               |
| attributes   | project_id           | string | The ID of the Jira project                                                                   |
| data         | type                 | enum   | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test",
          "type": "json"
        }
      },
      "issue_type_id": "12730",
      "jira-account": {
        "id": "80f16d40-1fba-486e-b1fc-983e6ca19bec"
      },
      "name": "test-template",
      "project_id": "10772"
    },
    "type": "jira-issue-template"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response containing a single Jira issue template

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | object    | Data object for a Jira issue template                                                        |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "fields": {
        "description": {
          "payload": "Test Description",
          "type": "json"
        }
      },
      "issue_type_id": "456",
      "name": "Test Template",
      "project_id": "123"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "relationships": {
      "jira-account": {
        "data": {
          "attributes": {
            "consumer_key": "consumer-key-1",
            "instance_url": "https://example.atlassian.net",
            "last_webhook_timestamp": "2024-01-15T10:30:00Z"
          },
          "id": "account-1",
          "type": "jira-account"
        }
      }
    },
    "type": "jira-issue-template"
  },
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
    }
  ]
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "jira-account": {
        "id": "80f16d40-1fba-486e-b1fc-983e6ca19bec"
      }
    }
  }
}
EOF
                
{% /tab %}

## List Jira issue templates{% #list-jira-issue-templates %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/jira/issue-templates |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/jira/issue-templates |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/jira/issue-templates      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/jira/issue-templates      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/jira/issue-templates     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/jira/issue-templates |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates |

### Overview

Get all Jira issue templates for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing Jira issue templates

| Parent field  | Field                           | Type      | Description                                                                                  |
| ------------- | ------------------------------- | --------- | -------------------------------------------------------------------------------------------- |
|               | data [*required*]          | [object]  | Array of Jira issue template data objects                                                    |
| data          | attributes [*required*]    | object    | Attributes of a Jira issue template                                                          |
| attributes    | fields [*required*]        | object    | Custom fields for the Jira issue template                                                    |
| attributes    | issue_type_id [*required*] | string    | The ID of the Jira issue type                                                                |
| attributes    | name [*required*]          | string    | The name of the issue template                                                               |
| attributes    | project_id [*required*]    | string    | The ID of the Jira project                                                                   |
| data          | id [*required*]            | uuid      | Unique identifier for the Jira issue template                                                |
| data          | relationships                   | object    | Relationships of a Jira issue template                                                       |
| relationships | jira-account [*required*]  | object    | Relationship to a Jira account                                                               |
| jira-account  | data [*required*]          | object    | Data object for a Jira account                                                               |
| data          | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| data          | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| data          | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |
| data          | type [*required*]          | enum      | Type identifier for Jira issue template resources Allowed enum values: `jira-issue-template` |
|               | included                        | [object]  | Array of Jira account data objects                                                           |
| included      | attributes [*required*]    | object    | Attributes of a Jira account                                                                 |
| attributes    | consumer_key [*required*]  | string    | The consumer key for the Jira account                                                        |
| attributes    | instance_url [*required*]  | string    | The URL of the Jira instance                                                                 |
| attributes    | last_webhook_timestamp          | date-time | Timestamp of the last webhook received                                                       |
| included      | id [*required*]            | string    | Unique identifier for the Jira account                                                       |
| included      | type [*required*]          | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account`               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "fields": {
          "description": {
            "payload": "Test Description",
            "type": "json"
          }
        },
        "issue_type_id": "456",
        "name": "Test Template",
        "project_id": "123"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "relationships": {
        "jira-account": {
          "data": {
            "attributes": {
              "consumer_key": "consumer-key-1",
              "instance_url": "https://example.atlassian.net",
              "last_webhook_timestamp": "2024-01-15T10:30:00Z"
            },
            "id": "account-1",
            "type": "jira-account"
          }
        }
      },
      "type": "jira-issue-template"
    }
  ],
  "included": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/issue-templates" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Delete Jira account{% #delete-jira-account %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                       |
| ----------------- | ---------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/jira/accounts/{account_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/jira/accounts/{account_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/jira/accounts/{account_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/jira/accounts/{account_id} |

### Overview

Delete a Jira account by ID.

### Arguments

#### Path Parameters

| Name                         | Type   | Description                          |
| ---------------------------- | ------ | ------------------------------------ |
| account_id [*required*] | string | The ID of the Jira account to delete |

### Response

{% tab title="204" %}
No Content
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
                  \# Path parametersexport account_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/accounts/${account_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## List Jira accounts{% #list-jira-accounts %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/jira/accounts |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/jira/accounts |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/jira/accounts      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/jira/accounts      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/jira/accounts     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/jira/accounts |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/jira/accounts |

### Overview

Get all Jira accounts for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing Jira accounts

| Parent field | Field                          | Type      | Description                                                                    |
| ------------ | ------------------------------ | --------- | ------------------------------------------------------------------------------ |
|              | data [*required*]         | [object]  | Array of Jira account data objects                                             |
| data         | attributes [*required*]   | object    | Attributes of a Jira account                                                   |
| attributes   | consumer_key [*required*] | string    | The consumer key for the Jira account                                          |
| attributes   | instance_url [*required*] | string    | The URL of the Jira instance                                                   |
| attributes   | last_webhook_timestamp         | date-time | Timestamp of the last webhook received                                         |
| data         | id [*required*]           | string    | Unique identifier for the Jira account                                         |
| data         | type [*required*]         | enum      | Type identifier for Jira account resources Allowed enum values: `jira-account` |
|              | meta                           | object    | Metadata for Jira accounts response                                            |
| meta         | public_key                     | string    | Public key for the Jira integration                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "consumer_key": "consumer-key-1",
        "instance_url": "https://example.atlassian.net",
        "last_webhook_timestamp": "2024-01-15T10:30:00Z"
      },
      "id": "account-1",
      "type": "jira-account"
    }
  ],
  "meta": {
    "public_key": "c29tZSBkYXRhIHdpdGggACBhbmQg77u/"
  }
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/jira/accounts" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}
