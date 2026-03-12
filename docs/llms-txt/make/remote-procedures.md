# Source: https://developers.make.com/white-label-documentation/admin-api-reference/remote-procedures.md

# Source: https://developers.make.com/api-documentation/api-reference/remote-procedures.md

# Remote procedures

## POST /rpcs/{appName}/{appVersion}/{rpcName}

> Call RPC

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Remote procedures"}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["organization:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/rpcs/{appName}/{appVersion}/{rpcName}":{"post":{"tags":["Remote procedures"],"summary":"Call RPC","requestBody":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"object"},"schema":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},"type":{"type":"string"},"required":{"type":"boolean"}}}}}}}}},"responses":{"200":{"description":"Successful response"}},"parameters":[{"name":"appName","in":"path","schema":{"type":"string"},"required":true},{"name":"appVersion","in":"path","schema":{"type":"string"},"required":true},{"name":"rpcName","in":"path","schema":{"type":"string"},"required":true},{"name":"imt-remote-formula","in":"header","schema":{"type":"integer"}},{"name":"imt-ignore-required","in":"header","schema":{"type":"string"}},{"name":"imt-validate-schema","in":"header","schema":{"type":"string"}}]}}}}
```

## OPTIONS /rpcs/{appName}/{appVersion}/{rpcName}

> Process action

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Remote procedures"}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["organization:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/rpcs/{appName}/{appVersion}/{rpcName}":{"options":{"tags":["Remote procedures"],"summary":"Process action","parameters":[{"name":"appName","in":"path","schema":{"type":"string"},"required":true},{"name":"appVersion","in":"path","schema":{"type":"string"},"required":true},{"name":"rpcName","in":"path","schema":{"type":"string"},"required":true},{"name":"imt-remote-formula","in":"header","schema":{"type":"integer"}},{"name":"imt-ignore-required","in":"header","schema":{"type":"string"}},{"name":"imt-validate-schema","in":"header","schema":{"type":"string"}}],"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"config":{"type":"array","items":{}}}}}}}}}}}}
```
