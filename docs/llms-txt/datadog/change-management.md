# Source: https://docs.datadoghq.com/api/latest/change-management.md

---
title: Change Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Change Management
---

# Change Management

View and manage change requests within Change Management. See the [Case Management page](https://docs.datadoghq.com/service_management/case_management/) for more information.

## Create a change request{% #create-a-change-request %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/change-management/change-request |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/change-management/change-request |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/change-management/change-request      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/change-management/change-request      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/change-management/change-request     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/change-management/change-request |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/change-management/change-request |

### Overview

Create a new change request.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#change-management) to access this endpoint.

### Request

#### Body Data (required)

Change request payload.

{% tab title="Model" %}

| Parent field | Field                                   | Type      | Description                                                                            |
| ------------ | --------------------------------------- | --------- | -------------------------------------------------------------------------------------- |
|              | data [*required*]                  | object    | Data object to create a change request.                                                |
| data         | attributes [*required*]            | object    | Attributes for creating a change request.                                              |
| attributes   | change_request_linked_incident_uuid     | string    | The UUID of an incident to link to the change request.                                 |
| attributes   | change_request_maintenance_window_query | string    | The maintenance window query for the change request.                                   |
| attributes   | change_request_plan                     | string    | The plan associated with the change request.                                           |
| attributes   | change_request_risk                     | enum      | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH` |
| attributes   | change_request_type                     | enum      | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`       |
| attributes   | description                             | string    | The description of the change request.                                                 |
| attributes   | end_date                                | date-time | The planned end date of the change request.                                            |
| attributes   | project_id                              | string    | The project UUID to associate with the change request.                                 |
| attributes   | requested_teams                         | [string]  | A list of team handles to request decisions from.                                      |
| attributes   | start_date                              | date-time | The planned start date of the change request.                                          |
| attributes   | title [*required*]                 | string    | The title of the change request.                                                       |
| data         | type [*required*]                  | enum      | Change request resource type. Allowed enum values: `change_request`                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "change_request_linked_incident_uuid": "00000000-0000-0000-0000-000000000000",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "1. Deploy to staging 2. Run tests 3. Deploy to production",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "requested_teams": ["team-handle-1"],
      "start_date": "2024-01-01T03:00:00Z",
      "title": "Deploy new payment service"
    },
    "type": "change_request"
  }
}

```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Response object for a change request.

| Parent field             | Field                                                     | Type            | Description                                                                                 |
| ------------------------ | --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                                    | object          | Data object for a change request response.                                                  |
| data                     | attributes [*required*]                              | object          | Attributes of a change request response.                                                    |
| attributes               | archived_at                                               | date-time       | Timestamp of when the change request was archived.                                          |
| attributes               | attributes [*required*]                              | object          | Custom attributes of the change request as key-value pairs.                                 |
| additionalProperties     | <any-key>                                                 | [string]        |
| attributes               | change_request_linked_incident_uuid [*required*]     | string          | The UUID of the linked incident.                                                            |
| attributes               | change_request_maintenance_window_query [*required*] | string          | The maintenance window query for the change request.                                        |
| attributes               | change_request_plan [*required*]                     | string          | The plan associated with the change request.                                                |
| attributes               | change_request_risk [*required*]                     | enum            | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type [*required*]                     | enum            | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | closed_at                                                 | date-time       | Timestamp of when the change request was closed.                                            |
| attributes               | created_at [*required*]                              | date-time       | Timestamp of when the change request was created.                                           |
| attributes               | creation_source [*required*]                         | string          | The source from which the change request was created.                                       |
| attributes               | description [*required*]                             | string          | The description of the change request.                                                      |
| attributes               | end_date                                                  | date-time       | The planned end date of the change request.                                                 |
| attributes               | key [*required*]                                     | string          | The human-readable key of the change request.                                               |
| attributes               | modified_at [*required*]                             | date-time       | Timestamp of when the change request was last modified.                                     |
| attributes               | plan_notebook_id [*required*]                        | int64           | The notebook ID associated with the change request plan.                                    |
| attributes               | priority [*required*]                                | string          | The priority of the change request.                                                         |
| attributes               | project_id [*required*]                              | string          | The project UUID associated with the change request.                                        |
| attributes               | start_date                                                | date-time       | The planned start date of the change request.                                               |
| attributes               | status [*required*]                                  | string          | The current status of the change request.                                                   |
| attributes               | title [*required*]                                   | string          | The title of the change request.                                                            |
| attributes               | type [*required*]                                    | string          | The case type.                                                                              |
| data                     | id [*required*]                                      | string          | The identifier of the change request.                                                       |
| data                     | relationships                                             | object          | Relationships of a change request.                                                          |
| relationships            | change_request_decisions [*required*]                | object          | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                                    | [object]        | Array of decision relationship data.                                                        |
| data                     | id [*required*]                                      | string          | The decision UUID.                                                                          |
| data                     | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| relationships            | created_by [*required*]                              | object          | Relationship to a user.                                                                     |
| created_by               | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| data                     | type [*required*]                                    | enum            | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                                  | [<oneOf>] | Included resources related to the change request.                                           |
| included                 | Option 1                                                  | object          | An included user resource.                                                                  |
| Option 1                 | attributes [*required*]                              | object          | Attributes of an included user.                                                             |
| attributes               | email [*required*]                                   | string          | The email of the user.                                                                      |
| attributes               | handle [*required*]                                  | string          | The handle of the user.                                                                     |
| attributes               | name [*required*]                                    | string          | The name of the user.                                                                       |
| Option 1                 | id [*required*]                                      | string          | The user UUID.                                                                              |
| Option 1                 | type [*required*]                                    | string          | The resource type.                                                                          |
| included                 | Option 2                                                  | object          | An included change request decision resource.                                               |
| Option 2                 | attributes [*required*]                              | object          | Attributes of a change request decision in a response.                                      |
| attributes               | change_request_status [*required*]                   | enum            | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | decided_at [*required*]                              | date-time       | Timestamp of when the decision was made.                                                    |
| attributes               | decision_reason [*required*]                         | string          | The reason for the decision.                                                                |
| attributes               | deleted_at [*required*]                              | date-time       | Timestamp of when the decision was deleted.                                                 |
| attributes               | request_reason [*required*]                          | string          | The reason for requesting the decision.                                                     |
| attributes               | requested_at [*required*]                            | date-time       | Timestamp of when the decision was requested.                                               |
| Option 2                 | id [*required*]                                      | string          | The decision UUID.                                                                          |
| Option 2                 | relationships                                             | object          | Relationships of a change request decision.                                                 |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_by_user [*required*]                       | object          | Relationship to a user.                                                                     |
| requested_by_user        | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_user [*required*]                          | object          | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| Option 2                 | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "change_request_linked_incident_uuid": "",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2024-01-01T00:00:00Z",
      "creation_source": "CS_MANUAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "key": "CHM-1234",
      "modified_at": "2024-01-01T00:00:00Z",
      "plan_notebook_id": 0,
      "priority": "NOT_DEFINED",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "start_date": "2024-01-01T03:00:00Z",
      "status": "OPEN",
      "title": "Deploy new payment service",
      "type": "CHANGE_REQUEST"
    },
    "id": "CHM-1234",
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      },
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "email": "john.doe@example.com",
        "handle": "john.doe@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "user"
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/change-management/change-request" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "title": "Deploy new payment service"
    },
    "type": "change_request"
  }
}
EOF

{% /tab %}

## Get a change request{% #get-a-change-request %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/change-management/change-request/{change_request_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/change-management/change-request/{change_request_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/change-management/change-request/{change_request_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |

### Overview

Get the details of a change request by its ID.

OAuth apps require the `cases_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#change-management) to access this endpoint.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                           |
| ----------------------------------- | ------ | ------------------------------------- |
| change_request_id [*required*] | string | The identifier of the change request. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a change request.

