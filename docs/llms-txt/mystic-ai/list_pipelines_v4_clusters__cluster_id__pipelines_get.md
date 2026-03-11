# Source: https://docs.mystic.ai/reference/list_pipelines_v4_clusters__cluster_id__pipelines_get.md

# List Pipelines

List pipelines deployed to a given cluster

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
    "/v4/clusters/{cluster_id}/pipelines": {
      "get": {
        "tags": [
          "Cluster"
        ],
        "summary": "List Pipelines",
        "description": "List pipelines deployed to a given cluster",
        "operationId": "list_pipelines_v4_clusters__cluster_id__pipelines_get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Cluster Id"
            },
            "name": "cluster_id",
            "in": "path"
          },
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Skip",
              "default": 0
            },
            "name": "skip",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Limit",
              "default": 20
            },
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Paginated_ClusterDeployedPipelineGet_"
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
      "ClusterDeployedPipelineGet": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "pointers": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Pointers"
          },
          "node_pool": {
            "type": "string",
            "title": "Node Pool"
          },
          "replicas": {
            "$ref": "#/components/schemas/PipelineScaling"
          }
        },
        "type": "object",
        "required": [
          "id",
          "name",
          "pointers",
          "node_pool",
          "replicas"
        ],
        "title": "ClusterDeployedPipelineGet",
        "description": "Base model for schemas."
      },
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
      "Paginated_ClusterDeployedPipelineGet_": {
        "properties": {
          "skip": {
            "type": "integer",
            "minimum": 0,
            "title": "Skip"
          },
          "limit": {
            "type": "integer",
            "maximum": 1000,
            "minimum": 1,
            "title": "Limit"
          },
          "total": {
            "type": "integer",
            "minimum": 0,
            "title": "Total"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/ClusterDeployedPipelineGet"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "skip",
          "limit",
          "total",
          "data"
        ],
        "title": "Paginated[ClusterDeployedPipelineGet]",
        "description": "Response for paginated resource lists."
      },
      "PipelineScaling": {
        "properties": {
          "desired": {
            "type": "integer",
            "title": "Desired"
          },
          "current": {
            "type": "integer",
            "title": "Current"
          }
        },
        "type": "object",
        "required": [
          "desired",
          "current"
        ],
        "title": "PipelineScaling",
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