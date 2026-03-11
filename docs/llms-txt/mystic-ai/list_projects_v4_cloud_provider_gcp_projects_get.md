# Source: https://docs.mystic.ai/reference/list_projects_v4_cloud_provider_gcp_projects_get.md

# List Projects

Get all projects on a user's cloud account

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
    "/v4/cloud/provider/gcp/projects": {
      "get": {
        "tags": [
          "Cloud",
          "GCP"
        ],
        "summary": "List Projects",
        "description": "Get all projects on a user's cloud account",
        "operationId": "list_projects_v4_cloud_provider_gcp_projects_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/ProjectGet"
                  },
                  "type": "array",
                  "title": "Response List Projects V4 Cloud Provider Gcp Projects Get"
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
      "ProjectGet": {
        "properties": {
          "project_id": {
            "type": "string",
            "title": "Project Id"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "state": {
            "type": "string",
            "title": "State"
          },
          "display_name": {
            "type": "string",
            "title": "Display Name"
          }
        },
        "type": "object",
        "required": [
          "project_id",
          "name",
          "state",
          "display_name"
        ],
        "title": "ProjectGet",
        "description": "Base model for schemas."
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