| Parent field             | Field                                                     | Type            | Description                                                                                 |
| ------------------------ | --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                                    | object          | Data object for a change request response.                                                  |
| data                     | attributes [*required*]                              | object          | Attributes of a change request response.                                                    |
| attributes               | archived_at                                               | date-time       | Timestamp of when the change request was archived.                                          |
| attributes               | attributes [*required*]                              | object          | Custom attributes of the change request as key-value pairs.                                 |
| additionalProperties     | <any-key>                                                 | [string]        |
| attributes               | change_request_linked_incident_uuid [*required*]     | string          | The UUID of the linked incident.                                                            |
| attributes               | change_request_maintenance_window_query [*required*] | string          | The maintenance window query for the change request.                                        |
| attributes               | change_request_plan [*required*]                     | string          | The plan associated with the change request.                                                |
| attributes               | change_request_risk [*required*]                     | enum            | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type [*required*]                     | enum            | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | closed_at                                                 | date-time       | Timestamp of when the change request was closed.                                            |
| attributes               | created_at [*required*]                              | date-time       | Timestamp of when the change request was created.                                           |
| attributes               | creation_source [*required*]                         | string          | The source from which the change request was created.                                       |
| attributes               | description [*required*]                             | string          | The description of the change request.                                                      |
| attributes               | end_date                                                  | date-time       | The planned end date of the change request.                                                 |
| attributes               | key [*required*]                                     | string          | The human-readable key of the change request.                                               |
| attributes               | modified_at [*required*]                             | date-time       | Timestamp of when the change request was last modified.                                     |
| attributes               | plan_notebook_id [*required*]                        | int64           | The notebook ID associated with the change request plan.                                    |
| attributes               | priority [*required*]                                | string          | The priority of the change request.                                                         |
| attributes               | project_id [*required*]                              | string          | The project UUID associated with the change request.                                        |
| attributes               | start_date                                                | date-time       | The planned start date of the change request.                                               |
| attributes               | status [*required*]                                  | string          | The current status of the change request.                                                   |
| attributes               | title [*required*]                                   | string          | The title of the change request.                                                            |
| attributes               | type [*required*]                                    | string          | The case type.                                                                              |
| data                     | id [*required*]                                      | string          | The identifier of the change request.                                                       |
| data                     | relationships                                             | object          | Relationships of a change request.                                                          |
| relationships            | change_request_decisions [*required*]                | object          | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                                    | [object]        | Array of decision relationship data.                                                        |
| data                     | id [*required*]                                      | string          | The decision UUID.                                                                          |
| data                     | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| relationships            | created_by [*required*]                              | object          | Relationship to a user.                                                                     |
| created_by               | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| data                     | type [*required*]                                    | enum            | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                                  | [<oneOf>] | Included resources related to the change request.                                           |
| included                 | Option 1                                                  | object          | An included user resource.                                                                  |
| Option 1                 | attributes [*required*]                              | object          | Attributes of an included user.                                                             |
| attributes               | email [*required*]                                   | string          | The email of the user.                                                                      |
| attributes               | handle [*required*]                                  | string          | The handle of the user.                                                                     |
| attributes               | name [*required*]                                    | string          | The name of the user.                                                                       |
| Option 1                 | id [*required*]                                      | string          | The user UUID.                                                                              |
| Option 1                 | type [*required*]                                    | string          | The resource type.                                                                          |
| included                 | Option 2                                                  | object          | An included change request decision resource.                                               |
| Option 2                 | attributes [*required*]                              | object          | Attributes of a change request decision in a response.                                      |
| attributes               | change_request_status [*required*]                   | enum            | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | decided_at [*required*]                              | date-time       | Timestamp of when the decision was made.                                                    |
| attributes               | decision_reason [*required*]                         | string          | The reason for the decision.                                                                |
| attributes               | deleted_at [*required*]                              | date-time       | Timestamp of when the decision was deleted.                                                 |
| attributes               | request_reason [*required*]                          | string          | The reason for requesting the decision.                                                     |
| attributes               | requested_at [*required*]                            | date-time       | Timestamp of when the decision was requested.                                               |
| Option 2                 | id [*required*]                                      | string          | The decision UUID.                                                                          |
| Option 2                 | relationships                                             | object          | Relationships of a change request decision.                                                 |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_by_user [*required*]                       | object          | Relationship to a user.                                                                     |
| requested_by_user        | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_user [*required*]                          | object          | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| Option 2                 | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "change_request_linked_incident_uuid": "",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2024-01-01T00:00:00Z",
      "creation_source": "CS_MANUAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "key": "CHM-1234",
      "modified_at": "2024-01-01T00:00:00Z",
      "plan_notebook_id": 0,
      "priority": "NOT_DEFINED",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "start_date": "2024-01-01T03:00:00Z",
      "status": "OPEN",
      "title": "Deploy new payment service",
      "type": "CHANGE_REQUEST"
    },
    "id": "CHM-1234",
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      },
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "email": "john.doe@example.com",
        "handle": "john.doe@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "user"
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
                  \# Path parametersexport change_request_id="CHM-1234"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/change-management/change-request/${change_request_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}

