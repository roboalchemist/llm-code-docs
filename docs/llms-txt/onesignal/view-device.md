# Source: https://documentation.onesignal.com/reference/view-device.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View player

> GET https://onesignal.com/api/v1/players/{player_id}

Retrieve a single player record (Subscription) data registered to a specific OneSignal app.

<Warning>
  This is a Legacy API. Use [View User](/reference/view-user) or [CSV Export API](/reference/csv-export) instead.
</Warning>

***

## Path Parameters

| Parameter   | Type   | Required | Description                     |
| ----------- | ------ | -------- | ------------------------------- |
| `player_id` | string | Yes      | The OneSignal ID of the device. |

***

## Query Parameters

| Parameter | Type   | Required | Description            |
| --------- | ------ | -------- | ---------------------- |
| `app_id`  | string | Yes      | Your OneSignal App ID. |

***

## Headers

| Header          | Value                            | Required | Description                        |
| --------------- | -------------------------------- | -------- | ---------------------------------- |
| `Authorization` | `Basic YOUR_LEGACY_REST_API_KEY` | Yes      | Your OneSignal LegacyREST API Key. |

***

## Example Request

```http  theme={null}
GET /api/v1/players/player_id_string?app_id=your_app_id HTTP/1.1
Host: onesignal.com
Authorization: Basic YOUR_LEGACY_REST_API_KEY
```

***

## Example Response

```json{  theme={null}
  "id": "player_id_string",
  "identifier": "push_token_or_email",
  "session_count": 5,
  "language": "en",
  "timezone": -28800,
  "game_version": "1.0",
  "device_os": "14.4",
  "device_type": 1,
  "tags": {
    "level": "10",
    "user_type": "free"
  },
  "last_active": 1625253300,
  "created_at": 1625249800,
  "invalid_identifier": false,
  "external_user_id": "user123"
}
```

### Response Fields

| Field                | Type      | Description                                             |
| -------------------- | --------- | ------------------------------------------------------- |
| `id`                 | string    | OneSignal player ID.                                    |
| `identifier`         | string    | Push token, email, or phone number.                     |
| `session_count`      | integer   | Number of sessions associated with this device.         |
| `language`           | string    | Language set on the device (e.g., "en").                |
| `timezone`           | integer   | Time zone offset in seconds.                            |
| `game_version`       | string    | Version of your app the device is running.              |
| `device_os`          | string    | Operating system version.                               |
| `device_type`        | integer   | Numeric code for platform (0 = iOS, 1 = Android, etc.). |
| `tags`               | object    | Custom tags set on the device.                          |
| `last_active`        | timestamp | Last time the user was active (Unix timestamp).         |
| `created_at`         | timestamp | When the device record was created.                     |
| `invalid_identifier` | boolean   | Whether the push token or identifier is invalid.        |
| `external_user_id`   | string    | Your internal user ID mapped to this device.            |

***

## Errors

* 400 Bad Request – Missing or invalid parameters.
* 401 Unauthorized – Invalid or missing API key.
* 403 Forbidden – Access denied for this app or resource.
* 404 Not Found – The specified player\_id does not exist.

***

Built with [Mintlify](https://mintlify.com).
