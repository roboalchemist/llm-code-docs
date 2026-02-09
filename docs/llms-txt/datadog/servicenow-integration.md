# Source: https://docs.datadoghq.com/api/latest/servicenow-integration.md

---
title: ServiceNow Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > ServiceNow Integration
---

# ServiceNow Integration

Manage your ServiceNow Integration. ServiceNow is a cloud-based platform that helps organizations manage digital workflows for enterprise operations.

## Delete ServiceNow template{% #delete-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/integration/servicenow/handles/{template_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/integration/servicenow/handles/{template_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/integration/servicenow/handles/{template_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |

### Overview

Delete a ServiceNow template by ID.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                 |
| ----------------------------- | ------ | ------------------------------------------- |
| template_id [*required*] | string | The ID of the ServiceNow template to delete |

### Response

{% tab title="200" %}
OK
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
                  \# Path parametersexport template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/${template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Update ServiceNow template{% #update-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/integration/servicenow/handles/{template_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/integration/servicenow/handles/{template_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/integration/servicenow/handles/{template_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |

### Overview

Update a ServiceNow template by ID.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                 |
| ----------------------------- | ------ | ------------------------------------------- |
| template_id [*required*] | string | The ID of the ServiceNow template to update |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for updating a ServiceNow template                                                |
| data                 | attributes [*required*]           | object | Attributes for updating a ServiceNow template                                                 |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template-updated",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "type": "servicenow_templates"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single ServiceNow template

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for a ServiceNow template                                                         |
| data                 | attributes [*required*]           | object | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid   | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "type": "servicenow_templates"
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
                  \# Path parametersexport template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/${template_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle_name": "incident-template-updated",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident"
    },
    "type": "servicenow_templates"
  }
}
EOF
                
{% /tab %}

## Get ServiceNow template{% #get-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/handles/{template_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/handles/{template_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/handles/{template_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/{template_id} |

### Overview

Get a ServiceNow template by ID.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                                   |
| ----------------------------- | ------ | --------------------------------------------- |
| template_id [*required*] | string | The ID of the ServiceNow template to retrieve |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing a single ServiceNow template

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for a ServiceNow template                                                         |
| data                 | attributes [*required*]           | object | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid   | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "type": "servicenow_templates"
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
                  \# Path parametersexport template_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles/${template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## Create ServiceNow template{% #create-servicenow-template %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/integration/servicenow/handles      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/integration/servicenow/handles      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/integration/servicenow/handles     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles |

### Overview

Create a new ServiceNow template.

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for creating a ServiceNow template                                                |
| data                 | attributes [*required*]           | object | Attributes for creating a ServiceNow template                                                 |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "type": "servicenow_templates"
  }
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response containing a single ServiceNow template

| Parent field         | Field                                  | Type   | Description                                                                                   |
| -------------------- | -------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | object | Data object for a ServiceNow template                                                         |
| data                 | attributes [*required*]           | object | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid   | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid   | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string |
| attributes           | handle_name [*required*]          | string | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid   | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid   | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid   | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum   | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "fields_mapping": {
        "<any-key>": "string"
      },
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident",
      "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
    },
    "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
    "type": "servicenow_templates"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "handle_name": "incident-template",
      "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "servicenow_tablename": "incident"
    },
    "type": "servicenow_templates"
  }
}
EOF
                
{% /tab %}

## List ServiceNow templates{% #list-servicenow-templates %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                            |
| ----------------- | ----------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/handles |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/handles |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/handles      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/handles      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/handles     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/handles |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles |

### Overview

Get all ServiceNow templates for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow templates

| Parent field         | Field                                  | Type     | Description                                                                                   |
| -------------------- | -------------------------------------- | -------- | --------------------------------------------------------------------------------------------- |
|                      | data [*required*]                 | [object] | Array of ServiceNow template data objects                                                     |
| data                 | attributes [*required*]           | object   | Attributes of a ServiceNow template                                                           |
| attributes           | assignment_group_id                    | uuid     | The ID of the assignment group                                                                |
| attributes           | business_service_id                    | uuid     | The ID of the business service                                                                |
| attributes           | fields_mapping                         | object   | Custom field mappings for the template                                                        |
| additionalProperties | <any-key>                              | string   |
| attributes           | handle_name [*required*]          | string   | The handle name of the template                                                               |
| attributes           | instance_id [*required*]          | uuid     | The ID of the ServiceNow instance                                                             |
| attributes           | servicenow_tablename [*required*] | string   | The name of the destination ServiceNow table                                                  |
| attributes           | user_id                                | uuid     | The ID of the user                                                                            |
| data                 | id [*required*]                   | uuid     | Unique identifier for the ServiceNow template                                                 |
| data                 | type [*required*]                 | enum     | Type identifier for ServiceNow template resources Allowed enum values: `servicenow_templates` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "assignment_group_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "business_service_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "fields_mapping": {
          "<any-key>": "string"
        },
        "handle_name": "incident-template",
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "servicenow_tablename": "incident",
        "user_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "servicenow_templates"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/handles" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## List ServiceNow assignment groups{% #list-servicenow-assignment-groups %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/assignment_groups/{instance_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/assignment_groups/{instance_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/assignment_groups/{instance_id} |

### Overview

Get all assignment groups for a ServiceNow instance.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                       |
| ----------------------------- | ------ | --------------------------------- |
| instance_id [*required*] | string | The ID of the ServiceNow instance |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow assignment groups

