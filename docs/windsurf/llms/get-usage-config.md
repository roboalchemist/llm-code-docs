# Source: https://docs.windsurf.com/windsurf/accounts/api-reference/get-usage-config.md

# Source: https://docs.windsurf.com/plugins/accounts/api-reference/get-usage-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.windsurf.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Usage Configuration

> Retrieve add-on credit cap configuration at team, group, or user level for enterprise billing management.

## Overview

Retrieve the current add-on credit cap configuration for your organization. You can query configurations at the team level, for specific groups, or for individual users.

## Request

<ParamField body="service_key" type="string" required>
  Your service key with "Billing Read" permissions
</ParamField>

### Scope Configuration (Choose One)

<ParamField body="team_level" type="boolean">
  Set to `true` to retrieve the configuration at the team level
</ParamField>

<ParamField body="group_id" type="string">
  Retrieve the configuration for a specific group by providing the group ID
</ParamField>

<ParamField body="user_email" type="string">
  Retrieve the configuration for a specific user by providing their email address
</ParamField>

<Info>
  You must provide one of `team_level`, `group_id`, or `user_email` to define the scope.
</Info>

### Example Request - Get Team-Level Configuration

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "team_level": true
}' \
https://server.codeium.com/api/v1/GetUsageConfig
```

### Example Request - Get Group Configuration

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "group_id": "engineering_team"
}' \
https://server.codeium.com/api/v1/GetUsageConfig
```

### Example Request - Get User Configuration

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "user_email": "user@example.com"
}' \
https://server.codeium.com/api/v1/GetUsageConfig
```

## Response

<ResponseField name="add_on_credit_cap" type="integer">
  The configured add-on credit cap value. If this field is not present in the response, there is no cap configured at the requested scope level.
</ResponseField>

### Example Response - With Cap Configured

```json  theme={null}
{
  "add_on_credit_cap": 10000
}
```

### Example Response - No Cap Configured

```json  theme={null}
{}
```

## Error Responses

Common error scenarios:

* Invalid service key or insufficient permissions
* Multiple scope parameters provided
* No scope parameter provided
* Invalid group ID or user email
* Rate limit exceeded
