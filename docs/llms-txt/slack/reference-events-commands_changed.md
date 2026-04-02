Source: https://docs.slack.dev/reference/events/commands_changed

# commands_changed event

### A slash command has been added or changed

## Facts

## Required Scopes

No scopes required!

## Compatible APIs

[`RTM`](/legacy/legacy-rtm-api)

## Usage info {#usage-info}

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `commands_changed` event.

```json
{    "token": "XXYYZZ",    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {        "type": "commands_changed",        "event_ts": "1361482916.000004"    },    "type": "event_callback",    "authorizations": [        {            "team_id": "T123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev123ABC456",    "event_time": 123456789}
```text

The `commands_changed` event is sent to all connections for a workspace when a slash command for that workspace is added, removed or changed.

This functionality is only used by our web client. The other APIs required to support slash command metadata are currently unstable. Until they are released other clients should ignore this event.
