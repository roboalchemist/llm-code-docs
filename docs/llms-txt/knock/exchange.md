# Source: https://docs.knock.app/mapi-reference/api_keys/exchange.md

### Exchange for API key

Given an authenticated service token and an environment, will exchange the service token for a secret API key that can be used to make requests to the public API.

#### Endpoint

`POST /v1/api_keys/exchange`

#### Query parameters

- **environment** (string) *required* - The environment slug.

#### Responses

##### 200

OK

###### Example

```json
{
  "api_key": "sk_1234567890"
}
```

