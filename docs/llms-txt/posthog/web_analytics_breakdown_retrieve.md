# Source: https://posthog.com/docs/open-api-spec/web_analytics_breakdown_retrieve.md

# web_analytics_breakdown_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/web_analytics/breakdown/
{
  "paths": {
    "/api/projects/{project_id}/web_analytics/breakdown/": {
      "get": {
        "operationId": "web_analytics_breakdown_retrieve",
        "description": "This endpoint is in Concept state, please join the feature preview to try it out when it's ready. Get a breakdown by a property (e.g. browser, device type, country, etc.).",
        "parameters": [
          {
            "in": "query",
            "name": "apply_path_cleaning",
            "schema": {
              "type": "boolean",
              "default": true
            },
            "description": "Apply URL path cleaning"
          },
          {
            "in": "query",
            "name": "breakdown_by",
            "schema": {
              "enum": [
                "DeviceType",
                "Browser",
                "OS",
                "Viewport",
                "InitialReferringDomain",
                "InitialUTMSource",
                "InitialUTMMedium",
                "InitialUTMCampaign",
                "InitialUTMTerm",
                "InitialUTMContent",
                "Country",
                "Region",
                "City",
                "InitialPage",
                "Page",
                "ExitPage",
                "InitialChannelType"
              ],
              "type": "string",
              "minLength": 1
            },
            "description": "Property to break down by\n\n* `DeviceType` - DeviceType\n* `Browser` - Browser\n* `OS` - OS\n* `Viewport` - Viewport\n* `InitialReferringDomain` - InitialReferringDomain\n* `InitialUTMSource` - InitialUTMSource\n* `InitialUTMMedium` - InitialUTMMedium\n* `InitialUTMCampaign` - InitialUTMCampaign\n* `InitialUTMTerm` - InitialUTMTerm\n* `InitialUTMContent` - InitialUTMContent\n* `Country` - Country\n* `Region` - Region\n* `City` - City\n* `InitialPage` - InitialPage\n* `Page` - Page\n* `ExitPage` - ExitPage\n* `InitialChannelType` - InitialChannelType",
            "required": true
          },
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
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "maximum": 1000,
              "minimum": 1,
              "default": 100
            },
            "description": "Number of results to return"
          },
          {
            "in": "query",
            "name": "offset",
            "schema": {
              "type": "integer",
              "minimum": 0,
              "default": 0
            },
            "description": "Number of results to skip"
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
                  "$ref": "#/components/schemas/WebAnalyticsBreakdownResponse"
                },
                "examples": {
                  "BreakdownResponse": {
                    "value": {
                      "next": "https://us.posthog.com/api/web_analytics/breakdown?offset=2&limit=2",
                      "results": [
                        {
                          "breakdown_value": "/home",
                          "visitors": 8500,
                          "views": 12000,
                          "sessions": 9200
                        },
                        {
                          "breakdown_value": "/about",
                          "visitors": 2100,
                          "views": 2800,
                          "sessions": 2300
                        }
                      ]
                    },
                    "summary": "Breakdown Response",
                    "description": "Example paginated response with breakdown data"
                  }
                }
              }
            },
            "description": "Get a breakdown of web analytics data by supported properties."
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "WebAnalyticsBreakdownResponse": {
        "type": "object",
        "properties": {
          "next": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "description": "URL for next page of results"
          },
          "results": {
            "type": "array",
            "items": {},
            "description": "Array of breakdown items"
          }
        },
        "required": [
          "results"
        ]
      }
    }
  }
}
```
