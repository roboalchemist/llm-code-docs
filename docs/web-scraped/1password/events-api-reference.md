# Source: https://developer.1password.com/docs/events-api/reference

On this page

# 1Password Events API reference

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

This API reference documents the latest version of the [1Password Events API specifications (1.4.1)](https://i.1password.com/media/1password-events-reporting/1password-events-api_1.4.1.yaml). Learn more about [API versions](/docs/events-api/endpoints#endpoint-versions).

## GET /api/v2/auth/introspect[â€‹](#get-apiv2authintrospect "Direct link to GET /api/v2/auth/introspect") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

A GET call to this endpoint returns a list of events (features) a bearer token is authorized to access, including one or more of: audit events, item usage, and sign-in attempts. It also returns the UUID of the account where the token was issued.

### Parameters[â€‹](#parameters "Direct link to Parameters") 

No parameters.

### Requests[â€‹](#requests "Direct link to Requests") 

Use the full URL of the `introspect` endpoint with your [bearer token](/docs/events-api/authorization/) and the required [request headers](/docs/events-api/request-headers/). A GET request doesn\'t include a body, so the content type header isn\'t needed.

For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Responses[â€‹](#responses "Direct link to Responses") 

200
:   Returns an `Introspection` object

400
:   Bad request

401
:   Unauthorized access

500
:   Internal server error

A successful `200` response returns an `Introspection` object with information about the token.

- Example introspection response
- IntrospectionV2 object schema

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
| Name                  | Type                  | Description                                                                                                          |
+=======================+=======================+======================================================================================================================+
| `uuid`                | string                | The UUID of the Events Reporting integration.                                                                        |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
| `issued_at`           | string                | The date and time the token was issued. Uses the [RFC 3339 standard](https://datatracker.ietf.org/doc/html/rfc3339). |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
| `features`            | array of strings      | A list of event features the integration has access to. Possible values are one or more of:                          |
|                       |                       |                                                                                                                      |
|                       |                       | ::: section                                                                                                          |
|                       |                       | - `auditevents`                                                                                                      |
|                       |                       | - `itemusages`                                                                                                       |
|                       |                       | - `signinattempts`                                                                                                   |
|                       |                       | :::                                                                                                                  |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+
| `account_uuid`        | string                | The UUID of the account where the bearer token was issued.                                                           |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------+

## POST /api/v2/auditevents[â€‹](#post-apiv2auditevents "Direct link to POST /api/v2/auditevents") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

A POST call to this endpoint returns information about actions performed by team members within a 1Password account. Events include when an action was performed and by whom, along with details about the type and object of the action and any other information about the activity. MSP accounts include additional information about the actor\'s account and type. Learn more about [audit events](/docs/events-api/audit-events/).

This endpoint requires a [bearer token](/docs/events-api/authorization/) with the `auditevents` feature. You can make an [introspection call](#get-apiv2authintrospect) to the API to verify if your token is authorized to access audit events.

### Parameters[â€‹](#parameters-1 "Direct link to Parameters") 

No parameters.

### Requests[â€‹](#requests-1 "Direct link to Requests") 

Use the full URL of the `auditevents` endpoint with your [bearer token](/docs/events-api/authorization/) and the required [request headers](/docs/events-api/request-headers/). You must include a [ResetCursor](/docs/events-api/pagination#reset-cursor) object or the [cursor](/docs/events-api/pagination#cursor) from a previous response in the request body.

- Example audit events request with a reset cursor
- Example audit events request with a continuing cursor

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Responses[â€‹](#responses-1 "Direct link to Responses") 

A successful `200` response returns an `AuditEventItemsV2` object wrapping cursor properties and an array of `AuditEventV2` objects. The included cursor can be used to fetch more data or continue the polling process.

200
:   Returns an `AuditEventItemsV2` object

400
:   Bad request

401
:   Unauthorized access

500
:   Internal server error

- Example audit event response
- AuditEventV2 object schemas

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

#### AuditEventItemsV2 object schema[â€‹](#auditeventitemsv2-object-schema "Direct link to AuditEventItemsV2 object schema") 

  Name         Type      Description
  ------------ --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `cursor`     string    Cursor to return more event data or to continue polling.
  `has_more`   boolean   Whether there\'s more data to be returned using the cursor. If the value is `true`, there may be more events. If the value is `false`, there are no more events.
  `items`      array     An array of [AuditEventV2 objects](#auditeventv2-object-schema).

##### AuditEventV2 object schema[â€‹](#auditeventv2-object-schema "Direct link to AuditEventV2 object schema") 

+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                  | Type                  | Description                                                                                                                                                                               |
+=======================+=======================+===========================================================================================================================================================================================+
| `uuid`                | string                | The UUID of the action event.                                                                                                                                                             |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `timestamp`           | string                | The date and time when the action was performed. Uses the [RFC 3339 standard](https://datatracker.ietf.org/doc/html/rfc3339).                                                             |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `actor_uuid`          | string                | The UUID of the user who performed the action.                                                                                                                                            |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `actor_details`       | object                | A [user object](#userv2-object-schema).                                                                                                                                                   |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `actor_type`          | string                | The type of user who performed the action (internal or external). Possible values are:                                                                                                    |
|                       |                       |                                                                                                                                                                                           |
|                       |                       | ::: section                                                                                                                                                                               |
|                       |                       | - `user`                                                                                                                                                                                  |
|                       |                       | - `external_user` (MSP accounts only)                                                                                                                                                     |
|                       |                       | :::                                                                                                                                                                                       |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `actor_account_uuid`  | string                | The UUID of the account the user belongs to.                                                                                                                                              |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `account_uuid`        | string                | The UUID of the account where the action was performed.                                                                                                                                   |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `action`              | string                | The type of action that was performed. Possible values are:                                                                                                                               |
|                       |                       |                                                                                                                                                                                           |
|                       |                       | ::: section                                                                                                                                                                               |
|                       |                       | - `"activate"`                                                                                                                                                                            |
|                       |                       | - `"addgsso"`                                                                                                                                                                             |
|                       |                       | - `"begin"`                                                                                                                                                                               |
|                       |                       | - `"beginr"`                                                                                                                                                                              |
|                       |                       | - `"cancel"`                                                                                                                                                                              |
|                       |                       | - `"cancelr"`                                                                                                                                                                             |
|                       |                       | - `"changeks"`                                                                                                                                                                            |
|                       |                       | - `"changeks"`                                                                                                                                                                            |
|                       |                       | - `"changela"`                                                                                                                                                                            |
|                       |                       | - `"changemp"`                                                                                                                                                                            |
|                       |                       | - `"changenm"`                                                                                                                                                                            |
|                       |                       | - `"changesk"`                                                                                                                                                                            |
|                       |                       | - `"chngasso"`                                                                                                                                                                            |
|                       |                       | - `"chngdsso"`                                                                                                                                                                            |
|                       |                       | - `"chngpsso"`                                                                                                                                                                            |
|                       |                       | - `"complete"`                                                                                                                                                                            |
|                       |                       | - `"completr"`                                                                                                                                                                            |
|                       |                       | - `"convert"`                                                                                                                                                                             |
|                       |                       | - `"create"`                                                                                                                                                                              |
|                       |                       | - `"dealldev"`                                                                                                                                                                            |
|                       |                       | - `"delete"`                                                                                                                                                                              |
|                       |                       | - `"delgsso"`                                                                                                                                                                             |
|                       |                       | - `"delshare"`                                                                                                                                                                            |
|                       |                       | - `"deolddev"`                                                                                                                                                                            |
|                       |                       | - `"detchild"`                                                                                                                                                                            |
|                       |                       | - `"disblduo"`                                                                                                                                                                            |
|                       |                       | - `"disblmfa"`                                                                                                                                                                            |
|                       |                       | - `"disblsso"`                                                                                                                                                                            |
|                       |                       | - `"dlgsess"`                                                                                                                                                                             |
|                       |                       | - `"dvrfydmn"`                                                                                                                                                                            |
|                       |                       | - `"enblduo"`                                                                                                                                                                             |
|                       |                       | - `"enblmfa"`                                                                                                                                                                             |
|                       |                       | - `"enblsso"`                                                                                                                                                                             |
|                       |                       | - `"expire"`                                                                                                                                                                              |
|                       |                       | - `"export"`                                                                                                                                                                              |
|                       |                       | - `"grant"`                                                                                                                                                                               |
|                       |                       | - `"hide"`                                                                                                                                                                                |
|                       |                       | - `"join"`                                                                                                                                                                                |
|                       |                       | - `"launchi"`                                                                                                                                                                             |
|                       |                       | - `"leave"`                                                                                                                                                                               |
|                       |                       | - `"musercom"`                                                                                                                                                                            |
|                       |                       | - `"muserdec"`                                                                                                                                                                            |
|                       |                       | - `"patch"`                                                                                                                                                                               |
|                       |                       | - `"propose"`                                                                                                                                                                             |
|                       |                       | - `"provsn"`                                                                                                                                                                              |
|                       |                       | - `"prsndall"`                                                                                                                                                                            |
|                       |                       | - `"purge"`                                                                                                                                                                               |
|                       |                       | - `"rdmchild"`                                                                                                                                                                            |
|                       |                       | - `"reactive"`                                                                                                                                                                            |
|                       |                       | - `"reauth"`                                                                                                                                                                              |
|                       |                       | - `"replace"`                                                                                                                                                                             |
|                       |                       | - `"replace"`                                                                                                                                                                             |
|                       |                       | - `"resendts"`                                                                                                                                                                            |
|                       |                       | - `"revoke"`                                                                                                                                                                              |
|                       |                       | - `"role"`                                                                                                                                                                                |
|                       |                       | - `"sdvcsso"`                                                                                                                                                                             |
|                       |                       | - `"sendpkg"`                                                                                                                                                                             |
|                       |                       | - `"sendts"`                                                                                                                                                                              |
|                       |                       | - `"share"`                                                                                                                                                                               |
|                       |                       | - `"ssotknv"`                                                                                                                                                                             |
|                       |                       | - `"suspend"`                                                                                                                                                                             |
|                       |                       | - `"tdvcsso"`                                                                                                                                                                             |
|                       |                       | - `"trename"`                                                                                                                                                                             |
|                       |                       | - `"trevoke"`                                                                                                                                                                             |
|                       |                       | - `"trvlaway"`                                                                                                                                                                            |
|                       |                       | - `"trvlback"`                                                                                                                                                                            |
|                       |                       | - `"tverify"`                                                                                                                                                                             |
|                       |                       | - `"uisas"`                                                                                                                                                                               |
|                       |                       | - `"unhide"`                                                                                                                                                                              |
|                       |                       | - `"unknown"`                                                                                                                                                                             |
|                       |                       | - `"unlink"`                                                                                                                                                                              |
|                       |                       | - `"updatduo"`                                                                                                                                                                            |
|                       |                       | - `"update"`                                                                                                                                                                              |
|                       |                       | - `"updatea"`                                                                                                                                                                             |
|                       |                       | - `"updatfw"`                                                                                                                                                                             |
|                       |                       | - `"updatmfa"`                                                                                                                                                                            |
|                       |                       | - `"upguest"`                                                                                                                                                                             |
|                       |                       | - `"uvrfydmn"`                                                                                                                                                                            |
|                       |                       | - `"verify"`                                                                                                                                                                              |
|                       |                       | - `"view"`                                                                                                                                                                                |
|                       |                       | - `"vrfydmn"`                                                                                                                                                                             |
|                       |                       | :::                                                                                                                                                                                       |
|                       |                       |                                                                                                                                                                                           |
|                       |                       | [Learn about audit event actions](/docs/events-api/audit-events/).                                                                                                                        |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `object_type`         | string                | The type of object the action was performed on. Possible values are:                                                                                                                      |
|                       |                       |                                                                                                                                                                                           |
|                       |                       | ::: section                                                                                                                                                                               |
|                       |                       | - `"account"`                                                                                                                                                                             |
|                       |                       | - `"card"`                                                                                                                                                                                |
|                       |                       | - `"cred"`                                                                                                                                                                                |
|                       |                       | - `"device"`                                                                                                                                                                              |
|                       |                       | - `"dlgdsess"`                                                                                                                                                                            |
|                       |                       | - `"ec"`                                                                                                                                                                                  |
|                       |                       | - `"famchild"`                                                                                                                                                                            |
|                       |                       | - `"file"`                                                                                                                                                                                |
|                       |                       | - `"gm"`                                                                                                                                                                                  |
|                       |                       | - `"group"`                                                                                                                                                                               |
|                       |                       | - `"gva"`                                                                                                                                                                                 |
|                       |                       | - `"invite"`                                                                                                                                                                              |
|                       |                       | - `"item"`                                                                                                                                                                                |
|                       |                       | - `"itemhist"`                                                                                                                                                                            |
|                       |                       | - `"items"`                                                                                                                                                                               |
|                       |                       | - `"miguser"`                                                                                                                                                                             |
|                       |                       | - `"mngdacc"`                                                                                                                                                                             |
|                       |                       | - `"pm"`                                                                                                                                                                                  |
|                       |                       | - `"report"`                                                                                                                                                                              |
|                       |                       | - `"sa"`                                                                                                                                                                                  |
|                       |                       | - `"satoken"`                                                                                                                                                                             |
|                       |                       | - `"slackapp"`                                                                                                                                                                            |
|                       |                       | - `"sso"`                                                                                                                                                                                 |
|                       |                       | - `"ssotkn"`                                                                                                                                                                              |
|                       |                       | - `"sub"`                                                                                                                                                                                 |
|                       |                       | - `"template"`                                                                                                                                                                            |
|                       |                       | - `"user"`                                                                                                                                                                                |
|                       |                       | - `"uva"`                                                                                                                                                                                 |
|                       |                       | - `"vault"`                                                                                                                                                                               |
|                       |                       | - `"vaultkey"`                                                                                                                                                                            |
|                       |                       | :::                                                                                                                                                                                       |
|                       |                       |                                                                                                                                                                                           |
|                       |                       | [Learn about audit event objects](/docs/events-api/audit-events/).                                                                                                                        |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `object_uuid`         | string                | The unique identifier for the object the action was performed on.                                                                                                                         |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `object_details`      | object                | An [object details object](#object-details-object-schema). Returned if the object is a user.                                                                                              |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `aux_id`              | integer               | The identifier for someone or something that provides additional information about the activity. For example, the ID of a device that a user adds or removes from an account.             |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `aux_uuid`            | string                | The unique identifier for someone or something that provides additional information about the activity. For example, the UUID of a team member who joins or leaves a group in an account. |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `aux_details`         | object                | An [aux details object](#aux-details-object-schema). Returned if the aux details relate to a user.                                                                                        |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `aux_info`            | string                | Additional information about the activity.                                                                                                                                                |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session`             | object                | A [session object](#session-object-schema).                                                                                                                                               |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `location`            | object                | A [location object](#location-object-schema) that contains details about the geolocation of the client based on the client\'s IP address at the time the event was performed.             |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### UserV2 object schema[â€‹](#userv2-object-schema "Direct link to UserV2 object schema") 

+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| Name                          | Type                  | Description                                                                            |
+===============================+=======================+========================================================================================+
| `uuid`                        | string                | The UUID of the user who performed the action.                                         |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `name`                        | string                | The name of the user who performed the action.                                         |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `email`                       | string                | The email address of the user who performed the action.                                |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `user_type`\                  | string                | The type of user who performed the action (internal or external). Possible values are: |
|                               |                       |                                                                                        |
| [(MSP accounts only)] |                       | ::: section                                                                            |
|                               |                       | - `user`                                                                               |
|                               |                       | - `external_user`                                                                      |
|                               |                       | :::                                                                                    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `user_account_uuid`\          | string                | The UUID of the user\'s account.                                                       |
|                               |                       |                                                                                        |
| [(MSP accounts only)] |                       |                                                                                        |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+

###### Object details object schema[â€‹](#object-details-object-schema "Direct link to Object details object schema") 

  Name      Type     Description
  --------- -------- ----------------------------------------------------------------
  `uuid`    string   The UUID of the user who is the object of the action.
  `name`    string   The name of the user who is the object of the action.
  `email`   string   The email address of the user who is the object of the action.

###### Aux details object schema[â€‹](#aux-details-object-schema "Direct link to Aux details object schema") 

  Name      Type     Description
  --------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `uuid`    string   The UUID of the user related to the additional information about the activity. For example, the user who was added to or removed from the account or vault or whom created or deleted the device.
  `name`    string   The name of the user related to the additional information about the activity.
  `email`   string   The email address of the user related to the additional information about the activity.

###### Session object schema[â€‹](#session-object-schema "Direct link to Session object schema") 

  Name            Type     Description
  --------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------
  `uuid`          string   The UUID of the session.
  `login_time`    string   The date and time the client signed in and started the session. Uses the [RFC 3339 standard](https://datatracker.ietf.org/doc/html/rfc3339).
  `device_uuid`   string   The UUID of the device signed in to the session.
  `ip`            string   The IP address used for the session.

###### Location object schema[â€‹](#location-object-schema "Direct link to Location object schema") 

  Name          Type     Description
  ------------- -------- -------------------------------------------------------------------------------------------
  `country`     string   The country where the action was performed.
  `region`      string   The region where the action was performed.
  `city`        string   The city where the action was performed.
  `longitude`   number   A coordinate that specifies the longitudinal location for where the action was performed.
  `latitude`    number   A coordinate that specifies the latitudinal location for where the action was performed.

## POST /api/v2/itemusages[â€‹](#post-apiv2itemusages "Direct link to POST /api/v2/itemusages") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

A POST call to this endpoint returns information about items in shared vaults that have been modified, accessed, or used. Events include the name and IP address of the user who accessed the item, when the item was accessed, and the vault where the item is stored. Learn more about [item usage actions](/docs/events-api/item-usage-actions/).

This endpoint requires a [bearer token](/docs/events-api/authorization/) with the `itemusages` feature. You can make an [introspection call](#get-apiv2authintrospect) to the API to verify if your token is authorized to access sign-in events.

### Parameters[â€‹](#parameters-2 "Direct link to Parameters") 

No parameters.

### Requests[â€‹](#requests-2 "Direct link to Requests") 

Use the full URL of the `itemusages` endpoint with your [bearer token](/docs/events-api/authorization/) and the required [request headers](/docs/events-api/request-headers/). You must include a [ResetCursor](/docs/events-api/pagination#reset-cursor) object or the [cursor](/docs/events-api/pagination#cursor) from a previous response in the request body.

- Example item usage request with a reset cursor
- Example item usage request with a continuing cursor

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Responses[â€‹](#responses-2 "Direct link to Responses") 

200
:   Returns an `ItemUsageV2` response object

400
:   Bad request

401
:   Unauthorized access

500
:   Internal server error

A successful `200` response returns an `ItemUsageItemsV2` object wrapping cursor properties and an array of `ItemUsageV2` objects. The included cursor can be used to fetch more data or continue the polling process.

The response also includes a cursor to continue fetching more data or to use the next time you make a request.

- Example item usage response
- ItemUsageV2 object schemas

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

#### ItemUsageItemsV2 object schema[â€‹](#itemusageitemsv2-object-schema "Direct link to ItemUsageItemsV2 object schema") 

  Name         Type      Description
  ------------ --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `items`      array     An array of [ItemUsageV2 objects](#itemusagev2-object-schema).
  `cursor`     string    Cursor to return more event data or to continue polling.
  `has_more`   boolean   Whether there\'s more data to be returned using the cursor. If the value is `true`, there may be more events. If the value is `false`, there are no more events.

##### ItemUsageV2 object schema[â€‹](#itemusagev2-object-schema "Direct link to ItemUsageV2 object schema") 

+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                          | Type                  | Description                                                                                                                                                                     |
+===============================+=======================+=================================================================================================================================================================================+
| `uuid`                        | string                | The UUID of the event.                                                                                                                                                          |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `timestamp`                   | string                | The date and time of the event. [RFC 3339 standard](https://datatracker.ietf.org/doc/html/rfc3339).                                                                             |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `used_version`                | integer               | The version of the item that was accessed.                                                                                                                                      |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `vault_uuid`                  | string                | The UUID of the vault the item is in.                                                                                                                                           |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `item_uuid`                   | string                | The UUID of the item that was accessed.                                                                                                                                         |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `action`                      | string                | Details about how the item was used. Actions are only captured from client apps using 1Password 8.4.0 or later. Possible values are:                                            |
|                               |                       |                                                                                                                                                                                 |
|                               |                       | ::: section                                                                                                                                                                     |
|                               |                       | - `"enter-item-edit-mode"`                                                                                                                                                      |
|                               |                       | - `"export"`                                                                                                                                                                    |
|                               |                       | - `"fill"`                                                                                                                                                                      |
|                               |                       | - `"other"`                                                                                                                                                                     |
|                               |                       | - `"reveal"`                                                                                                                                                                    |
|                               |                       | - `"secure-copy"`                                                                                                                                                               |
|                               |                       | - `"select-sso-provider"`                                                                                                                                                       |
|                               |                       | - `"server-create"`                                                                                                                                                             |
|                               |                       | - `"server-fetch"`                                                                                                                                                              |
|                               |                       | - `"server-update"`                                                                                                                                                             |
|                               |                       | - `"share"`                                                                                                                                                                     |
|                               |                       | :::                                                                                                                                                                             |
|                               |                       |                                                                                                                                                                                 |
|                               |                       | [Learn about item usage actions](/docs/events-api/item-usage-actions/).                                                                                                         |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `user`                        | object                | A [user object](#userv2-object-schema-1).                                                                                                                                       |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `client`                      | object                | A [client object](#client-object-schema).                                                                                                                                       |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `location`                    | object                | A [location object](#location-object-schema-1) that contains details about the geolocation of the client based on the client\'s IP address at the time the event was performed. |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `account_uuid`\               | string                | The UUID of the account where the action was performed.                                                                                                                         |
|                               |                       |                                                                                                                                                                                 |
| [(MSP accounts only)] |                       |                                                                                                                                                                                 |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### UserV2 object schema[â€‹](#userv2-object-schema-1 "Direct link to UserV2 object schema") 

+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| Name                          | Type                  | Description                                                                            |
+===============================+=======================+========================================================================================+
| `uuid`                        | string                | The UUID of the user that accessed the item or attempted to sign in to the account.    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `name`                        | string                | The name of the user, hydrated at the time the event was generated.                    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `email`                       | string                | The email address of the user, hydrated at the time the event was generated.           |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `user_type`\                  | string                | The type of user who performed the action (internal or external). Possible values are: |
|                               |                       |                                                                                        |
| [(MSP accounts only)] |                       | ::: section                                                                            |
|                               |                       | - `user`                                                                               |
|                               |                       | - `external_user`                                                                      |
|                               |                       | :::                                                                                    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `user_account_uuid`\          | string                | The UUID of the user\'s account.                                                       |
|                               |                       |                                                                                        |
| [(MSP accounts only)] |                       |                                                                                        |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+

###### Client object schema[â€‹](#client-object-schema "Direct link to Client object schema") 

  Name                 Type     Description
  -------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  `app_name`           string   The name of the 1Password app the item was accessed from.
  `app_version`        string   The version number of the app.
  `platform_name`      string   The name of the platform the item was accessed from.
  `platform_version`   string   The version of the browser or computer where 1Password is installed or the CPU of the machine where the 1Password command-line tool is installed.
  `os_name`            string   The name of the operating system the item was accessed from.
  `os_version`         string   The version of the operating system the item was accessed from.
  `ip_address`         string   The IP address the item was accessed from.

###### Location object schema[â€‹](#location-object-schema-1 "Direct link to Location object schema") 

  Name          Type     Description
  ------------- -------- ----------------------------------------------------------------------------------------
  `country`     string   The country where the item was accessed.
  `region`      string   The region where the item was accessed.
  `city`        string   The city where the item was accessed.
  `longitude`   number   A coordinate that specifies the longitudinal location for where the item was accessed.
  `latitude`    number   A coordinate that specifies the latitudinal location for where the item was accessed.

## POST /api/v2/signinattempts[â€‹](#post-apiv2signinattempts "Direct link to POST /api/v2/signinattempts") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

A POST call to this endpoint returns information about sign-in attempts. Events include the name and IP address of the user who attempted to sign in to the account, when the attempt was made, and â€" for failed attempts â€" the cause of the failure. For MSP accounts, events also include additional information about the user\'s account and type.

This endpoint requires a [bearer token](/docs/events-api/authorization/) with the `signinattempts` feature. You can make an [introspection call](#get-apiv2authintrospect) to the API to verify if your token is authorized to access sign-in events.

### Parameters[â€‹](#parameters-3 "Direct link to Parameters") 

No parameters.

### Requests[â€‹](#requests-3 "Direct link to Requests") 

Use the full URL of the `signinattempts` endpoint with your [bearer token](/docs/events-api/authorization/) and the required [request headers](/docs/events-api/request-headers/). You must include a [ResetCursor](/docs/events-api/pagination#reset-cursor) object or the [cursor](/docs/events-api/pagination#cursor) from a previous response in the request body.

- Example request with a reset cursor
- Example request with a continuing cursor

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Responses[â€‹](#responses-3 "Direct link to Responses") 

200
:   Returns a `SignInAttemptItemsV2` object

400
:   Bad request

401
:   Unauthorized access

500
:   Internal server error

A successful `200` response returns a `SignInAttemptItemsV2` object wrapping cursor properties and an array of `SignInAttemptV2` objects. The included cursor can be used to fetch more data or continue the polling process.

- Example sign-in attempt response
- SignInAttemptsV2 object schemas

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

#### SignInAttemptItemsV2 object schema[â€‹](#signinattemptitemsv2-object-schema "Direct link to SignInAttemptItemsV2 object schema") 

  Name         Type      Description
  ------------ --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `items`      array     An array of [SignInAttemptsV2 objects](#signinattemptsv2-object-schema).
  `cursor`     string    Cursor to return more event data or to continue polling.
  `has_more`   boolean   Whether there\'s more data to be returned using the cursor. If the value is `true`, there may be more events. If the value is `false`, there are no more events.

##### SignInAttemptsV2 object schema[â€‹](#signinattemptsv2-object-schema "Direct link to SignInAttemptsV2 object schema") 

+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                          | Type                  | Description                                                                                                                                                                     |
+===============================+=======================+=================================================================================================================================================================================+
| `uuid`                        | string                | The UUID of the event.                                                                                                                                                          |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `session_uuid`                | string                | The UUID of the session that created the event.                                                                                                                                 |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `timestamp`                   | string                | The date and time of the sign-in attempt. Uses the [RFC 3339 standard](https://datatracker.ietf.org/doc/html/rfc3339).                                                          |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `category`                    | string                | The category of the sign-in attempt. Possible values are:                                                                                                                       |
|                               |                       |                                                                                                                                                                                 |
|                               |                       | ::: section                                                                                                                                                                     |
|                               |                       | - `"success"`                                                                                                                                                                   |
|                               |                       | - `"credentials_failed"`                                                                                                                                                        |
|                               |                       | - `"mfa_failed"`                                                                                                                                                                |
|                               |                       | - `"sso_failed"`                                                                                                                                                                |
|                               |                       | - `"modern_version_failed"`                                                                                                                                                     |
|                               |                       | - `"firewall_failed"`                                                                                                                                                           |
|                               |                       | - `"firewall_reported_success"`                                                                                                                                                 |
|                               |                       | :::                                                                                                                                                                             |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `type`                        | string                | Details about the sign-in attempt. Possible values are:                                                                                                                         |
|                               |                       |                                                                                                                                                                                 |
|                               |                       | ::: section                                                                                                                                                                     |
|                               |                       | - `"all_blocked"`                                                                                                                                                               |
|                               |                       | - `"anonymous_blocked"`                                                                                                                                                         |
|                               |                       | - `"code_bad"`                                                                                                                                                                  |
|                               |                       | - `"code_disabled"`                                                                                                                                                             |
|                               |                       | - `"code_timeout"`                                                                                                                                                              |
|                               |                       | - `"continent_blocked"`                                                                                                                                                         |
|                               |                       | - `"country_blocked"`                                                                                                                                                           |
|                               |                       | - `"credentials_ok"`                                                                                                                                                            |
|                               |                       | - `"duo_bad"`                                                                                                                                                                   |
|                               |                       | - `"duo_disabled"`                                                                                                                                                              |
|                               |                       | - `"duo_native_bad"`                                                                                                                                                            |
|                               |                       | - `"duo_timeout"`                                                                                                                                                               |
|                               |                       | - `"federated"`                                                                                                                                                                 |
|                               |                       | - `"ip_blocked"`                                                                                                                                                                |
|                               |                       | - `"mfa_missing"`                                                                                                                                                               |
|                               |                       | - `"mfa_ok"`                                                                                                                                                                    |
|                               |                       | - `"modern_version_missing"`                                                                                                                                                    |
|                               |                       | - `"modern_version_old"`                                                                                                                                                        |
|                               |                       | - `"non_sso_user"`                                                                                                                                                              |
|                               |                       | - `"password_secret_bad"`                                                                                                                                                       |
|                               |                       | - `"platform_secret_bad"`                                                                                                                                                       |
|                               |                       | - `"platform_secret_disabled"`                                                                                                                                                  |
|                               |                       | - `"platform_secret_proxy"`                                                                                                                                                     |
|                               |                       | - `"service_account_sso_denied"`                                                                                                                                                |
|                               |                       | - `"sso_user_mismatch"`                                                                                                                                                         |
|                               |                       | - `"totp_bad"`                                                                                                                                                                  |
|                               |                       | - `"totp_disabled"`                                                                                                                                                             |
|                               |                       | - `"totp_timeout"`                                                                                                                                                              |
|                               |                       | - `"u2f_bad"`                                                                                                                                                                   |
|                               |                       | - `"u2f_disabled"`                                                                                                                                                              |
|                               |                       | - `"u2f_timeout"`                                                                                                                                                               |
|                               |                       | :::                                                                                                                                                                             |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `country`                     | string                | The country code of the event. Uses the [ISO 3166 standard](https://www.iso.org/iso-3166-country-codes.html).                                                                   |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `details`                     | object                | A [details object](#details-object-schema) that contains additional information about the sign-in attempt.                                                                      |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `target_user`                 | object                | A [user object](#userv2-object-schema-2).                                                                                                                                       |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `client`                      | object                | A [client object](#client-object-schema-1).                                                                                                                                     |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `location`                    | object                | A [location object](#location-object-schema-2) that contains details about the geolocation of the client based on the client\'s IP address at the time the event was performed. |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `account_uuid`\               | string                | The UUID of the account where the action was performed.                                                                                                                         |
|                               |                       |                                                                                                                                                                                 |
| [(MSP accounts only)] |                       |                                                                                                                                                                                 |
+-------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### Details object schema[â€‹](#details-object-schema "Direct link to Details object schema") 

  Name      Type     Description
  --------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `value`   string   The additional information about the sign-in attempt, such as any firewall rules that prevent a user from signing in. For example, in the event of a sign-in attempt blocked by firewall rules, the value is the country, continent, or IP address of the sign-in attempt.

###### UserV2 object schema[â€‹](#userv2-object-schema-2 "Direct link to UserV2 object schema") 

+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| Name                          | Type                  | Description                                                                            |
+===============================+=======================+========================================================================================+
| `uuid`                        | string                | The UUID of the user that accessed the item or attempted to sign in to the account.    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `name`                        | string                | The name of the user, hydrated at the time the event was generated.                    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `email`                       | string                | The email address of the user, hydrated at the time the event was generated.           |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `user_type`\                  | string                | The type of user who performed the action (internal or external). Possible values are: |
|                               |                       |                                                                                        |
| [(MSP accounts only)] |                       | ::: section                                                                            |
|                               |                       | - `user`                                                                               |
|                               |                       | - `external_user`                                                                      |
|                               |                       | :::                                                                                    |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+
| `user_account_uuid`\          | string                | The UUID of the user\'s account.                                                       |
|                               |                       |                                                                                        |
| [(MSP accounts only)] |                       |                                                                                        |
+-------------------------------+-----------------------+----------------------------------------------------------------------------------------+

###### Client object schema[â€‹](#client-object-schema-1 "Direct link to Client object schema") 

  Name                 Type     Description
  -------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  `app_name`           string   The name of the 1Password app the item was accessed from.
  `app_version`        string   The version number of the app.
  `platform_name`      string   The name of the platform the item was accessed from.
  `platform_version`   string   The version of the browser or computer where 1Password is installed or the CPU of the machine where the 1Password command-line tool is installed.
  `os_name`            string   The name of the operating system the item was accessed from.
  `os_version`         string   The version of the operating system the item was accessed from.
  `ip_address`         string   The IP address the item was accessed from.

###### Location object schema[â€‹](#location-object-schema-2 "Direct link to Location object schema") 

  Name          Type     Description
  ------------- -------- -------------------------------------------------------------------------------------------
  `country`     string   The country where the sign-in attempt was made.
  `region`      string   The region where the sign-in attempt was made.
  `city`        string   The city where the sign-in attempt was made.
  `longitude`   number   A coordinate that specifies the longitudinal location where the sign-in attempt was made.
  `latitude`    number   A coordinate that specifies the latitudinal location where the sign-in attempt was made.

## ErrorResponse object[â€‹](#errorresponse-object "Direct link to ErrorResponse object") 

- Example error response
- ErrorResponse object schema

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

  Name        Type      Description
  ----------- --------- --------------------------------
  `status`    integer   The HTTP status code.
  `message`   string    A message detailing the error.