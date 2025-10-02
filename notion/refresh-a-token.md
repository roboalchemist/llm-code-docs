# Refresh a token

POST https://api.notion.com/v1/oauth/token

Refreshes an access token, generating a new access token and new refresh token.

**Note:** For step-by-step instructions on how to use this endpoint to refresh an access token, check out the [Authorization guide](https://developers.notion.com/docs/authorization).

**Note:** Each Public API endpoint can return several possible error codes. To see a full description of each type of error code, see the [Error codes section](https://developers.notion.com/reference/status-codes) of the Status codes documentation.

## Path Params

**grant_type** (string, required)
Defaults to "refresh_token"
A constant string: "refresh_token"

**refresh_token** (string, required)
A unique token that Notion generates to refresh your token, generated when a user initiates the OAuth flow.

## Headers

**Authorization** (string)
Defaults to Basic $BASE64_ENCODED_ID_AND_SECRET

## Responses

### 200
200 - Response body: object

- **access_token** (string)
- **refresh_token** (string)
- **bot_id** (string)
- **duplicated_template_id** (string)
- **owner** (object)
  - **workspace** (boolean) - Defaults to true
- **workspace_icon** (string)
- **workspace_id** (string)
- **workspace_name** (string)

### 400
400 - Response body: object

- **error** (string)
- **error_description** (string)

---

## Example Request

```shell
curl --location --request POST 'https://api.notion.com/v1/oauth/token' \
--header 'Authorization: Basic '$BASE64_ENCODED_ID_AND_SECRET'' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2022-06-28' \
--data '{
  "grant_type": "refresh_token",
  "refresh_token": "nrt_4991090011501Ejc6Xn4sHguI7jZIN449mKe9PRhpMfNK"
}'
```

## Example Response (200)

```json
{
  "access_token": "ntn_e4502e8c9-1990-60af-845f-ff8f872b1ec6c",
  "refresh_token": "ntn_1202e8c9-0920-412f-055f-8f872ba1df26c",
  "bot_id": "b3414d659-1224-5ty7-6ffr-cc9d8773drt601288f",
  "duplicated_template_id": null,
  "owner": {
    "workspace": true
  },
  "workspace_icon": "https://website.domain/images/image.png",
  "workspace_id": "j565j4d7x3-2882-61bs-564a-jj9d9ui-c36hxfr7x",
  "workspace_name": "Ada's Notion Workspace"
}
```

---

Updated about 2 months ago

**Previous:** [Revoke token](/reference/revoke-token)
**Next:** [Blocks](/reference/patch-block-children)
