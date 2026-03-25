# Source: https://docs.mystic.ai/reference/list_regions_v4_cloud_provider_gcp_projects__project_id__regions_get.md

# List Regions

Get all the available regions under a project

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/cloud/provider/gcp/projects/{project_id}/regions": {
      "get": {
        "tags": [
          "Cloud",
          "GCP"
        ],
        "summary": "List Regions",
        "description": "Get all the available regions under a project",
        "operationId": "list_regions_v4_cloud_provider_gcp_projects__project_id__regions_get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Project Id"
            },
            "name": "project_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/RegionGet"
                  },
                  "type": "array",
                  "title": "Response List Regions V4 Cloud Provider Gcp Projects  Project Id  Regions Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          },
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "RegionGet": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "kind": {
            "type": "string",
            "title": "Kind"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "self_link": {
            "type": "string",
            "title": "Self Link"
          },
          "status": {
            "type": "string",
            "title": "Status"
          },
          "zones": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Zones"
          }
        },
        "type": "object",
        "required": [
          "id",
          "kind",
          "name",
          "self_link",
          "status",
          "zones"
        ],
        "title": "RegionGet",
        "description": "Base model for schemas."
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    },
    "securitySchemes": {
      "HTTPBearer": {
        "type": "http",
        "scheme": "bearer"
      },
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```