## Update a change request{% #update-a-change-request %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/change-management/change-request/{change_request_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/change-management/change-request/{change_request_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/change-management/change-request/{change_request_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/change-management/change-request/{change_request_id} |

### Overview

Update the properties of a change request.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#change-management) to access this endpoint.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                           |
| ----------------------------------- | ------ | ------------------------------------- |
| change_request_id [*required*] | string | The identifier of the change request. |

### Request

#### Body Data (required)

Change request update payload.

{% tab title="Model" %}

| Parent field             | Field                    | Type      | Description                                                                                 |
| ------------------------ | ------------------------ | --------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]   | object    | Data object to update a change request.                                                     |
| data                     | attributes               | object    | Attributes for updating a change request.                                                   |
| attributes               | change_request_plan      | string    | The plan associated with the change request.                                                |
| attributes               | change_request_risk      | enum      | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type      | enum      | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | end_date                 | date-time | The planned end date of the change request.                                                 |
| attributes               | id                       | string    | The identifier of the change request to update.                                             |
| attributes               | start_date               | date-time | The planned start date of the change request.                                               |
| data                     | relationships            | object    | Relationships for updating a change request.                                                |
| relationships            | change_request_decisions | object    | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]   | [object]  | Array of decision relationship data.                                                        |
| data                     | id [*required*]     | string    | The decision UUID.                                                                          |
| data                     | type [*required*]   | enum      | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| data                     | type [*required*]   | enum      | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                 | [object]  | Included resources for the change request update.                                           |
| included                 | attributes               | object    | Attributes for creating a change request decision.                                          |
| attributes               | change_request_status    | enum      | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | request_reason           | string    | The reason for requesting the decision.                                                     |
| included                 | id [*required*]     | string    | The decision identifier.                                                                    |
| included                 | relationships            | object    | Relationships for creating a change request decision.                                       |
| relationships            | requested_user           | object    | Relationship to a user.                                                                     |
| requested_user           | data [*required*]   | object    | User relationship data.                                                                     |
| data                     | id [*required*]     | string    | The user UUID.                                                                              |
| data                     | type [*required*]   | string    | The user resource type.                                                                     |
| included                 | type [*required*]   | enum      | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "change_request_plan": "Updated deployment plan",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "end_date": "2024-01-02T15:00:00Z",
      "id": "CHM-1234",
      "start_date": "2024-01-01T03:00:00Z"
    },
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "change_request_status": "REQUESTED",
        "request_reason": "Please review and approve this change"
      },
      "id": "decision-id-0",
      "relationships": {
        "requested_user": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        }
      },
      "type": "change_request_decision"
    }]
}

