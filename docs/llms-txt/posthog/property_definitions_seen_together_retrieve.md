# Source: https://posthog.com/docs/open-api-spec/property_definitions_seen_together_retrieve.md

# property_definitions_seen_together_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/property_definitions/seen_together/
{
  "paths": {
    "/api/projects/{project_id}/property_definitions/seen_together/": {
      "get": {
        "operationId": "property_definitions_seen_together_retrieve",
        "description": "Allows a caller to provide a list of event names and a single property name\nReturns a map of the event names to a boolean representing whether that property has ever been seen with that event_name",
        "parameters": [
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
          "core",
          "property_definitions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "property_definition:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
