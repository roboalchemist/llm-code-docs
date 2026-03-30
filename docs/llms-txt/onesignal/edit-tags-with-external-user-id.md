# Source: https://documentation.onesignal.com/reference/edit-tags-with-external-user-id.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit tags with external user id

> put https://onesignal.com/api/v1/apps/{app_id}/users/{external_user_id}

Update a player's (Subscription's) information using the External ID.

<Warning>
  This is a Legacy API. Use [Update User](/reference/update-user) or [Update Subscription](/reference/update-subscription) instead.
</Warning>

***

## Path Parameters

| Parameter          | Type   | Required | Description             |
| ------------------ | ------ | -------- | ----------------------- |
| `app_id`           | string | Yes      | Your OneSignal App ID.  |
| `external_user_id` | string | Yes      | The user's External ID. |

***

## Headers

| Header          | Value                            | Required | Description                      |
| --------------- | -------------------------------- | -------- | -------------------------------- |
| `Authorization` | `Basic YOUR_LEGACY_REST_API_KEY` | Yes      | Your Legacy OneSignal API key.   |
| `Content-Type`  | `application/json`               | Yes      | The content type of the request. |

***

## Request Body Parameters

| Field  | Type   | Required | Description                       |
| ------ | ------ | -------- | --------------------------------- |
| `tags` | object | Yes      | Key-value pairs to set or update. |

* To **delete a tag**, set its value to an empty string (`""`).
* Existing tags with the same keys will be **overwritten**.

***

## Example Request

```http  theme={null}
PATCH /api/v1/apps/your_app_id/users/user123 HTTP/1.1
Host: onesignal.com
Authorization: Basic YOUR_LEGACY_REST_API_KEY
Content-Type: application/json

{
  "tags": {
    "plan": "premium",
    "logged_in": "true",
    "referral": ""
  }
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

* 400 Bad Request – Invalid request or payload.
* 401 Unauthorized – Invalid or missing keys.
* 403 Forbidden – Access denied due to insufficient permissions.
* 404 Not Found – No players found for given `external_user_id`.

***

Built with [Mintlify](https://mintlify.com).
