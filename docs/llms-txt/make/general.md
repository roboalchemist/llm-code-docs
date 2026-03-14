# Source: https://developers.make.com/api-documentation/api-reference/general.md

# General

This section contains endpoints that provide general functionality for the Make API.

## Ping

> Pings the Make API service. Successful response contains plain text.

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"General","description":"This section contains endpoints that provide general functionality for the Make API."}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["organization:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/ping":{"get":{"tags":["General"],"summary":"Ping","description":"Pings the Make API service. Successful response contains plain text.","responses":{"200":{"description":"Successful response","content":{"text/plain":{"schema":{"type":"string"}}}}}}}}}
```
