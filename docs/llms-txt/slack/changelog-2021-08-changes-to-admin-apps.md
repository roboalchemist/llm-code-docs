Source: https://docs.slack.dev/changelog/2021-08-changes-to-admin-apps

# Changes to admin apps

August 30, 2021

Admin apps API response is enhanced to include the **developer\_type** of the app.

## What's changing {#changed}

**developer\_type** will be part of the response for APIs

* [`admin.apps.requests.list`](/reference/methods/admin.apps.requests.list)
* [`admin.apps.approved.list`](/reference/methods/admin.apps.approved.list)
* [`admin.apps.restricted.list`](/reference/methods/admin.apps.restricted.list)

**developer\_type** is an enum with values

* `slack` - identifies the app is developed by Slack.
* `internal` - identifies the app is developed by the same team.
* `third_party` - identifies the app is developed by external developer.

API response including **developer\_type**:

```json
{"ok": true,    "app_requests": [        {            "id": "AXXXXXX",            "app": {                "id": "AXXXXXX",                "is_app_directory_approved": true,                "is_internal": false,                "developer_type": "third_party"                },                "additional_info": ""            },            "previous_resolution": null,            "user": {                "id": "UXXXXXX"            },            "team": {                "id": "TXXXXXX"            },            "scopes": [                {                    "name": "bot",                    "description": "Add the ability for people to direct message",                    "is_sensitive": true,                    "token_type": "bot"                },            ],            "message": "Please approve"        }    ],    "response_metadata": {        "next_cursor": ""    }}
```text

## How to respond or prepare {#prepare}

If you don't plan to consume the `developer_type`, you don't need to do anything.

## When is this happening {#when}

This change happens on August 31, 2021.

## Tags:

* [New feature](/changelog/tags/new-feature)