```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a change request.

| Parent field             | Field                                                     | Type            | Description                                                                                 |
| ------------------------ | --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                                    | object          | Data object for a change request response.                                                  |
| data                     | attributes [*required*]                              | object          | Attributes of a change request response.                                                    |
| attributes               | archived_at                                               | date-time       | Timestamp of when the change request was archived.                                          |
| attributes               | attributes [*required*]                              | object          | Custom attributes of the change request as key-value pairs.                                 |
| additionalProperties     | <any-key>                                                 | [string]        |
| attributes               | change_request_linked_incident_uuid [*required*]     | string          | The UUID of the linked incident.                                                            |
| attributes               | change_request_maintenance_window_query [*required*] | string          | The maintenance window query for the change request.                                        |
| attributes               | change_request_plan [*required*]                     | string          | The plan associated with the change request.                                                |
| attributes               | change_request_risk [*required*]                     | enum            | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type [*required*]                     | enum            | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | closed_at                                                 | date-time       | Timestamp of when the change request was closed.                                            |
| attributes               | created_at [*required*]                              | date-time       | Timestamp of when the change request was created.                                           |
| attributes               | creation_source [*required*]                         | string          | The source from which the change request was created.                                       |
| attributes               | description [*required*]                             | string          | The description of the change request.                                                      |
| attributes               | end_date                                                  | date-time       | The planned end date of the change request.                                                 |
| attributes               | key [*required*]                                     | string          | The human-readable key of the change request.                                               |
| attributes               | modified_at [*required*]                             | date-time       | Timestamp of when the change request was last modified.                                     |
| attributes               | plan_notebook_id [*required*]                        | int64           | The notebook ID associated with the change request plan.                                    |
| attributes               | priority [*required*]                                | string          | The priority of the change request.                                                         |
| attributes               | project_id [*required*]                              | string          | The project UUID associated with the change request.                                        |
| attributes               | start_date                                                | date-time       | The planned start date of the change request.                                               |
| attributes               | status [*required*]                                  | string          | The current status of the change request.                                                   |
| attributes               | title [*required*]                                   | string          | The title of the change request.                                                            |
| attributes               | type [*required*]                                    | string          | The case type.                                                                              |
| data                     | id [*required*]                                      | string          | The identifier of the change request.                                                       |
| data                     | relationships                                             | object          | Relationships of a change request.                                                          |
| relationships            | change_request_decisions [*required*]                | object          | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                                    | [object]        | Array of decision relationship data.                                                        |
| data                     | id [*required*]                                      | string          | The decision UUID.                                                                          |
| data                     | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| relationships            | created_by [*required*]                              | object          | Relationship to a user.                                                                     |
| created_by               | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| data                     | type [*required*]                                    | enum            | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                                  | [<oneOf>] | Included resources related to the change request.                                           |
| included                 | Option 1                                                  | object          | An included user resource.                                                                  |
| Option 1                 | attributes [*required*]                              | object          | Attributes of an included user.                                                             |
| attributes               | email [*required*]                                   | string          | The email of the user.                                                                      |
| attributes               | handle [*required*]                                  | string          | The handle of the user.                                                                     |
| attributes               | name [*required*]                                    | string          | The name of the user.                                                                       |
| Option 1                 | id [*required*]                                      | string          | The user UUID.                                                                              |
| Option 1                 | type [*required*]                                    | string          | The resource type.                                                                          |
| included                 | Option 2                                                  | object          | An included change request decision resource.                                               |
| Option 2                 | attributes [*required*]                              | object          | Attributes of a change request decision in a response.                                      |
| attributes               | change_request_status [*required*]                   | enum            | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | decided_at [*required*]                              | date-time       | Timestamp of when the decision was made.                                                    |
| attributes               | decision_reason [*required*]                         | string          | The reason for the decision.                                                                |
| attributes               | deleted_at [*required*]                              | date-time       | Timestamp of when the decision was deleted.                                                 |
| attributes               | request_reason [*required*]                          | string          | The reason for requesting the decision.                                                     |
| attributes               | requested_at [*required*]                            | date-time       | Timestamp of when the decision was requested.                                               |
| Option 2                 | id [*required*]                                      | string          | The decision UUID.                                                                          |
| Option 2                 | relationships                                             | object          | Relationships of a change request decision.                                                 |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_by_user [*required*]                       | object          | Relationship to a user.                                                                     |
| requested_by_user        | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_user [*required*]                          | object          | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| Option 2                 | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "change_request_linked_incident_uuid": "",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2024-01-01T00:00:00Z",
      "creation_source": "CS_MANUAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "key": "CHM-1234",
      "modified_at": "2024-01-01T00:00:00Z",
      "plan_notebook_id": 0,
      "priority": "NOT_DEFINED",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "start_date": "2024-01-01T03:00:00Z",
      "status": "OPEN",
      "title": "Deploy new payment service",
      "type": "CHANGE_REQUEST"
    },
    "id": "CHM-1234",
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      },
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "email": "john.doe@example.com",
        "handle": "john.doe@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "user"
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
                  \# Path parametersexport change_request_id="CHM-1234"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/change-management/change-request/${change_request_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      }
    },
    "type": "change_request"
  },
  "included": [{
      "id": "decision-id-0",
      "relationships": {
        "requested_user": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        }
      },
      "type": "change_request_decision"
    }]
}
EOF

{% /tab %}

## Create a change request branch{% #create-a-change-request-branch %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/branch |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/branch |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/change-management/change-request/{change_request_id}/branch      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/change-management/change-request/{change_request_id}/branch      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/branch     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/branch |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/branch |

### Overview

Create a new branch in a repository for a change request.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#change-management) to access this endpoint.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                           |
| ----------------------------------- | ------ | ------------------------------------- |
| change_request_id [*required*] | string | The identifier of the change request. |

### Request

#### Body Data (required)

Branch creation payload.

{% tab title="Model" %}

| Parent field | Field                         | Type   | Description                                                                       |
| ------------ | ----------------------------- | ------ | --------------------------------------------------------------------------------- |
|              | data [*required*]        | object | Data object to create a change request branch.                                    |
| data         | attributes [*required*]  | object | Attributes for creating a change request branch.                                  |
| attributes   | branch_name [*required*] | string | The name of the branch to create.                                                 |
| attributes   | repo_id [*required*]     | string | The repository identifier in the format owner/repository.                         |
| data         | type [*required*]        | enum   | Change request branch resource type. Allowed enum values: `change_request_branch` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "branch_name": "chm/CHM-1234",
      "repo_id": "DataDog/dd-source"
    },
    "type": "change_request_branch"
  }
}

```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a change request.

