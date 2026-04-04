Source: https://docs.slack.dev/reference/events/message/group_archive

# group_archive message

### A group was archived

## Facts

## Required Scopes

No scopes required!

## Compatible APIs

[`RTM`](/legacy/legacy-rtm-api)

## Usage info {#usage-info}

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_archive` message subtype event.

```json

{    "token": "XXYYZZ",    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {        "type": "message",        "subtype": "group_archive",        "ts": "1361482916.000003",        "text": "<U1234|@cal> archived the group",        "user": "U123ABC456",        "members": [            "U1234",            "U5678"        ]    },    "type": "event_callback",    "authorizations": [        {            "team_id": "T123ABC456",            "user_id": "U123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev123ABC456",    "event_time": 123456789}

A `group_archive` message is sent when a private group is archived.
