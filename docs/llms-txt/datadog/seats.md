# Source: https://docs.datadoghq.com/api/latest/seats.md

---
title: Seats
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Seats
---

# Seats

The seats API allows you to view, assign, and unassign seats for your organization.

## Get users with seats{% #get-users-with-seats %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/seats/users |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/seats/users |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/seats/users      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/seats/users      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/seats/users     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/seats/users |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/seats/users |

### Overview

Get the list of users assigned seats for a product code. This endpoint requires any of the following permissions:
`billing_read``incident_read``on_call_read`


### Arguments

#### Query Strings

| Name                           | Type    | Description                                        |
| ------------------------------ | ------- | -------------------------------------------------- |
| product_code [*required*] | string  | The product code for which to retrieve seat users. |
| page[limit]                    | integer | Maximum number of results to return.               |
| page[cursor]                   | string  | Cursor for pagination.                             |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Parent field | Field       | Type      | Description                                                 |
| ------------ | ----------- | --------- | ----------------------------------------------------------- |
|              | data        | [object]  | The list of seat users.                                     |
| data         | attributes  | object    | The attributes of the seat user.                            |
| attributes   | assigned_at | date-time | The date and time the seat was assigned.                    |
| attributes   | email       | string    | The email of the user.                                      |
| attributes   | name        | string    | The name of the user.                                       |
| data         | id          | string    | The ID of the seat user.                                    |
| data         | type        | enum      | Seat users resource type. Allowed enum values: `seat-users` |
|              | meta        | object    | The metadata of the seat users.                             |
| meta         | cursor      | string    | The cursor for the seat users.                              |
| meta         | limit       | int64     | The limit for the seat users.                               |
| meta         | next_cursor | string    | The next cursor for the seat users.                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "assigned_at": "2021-01-01T00:00:00Z",
        "email": "user@example.com",
        "name": "John Doe"
      },
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "seat-users"
    }
  ],
  "meta": {
    "cursor": "string",
    "limit": "integer",
    "next_cursor": "string"
  }
}
```text

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
```text

{% /tab %}

{% /tab %}

{% tab title="422" %}
Unprocessable Entity
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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Required query argumentsexport product_code="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/seats/users?product_code=${product_code}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

{% /tab %}

## Assign seats to users{% #assign-seats-to-users %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/seats/users |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/seats/users |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/seats/users      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/seats/users      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/seats/users     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/seats/users |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/seats/users |

### Overview

Assign seats to users for a product code. This endpoint requires any of the following permissions:
`billing_edit``incident_write``on_call_write`


### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                          | Type     | Description                                                                        |
| ------------ | ------------------------------ | -------- | ---------------------------------------------------------------------------------- |
|              | data                           | object   | The data for the assign seats user request.                                        |
| data         | attributes [*required*]   | object   | The attributes of the assign seats user request.                                   |
| attributes   | product_code [*required*] | string   | The product code for which to assign seats.                                        |
| attributes   | user_uuids [*required*]   | [string] | The list of user IDs to assign seats to.                                           |
| data         | id                             | string   | The ID of the assign seats user request.                                           |
| data         | type [*required*]         | enum     | The type of the assign seats user request. Allowed enum values: `seat-assignments` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "product_code": "",
      "user_uuids": [
        ""
      ]
    },
    "id": "string",
    "type": "seat-assignments"
  }
}
```text

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}

| Parent field | Field        | Type     | Description                                                             |
| ------------ | ------------ | -------- | ----------------------------------------------------------------------- |
|              | data         | object   | The data for the assign seats user response.                            |
| data         | attributes   | object   | The attributes of the assign seats user response.                       |
| attributes   | assigned_ids | [string] | The list of user IDs to which the seats were assigned.                  |
| attributes   | product_code | string   | The product code for which the seats were assigned.                     |
| data         | id           | string   | The ID of the assign seats user response.                               |
| data         | type         | enum     | Seat assignments resource type. Allowed enum values: `seat-assignments` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "assigned_ids": [],
      "product_code": "string"
    },
    "id": "string",
    "type": "seat-assignments"
  }
}
```text

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
```text

{% /tab %}

{% /tab %}

{% tab title="422" %}
Unprocessable Entity
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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/seats/users" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "product_code": "",
      "user_uuids": [
        ""
      ]
    },
    "type": "seat-assignments"
  }
}
EOF

{% /tab %}

## Unassign seats from users{% #unassign-seats-from-users %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/seats/users |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/seats/users |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/seats/users      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/seats/users      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/seats/users     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/seats/users |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/seats/users |

### Overview

Unassign seats from users for a product code. This endpoint requires any of the following permissions:
`billing_edit``incident_write``on_call_write`


### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                          | Type     | Description                                                                          |
| ------------ | ------------------------------ | -------- | ------------------------------------------------------------------------------------ |
|              | data                           | object   | The data for the unassign seats user request.                                        |
| data         | attributes [*required*]   | object   | The attributes of the unassign seats user request.                                   |
| attributes   | product_code [*required*] | string   | The product code for which to unassign seats.                                        |
| attributes   | user_uuids [*required*]   | [string] | The list of user IDs to unassign seats from.                                         |
| data         | id                             | string   | The ID of the unassign seats user request.                                           |
| data         | type [*required*]         | enum     | The type of the unassign seats user request. Allowed enum values: `seat-assignments` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "product_code": "",
      "user_uuids": [
        ""
      ]
    },
    "id": "string",
    "type": "seat-assignments"
  }
}
```text

{% /tab %}

### Response

{% tab title="204" %}
No Content
{% /tab %}

{% tab title="400" %}
Bad Request
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
```text

{% /tab %}

{% /tab %}

{% tab title="422" %}
Unprocessable Entity
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
```text

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
```text

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/seats/users" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "product_code": "",
      "user_uuids": [
        ""
      ]
    },
    "type": "seat-assignments"
  }
}
EOF

{% /tab %}
