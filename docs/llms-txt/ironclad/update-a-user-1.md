# Source: https://clickwrap-developer.ironcladapp.com/reference/update-a-user-1.md

# Update a User's Permissions

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "contact": {
      "email": "support@ironcladapp.com",
      "name": "Ironclad Support"
    },
    "title": "REST API",
    "version": "v1.1"
  },
  "security": [
    {
      "Bearer": []
    }
  ],
  "servers": [
    {
      "description": "Ironclad Clickwrap REST API",
      "url": "https://api.pactsafe.com/v1.1"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "scheme": "bearer",
        "type": "http"
      }
    }
  },
  "paths": {
    "/sites/{site_id}/memberships/{user_id}": {
      "patch": {
        "summary": "Update a User's Permissions",
        "tags": [
          "Sites"
        ],
        "operationId": "update-a-user",
        "parameters": [
          {
            "name": "site_id",
            "in": "path",
            "description": "The ID of the PactSafe Site.",
            "schema": {
              "type": "integer",
              "format": "integer"
            },
            "required": true
          },
          {
            "name": "user_id",
            "in": "path",
            "description": "The ID of the User.",
            "schema": {
              "type": "integer",
              "format": "integer"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "default": {
                    "type": "boolean",
                    "example": false
                  },
                  "role": {
                    "enum": [
                      "member",
                      "admin",
                      "owner"
                    ],
                    "title": "Role",
                    "type": "string"
                  },
                  "permissions": {
                    "properties": {
                      "approval_order": {
                        "default": 0,
                        "type": "integer"
                      },
                      "can_approve": {
                        "default": false,
                        "type": "boolean"
                      },
                      "complete": {
                        "default": false,
                        "type": "boolean"
                      },
                      "contract:metadata:edit": {
                        "default": true,
                        "type": "boolean"
                      },
                      "create": {
                        "default": true,
                        "type": "boolean"
                      },
                      "edit": {
                        "default": true,
                        "type": "boolean"
                      },
                      "export": {
                        "default": false,
                        "type": "boolean"
                      },
                      "fiel:secure:read": {
                        "default": false,
                        "type": "boolean"
                      },
                      "guides:publish": {
                        "default": true,
                        "type": "boolean"
                      },
                      "integration:sfdc:edit": {
                        "type": "boolean"
                      },
                      "mergefield:manage": {
                        "type": "boolean"
                      },
                      "needs_approval": {
                        "default": true,
                        "type": "boolean"
                      },
                      "publish": {
                        "default": true,
                        "type": "boolean"
                      },
                      "send": {
                        "default": true,
                        "type": "boolean"
                      },
                      "snapshots:manage": {
                        "default": false,
                        "type": "boolean"
                      },
                      "snapshots:upload": {
                        "default": false,
                        "type": "boolean"
                      }
                    },
                    "type": "object"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully updated",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "default": {
                      "type": "boolean",
                      "example": false
                    },
                    "role": {
                      "enum": [
                        "member",
                        "admin",
                        "owner"
                      ],
                      "title": "Role",
                      "type": "string"
                    },
                    "permissions": {
                      "properties": {
                        "approval_order": {
                          "default": 0,
                          "type": "integer"
                        },
                        "can_approve": {
                          "default": false,
                          "type": "boolean"
                        },
                        "complete": {
                          "default": false,
                          "type": "boolean"
                        },
                        "contract:metadata:edit": {
                          "default": true,
                          "type": "boolean"
                        },
                        "create": {
                          "default": true,
                          "type": "boolean"
                        },
                        "edit": {
                          "default": true,
                          "type": "boolean"
                        },
                        "export": {
                          "default": false,
                          "type": "boolean"
                        },
                        "fiel:secure:read": {
                          "default": false,
                          "type": "boolean"
                        },
                        "guides:publish": {
                          "default": true,
                          "type": "boolean"
                        },
                        "integration:sfdc:edit": {
                          "type": "boolean"
                        },
                        "mergefield:manage": {
                          "type": "boolean"
                        },
                        "needs_approval": {
                          "default": true,
                          "type": "boolean"
                        },
                        "publish": {
                          "default": true,
                          "type": "boolean"
                        },
                        "send": {
                          "default": true,
                          "type": "boolean"
                        },
                        "snapshots:manage": {
                          "default": false,
                          "type": "boolean"
                        },
                        "snapshots:upload": {
                          "default": false,
                          "type": "boolean"
                        }
                      },
                      "type": "object"
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden."
          },
          "404": {
            "description": "Not found."
          }
        },
        "deprecated": false
      }
    }
  }
}
```