# Source: https://docs.socket.dev/reference/getrepolist.md

# List GitHub repositories

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/getorgrepolist) instead.

Deprecated: Use `/orgs/{org_slug}/repos` instead. Get all GitHub repositories associated with a Socket org.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- repo:list

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
      "name": "deprecated"
    }
  ],
  "components": {
    "responses": {
      "SocketBadRequest": {
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
        "description": "Bad request"
      },
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
      "SocketNotFoundResponse": {
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
        "description": "Resource not found"
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
    "/repo/list": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "List GitHub repositories",
        "deprecated": true,
        "operationId": "getRepoList",
        "parameters": [
          {
            "name": "pageToken",
            "in": "query",
            "required": false,
            "description": "",
            "schema": {
              "type": "string",
              "default": ""
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "repo:list"
            ]
          },
          {
            "basicAuth": [
              "repo:list"
            ]
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/getorgrepolist) instead.\n\nDeprecated: Use `/orgs/{org_slug}/repos` instead. Get all GitHub repositories associated with a Socket org.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- repo:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "created_at": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "updated_at": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "github_install_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "github_repo_id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "github_full_name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "organization_id": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "workspace": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "latest_project_report": {
                            "type": "object",
                            "additionalProperties": false,
                            "description": "",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "created_at": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              }
                            },
                            "required": [
                              "created_at",
                              "id"
                            ]
                          }
                        },
                        "required": [
                          "created_at",
                          "github_full_name",
                          "github_install_id",
                          "github_repo_id",
                          "id",
                          "name",
                          "organization_id",
                          "updated_at",
                          "workspace"
                        ]
                      },
                      "description": ""
                    }
                  },
                  "required": [
                    "results"
                  ]
                }
              }
            },
            "description": "List of GitHub repositories associated with the organization."
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
          },
          "404": {
            "$ref": "#/components/responses/SocketNotFoundResponse"
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