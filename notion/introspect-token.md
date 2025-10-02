# Introspect token

POST https://api.notion.com/v1/oauth/introspect

Get a token's active status, scope, and issued time.

## Body Params

**token** (string, required)
The access token

## Headers

**Authorization** (string)
Defaults to Basic $BASE64_ENCODED_ID_AND_SECRET

## Responses

### 200
200 - Response body: object

- **active** (boolean) - Defaults to true
- **scope** (string)
- **iat** (integer) - Defaults to 0

### 400
400 - Response body: object

---

## Example Request

```shell
curl --location --request POST 'https://api.notion.com/v1/oauth/introspect' \
--header 'Authorization: Basic '$BASE64_ENCODED_ID_AND_SECRET'' \
--header 'Content-Type: application/json' \
--data '{
  "token": "'$ACCESS_TOKEN'"
}'
```

## Example Response (200)

```json
{
  "active": true,
  "scope": "read_content insert_content update_content",
  "iat": 1727554061083
}
```

---

Updated 7 months ago

**Previous:** [Create a token](/reference/create-a-token)
**Next:** [Revoke token](/reference/revoke-token)
