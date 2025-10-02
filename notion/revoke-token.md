# Revoke token

POST https://api.notion.com/v1/oauth/revoke

Revoke an access token.

## Body Params

**token** (string, required)
Revoke an access token

## Headers

**Authorization** (string)
Defaults to Basic $BASE64_ENCODED_ID_AND_SECRET

## Responses

### 200
200 - Response body: json

### 400
400 - Response body: object

---

## Example Request

```shell
curl --location --request POST 'https://api.notion.com/v1/oauth/revoke' \
--header 'Authorization: Basic '$BASE64_ENCODED_ID_AND_SECRET'' \
--header 'Content-Type: application/json' \
--data '{
  "token": "'$ACCESS_TOKEN'"
}'
```

---

Updated 7 months ago

**Previous:** [Introspect token](/reference/introspect-token)
**Next:** [Refresh a token](/reference/refresh-a-token)
