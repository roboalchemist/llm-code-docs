# Source: https://docs.socket.dev/reference/getapitokens.md

# List API Tokens

List all API Tokens.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- api-tokens:list

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
    "/orgs/{org_slug}/api-tokens": {
      "get": {
        "tags": [
          "api-tokens"
        ],
        "summary": "List API Tokens",
        "operationId": "getAPITokens",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "sort",
            "in": "query",
            "required": false,
            "description": "Specify Sort order.",
            "schema": {
              "type": "string",
              "enum": [
                "created_at"
              ],
              "default": "created_at"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "required": false,
            "description": "Specify sort direction.",
            "schema": {
              "type": "string",
              "enum": [
                "asc",
                "desc"
              ],
              "default": "desc"
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Specify the maximum number of results to return per page.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 30
            }
          },
          {
            "name": "page",
            "in": "query",
            "required": false,
            "description": "The token specifying which page to return.",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            }
          },
          {
            "name": "token_values",
            "in": "query",
            "required": false,
            "description": "Whether to include token values in response. Use \"omit\" to exclude tokens entirely.",
            "schema": {
              "type": "string",
              "enum": [
                "include",
                "omit"
              ],
              "default": "omit"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "api-tokens:list"
            ]
          },
          {
            "basicAuth": [
              "api-tokens:list"
            ]
          }
        ],
        "description": "List all API Tokens.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- api-tokens:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "tokens": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "API Token response schema",
                        "properties": {
                          "committers": {
                            "type": "array",
                            "items": {
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
                              "description": "Committer information associated with the API Token"
                            },
                            "description": "List of committers associated with this API Token"
                          },
                          "created_by": {
                            "type": "string",
                            "description": "ID of the Socket user who created the API Token",
                            "default": "",
                            "format": "uuid",
                            "nullable": true
                          },
                          "created_at": {
                            "type": "string",
                            "description": "Timestamp when the API Token was created",
                            "default": "",
                            "format": "date"
                          },
                          "group_uuid": {
                            "type": "string",
                            "description": "The stable group UUID that remains constant across token rotations",
                            "default": "",
                            "format": "uuid"
                          },
                          "hash": {
                            "type": "string",
                            "description": "SRI-format hash of the token (e.g., sha512-base64hash). Null for tokens created before hash column was added.",
                            "default": "",
                            "nullable": true
                          },
                          "id": {
                            "type": "string",
                            "description": "The ID of the API Token",
                            "default": ""
                          },
                          "last_used_at": {
                            "type": "string",
                            "description": "Timestamp when the API Token was last used",
                            "default": "",
                            "format": "date"
                          },
                          "max_quota": {
                            "type": "integer",
                            "description": "Maximum number of API calls allowed per month",
                            "default": 1000
                          },
                          "name": {
                            "type": "string",
                            "description": "Name for the API Token",
                            "default": "api token",
                            "nullable": true
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
                          "token": {
                            "type": "string",
                            "description": "The token of the API Token (redacted or omitted)",
                            "default": "",
                            "nullable": true
                          },
                          "visibility": {
                            "type": "string",
                            "enum": [
                              "admin",
                              "organization"
                            ],
                            "description": "The visibility of the API Token. Warning: this field is deprecated and will be removed in the future.",
                            "default": "organization"
                          }
                        },
                        "required": [
                          "committers",
                          "created_at",
                          "created_by",
                          "group_uuid",
                          "hash",
                          "id",
                          "last_used_at",
                          "max_quota",
                          "name",
                          "scopes",
                          "token",
                          "visibility"
                        ]
                      },
                      "description": ""
                    },
                    "nextPage": {
                      "type": "integer",
                      "description": "",
                      "default": 0,
                      "nullable": true
                    }
                  },
                  "required": [
                    "nextPage",
                    "tokens"
                  ]
                }
              }
            },
            "description": "The paginated array of API tokens for the organization, and related metadata."
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