| Parent field | Field                                     | Type     | Description                                                                                        |
| ------------ | ----------------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data [*required*]                    | [object] | Array of ServiceNow assignment group data objects                                                  |
| data         | attributes [*required*]              | object   | Attributes of a ServiceNow assignment group                                                        |
| attributes   | assignment_group_name [*required*]   | string   | The name of the assignment group                                                                   |
| attributes   | assignment_group_sys_id [*required*] | string   | The system ID of the assignment group in ServiceNow                                                |
| attributes   | instance_id [*required*]             | uuid     | The ID of the ServiceNow instance                                                                  |
| data         | id [*required*]                      | uuid     | Unique identifier for the ServiceNow assignment group                                              |
| data         | type [*required*]                    | enum     | Type identifier for ServiceNow assignment group resources Allowed enum values: `assignment_groups` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "assignment_group_name": "Network Team",
        "assignment_group_sys_id": "abc123def456",
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "assignment_groups"
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
                  \# Path parametersexport instance_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/assignment_groups/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## List ServiceNow business services{% #list-servicenow-business-services %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/business_services/{instance_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/business_services/{instance_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/business_services/{instance_id} |

### Overview

Get all business services for a ServiceNow instance.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                       |
| ----------------------------- | ------ | --------------------------------- |
| instance_id [*required*] | string | The ID of the ServiceNow instance |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow business services

| Parent field | Field                            | Type     | Description                                                                                        |
| ------------ | -------------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
|              | data [*required*]           | [object] | Array of ServiceNow business service data objects                                                  |
| data         | attributes [*required*]     | object   | Attributes of a ServiceNow business service                                                        |
| attributes   | instance_id [*required*]    | uuid     | The ID of the ServiceNow instance                                                                  |
| attributes   | service_name [*required*]   | string   | The name of the business service                                                                   |
| attributes   | service_sys_id [*required*] | string   | The system ID of the business service in ServiceNow                                                |
| data         | id [*required*]             | uuid     | Unique identifier for the ServiceNow business service                                              |
| data         | type [*required*]           | enum     | Type identifier for ServiceNow business service resources Allowed enum values: `business_services` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "service_name": "IT Support",
        "service_sys_id": "abc123def456"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "business_services"
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
                  \# Path parametersexport instance_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/business_services/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## List ServiceNow users{% #list-servicenow-users %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                        |
| ----------------- | ----------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/users/{instance_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/users/{instance_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/users/{instance_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/users/{instance_id} |

### Overview

Get all users for a ServiceNow instance.

### Arguments

#### Path Parameters

| Name                          | Type   | Description                       |
| ----------------------------- | ------ | --------------------------------- |
| instance_id [*required*] | string | The ID of the ServiceNow instance |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow users

| Parent field | Field                         | Type     | Description                                                                |
| ------------ | ----------------------------- | -------- | -------------------------------------------------------------------------- |
|              | data [*required*]        | [object] | Array of ServiceNow user data objects                                      |
| data         | attributes [*required*]  | object   | Attributes of a ServiceNow user                                            |
| attributes   | email [*required*]       | string   | The email address of the user                                              |
| attributes   | full_name                     | string   | The full name of the user                                                  |
| attributes   | instance_id [*required*] | uuid     | The ID of the ServiceNow instance                                          |
| attributes   | user_name [*required*]   | string   | The username of the ServiceNow user                                        |
| attributes   | user_sys_id [*required*] | string   | The system ID of the user in ServiceNow                                    |
| data         | id [*required*]          | uuid     | Unique identifier for the ServiceNow user                                  |
| data         | type [*required*]        | enum     | Type identifier for ServiceNow user resources Allowed enum values: `users` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "email": "john.doe@example.com",
        "full_name": "John Doe",
        "instance_id": "65b3341b-0680-47f9-a6d4-134db45c603e",
        "user_name": "john.doe",
        "user_sys_id": "abc123def456"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "users"
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
                  \# Path parametersexport instance_id="65b3341b-0680-47f9-a6d4-134db45c603e"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/users/${instance_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}

## List ServiceNow instances{% #list-servicenow-instances %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                              |
| ----------------- | ------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/integration/servicenow/instances |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/integration/servicenow/instances |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/integration/servicenow/instances      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/integration/servicenow/instances      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/integration/servicenow/instances     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/integration/servicenow/instances |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/integration/servicenow/instances |

### Overview

Get all ServiceNow instances for the organization.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response containing ServiceNow instances

| Parent field | Field                           | Type     | Description                                                                       |
| ------------ | ------------------------------- | -------- | --------------------------------------------------------------------------------- |
|              | data [*required*]          | [object] | Array of ServiceNow instance data objects                                         |
| data         | attributes [*required*]    | object   | Attributes of a ServiceNow instance                                               |
| attributes   | instance_name [*required*] | string   | The name of the ServiceNow instance                                               |
| data         | id [*required*]            | uuid     | Unique identifier for the ServiceNow instance                                     |
| data         | type [*required*]          | enum     | Type identifier for ServiceNow instance resources Allowed enum values: `instance` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "instance_name": "my-servicenow-instance"
      },
      "id": "65b3341b-0680-47f9-a6d4-134db45c603e",
      "type": "instance"
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/integration/servicenow/instances" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
{% /tab %}