| Parent field             | Field                                                     | Type            | Description                                                                                 |
| ------------------------ | --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                                    | object          | Data object for a change request response.                                                  |
| data                     | attributes [*required*]                              | object          | Attributes of a change request response.                                                    |
| attributes               | archived_at                                               | date-time       | Timestamp of when the change request was archived.                                          |
| attributes               | attributes [*required*]                              | object          | Custom attributes of the change request as key-value pairs.                                 |
| additionalProperties     | <any-key>                                                 | [string]        |
| attributes               | change_request_linked_incident_uuid [*required*]     | string          | The UUID of the linked incident.                                                            |
| attributes               | change_request_maintenance_window_query [*required*] | string          | The maintenance window query for the change request.                                        |
| attributes               | change_request_plan [*required*]                     | string          | The plan associated with the change request.                                                |
| attributes               | change_request_risk [*required*]                     | enum            | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type [*required*]                     | enum            | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | closed_at                                                 | date-time       | Timestamp of when the change request was closed.                                            |
| attributes               | created_at [*required*]                              | date-time       | Timestamp of when the change request was created.                                           |
| attributes               | creation_source [*required*]                         | string          | The source from which the change request was created.                                       |
| attributes               | description [*required*]                             | string          | The description of the change request.                                                      |
| attributes               | end_date                                                  | date-time       | The planned end date of the change request.                                                 |
| attributes               | key [*required*]                                     | string          | The human-readable key of the change request.                                               |
| attributes               | modified_at [*required*]                             | date-time       | Timestamp of when the change request was last modified.                                     |
| attributes               | plan_notebook_id [*required*]                        | int64           | The notebook ID associated with the change request plan.                                    |
| attributes               | priority [*required*]                                | string          | The priority of the change request.                                                         |
| attributes               | project_id [*required*]                              | string          | The project UUID associated with the change request.                                        |
| attributes               | start_date                                                | date-time       | The planned start date of the change request.                                               |
| attributes               | status [*required*]                                  | string          | The current status of the change request.                                                   |
| attributes               | title [*required*]                                   | string          | The title of the change request.                                                            |
| attributes               | type [*required*]                                    | string          | The case type.                                                                              |
| data                     | id [*required*]                                      | string          | The identifier of the change request.                                                       |
| data                     | relationships                                             | object          | Relationships of a change request.                                                          |
| relationships            | change_request_decisions [*required*]                | object          | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                                    | [object]        | Array of decision relationship data.                                                        |
| data                     | id [*required*]                                      | string          | The decision UUID.                                                                          |
| data                     | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| relationships            | created_by [*required*]                              | object          | Relationship to a user.                                                                     |
| created_by               | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| data                     | type [*required*]                                    | enum            | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                                  | [<oneOf>] | Included resources related to the change request.                                           |
| included                 | Option 1                                                  | object          | An included user resource.                                                                  |
| Option 1                 | attributes [*required*]                              | object          | Attributes of an included user.                                                             |
| attributes               | email [*required*]                                   | string          | The email of the user.                                                                      |
| attributes               | handle [*required*]                                  | string          | The handle of the user.                                                                     |
| attributes               | name [*required*]                                    | string          | The name of the user.                                                                       |
| Option 1                 | id [*required*]                                      | string          | The user UUID.                                                                              |
| Option 1                 | type [*required*]                                    | string          | The resource type.                                                                          |
| included                 | Option 2                                                  | object          | An included change request decision resource.                                               |
| Option 2                 | attributes [*required*]                              | object          | Attributes of a change request decision in a response.                                      |
| attributes               | change_request_status [*required*]                   | enum            | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | decided_at [*required*]                              | date-time       | Timestamp of when the decision was made.                                                    |
| attributes               | decision_reason [*required*]                         | string          | The reason for the decision.                                                                |
| attributes               | deleted_at [*required*]                              | date-time       | Timestamp of when the decision was deleted.                                                 |
| attributes               | request_reason [*required*]                          | string          | The reason for requesting the decision.                                                     |
| attributes               | requested_at [*required*]                            | date-time       | Timestamp of when the decision was requested.                                               |
| Option 2                 | id [*required*]                                      | string          | The decision UUID.                                                                          |
| Option 2                 | relationships                                             | object          | Relationships of a change request decision.                                                 |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_by_user [*required*]                       | object          | Relationship to a user.                                                                     |
| requested_by_user        | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_user [*required*]                          | object          | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| Option 2                 | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "change_request_linked_incident_uuid": "",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2024-01-01T00:00:00Z",
      "creation_source": "CS_MANUAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "key": "CHM-1234",
      "modified_at": "2024-01-01T00:00:00Z",
      "plan_notebook_id": 0,
      "priority": "NOT_DEFINED",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "start_date": "2024-01-01T03:00:00Z",
      "status": "OPEN",
      "title": "Deploy new payment service",
      "type": "CHANGE_REQUEST"
    },
    "id": "CHM-1234",
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      },
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "email": "john.doe@example.com",
        "handle": "john.doe@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "user"
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
                  \# Path parametersexport change_request_id="CHM-1234"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/change-management/change-request/${change_request_id}/branch" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "branch_name": "chm/CHM-1234",
      "repo_id": "DataDog/dd-source"
    },
    "type": "change_request_branch"
  }
}
EOF

