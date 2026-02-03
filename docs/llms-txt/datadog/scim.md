# Source: https://docs.datadoghq.com/account_management/scim.md

# Source: https://docs.datadoghq.com/api/latest/scim.md

---
title: SCIM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > SCIM
---

# SCIM

Provision Datadog users and teams using SCIM APIs.

Note: SCIM provisioning for Datadog teams is only available for select organizations at this point. Request access by contacting Datadog support, or see the [SCIM page](https://docs.datadoghq.com/account_management/scim/) for more information.

## List users{% #list-users %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/scim/Users |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/scim/Users |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/scim/Users      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/scim/Users      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/scim/Users     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/scim/Users |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/scim/Users |

### Overview

List users in the organization. Results are paginated by `startIndex` and `count` parameters. Results can be narrowed down by the `filter` parameter. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Query Strings

| Name       | Type    | Description                                                                                                                 |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| startIndex | integer | Specifies the start index to fetch the results (1-indexed).                                                                 |
| count      | integer | Specifies the number of users to be returned.                                                                               |
| filter     | string  | Specifies the url encoded filter to use to narrow down the results. Filter should be of the form `userName eq <user name>`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List users response object.

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | Resources    | [object]  | List of users matching the request criteria.                                                           |
| Resources    | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
| Resources    | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
| Resources    | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
| Resources    | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
| Resources    | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
| Resources    | schemas      | [string]  | User JSON Schemas.                                                                                     |
| Resources    | title        | string    | The user's title.                                                                                      |
| Resources    | userName     | string    | Unique identifier for the User.                                                                        |
|              | itemsPerPage | int64     | Number of users returned per page.                                                                     |
|              | schemas      | [string]  | List response JSON Schemas.                                                                            |
|              | startIndex   | int64     | Starting index of the users for this page (1-indexed).                                                 |
|              | totalResults | int64     | Total number of users matching the request criteria.                                                   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "Resources": [
    {
      "active": true,
      "emails": [
        {
          "primary": true,
          "type": "work",
          "value": "john.doe@datadoghq.com"
        }
      ],
      "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
      "meta": {
        "created": "2024-11-22T15:05:52.055138963Z",
        "lastModified": "2024-11-22T15:05:52.055139017Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Users/e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
        "resourceType": "User"
      },
      "name": {
        "formatted": "John Doe"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "title": "Mr.",
      "userName": "john.doe@datadoghq.com"
    },
    {
      "active": true,
      "emails": [
        {
          "primary": true,
          "type": "work",
          "value": "jane.doe@datadoghq.com"
        }
      ],
      "id": "79ef0d28-f257-4829-97e6-d23d2a26cb1a",
      "meta": {
        "created": "2024-11-22T15:05:52.055139748Z",
        "lastModified": "2024-11-22T15:05:52.055139813Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Users/79ef0d28-f257-4829-97e6-d23d2a26cb1a",
        "resourceType": "User"
      },
      "name": {
        "formatted": "Jane Doe"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "title": "Mrs.",
      "userName": "jane.doe@datadoghq.com"
    }
  ],
  "itemsPerPage": 2,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "startIndex": 1,
  "totalResults": 2
}
```

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"
                
{% /tab %}

## Create user{% #create-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/scim/Users |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/scim/Users |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/scim/Users      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/scim/Users      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/scim/Users     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/scim/Users |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/scim/Users |

### Overview

Create a new user. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
|              | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
|              | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
|              | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
|              | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
|              | schemas      | [string]  | User JSON Schemas.                                                                                     |
|              | title        | string    | The user's title.                                                                                      |
|              | userName     | string    | Unique identifier for the User.                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Definition of a user.

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
|              | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
|              | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
|              | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
|              | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
|              | schemas      | [string]  | User JSON Schemas.                                                                                     |
|              | title        | string    | The user's title.                                                                                      |
|              | userName     | string    | Unique identifier for the User.                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

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
                  \## json-request-body
# 
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "active": true,
  "emails": [
    {
      "primary": true,
      "type": "work",
      "value": "john.doe@datadoghq.com"
    }
  ],
  "name": {
    "formatted": "John Doe"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "Mr.",
  "userName": "john.doe@datadoghq.com"
}
EOF
                
{% /tab %}

## Get user{% #get-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid} |

### Overview

Get a single user using the `user_uuid`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| user_uuid [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Definition of a user.

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
|              | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
|              | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
|              | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
|              | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
|              | schemas      | [string]  | User JSON Schemas.                                                                                     |
|              | title        | string    | The user's title.                                                                                      |
|              | userName     | string    | Unique identifier for the User.                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport user_uuid="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"
                
{% /tab %}

## Update user{% #update-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid} |

### Overview

Update the user with the given `user_uuid`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| user_uuid [*required*] | string | None        |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
|              | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
|              | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
|              | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
|              | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
|              | schemas      | [string]  | User JSON Schemas.                                                                                     |
|              | title        | string    | The user's title.                                                                                      |
|              | userName     | string    | Unique identifier for the User.                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Definition of a user.

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
|              | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
|              | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
|              | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
|              | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
|              | schemas      | [string]  | User JSON Schemas.                                                                                     |
|              | title        | string    | The user's title.                                                                                      |
|              | userName     | string    | Unique identifier for the User.                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

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
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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
                  \## json-request-body
# 
\# Path parametersexport user_uuid="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "active": true,
  "emails": [
    {
      "primary": true,
      "type": "work",
      "value": "john.doe@datadoghq.com"
    }
  ],
  "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
  "name": {
    "formatted": "John Doe"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "Mr.",
  "userName": "john.doe@datadoghq.com"
}
EOF
                
{% /tab %}

## Patch user{% #patch-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid} |

### Overview

Patch the user with the given `user_uuid`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| user_uuid [*required*] | string | None        |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field      | Type     | Description                                                       |
| ------------ | ---------- | -------- | ----------------------------------------------------------------- |
|              | Operations | [object] | A list of update operations to be performed on a user.            |
| Operations   | op         | enum     | The operation to be performed. Allowed enum values: `add,replace` |
| Operations   | path       | string   | An attribute path describing the target of the operation.         |
| Operations   | value      |          | New value to use for the patch operation.                         |
|              | schemas    | [string] | Input JSON Schemas                                                |

{% /tab %}

{% tab title="Example" %}

```json
{
  "Operations": [
    {
      "op": "string",
      "path": "title",
      "value": "undefined"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Definition of a user.

| Parent field | Field        | Type      | Description                                                                                            |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------------------------------------ |
|              | active       | boolean   | A Boolean value indicating the User's administrative status.                                           |
|              | emails       | [object]  | Email addresses for the user.                                                                          |
| emails       | primary      | boolean   | Boolean indicating if this email is the primary email address.                                         |
| emails       | type         | enum      | The type of email. Allowed enum values: `work`                                                         |
| emails       | value        | string    | Email addresses for the user.                                                                          |
|              | id           | string    | The identifier of the resource. Not required when creating a user.                                     |
|              | meta         | object    | Metadata associated with a user.                                                                       |
| meta         | created      | date-time | The date and time the user was created.                                                                |
| meta         | lastModified | date-time | The date and time the user was last changed.                                                           |
| meta         | location     | string    | URL identifying the resource.                                                                          |
| meta         | resourceType | string    | Type of resource.                                                                                      |
|              | name         | object    | The components of user's real name                                                                     |
| name         | formatted    | string    | The full name, including all middle names, titles, and suffixes as appropriate, formatted for display. |
|              | schemas      | [string]  | User JSON Schemas.                                                                                     |
|              | title        | string    | The user's title.                                                                                      |
|              | userName     | string    | Unique identifier for the User.                                                                        |

{% /tab %}

{% tab title="Example" %}

```json
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

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
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \## json-request-body
# 
\# Path parametersexport user_uuid="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "Operations": [
    {
      "op": "replace",
      "path": "title",
      "value": "CEO"
    },
    {
      "op": "replace",
      "value": {
        "name": {
          "formatted": "John Doe"
        }
      }
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
EOF
                
{% /tab %}

## Delete user{% #delete-user %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid} |

### Overview

Delete the group with the given `user_uuid`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                        | Type   | Description |
| --------------------------- | ------ | ----------- |
| user_uuid [*required*] | string | None        |

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
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport user_uuid="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"
                
{% /tab %}

## List groups{% #list-groups %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/scim/Groups |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/scim/Groups |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/scim/Groups      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/scim/Groups      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/scim/Groups     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/scim/Groups |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/scim/Groups |

### Overview

List groups in the organization. Results are paginated by `startIndex` and `count` parameters. Results can be narrowed down by the `filter` parameter. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Query Strings

| Name       | Type    | Description                                                                                                                                                                                                                                                                  |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| startIndex | integer | Specifies the start index to fetch the results (1-indexed).                                                                                                                                                                                                                  |
| count      | integer | Specifies the number of groups to be returned.                                                                                                                                                                                                                               |
| filter     | string  | Specifies the url encoded filter to use to narrow down the results. Filters can be in the form of `displayName eq <group name>` or `externalId eq <external id of group>` or `id eq <group id> and members eq <user uuid>` or `members eq <user uuid> and id eq <group id>`. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
List groups response object.

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | Resources    | [object]  | List of groups matching the request criteria.                            |
| Resources    | displayName  | string    | A human-readable name for the group.                                     |
| Resources    | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
| Resources    | id           | string    | The identifier of the resource. Not required when creating a group.      |
| Resources    | members      | [object]  | A list of members belonging to the team.                                 |
| members      | $ref         | string    | The URI corresponding to a resource that is a member of this group.      |
| members      | display      | string    | Full name of the user.                                                   |
| members      | type         | string    | A label indicating the type of resource. Only supported value is "User". |
| members      | value        | string    | The identifier of the member of this group.                              |
| Resources    | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
| Resources    | schemas      | [string]  | Group JSON Schemas.                                                      |
|              | itemsPerPage | int64     | Number of groups returned per page.                                      |
|              | schemas      | [string]  | List response JSON Schemas.                                              |
|              | startIndex   | int64     | Starting index of the groups for this page (1-indexed).                  |
|              | totalResults | int64     | Total number of groups matching the request criteria.                    |

{% /tab %}

{% tab title="Example" %}

```json
{
  "Resources": [
    {
      "displayName": "Group 1",
      "externalId": "group1",
      "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
      "members": [
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/d34a5f93-5690-4d3f-a293-f2ad5c7a82a4",
          "display": "John Doe",
          "type": "User",
          "value": "d34a5f93-5690-4d3f-a293-f2ad5c7a82a4"
        },
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
          "display": "Jane Doe",
          "type": "User",
          "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
        }
      ],
      "meta": {
        "created": "2024-11-22T15:05:52.055138963Z",
        "lastModified": "2024-11-22T15:05:52.055139017Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Groups/e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
        "resourceType": "Group"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
      ]
    },
    {
      "displayName": "Group 2",
      "externalId": "group2",
      "id": "79ef0d28-f257-4829-97e6-d23d2a26cb1a",
      "members": [
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/29da9fb7-8fca-4e87-bf58-86652253deae",
          "display": "Alice Smith",
          "type": "User",
          "value": "29da9fb7-8fca-4e87-bf58-86652253deae"
        },
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9",
          "display": "Bob Smith",
          "type": "User",
          "value": "f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9"
        }
      ],
      "meta": {
        "created": "2024-11-22T15:05:52.055139748Z",
        "lastModified": "2024-11-22T15:05:52.055139813Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Groups/79ef0d28-f257-4829-97e6-d23d2a26cb1a",
        "resourceType": "Group"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
      ]
    }
  ],
  "itemsPerPage": 2,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "startIndex": 1,
  "totalResults": 2
}
```

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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"
                
{% /tab %}

## Create group{% #create-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/scim/Groups |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/scim/Groups |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/scim/Groups      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/scim/Groups      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/scim/Groups     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/scim/Groups |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/scim/Groups |

### Overview

Create a new group. The group may contain members. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | displayName  | string    | A human-readable name for the group.                                     |
|              | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
|              | id           | string    | The identifier of the resource. Not required when creating a group.      |
|              | members      | [object]  | Members of the group.                                                    |
| members      | $ref         | string    | The URI corresponding to a SCIM resource that is a member of this group. |
| members      | display      | string    | A human-readable name for the group member.                              |
| members      | type         | string    | A label indicating the type of resource.                                 |
| members      | value        | string    | The identifier of the member of this group.                              |
|              | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
|              | schemas      | [string]  | Input JSON Schemas.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

{% /tab %}

### Response

{% tab title="201" %}
Created
{% tab title="Model" %}
Definition of a group.

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | displayName  | string    | A human-readable name for the group.                                     |
|              | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
|              | id           | string    | The identifier of the resource. Not required when creating a group.      |
|              | members      | [object]  | Members of the group.                                                    |
| members      | $ref         | string    | The URI corresponding to a SCIM resource that is a member of this group. |
| members      | display      | string    | A human-readable name for the group member.                              |
| members      | type         | string    | A label indicating the type of resource.                                 |
| members      | value        | string    | The identifier of the member of this group.                              |
|              | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
|              | schemas      | [string]  | Input JSON Schemas.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

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
                  \## json-request-body
# 
\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "displayName": "Group 1",
  "externalId": "group1",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/d34a5f93-5690-4d3f-a293-f2ad5c7a82a4",
      "display": "John Doe",
      "type": "User",
      "value": "d34a5f93-5690-4d3f-a293-f2ad5c7a82a4"
    },
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "Jane Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
EOF
                
{% /tab %}

## Get group{% #get-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/scim/Groups/{group_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id} |

### Overview

Get a single group using the `group_id`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                       | Type   | Description |
| -------------------------- | ------ | ----------- |
| group_id [*required*] | string | None        |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Definition of a group.

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | displayName  | string    | A human-readable name for the group.                                     |
|              | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
|              | id           | string    | The identifier of the resource. Not required when creating a group.      |
|              | members      | [object]  | Members of the group.                                                    |
| members      | $ref         | string    | The URI corresponding to a SCIM resource that is a member of this group. |
| members      | display      | string    | A human-readable name for the group member.                              |
| members      | type         | string    | A label indicating the type of resource.                                 |
| members      | value        | string    | The identifier of the member of this group.                              |
|              | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
|              | schemas      | [string]  | Input JSON Schemas.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

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
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport group_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"
                
{% /tab %}

## Update group{% #update-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                    |
| ----------------- | --------------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v2/scim/Groups/{group_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id} |

### Overview

Update the group with the given `group_id`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                       | Type   | Description |
| -------------------------- | ------ | ----------- |
| group_id [*required*] | string | None        |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | displayName  | string    | A human-readable name for the group.                                     |
|              | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
|              | id           | string    | The identifier of the resource. Not required when creating a group.      |
|              | members      | [object]  | Members of the group.                                                    |
| members      | $ref         | string    | The URI corresponding to a SCIM resource that is a member of this group. |
| members      | display      | string    | A human-readable name for the group member.                              |
| members      | type         | string    | A label indicating the type of resource.                                 |
| members      | value        | string    | The identifier of the member of this group.                              |
|              | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
|              | schemas      | [string]  | Input JSON Schemas.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Definition of a group.

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | displayName  | string    | A human-readable name for the group.                                     |
|              | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
|              | id           | string    | The identifier of the resource. Not required when creating a group.      |
|              | members      | [object]  | Members of the group.                                                    |
| members      | $ref         | string    | The URI corresponding to a SCIM resource that is a member of this group. |
| members      | display      | string    | A human-readable name for the group member.                              |
| members      | type         | string    | A label indicating the type of resource.                                 |
| members      | value        | string    | The identifier of the member of this group.                              |
|              | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
|              | schemas      | [string]  | Input JSON Schemas.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

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
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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

{% tab title="409" %}
Conflict
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
                  \## json-request-body
# 
\# Path parametersexport group_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "displayName": "Group 1",
  "externalId": "group1",
  "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/d34a5f93-5690-4d3f-a293-f2ad5c7a82a4",
      "display": "John Doe",
      "type": "User",
      "value": "d34a5f93-5690-4d3f-a293-f2ad5c7a82a4"
    },
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "Jane Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
EOF
                
{% /tab %}

## Patch group{% #patch-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/scim/Groups/{group_id}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id} |

### Overview

Patch the group with the given `group_id`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                       | Type   | Description |
| -------------------------- | ------ | ----------- |
| group_id [*required*] | string | None        |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field      | Type     | Description                                                                      |
| ------------ | ---------- | -------- | -------------------------------------------------------------------------------- |
|              | Operations | [object] | A list of update operations to be performed on a group.                          |
| Operations   | op         | enum     | The operation to be performed. Allowed enum values: `add,replace,remove`         |
| Operations   | path       | string   | An attribute path describing the target of the operation.                        |
| Operations   | value      |          | JSON element containing the target values required to apply the patch operation. |
|              | schemas    | [string] | Input JSON Schemas                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "Operations": [
    {
      "op": "string",
      "path": "members",
      "value": "{\n    \"displayName\": \"Real new group\",\n    \"id\": \"80df3a9b-24f5-4ebf-9ba0-714455453621\"\n}"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Definition of a group.

| Parent field | Field        | Type      | Description                                                              |
| ------------ | ------------ | --------- | ------------------------------------------------------------------------ |
|              | displayName  | string    | A human-readable name for the group.                                     |
|              | externalId   | string    | An identifier for the resource as defined by the provisioning client.    |
|              | id           | string    | The identifier of the resource. Not required when creating a group.      |
|              | members      | [object]  | Members of the group.                                                    |
| members      | $ref         | string    | The URI corresponding to a SCIM resource that is a member of this group. |
| members      | display      | string    | A human-readable name for the group member.                              |
| members      | type         | string    | A label indicating the type of resource.                                 |
| members      | value        | string    | The identifier of the member of this group.                              |
|              | meta         | object    | Metadata associated with a group.                                        |
| meta         | created      | date-time | The date and time the group was created.                                 |
| meta         | lastModified | date-time | The date and time the group was last changed.                            |
| meta         | location     | string    | URL identifying the resource.                                            |
| meta         | resourceType | string    | Type of resource.                                                        |
|              | schemas      | [string]  | Input JSON Schemas.                                                      |

{% /tab %}

{% tab title="Example" %}

```json
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

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
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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
                  \## json-request-body
# 
\# Path parametersexport group_id="CHANGE_ME"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "Operations": [
    {
      "op": "replace",
      "path": "None",
      "value": {
        "displayName": "Real new group",
        "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad"
      }
    },
    {
      "op": "add",
      "path": "None",
      "value": {
        "members": [
          {
            "$ref": "https://app.datadoghq.com/api/scim/v2/Users/f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9",
            "displayName": "Bob Smith",
            "value": "f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9"
          }
        ]
      }
    },
    {
      "op": "remove",
      "path": "members[value eq \"fddf0cf2-9b60-11ef-ad4b-d6754a54a839\"]",
      "value": null
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
EOF
                
{% /tab %}

## Delete group{% #delete-group %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                       |
| ----------------- | ------------------------------------------------------------------ |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v2/scim/Groups/{group_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id} |

### Overview

Delete the group with the given `group_id`. This endpoint requires all of the following permissions:
`user_access_invite``user_access_manage`


### Arguments

#### Path Parameters

| Name                       | Type   | Description |
| -------------------------- | ------ | ----------- |
| group_id [*required*] | string | None        |

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
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport group_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"
                
{% /tab %}
