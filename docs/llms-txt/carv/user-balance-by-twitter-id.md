# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/user-balance-by-twitter-id.md

# User Balance by Twitter ID

{% hint style="info" %}
This endpoint relies on CARV ID to establish the relationship between the provided Twitter ID and the corresponding blockchain address. If the specified twitter\_user\_id is not connected to any address through CARV ID, the API will not be able to retrieve the expected result. Ensure that the Twitter account is properly linked to a blockchain address via CARV ID before making a request.
{% endhint %}

### GET UserBalanceByTwitter

#### Endpoint

`GET /ai-agent-backend/user_balance_by_twitter_id`

#### Parameters

| Name              | Location | Type   | Required | Description                       |
| ----------------- | -------- | ------ | -------- | --------------------------------- |
| twitter\_user\_id | query    | string | no       | Twitter handle                    |
| chain\_name       | query    | string | no       | Blockchain name, e.g., "ethereum" |
| token\_ticker     | query    | string | no       | Token ticker, e.g., "ETH"         |
| Authorization     | header   | string | yes      | Login token in Redis              |

**Description**

* **chain\_name**: Supported values include `"ethereum_mainnet"`, `"base_mainnet"`, `"solana_mainnet"`, `"opbnb_mainnet"` (and all testnets as well).

#### Example Request (HTTP)

```http
GET /ai-agent-backend/user_balance_by_twitter_id?twitter_user_id=123456&chain_name=ethereum_testnet&token_ticker=aave
Authorization: <your-auth-token>
```

#### Example Request (Shell)

```bash
curl -X GET "https://interface.carv.io/ai-agent-backend/user_balance_by_twitter_id" \
-H "Authorization: <your-auth-token>" \
-d "twitter_user_id=123456" \
-d "chain_name=ethereum_mainnet" \
-d "token_ticker=eth"
```

#### Example Request (JavaScript)

```javascript
const fetch = require('node-fetch');

const url = 'https://interface.carv.io/ai-agent-backend/user_balance_by_twitter_id';
const params = new URLSearchParams({
    twitter_user_id: '123456',
    chain_name: 'ethereum_testnet',
    token_ticker: 'eth'
});

const options = {
    method: 'GET',
    headers: {
        'Authorization': '<your-auth-token>'
    }
};

fetch(`${url}?${params.toString()}`, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

4o

#### Example Response (200 OK)

```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "balance": "0.010000"
  }
}
```

**Error Response (400):**

```json
jsonCopy code{
  "error": "Invalid request"
}
```

#### Responses

| HTTP Status Code | Meaning                                                          | Description | Data Schema |
| ---------------- | ---------------------------------------------------------------- | ----------- | ----------- |
| 200              | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | none        | Inline      |
| 400              | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | none        | Inline      |

#### Response Data Schema

**HTTP Status Code 200**

| Name    | Type    | Required | Restrictions | Title | Description      |
| ------- | ------- | -------- | ------------ | ----- | ---------------- |
| code    | integer | true     | none         |       | Response code    |
| msg     | string  | true     | none         |       | Response message |
| data    | object  | true     | none         |       | Response data    |
| balance | string  | true     | none         |       | User balance     |

**HTTP Status Code 400**

| Name  | Type   | Required | Restrictions | Title | Description       |
| ----- | ------ | -------- | ------------ | ----- | ----------------- |
| error | string | true     | none         |       | Error description |
