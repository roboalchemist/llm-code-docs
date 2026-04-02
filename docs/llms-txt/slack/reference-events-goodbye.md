Source: https://docs.slack.dev/reference/events/goodbye

# goodbye event

### The server intends to close the connection soon

## Facts

## Required Scopes

No scopes required!

## Compatible APIs

[`RTM`](/legacy/legacy-rtm-api)

## Usage info {#usage-info}

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `goodbye` event.

```json
{    "token": "XXYYZZ",    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {        "type": "goodbye"    },    "type": "event_callback",    "authorizations": [        {            "team_id": "T123ABC456",            "user_id": "U123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev123ABC456",    "event_time": 123456789}
```text

The `goodbye` event may be sent by a server that expects it will close the connection after an unspecified amount of time. A well formed client should reconnect to avoid data loss.

Other scenarios where you might encounter the `goodbye` event are:

* reaching the maximum duration of a RTM web socket connection (8 hours)
* your workspace has been inactive for over two minutes
