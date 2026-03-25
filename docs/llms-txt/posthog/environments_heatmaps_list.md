# Source: https://posthog.com/docs/open-api-spec/environments_heatmaps_list.md

# environments_heatmaps_list

## OpenAPI

```json GET /api/environments/{environment_id}/heatmaps/
{
  "paths": {
    "/api/environments/{environment_id}/heatmaps/": {
      "get": {
        "operationId": "environments_heatmaps_list",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "tags": [
          "heatmaps"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "heatmap:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedHeatmapsResponseList"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedHeatmapsResponseList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HeatmapsResponse"
            }
          }
        }
      },
      "HeatmapsResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HeatmapResponseItem"
            }
          }
        },
        "required": [
          "results"
        ]
      },
      "HeatmapResponseItem": {
        "type": "object",
        "properties": {
          "count": {
            "type": "integer"
          },
          "pointer_y": {
            "type": "integer"
          },
          "pointer_relative_x": {
            "type": "number",
            "format": "double"
          },
          "pointer_target_fixed": {
            "type": "boolean"
          }
        },
        "required": [
          "count",
          "pointer_relative_x",
          "pointer_target_fixed",
          "pointer_y"
        ]
      }
    }
  }
}
```