{% /tab %}

## Update a change request decision{% #update-a-change-request-decision %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |

### Overview

Update a decision on a change request, such as approving or declining it.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#change-management) to access this endpoint.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                    |
| ----------------------------------- | ------ | ---------------------------------------------- |
| change_request_id [*required*] | string | The identifier of the change request.          |
| decision_id [*required*]       | string | The identifier of the change request decision. |

### Request

#### Body Data (required)

Decision update payload.

{% tab title="Model" %}

| Parent field             | Field                                      | Type     | Description                                                                                 |
| ------------------------ | ------------------------------------------ | -------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                     | object   | Data object to update a change request decision.                                            |
| data                     | attributes                                 | object   | Attributes of the parent change request for a decision update.                              |
| attributes               | id                                         | string   | The identifier of the change request.                                                       |
| data                     | relationships                              | object   | Relationships for updating a change request decision.                                       |
| relationships            | change_request_decisions [*required*] | object   | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                     | [object] | Array of decision relationship data.                                                        |
| data                     | id [*required*]                       | string   | The decision UUID.                                                                          |
| data                     | type [*required*]                     | enum     | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| data                     | type [*required*]                     | enum     | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                   | [object] | Included resources for the change request update.                                           |
| included                 | attributes                                 | object   | Attributes for creating a change request decision.                                          |
| attributes               | change_request_status                      | enum     | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | request_reason                             | string   | The reason for requesting the decision.                                                     |
| included                 | id [*required*]                       | string   | The decision identifier.                                                                    |
| included                 | relationships                              | object   | Relationships for creating a change request decision.                                       |
| relationships            | requested_user                             | object   | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                     | object   | User relationship data.                                                                     |
| data                     | id [*required*]                       | string   | The user UUID.                                                                              |
| data                     | type [*required*]                     | string   | The user resource type.                                                                     |
| included                 | type [*required*]                     | enum     | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "id": "CHM-1234"
    },
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "change_request_status": "REQUESTED",
        "request_reason": "Please review and approve this change"
      },
      "id": "decision-id-0",
      "relationships": {
        "requested_user": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        }
      },
      "type": "change_request_decision"
    }]
}

