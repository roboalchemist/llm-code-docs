# Source: https://posthog.com/docs/open-api-spec/web_analytics_overview_retrieve.md

# web_analytics_overview_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/web_analytics/overview/
{
  "paths": {
    "/api/projects/{project_id}/web_analytics/overview/": {
      "get": {
        "operationId": "web_analytics_overview_retrieve",
        "description": "This endpoint is in Concept state, please join the feature preview to try it out when it's ready. Get an overview of web analytics data including visitors, views, sessions, bounce rate, and session duration.",
        "parameters": [
          {
            "in": "query",
            "name": "date_from",
            "schema": {
              "type": "string",
              "format": "date"
            },
            "description": "Start date for the query (format: YYYY-MM-DD)",
            "required": true
          },
          {
            "in": "query",
            "name": "date_to",
            "schema": {
              "type": "string",
              "format": "date"
            },
            "description": "End date for the query (format: YYYY-MM-DD)",
            "required": true
          },
          {
            "in": "query",
            "name": "filter_test_accounts",
            "schema": {
              "type": "boolean",
              "default": true
            },
            "description": "Filter out test accounts"
          },
          {
            "in": "query",
            "name": "host",
            "schema": {
              "type": "string",
              "nullable": true,
              "minLength": 1
            },
            "description": "Host to filter by (e.g. example.com)"
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
          "web_analytics"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WebAnalyticsOverviewResponse"
                },
                "examples": {
                  "OverviewResponse": {
                    "value": {
                      "visitors": 12500,
                      "views": 45000,
                      "sessions": 18200,
                      "bounce_rate": 0.32,
                      "session_duration": 185.5
                    },
                    "summary": "Overview Response",
                    "description": "Example response with key metrics"
                  }
                }
              }
            },
            "description": "Get simple overview metrics: visitors, views, sessions, bounce rate, session duration"
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "WebAnalyticsOverviewResponse": {
        "type": "object",
        "properties": {
          "visitors": {
            "type": "integer",
            "description": "Unique visitors"
          },
          "views": {
            "type": "integer",
            "description": "Total page views"
          },
          "sessions": {
            "type": "integer",
            "description": "Total sessions"
          },
          "bounce_rate": {
            "type": "number",
            "format": "double",
            "maximum": 1,
            "minimum": 0,
            "description": "Bounce rate"
          },
          "session_duration": {
            "type": "number",
            "format": "double",
            "description": "Average session duration in seconds"
          }
        },
        "required": [
          "bounce_rate",
          "session_duration",
          "sessions",
          "views",
          "visitors"
        ]
      }
    }
  }
}
```
