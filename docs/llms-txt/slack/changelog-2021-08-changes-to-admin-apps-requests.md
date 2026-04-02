Source: https://docs.slack.dev/changelog/2021-08-changes-to-admin-apps-requests

# Changes to admin app requests

August 30, 2021

`admin.apps.requests.list` API response is enhanced to include the **is\_user\_app\_collaborator** of the app.

## What's changing {#changed}

**is\_user\_app\_collaborator** will be part of the response of the API [`admin.apps.requests.list`](/reference/methods/admin.apps.requests.list) `is_user_app_collaborator` - true if the requesting user is one of the collaborator of the app.

API response including **is\_user\_app\_collaborator**:

```json
{    "ok": true,    "app_requests": [        {            "id": "AXXXXXX",            "app": {                "id": "AXXXXXXXX",                "is_internal": false,                "socket_mode_enabled": false,                "additional_info": ""            },            "previous_resolution": null,            "user": {                "id": "UXXXXXXX"            },            "team": {                "id": "TXXXXXXX"            },            "scopes": [                {                    "name": "bot",                    "description": "Add the ability for people to direct message",                    "is_sensitive": true,                    "token_type": "bot"                },            ],            "message": "Please approve the app",            "is_user_app_collaborator": false        }    ],    "response_metadata": {        "next_cursor": ""    }}
```text

## How to respond or prepare {#prepare}

If you don't plan to consume the `is_user_app_collaborator`, you don't need to do anything.

## When is this happening {#when}

This change happens on August 31, 2021.

## Tags:

* [New feature](/changelog/tags/new-feature)
