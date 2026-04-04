# Source: https://posthog.com/docs/open-api-spec/customer_profile_configs_destroy.md

# customer_profile_configs_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/customer_profile_configs/{id}/
{
  "paths": {
    "/api/environments/{project_id}/customer_profile_configs/{id}/": {
      "delete": {
        "operationId": "customer_profile_configs_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this customer profile config.",
            "required": true
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          }
        ],
        "tags": [
          "customer_profile_configs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "customer_profile_config:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
