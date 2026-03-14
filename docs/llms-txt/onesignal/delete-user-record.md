# Source: https://documentation.onesignal.com/reference/delete-user-record.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete player record

> delete https://onesignal.com/api/v1/players/{player_id}?app_id={app_id}

Delete a player (aka Subscription).

<Warning>
  This is a Legacy API. Use [Delete User](/reference/delete-user) or [Delete Subscription](/reference/delete-subscription) instead.
</Warning>

***

## Path Parameters

| Parameter   | Type   | Required | Description                    |
| ----------- | ------ | -------- | ------------------------------ |
| `app_id`    | string | Yes      | Your OneSignal App ID.         |
| `player_id` | string | Yes      | The Subscription ID to delete. |

***

## Headers

| Header          | Value                            | Required | Description                      |
| --------------- | -------------------------------- | -------- | -------------------------------- |
| `Authorization` | `Basic YOUR_LEGACY_REST_API_KEY` | Yes      | Your Legacy OneSignal API key.   |
| `Content-Type`  | `application/json`               | Yes      | The content type of the request. |

***

## Example Request

```http  theme={null}
DELETE /api/v1/apps/your_app_id/users/user123 HTTP/1.1
Host: onesignal.com
Authorization: Basic YOUR_LEGACY_REST_API_KEY
Content-Type: application/json
```

***

## Example Response

```json  theme={null}
{
  "success": true
}
```

The Subscription will be deleted from the OneSignal database.

***

Built with [Mintlify](https://mintlify.com).
