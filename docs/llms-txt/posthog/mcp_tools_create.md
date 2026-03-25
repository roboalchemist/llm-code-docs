# Source: https://posthog.com/docs/open-api-spec/mcp_tools_create.md

# mcp_tools_create

## OpenAPI

```json POST /api/environments/{project_id}/mcp_tools/{tool_name}/
{
  "paths": {
    "/api/environments/{project_id}/mcp_tools/{tool_name}/": {
      "post": {
        "operationId": "mcp_tools_create",
        "description": "Invoke an MCP tool by name.\n\nThis endpoint allows MCP callers to invoke Max AI tools directly\nwithout going through the full LangChain conversation flow.\n\nScopes are resolved dynamically per tool via dangerously_get_required_scopes.",
        "parameters": [
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          },
          {
            "in": "path",
            "name": "tool_name",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "mcp_tools"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "posthog_ai"
        ]
      }
    }
  }
}
```
