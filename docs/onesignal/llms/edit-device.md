# Source: https://documentation.onesignal.com/reference/edit-device.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit player

> put https://onesignal.com/api/v1/players/{player_id}

Update a player's (Subscription's) information using the Subscription ID.

<Warning>
  This is a Legacy API. Use [Update User](/reference/update-user) or [Update Subscription](/reference/update-subscription) instead.
</Warning>

***

## Path Parameters

| Parameter   | Type   | Required | Description                    |
| ----------- | ------ | -------- | ------------------------------ |
| `player_id` | string | Yes      | The OneSignal Subscription ID. |

***

## Headers

| Header          | Value                            | Required | Description                         |
| --------------- | -------------------------------- | -------- | ----------------------------------- |
| `Authorization` | `Basic YOUR_LEGACY_REST_API_KEY` | Yes      | Your OneSignal Legacy REST API Key. |
| `Content-Type`  | `application/json`               | Yes      | The content type of the request.    |

***

## Request Body Parameters

| Field                | Type    | Required | Description                                                |
| -------------------- | ------- | -------- | ---------------------------------------------------------- |
| `app_id`             | string  | Yes      | Your OneSignal App ID.                                     |
| `identifier`         | string  | No       | Push token, email, or phone number.                        |
| `language`           | string  | No       | Language code (e.g., "en").                                |
| `timezone`           | integer | No       | Time zone offset in seconds.                               |
| `game_version`       | string  | No       | App version.                                               |
| `device_model`       | string  | No       | Device model (e.g., "iPhone12,1").                         |
| `device_os`          | string  | No       | OS version (e.g., "14.5").                                 |
| `ad_id`              | string  | No       | Advertising ID.                                            |
| `sdk`                | string  | No       | OneSignal SDK version.                                     |
| `tags`               | object  | No       | Custom key-value pairs.                                    |
| `external_user_id`   | string  | No       | Your internal user ID.                                     |
| `notification_types` | integer | No       | 1 = subscribed, -2 = unsubscribed, 0 = no permission, etc. |
| `email_auth_hash`    | string  | No       | Required to update email identifiers securely.             |
| `sms_auth_hash`      | string  | No       | Required to update SMS identifiers securely.               |

> Only include fields you want to change. Fields left out will not be modified.

***

## Example Request

```json  theme={null}
PUT /api/v1/players/player_id_string HTTP/1.1
Host: onesignal.com
Authorization: Basic YOUR_REST_API_KEY
Content-Type: application/json

{
  "app_id": "your_app_id",
  "external_user_id": "user123",
  "tags": {
    "level": "20",
    "subscription": "active"
  },
  "language": "fr",
  "timezone": 3600,
  "device_os": "16.0"
}
```

***

## Response

```json  theme={null}
{
  "success": true
}
```

***

## Errors

* 400 Bad Request – Missing or invalid fields.
* 401 Unauthorized – Invalid or missing API key.
* 403 Forbidden – Access denied.
* 404 Not Found – Device with player\_id not found.

***

Built with [Mintlify](https://mintlify.com).
