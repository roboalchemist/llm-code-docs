# Source: https://docs.airbyte.com/ai-agents/api/api-reference/create-integrations-templates-connections-cron-describe.md

# Describe Cron Expression

```
POST 
/api/v1/integrations/templates/connections/cron/describe
```

**Requires an Access Token as the bearer token.**

Validate and describe a Quartz cron expression. Returns a human-readable description of when the schedule will run.

## Request[​](#request "Direct link to request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 403
* 422
* 500

Successful Response

Bad request

Forbidden

Unprocessable entity

Internal server error
