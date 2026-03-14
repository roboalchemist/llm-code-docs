# Source: https://developers.make.com/white-label-documentation/admin-api-reference/admin-greater-than-platform-settings.md

# Admin > Platform settings

The following endpoints allow you to inspect the settings of your Make platform instance.

## Get default license

> Gets the default organization license for your Make White Label instance. Make uses the default organization license when you create a new organization without specifying the organization's license.

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Admin > Platform settings","description":"The following endpoints allow you to inspect the settings of your Make platform instance."}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["admin:read","system:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/admin/system-settings/default-license":{"get":{"tags":["Admin > Platform settings"],"summary":"Get default license","description":"Gets the default organization license for your Make White Label instance. Make uses the default organization license when you create a new organization without specifying the organization's license.","responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"defaultLicense":{"type":"object","additionalProperties":{}}}}}}}}}}}}
```
