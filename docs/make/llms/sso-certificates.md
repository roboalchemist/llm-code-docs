# Source: https://developers.make.com/api-documentation/api-reference/sso-certificates.md

# SSO certificates

Managing of SSO certificates.

## Get SSO certificates

> Get all SSO certificates.

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"SSO certificates","description":"Managing of SSO certificates."}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["organizations:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/organizations/{organizationId}/sso-certificates":{"get":{"tags":["SSO certificates"],"summary":"Get SSO certificates","description":"Get all SSO certificates.","parameters":[{"name":"organizationId","in":"path","schema":{"type":"integer"},"required":true,"description":"The ID of the organization."},{"name":"type","in":"query","schema":{"type":"string"},"required":true,"description":"Type of SSO certificate."}],"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object"}}}}}}}}}
```
