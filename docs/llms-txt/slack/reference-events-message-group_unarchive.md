Source: https://docs.slack.dev/reference/events/message/group_unarchive

# group_unarchive message

### A group was unarchived

## Facts

## Required Scopes

No scopes required!

## Compatible APIs

[`RTM`](/legacy/legacy-rtm-api)

## Usage info {#usage-info}

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_unarchive` message subtype event.

```json

{    "token": "XXYYZZ",    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {        "type": "message",        "subtype": "group_unarchive",        "ts": "1361482916.000003",        "text": "<U1234ABC56|@cal> un-archived the group",        "user": "U1234ABC56"    },    "type": "event_callback",    "authorizations": [        {            "team_id": "T123ABC456",            "user_id": "U1234ABC56",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev123ABC456",    "event_time": 123456789}

A `group_unarchive` message is sent when a private group is unarchived.
