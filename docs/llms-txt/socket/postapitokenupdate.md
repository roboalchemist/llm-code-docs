# Source: https://docs.socket.dev/reference/postapitokenupdate.md

# Update API Token

Update an API Token. The API Token created must use a subset of permissions the API token creating them.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- api-tokens:create

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "Specification of the Socket API endpoints",
    "title": "API Endpoints",
    "version": "0"
  },
  "servers": [
    {
      "url": "https://api.socket.dev/v0"
    }
  ],
  "tags": [
    {
      "name": "api-tokens"
    }
  ],
  "components": {
    "responses": {
      "SocketUnauthorized": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Unauthorized"
      },
      "SocketForbidden": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Insufficient max_quota for API method"
      },
      "SocketTooManyRequestsResponse": {
        "description": "Insufficient quota for API route",
        "headers": {
          "Retry-After": {
            "description": "Retry contacting the endpoint *at least* after seconds.\nSee https://tools.ietf.org/html/rfc7231#section-7.1.3",
            "schema": {
              "format": "int32",
              "type": "integer"
            }
          }
        },
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "description": "Organization Tokens can be passed as a Bearer token"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Organization Tokens can be passed as the user field in basic auth"
      }
    }
  },
  "paths": {
    "/orgs/{org_slug}/api-tokens/update": {
      "post": {
        "tags": [
          "api-tokens"
        ],
        "summary": "Update API Token",
        "operationId": "postAPITokenUpdate",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "max_quota": {
                    "type": "integer",
                    "description": "Maximum number of API calls allowed per hour",
                    "default": 1000
                  },
                  "scopes": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "enum": [
                        "alerts",
                        "alerts:list",
                        "alerts:trend",
                        "alert-resolution",
                        "alert-resolution:list",
                        "alert-resolution:create",
                        "alert-resolution:read",
                        "alert-resolution:delete",
                        "api-tokens",
                        "api-tokens:create",
                        "api-tokens:update",
                        "api-tokens:revoke",
                        "api-tokens:rotate",
                        "api-tokens:list",
                        "audit-log",
                        "audit-log:list",
                        "dependencies",
                        "dependencies:list",
                        "dependencies:trend",
                        "fixes",
                        "fixes:list",
                        "full-scans",
                        "full-scans:list",
                        "full-scans:create",
                        "full-scans:delete",
                        "diff-scans",
                        "diff-scans:list",
                        "diff-scans:create",
                        "diff-scans:delete",
                        "entitlements",
                        "entitlements:list",
                        "historical",
                        "historical:snapshots-list",
                        "historical:snapshots-start",
                        "historical:alerts-list",
                        "historical:alerts-trend",
                        "historical:dependencies-list",
                        "historical:dependencies-trend",
                        "integration",
                        "integration:list",
                        "integration:create",
                        "integration:update",
                        "integration:delete",
                        "license-policy",
                        "license-policy:update",
                        "license-policy:read",
                        "packages",
                        "packages:list",
                        "report",
                        "report:list",
                        "report:read",
                        "report:write",
                        "repo",
                        "repo:list",
                        "repo:create",
                        "repo:update",
                        "repo:delete",
                        "repo-label",
                        "repo-label:list",
                        "repo-label:create",
                        "repo-label:update",
                        "repo-label:delete",
                        "security-policy",
                        "security-policy:update",
                        "security-policy:read",
                        "socket-basics",
                        "socket-basics:read",
                        "telemetry-policy",
                        "telemetry-policy:update",
                        "telemetry-events",
                        "telemetry-events:list",
                        "threat-feed",
                        "threat-feed:list",
                        "triage",
                        "triage:alerts-list",
                        "triage:alerts-update",
                        "uploaded-artifacts",
                        "uploaded-artifacts:create",
                        "uploaded-artifacts:list",
                        "webhooks",
                        "webhooks:create",
                        "webhooks:list",
                        "webhooks:update",
                        "webhooks:delete",
                        "*"
                      ],
                      "description": "The scope of permissions for this API Token",
                      "default": "repo:list"
                    },
                    "description": "List of scopes granted to the API Token"
                  },
                  "visibility": {
                    "type": "string",
                    "enum": [
                      "admin",
                      "organization"
                    ],
                    "description": "The visibility of the API Token. Warning: this field is deprecated and will be removed in the future.",
                    "default": "organization"
                  },
                  "committer": {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "email": {
                        "type": "string",
                        "description": "Email address of the committer",
                        "default": ""
                      },
                      "provider": {
                        "type": "string",
                        "enum": [
                          "api",
                          "azure",
                          "bitbucket",
                          "github",
                          "gitlab"
                        ],
                        "description": "The source control provider for the committer",
                        "default": "api"
                      },
                      "providerLoginName": {
                        "type": "string",
                        "description": "Login name on the provider platform",
                        "default": ""
                      },
                      "providerUserId": {
                        "type": "string",
                        "description": "User ID on the provider platform",
                        "default": ""
                      }
                    },
                    "description": "Committer information to associate with the API Token"
                  },
                  "name": {
                    "type": "string",
                    "description": "Name for the API Token",
                    "default": "api token"
                  },
                  "uuid": {
                    "type": "string",
                    "description": "The stable group UUID to update (provide uuid, id, token, or hash. May provide uuid+hash together for validation)",
                    "default": "",
                    "format": "uuid"
                  },
                  "id": {
                    "type": "string",
                    "description": "The API token ID to update (provide uuid, id, token, or hash)",
                    "default": ""
                  },
                  "token": {
                    "type": "string",
                    "description": "The API token to update (provide uuid, id, token, or hash)",
                    "default": ""
                  },
                  "hash": {
                    "type": "string",
                    "description": "The API token hash to update (provide uuid, id, token, or hash)",
                    "default": ""
                  }
                },
                "required": [
                  "committer",
                  "max_quota",
                  "scopes",
                  "visibility"
                ]
              }
            }
          },
          "description": "The token and properties to update on the token.",
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "api-tokens:create"
            ]
          },
          {
            "basicAuth": [
              "api-tokens:create"
            ]
          }
        ],
        "description": "Update an API Token. The API Token created must use a subset of permissions the API token creating them.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- api-tokens:create",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "hash": {
                      "type": "string",
                      "description": "SRI-format hash of the API token (e.g., sha512-base64hash)",
                      "default": ""
                    }
                  },
                  "required": [
                    "hash"
                  ]
                }
              }
            },
            "description": "The updated token."
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
          },
          "429": {
            "$ref": "#/components/responses/SocketTooManyRequestsResponse"
          }
        },
        "x-readme": {}
      }
    }
  }
}
```