# Source: https://developers.make.com/api-documentation/api-reference/cashier.md

# Cashier

## GET /cashier/products

> Get list of cashier products

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Cashier"}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["organization:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/cashier/products":{"get":{"tags":["Cashier"],"summary":"Get list of cashier products","parameters":[{"name":"type","in":"query","schema":{"type":"string","enum":["PLAN","EXTRA"]},"required":false},{"name":"includeInvisible","in":"query","schema":{"type":"boolean"}},{"name":"relatedPriceId","in":"query","schema":{"type":"integer"}},{"name":"organizationId","in":"query","schema":{"type":"integer"},"required":false}],"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"products":{"type":"array","items":{"type":"object"}}}}}}}}}}}}
```

## GET /cashier/prices/{priceId}

> Get price detail

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Cashier"}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["organization:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/cashier/prices/{priceId}":{"get":{"tags":["Cashier"],"summary":"Get price detail","parameters":[{"name":"priceId","in":"path","required":true,"schema":{"type":"number"}}],"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"number"},"productId":{"type":"number"},"price":{"type":"number"},"currencyCode":{"type":"string"},"period":{"type":"string"},"priority":{"type":"number"},"visible":{"type":"boolean"},"default":{"type":"boolean"},"config":{"type":"object","properties":{"dslimit":{"type":"number"},"iolimit":{"type":"number"},"dsslimit":{"type":"number"},"transfer":{"type":"number"},"dlqStorage":{"type":"number"},"operations":{"type":"number"},"restartPeriod":{"type":"string"}}}}}}}}}}}}}
```
