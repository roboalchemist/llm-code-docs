# Source: https://docs.carv.io/d.a.t.a.-ai-framework/api-documentation/token-info-and-price.md

# Token Info and Price

### GET TokenInfo

#### Endpoint

`GET /ai-agent-backend/token_info`

#### Parameters

| Name          | Location | Type   | Required | Description                |
| ------------- | -------- | ------ | -------- | -------------------------- |
| ticker        | query    | string | No       | The token's ticker symbol. |
| Authorization | header   | string | Yes      | Login token in Redis.      |

#### Example Request (HTTP)

```http
curl -X GET "https://interface.carv.io/ai-agent-backend/token_info?ticker=aave" \
      -H "Content-Type: application/json" \
      -H "Authorization: <YOUR_AUTH_TOKEN>"
```

#### Example Request (Shell)

```bash
curl -X GET "https://interface.carv.io/ai-agent-backend/token_info?ticker=aave" \
    -H "Authorization: your_token_here"
```

#### Example Request (JavaScript)

```javascript
fetch('https://interface.carv.io/ai-agent-backend/token_info?ticker=aave', {
  method: 'GET',
  headers: {
    'Authorization': 'your_token_here'
  }
})
  .then(response => response.json())
  .then(data => console.log(data));
```

#### Example Response (200 OK)

```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "ticker": "aave",
    "symbol": "aave",
    "name": "Aave",
    "platform": "ethereum",
    "categories": [
      "Decentralized Finance (DeFi)",
      "Governance",
      "Yield Farming",
      "BNB Chain Ecosystem",
      "Lending/Borrowing Protocols",
      "Avalanche Ecosystem",
      "Polygon Ecosystem",
      "Near Protocol Ecosystem",
      "Fantom Ecosystem",
      "Harmony Ecosystem",
      "Arbitrum Ecosystem",
      "Ethereum Ecosystem",
      "Optimism Ecosystem",
      "Index Coop Defi Index",
      "Energi Ecosystem",
      "Sora Ecosystem",
      "Huobi ECO Chain Ecosystem",
      "GMCI DeFi Index",
      "Blockchain Capital Portfolio",
      "Index Coop Index",
      "GMCI Index",
      "World Liberty Financial Portfolio"
    ],
    "contract_infos": [
      {
        "platform": "near-protocol",
        "address": "7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9.factory.bridge.near"
      },
      {
        "platform": "huobi-token",
        "address": "0x202b4936fe1a82a4965220860ae46d7d3939bb25"
      },
      {
        "platform": "fantom",
        "address": "0x6a07a792ab2965c72a5b8088d3a069a7ac3a993b"
      },
      {
        "platform": "energi",
        "address": "0xa7f2f790355e0c32cab03f92f6eb7f488e6f049a"
      },
      {
        "platform": "binance-smart-chain",
        "address": "0xfb6115445bff7b52feb98650c87f44907e58f802"
      },
      {
        "platform": "ethereum",
        "address": "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9"
      },
      {
        "platform": "optimistic-ethereum",
        "address": "0x76fb31fb4af56892a25e32cfc43de717950c9278"
      },
      {
        "platform": "polygon-pos",
        "address": "0xd6df932a45c0f255f85145f286ea0b292b21c90b"
      },
      {
        "platform": "harmony-shard-0",
        "address": "0xcf323aad9e522b93f11c352caa519ad0e14eb40f"
      },
      {
        "platform": "arbitrum-one",
        "address": "0xba5ddd1f9d7f570dc94a51479a000e3bce967196"
      },
      {
        "platform": "avalanche",
        "address": "0x63a72806098bd3d9520cc43356dd78afe5d386d9"
      },
      {
        "platform": "sora",
        "address": "0x0091bd8d8295b25cab5a7b8b0e44498e678cfc15d872ede3215f7d4c7635ba36"
      }
    ],
    "price": 12.34
  }
}
```

#### Example Response (400 Bad Request)

```json
{
  "error": "Invalid token ticker."
}
```

#### Response Data Schema

**HTTP Status Code: 200 OK**

<table><thead><tr><th width="160">Name</th><th width="106">Type</th><th width="97">Required</th><th width="97">Restrictions</th><th>Title</th><th>Description</th></tr></thead><tbody><tr><td>code</td><td>integer</td><td>Yes</td><td>None</td><td>Response Code</td><td>The status code of the response.</td></tr><tr><td>msg</td><td>string</td><td>Yes</td><td>None</td><td>Response Message</td><td>A descriptive message about the response.</td></tr><tr><td>data</td><td>object</td><td>Yes</td><td>None</td><td>Token Data</td><td>The data object containing token details.</td></tr><tr><td>data.ticker</td><td>string</td><td>Yes</td><td>None</td><td>Ticker Symbol</td><td>The token’s ticker symbol.</td></tr><tr><td>data.symbol</td><td>string</td><td>Yes</td><td>None</td><td>Symbol</td><td>The token’s symbol.</td></tr><tr><td>data.name</td><td>string</td><td>Yes</td><td>None</td><td>Name</td><td>The token’s name.</td></tr><tr><td>data.platform</td><td>string</td><td>Yes</td><td>None</td><td>Platform</td><td>The blockchain platform of the token.</td></tr><tr><td>data.categories</td><td>array of strings</td><td>Yes</td><td>None</td><td>Categories</td><td>The categories associated with the token.</td></tr><tr><td>data.contract_infos</td><td>array of objects</td><td>Yes</td><td>None</td><td>Contract Info</td><td>The contract information for different platforms.</td></tr><tr><td>data.price</td><td>number</td><td>Yes</td><td>None</td><td>Price</td><td>The token's price in USD.</td></tr></tbody></table>

**HTTP Status Code: 400 Bad Request**

<table><thead><tr><th>Name</th><th width="100">Type</th><th width="109">Required</th><th width="128">Restrictions</th><th width="89">Title</th><th width="211">Description</th></tr></thead><tbody><tr><td>error</td><td>string</td><td>Yes</td><td>None</td><td>Error</td><td>Error message indicating the issue with the request.</td></tr></tbody></table>
