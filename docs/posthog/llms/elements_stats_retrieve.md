# Source: https://posthog.com/docs/open-api-spec/elements_stats_retrieve.md

# elements_stats_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/elements/stats/
{
  "paths": {
    "/api/projects/{project_id}/elements/stats/": {
      "get": {
        "operationId": "elements_stats_retrieve",
        "description": "The original version of this API always and only returned $autocapture elements\nIf no include query parameter is sent this remains true.\nNow, you can pass a combination of include query parameters to get different types of elements\nCurrently only $autocapture and $rageclick and $dead_click are supported",
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
          "product_analytics",
          "elements"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "element:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "product_analytics"
        ]
      }
    }
  }
}
```