```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a change request.

| Parent field             | Field                                                     | Type            | Description                                                                                 |
| ------------------------ | --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                                    | object          | Data object for a change request response.                                                  |
| data                     | attributes [*required*]                              | object          | Attributes of a change request response.                                                    |
| attributes               | archived_at                                               | date-time       | Timestamp of when the change request was archived.                                          |
| attributes               | attributes [*required*]                              | object          | Custom attributes of the change request as key-value pairs.                                 |
| additionalProperties     | <any-key>                                                 | [string]        |
| attributes               | change_request_linked_incident_uuid [*required*]     | string          | The UUID of the linked incident.                                                            |
| attributes               | change_request_maintenance_window_query [*required*] | string          | The maintenance window query for the change request.                                        |
| attributes               | change_request_plan [*required*]                     | string          | The plan associated with the change request.                                                |
| attributes               | change_request_risk [*required*]                     | enum            | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type [*required*]                     | enum            | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | closed_at                                                 | date-time       | Timestamp of when the change request was closed.                                            |
| attributes               | created_at [*required*]                              | date-time       | Timestamp of when the change request was created.                                           |
| attributes               | creation_source [*required*]                         | string          | The source from which the change request was created.                                       |
| attributes               | description [*required*]                             | string          | The description of the change request.                                                      |
| attributes               | end_date                                                  | date-time       | The planned end date of the change request.                                                 |
| attributes               | key [*required*]                                     | string          | The human-readable key of the change request.                                               |
| attributes               | modified_at [*required*]                             | date-time       | Timestamp of when the change request was last modified.                                     |
| attributes               | plan_notebook_id [*required*]                        | int64           | The notebook ID associated with the change request plan.                                    |
| attributes               | priority [*required*]                                | string          | The priority of the change request.                                                         |
| attributes               | project_id [*required*]                              | string          | The project UUID associated with the change request.                                        |
| attributes               | start_date                                                | date-time       | The planned start date of the change request.                                               |
| attributes               | status [*required*]                                  | string          | The current status of the change request.                                                   |
| attributes               | title [*required*]                                   | string          | The title of the change request.                                                            |
| attributes               | type [*required*]                                    | string          | The case type.                                                                              |
| data                     | id [*required*]                                      | string          | The identifier of the change request.                                                       |
| data                     | relationships                                             | object          | Relationships of a change request.                                                          |
| relationships            | change_request_decisions [*required*]                | object          | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                                    | [object]        | Array of decision relationship data.                                                        |
| data                     | id [*required*]                                      | string          | The decision UUID.                                                                          |
| data                     | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| relationships            | created_by [*required*]                              | object          | Relationship to a user.                                                                     |
| created_by               | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| data                     | type [*required*]                                    | enum            | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                                  | [<oneOf>] | Included resources related to the change request.                                           |
| included                 | Option 1                                                  | object          | An included user resource.                                                                  |
| Option 1                 | attributes [*required*]                              | object          | Attributes of an included user.                                                             |
| attributes               | email [*required*]                                   | string          | The email of the user.                                                                      |
| attributes               | handle [*required*]                                  | string          | The handle of the user.                                                                     |
| attributes               | name [*required*]                                    | string          | The name of the user.                                                                       |
| Option 1                 | id [*required*]                                      | string          | The user UUID.                                                                              |
| Option 1                 | type [*required*]                                    | string          | The resource type.                                                                          |
| included                 | Option 2                                                  | object          | An included change request decision resource.                                               |
| Option 2                 | attributes [*required*]                              | object          | Attributes of a change request decision in a response.                                      |
| attributes               | change_request_status [*required*]                   | enum            | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | decided_at [*required*]                              | date-time       | Timestamp of when the decision was made.                                                    |
| attributes               | decision_reason [*required*]                         | string          | The reason for the decision.                                                                |
| attributes               | deleted_at [*required*]                              | date-time       | Timestamp of when the decision was deleted.                                                 |
| attributes               | request_reason [*required*]                          | string          | The reason for requesting the decision.                                                     |
| attributes               | requested_at [*required*]                            | date-time       | Timestamp of when the decision was requested.                                               |
| Option 2                 | id [*required*]                                      | string          | The decision UUID.                                                                          |
| Option 2                 | relationships                                             | object          | Relationships of a change request decision.                                                 |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_by_user [*required*]                       | object          | Relationship to a user.                                                                     |
| requested_by_user        | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_user [*required*]                          | object          | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| Option 2                 | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "change_request_linked_incident_uuid": "",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2024-01-01T00:00:00Z",
      "creation_source": "CS_MANUAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "key": "CHM-1234",
      "modified_at": "2024-01-01T00:00:00Z",
      "plan_notebook_id": 0,
      "priority": "NOT_DEFINED",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "start_date": "2024-01-01T03:00:00Z",
      "status": "OPEN",
      "title": "Deploy new payment service",
      "type": "CHANGE_REQUEST"
    },
    "id": "CHM-1234",
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      },
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "email": "john.doe@example.com",
        "handle": "john.doe@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "user"
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
                  \# Path parametersexport change_request_id="CHM-1234"export decision_id="decision-id-0"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/change-management/change-request/${change_request_id}/decisions/${decision_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      }
    },
    "type": "change_request"
  },
  "included": [{
      "id": "decision-id-0",
      "relationships": {
        "requested_user": {
          "data": {
            "id": "00000000-0000-0000-0000-000000000000",
            "type": "user"
          }
        }
      },
      "type": "change_request_decision"
    }]
}
EOF

{% /tab %}

## Delete a change request decision{% #delete-a-change-request-decision %}

{% tab title="v2" %}
**Note**: This endpoint is in preview and is subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/change-management/change-request/{change_request_id}/decisions/{decision_id} |

### Overview

Delete a decision from a change request.

OAuth apps require the `cases_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#change-management) to access this endpoint.

### Arguments

#### Path Parameters

| Name                                | Type   | Description                                    |
| ----------------------------------- | ------ | ---------------------------------------------- |
| change_request_id [*required*] | string | The identifier of the change request.          |
| decision_id [*required*]       | string | The identifier of the change request decision. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for a change request.

