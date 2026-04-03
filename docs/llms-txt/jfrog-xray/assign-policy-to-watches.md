# Source: https://docs.jfrog.com/security/reference/assign-policy-to-watches.md

# Assign Policy to Watches

Assigns an existing policy to one or more watches. Each watch name in the request is processed independently — the response reports the result for each watch separately. If a watch does not exist or the policy is already assigned, the response indicates the status per watch rather than failing the entire request.

Requires the "Manage Watches" role to be set on the User or Group level.

Note: This endpoint does not support the `projectKey` query parameter. The policy is looked up by name across all scopes.


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v1/policies/{name}/assign": {
      "post": {
        "operationId": "assign-policy-to-watches",
        "summary": "Assign Policy to Watches",
        "description": "Assigns an existing policy to one or more watches. Each watch name in the request is processed independently — the response reports the result for each watch separately. If a watch does not exist or the policy is already assigned, the response indicates the status per watch rather than failing the entire request.\n\nRequires the \"Manage Watches\" role to be set on the User or Group level.\n\nNote: This endpoint does not support the `projectKey` query parameter. The policy is looked up by name across all scopes.\n",
        "tags": [
          "Policies V1"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The name of the policy to assign.",
            "example": "sec-policy"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PolicyAssignToWatchesRequest"
              },
              "example": {
                "watches": [
                  "prod-watch",
                  "staging-watch"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Assignment processed. Check the `result` map for per-watch status — some watches may have succeeded while others failed.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PolicyAssignToWatchesResponse"
                },
                "example": {
                  "result": {
                    "prod-watch": "Policy assigned successfully to Watch",
                    "staging-watch": "Watch was not found"
                  }
                }
              }
            }
          },
          "404": {
            "description": "The specified policy does not exist.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Policy sec-policy doesn't exist"
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse the request body.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Failed to parse request"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                },
                "example": {
                  "error": "Failed to assign Policy to watches"
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
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    },
    "schemas": {
      "PolicyAssignToWatchesRequest": {
        "type": "object",
        "description": "Request body containing the list of watch names to assign the policy to.\n",
        "required": [
          "watches"
        ],
        "properties": {
          "watches": {
            "type": "array",
            "description": "List of watch names to assign the policy to. Each watch is processed independently.\n",
            "items": {
              "type": "string"
            },
            "example": [
              "prod-watch",
              "staging-watch"
            ]
          }
        }
      },
      "PolicyAssignToWatchesResponse": {
        "type": "object",
        "description": "Result of the assignment operation. The `result` object contains one entry per watch name from the request, with a status message indicating the outcome. Possible status values: \"Policy assigned successfully to Watch\", \"Policy was already assigned to Watch\", \"Watch was not found\", \"Error Assigning Policy to Watch\".\n",
        "properties": {
          "result": {
            "type": "object",
            "description": "Map of watch name to assignment status string.\n",
            "properties": {
              "{watch_name}": {
                "type": "string",
                "description": "Status message for the watch. Key is the watch name.\n",
                "example": "Policy assigned successfully to Watch"
              }
            },
            "example": {
              "prod-watch": "Policy assigned successfully to Watch",
              "staging-watch": "Watch was not found"
            }
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "Policies V1",
      "description": "APIs from Policies V1"
    }
  ]
}
```