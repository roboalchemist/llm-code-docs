# Source: https://docs.mystic.ai/reference/list_clusters_v4_clusters_get.md

# List Clusters

List all clusters belonging to a user

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
    "/v4/clusters": {
      "get": {
        "tags": [
          "Cluster"
        ],
        "summary": "List Clusters",
        "description": "List all clusters belonging to a user",
        "operationId": "list_clusters_v4_clusters_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/ClusterGet"
                  },
                  "type": "array",
                  "title": "Response List Clusters V4 Clusters Get"
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
      "ClusterGet": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "provider": {
            "type": "string",
            "title": "Provider"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "state": {
            "type": "string",
            "title": "State"
          },
          "credential_id": {
            "type": "string",
            "title": "Credential Id"
          },
          "error_message": {
            "type": "string",
            "title": "Error Message"
          }
        },
        "type": "object",
        "required": [
          "id",
          "provider",
          "name",
          "state",
          "credential_id"
        ],
        "title": "ClusterGet",
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