# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/user-balance-by-discord-id.md

# User Balance by Discord ID

{% hint style="info" %}
This endpoint relies on CARV ID to establish the relationship between the provided Discord ID and the corresponding blockchain address. If the specified discord\_user\_id is not connected to any address through CARV ID, the API will not be able to retrieve the expected result. Ensure that the Discord account is properly linked to a blockchain address via CARV ID before making a request.
{% endhint %}

### GET UserBalanceByDiscordID

GET /ai-agent-backend/user\_balance\_by\_discord\_id

#### Params

| Name              | Location | Type   | Required | Description          |
| ----------------- | -------- | ------ | -------- | -------------------- |
| discord\_user\_id | query    | string | no       | none                 |
| chain\_name       | query    | string | no       | "ethereum"           |
| token\_ticker     | query    | string | no       | none                 |
| Authorization     | header   | string | yes      | login token in redis |
| Origin            | header   | string | yes      | none                 |

**Description**

* **chain\_name**: Supported values include `"ethereum_mainnet"`, `"base_mainnet"`, `"solana_mainnet"`, `"opbnb_mainnet"` (and all testnets as well).

#### Example Request (HTTP)

```http
GET /ai-agent-backend/user_balance_by_discord_id?discord_user_id=123456&chain_name=ethereum_testnet&token_ticker=aave
Authorization: <your-auth-token>
```

> Response Examples

```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "balance": "0.010000"
  }
}
```

> 400 Response

```json
{
  "error": "string"
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description | Data schema |
| ---------------- | ---------------------------------------------------------------- | ----------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | none        | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | none        | Inline      |

#### Responses Data Schema

HTTP Status Code **200**

| Name       | Type    | Required | Restrictions | Title | description |
| ---------- | ------- | -------- | ------------ | ----- | ----------- |
| » code     | integer | true     | none         |       | none        |
| » msg      | string  | true     | none         |       | none        |
| » data     | object  | true     | none         |       | none        |
| »» balance | string  | true     | none         |       | none        |

HTTP Status Code **400**

| Name    | Type   | Required | Restrictions | Title | description |
| ------- | ------ | -------- | ------------ | ----- | ----------- |
| » error | string | true     | none         |       | none        |
