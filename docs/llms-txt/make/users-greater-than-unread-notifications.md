# Source: https://developers.make.com/api-documentation/api-reference/users-greater-than-unread-notifications.md

# Users > Unread notifications

The following endpoint retrieves the number of unread notifications of the currently authenticated user.

## Unread notifications

> Gets the number of unread notifications for the currently authenticated user.

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Users > Unread notifications","description":"The following endpoint retrieves the number of unread notifications of the currently authenticated user."}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["user:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/users/unread-notifications":{"get":{"tags":["Users > Unread notifications"],"summary":"Unread notifications","description":"Gets the number of unread notifications for the currently authenticated user.","responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"userUnreadNotifications":{"type":"integer"},"userZoneUnreadNotifications":{"type":"array","items":{"type":"object","properties":{"zoneId":{"type":"integer"},"unreadNotifications":{"type":"integer"}}}}}}}}}}}}}}
```
