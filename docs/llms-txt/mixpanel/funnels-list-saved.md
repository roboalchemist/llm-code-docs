# Source: https://developer.mixpanel.com/reference/funnels-list-saved.md

# List Saved Funnels

Get the names and funnel_ids of your funnels.

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Query API",
    "description": "query api",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/query",
      "description": "Mixpanel's calculated data API",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "ServiceAccount": []
    },
    {
      "ProjectSecret": []
    }
  ],
  "tags": [
    {
      "name": "Funnels",
      "description": "Query data shown in your Funnels reports"
    }
  ],
  "paths": {
    "/funnels/list": {
      "get": {
        "operationId": "funnels-list-saved",
        "summary": "List Saved Funnels",
        "tags": [
          "Funnels"
        ],
        "description": "Get the names and funnel_ids of your funnels.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          }
        ],
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": [
                      {
                        "funnel_id": 7509,
                        "name": "Signup funnel"
                      },
                      {
                        "funnel_id": 9070,
                        "name": "Funnel tutorial"
                      }
                    ]
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "funnel_id": {
                        "type": "integer",
                        "description": "The id of the funnel."
                      },
                      "name": {
                        "type": "string",
                        "description": "The name of the funnel"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      },
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      }
    },
    "parameters": {
      "workspaceId": {
        "in": "query",
        "name": "workspace_id",
        "schema": {
          "type": "integer"
        },
        "description": "The id of the workspace if applicable."
      },
      "projectId": {
        "in": "query",
        "name": "project_id",
        "schema": {
          "type": "integer"
        },
        "description": "Required if using service account to authenticate request.",
        "required": true
      }
    }
  },
  "x-readme-deploy-id": "query"
}
```