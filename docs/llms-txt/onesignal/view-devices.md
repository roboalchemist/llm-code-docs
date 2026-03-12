# Source: https://documentation.onesignal.com/reference/view-devices.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View players

> GET `https://onesignal.com/api/v1/players?app_id={app_id}&limit={limit}&offset={offset}`

Retrieve up to 80,000 player records (Subscriptions) registered to a specific OneSignal app.

<Warning>
  This is a Legacy API. Use [View User](/reference/view-user) or [CSV Export API](/reference/csv-export) instead.
</Warning>

***

## Query Parameters

| Parameter | Type   | Required | Description                                            |
| --------- | ------ | -------- | ------------------------------------------------------ |
| `app_id`  | string | Yes      | Your OneSignal App ID.                                 |
| `limit`   | int    | No       | Number of entries to return (max 300, default is 300). |
| `offset`  | int    | No       | Result offset for pagination.                          |

***

## Headers

| Header          | Value                            | Required | Description                         |
| --------------- | -------------------------------- | -------- | ----------------------------------- |
| `Authorization` | `Basic YOUR_LEGACY_REST_API_KEY` | Yes      | Your OneSignal Legacy REST API Key. |

***

## Example Request

```http  theme={null}
GET /api/v1/players?app_id=your_app_id&limit=100&offset=0 HTTP/1.1
Host: onesignal.com
Authorization: Basic YOUR_LEGACY_REST_API_KEY
```

***

## Example Response

```json  theme={null}
{
  "total_count": 6,
  "offset": 0,
  "limit": 300,
  "players": [
    {
      "id": "player_id_1",
      "identifier": "push_token_or_email",
      "session_count": 3,
      "language": "en",
      "timezone": -28800,
      "game_version": "1.0",
      "device_os": "15.0",
      "device_type": 1,
      "tags": {
        "level": "15",
        "user_type": "free"
      },
      "last_active": 1625253300,
      "created_at": 1625249800,
      "invalid_identifier": false,
      "external_user_id": "user123"
    }
  ]
}
```

### Response Fields

| Field                        | Type    | Description                                  |
| ---------------------------- | ------- | -------------------------------------------- |
| `total_count`                | integer | Total number of devices for the app.         |
| `offset`                     | integer | Current pagination offset.                   |
| `limit`                      | integer | Number of devices returned in this response. |
| `players`                    | array   | List of device objects.                      |
| `players[].id`               | string  | Unique OneSignal player ID.                  |
| `players[].identifier`       | string  | Push token, email, or phone number.          |
| `players[].tags`             | object  | Custom tags set on the device.               |
| `players[].external_user_id` | string  | Your internal user ID.                       |

***

## Errors

* 400 Bad Request – Invalid query parameters.
* 401 Unauthorized – Invalid or missing API key.
* 403 Forbidden – Access not allowed for this app or key.

***

Built with [Mintlify](https://mintlify.com).