| Parent field             | Field                                                     | Type            | Description                                                                                 |
| ------------------------ | --------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------- |
|                          | data [*required*]                                    | object          | Data object for a change request response.                                                  |
| data                     | attributes [*required*]                              | object          | Attributes of a change request response.                                                    |
| attributes               | archived_at                                               | date-time       | Timestamp of when the change request was archived.                                          |
| attributes               | attributes [*required*]                              | object          | Custom attributes of the change request as key-value pairs.                                 |
| additionalProperties     | <any-key>                                                 | [string]        |
| attributes               | change_request_linked_incident_uuid [*required*]     | string          | The UUID of the linked incident.                                                            |
| attributes               | change_request_maintenance_window_query [*required*] | string          | The maintenance window query for the change request.                                        |
| attributes               | change_request_plan [*required*]                     | string          | The plan associated with the change request.                                                |
| attributes               | change_request_risk [*required*]                     | enum            | The risk level of the change request. Allowed enum values: `UNDEFINED,LOW,MEDIUM,HIGH`      |
| attributes               | change_request_type [*required*]                     | enum            | The type of the change request. Allowed enum values: `NORMAL,STANDARD,EMERGENCY`            |
| attributes               | closed_at                                                 | date-time       | Timestamp of when the change request was closed.                                            |
| attributes               | created_at [*required*]                              | date-time       | Timestamp of when the change request was created.                                           |
| attributes               | creation_source [*required*]                         | string          | The source from which the change request was created.                                       |
| attributes               | description [*required*]                             | string          | The description of the change request.                                                      |
| attributes               | end_date                                                  | date-time       | The planned end date of the change request.                                                 |
| attributes               | key [*required*]                                     | string          | The human-readable key of the change request.                                               |
| attributes               | modified_at [*required*]                             | date-time       | Timestamp of when the change request was last modified.                                     |
| attributes               | plan_notebook_id [*required*]                        | int64           | The notebook ID associated with the change request plan.                                    |
| attributes               | priority [*required*]                                | string          | The priority of the change request.                                                         |
| attributes               | project_id [*required*]                              | string          | The project UUID associated with the change request.                                        |
| attributes               | start_date                                                | date-time       | The planned start date of the change request.                                               |
| attributes               | status [*required*]                                  | string          | The current status of the change request.                                                   |
| attributes               | title [*required*]                                   | string          | The title of the change request.                                                            |
| attributes               | type [*required*]                                    | string          | The case type.                                                                              |
| data                     | id [*required*]                                      | string          | The identifier of the change request.                                                       |
| data                     | relationships                                             | object          | Relationships of a change request.                                                          |
| relationships            | change_request_decisions [*required*]                | object          | Relationship to change request decisions.                                                   |
| change_request_decisions | data [*required*]                                    | [object]        | Array of decision relationship data.                                                        |
| data                     | id [*required*]                                      | string          | The decision UUID.                                                                          |
| data                     | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |
| relationships            | created_by [*required*]                              | object          | Relationship to a user.                                                                     |
| created_by               | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| data                     | type [*required*]                                    | enum            | Change request resource type. Allowed enum values: `change_request`                         |
|                          | included                                                  | [<oneOf>] | Included resources related to the change request.                                           |
| included                 | Option 1                                                  | object          | An included user resource.                                                                  |
| Option 1                 | attributes [*required*]                              | object          | Attributes of an included user.                                                             |
| attributes               | email [*required*]                                   | string          | The email of the user.                                                                      |
| attributes               | handle [*required*]                                  | string          | The handle of the user.                                                                     |
| attributes               | name [*required*]                                    | string          | The name of the user.                                                                       |
| Option 1                 | id [*required*]                                      | string          | The user UUID.                                                                              |
| Option 1                 | type [*required*]                                    | string          | The resource type.                                                                          |
| included                 | Option 2                                                  | object          | An included change request decision resource.                                               |
| Option 2                 | attributes [*required*]                              | object          | Attributes of a change request decision in a response.                                      |
| attributes               | change_request_status [*required*]                   | enum            | The status of a change request decision. Allowed enum values: `REQUESTED,APPROVED,DECLINED` |
| attributes               | decided_at [*required*]                              | date-time       | Timestamp of when the decision was made.                                                    |
| attributes               | decision_reason [*required*]                         | string          | The reason for the decision.                                                                |
| attributes               | deleted_at [*required*]                              | date-time       | Timestamp of when the decision was deleted.                                                 |
| attributes               | request_reason [*required*]                          | string          | The reason for requesting the decision.                                                     |
| attributes               | requested_at [*required*]                            | date-time       | Timestamp of when the decision was requested.                                               |
| Option 2                 | id [*required*]                                      | string          | The decision UUID.                                                                          |
| Option 2                 | relationships                                             | object          | Relationships of a change request decision.                                                 |
| relationships            | modified_by [*required*]                             | object          | Relationship to a user.                                                                     |
| modified_by              | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_by_user [*required*]                       | object          | Relationship to a user.                                                                     |
| requested_by_user        | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| relationships            | requested_user [*required*]                          | object          | Relationship to a user.                                                                     |
| requested_user           | data [*required*]                                    | object          | User relationship data.                                                                     |
| data                     | id [*required*]                                      | string          | The user UUID.                                                                              |
| data                     | type [*required*]                                    | string          | The user resource type.                                                                     |
| Option 2                 | type [*required*]                                    | enum            | Change request decision resource type. Allowed enum values: `change_request_decision`       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "archived_at": "2019-09-19T10:00:00.000Z",
      "attributes": {
        "<any-key>": []
      },
      "change_request_linked_incident_uuid": "",
      "change_request_maintenance_window_query": "",
      "change_request_plan": "",
      "change_request_risk": "LOW",
      "change_request_type": "NORMAL",
      "closed_at": "2019-09-19T10:00:00.000Z",
      "created_at": "2024-01-01T00:00:00Z",
      "creation_source": "CS_MANUAL",
      "description": "Deploying new payment service v2.1",
      "end_date": "2024-01-02T15:00:00Z",
      "key": "CHM-1234",
      "modified_at": "2024-01-01T00:00:00Z",
      "plan_notebook_id": 0,
      "priority": "NOT_DEFINED",
      "project_id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e",
      "start_date": "2024-01-01T03:00:00Z",
      "status": "OPEN",
      "title": "Deploy new payment service",
      "type": "CHANGE_REQUEST"
    },
    "id": "CHM-1234",
    "relationships": {
      "change_request_decisions": {
        "data": [{
            "id": "decision-id-0",
            "type": "change_request_decision"
          }]
      },
      "created_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      },
      "modified_by": {
        "data": {
          "id": "00000000-0000-0000-0000-000000000000",
          "type": "user"
        }
      }
    },
    "type": "change_request"
  },
  "included": [{
      "attributes": {
        "email": "john.doe@example.com",
        "handle": "john.doe@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "user"
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
                  \# Path parametersexport change_request_id="CHM-1234"export decision_id="decision-id-0"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/change-management/change-request/${change_request_id}/decisions/${decision_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}
