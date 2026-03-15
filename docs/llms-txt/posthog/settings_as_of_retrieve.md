# Source: https://posthog.com/docs/open-api-spec/settings_as_of_retrieve.md

# settings_as_of_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/environments/{id}/settings_as_of/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/settings_as_of/": {
      "get": {
        "operationId": "settings_as_of_retrieve",
        "description": "Return the team settings as of the provided timestamp.\nQuery params:\n- at: ISO8601 datetime (required)\n- scope: optional, one or multiple keys to filter the returned settings",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this environment (aka team).",
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
          "environments"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
