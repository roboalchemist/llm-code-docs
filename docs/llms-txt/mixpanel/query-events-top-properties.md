# Source: https://developer.mixpanel.com/reference/query-events-top-properties.md

# Top Event Properties

Get the top property names for an event. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

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
      "name": "Event Breakdown",
      "description": "Breakdowns on the most common events in your project"
    }
  ],
  "paths": {
    "/events/properties/top": {
      "get": {
        "operationId": "query-events-top-properties",
        "summary": "Top Event Properties",
        "tags": [
          "Event Breakdown"
        ],
        "description": "Get the top property names for an event. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "$ref": "#/components/parameters/eventName"
          },
          {
            "$ref": "#/components/parameters/limit10"
          }
        ],
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "ad version": {
                        "count": 295
                      },
                      "user type": {
                        "count": 91
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "description": "The keys are the name of the properties",
                  "additionalProperties": {
                    "type": "object",
                    "properties": {
                      "count": {
                        "type": "integer",
                        "description": "The number of events with that property"
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
      "eventName": {
        "in": "query",
        "name": "event",
        "schema": {
          "type": "string"
        },
        "description": "The event that you wish to get data for. Note: this is a single event name, not an array.",
        "required": true
      },
      "limit10": {
        "in": "query",
        "name": "limit",
        "schema": {
          "type": "integer"
        },
        "description": "The maximum number of properties to return. Defaults to 10."
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