# Source: https://documentation.onesignal.com/reference/add-a-device.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a player

> POST `https://onesignal.com/api/v1/players`

Register a new Subscription (aka player) to one of your OneSignal apps.

<Warning>
  This is a Legacy API. Use [Create User](/reference/create-user) or [Create Subscription](/reference/create-subscription) instead.
</Warning>

***

## Headers

| Header          | Value                     | Required | Description                      |
| --------------- | ------------------------- | -------- | -------------------------------- |
| `Content-Type`  | `application/json`        | Yes      | The content type of the request. |
| `Authorization` | `Basic YOUR_REST_API_KEY` | Yes      | Your OneSignal REST API key.     |

***

## Request Body Parameters

| Field                | Type    | Required | Description                                                                |
| -------------------- | ------- | -------- | -------------------------------------------------------------------------- |
| `app_id`             | string  | Yes      | Your OneSignal App ID.                                                     |
| `device_type`        | integer | Yes      | Device platform: 0 = iOS, 1 = Android, 2 = Amazon, 3 = Windows Phone, etc. |
| `identifier`         | string  | No       | Push token, email address, or phone number.                                |
| `language`           | string  | No       | Language code (e.g. "en").                                                 |
| `timezone`           | integer | No       | Time zone offset in seconds.                                               |
| `game_version`       | string  | No       | Version of your app.                                                       |
| `device_model`       | string  | No       | Device model (e.g., "iPhone12,1").                                         |
| `device_os`          | string  | No       | Operating system version (e.g., "13.3").                                   |
| `ad_id`              | string  | No       | Advertising ID.                                                            |
| `sdk`                | string  | No       | OneSignal SDK version (e.g., "050201" for 5.2.1).                          |
| `session_count`      | integer | No       | Number of times the user has used the app.                                 |
| `tags`               | object  | No       | Custom tags as key-value pairs.                                            |
| `external_user_id`   | string  | No       | Your system's user ID for this device.                                     |
| `notification_types` | integer | No       | 1 = subscribed, -2 = unsubscribed, 0 = no permission, etc.                 |

***

## Example Request

```json  theme={null}
POST /api/v1/players HTTP/1.1
Host: onesignal.com
Authorization: Basic YOUR_REST_API_KEY
Content-Type: application/json

{
  "app_id": "your_app_id",
  "device_type": 1,
  "identifier": "abcdef123456",
  "language": "en",
  "timezone": -28800,
  "game_version": "1.0",
  "device_model": "Pixel 4",
  "device_os": "12",
  "ad_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "sdk": "050401",
  "session_count": 5,
  "tags": {
    "user_type": "free",
    "level": "10"
  },
  "external_user_id": "user123",
  "notification_types": 1
}
```

***

## Response

```json  theme={null}
{
  "id": "Subscription_id_string"
}
```

## Errors

* 400 Bad Request – Invalid parameters or missing required fields.
* 401 Unauthorized – Invalid or missing API key.
* 403 Forbidden – Not allowed for your account type or plan.

Built with [Mintlify](https://mintlify.com).
