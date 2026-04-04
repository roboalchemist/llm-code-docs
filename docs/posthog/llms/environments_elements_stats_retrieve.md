# Source: https://posthog.com/docs/open-api-spec/environments_elements_stats_retrieve.md

# environments_elements_stats_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/elements/stats/
{
  "paths": {
    "/api/environments/{environment_id}/elements/stats/": {
      "get": {
        "operationId": "environments_elements_stats_retrieve",
        "description": "The original version of this API always and only returned $autocapture elements\nIf no include query parameter is sent this remains true.\nNow, you can pass a combination of include query parameters to get different types of elements\nCurrently only $autocapture and $rageclick and $dead_click are supported",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
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
        "deprecated": true,
        "x-explicit-tags": [
          "product_analytics"
        ]
      }
    }
  }
}
```
