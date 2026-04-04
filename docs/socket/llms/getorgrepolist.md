# Source: https://docs.socket.dev/reference/getorgrepolist.md

# List repositories

Lists repositories for the specified organization.

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
      "name": "repos"
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
    "/orgs/{org_slug}/repos": {
      "get": {
        "tags": [
          "repos"
        ],
        "summary": "List repositories",
        "operationId": "getOrgRepoList",
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
            "description": "",
            "schema": {
              "type": "string",
              "default": "created_at"
            }
          },
          {
            "name": "direction",
            "in": "query",
            "required": false,
            "description": "",
            "schema": {
              "type": "string",
              "default": "desc"
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "",
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
            "description": "",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "default": 1
            }
          },
          {
            "name": "include_archived",
            "in": "query",
            "required": false,
            "description": "Include archived repositories in the results",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "workspace",
            "in": "query",
            "required": false,
            "description": "Filter repositories by workspace. When provided (including empty string), only repos in that workspace are returned.",
            "schema": {
              "type": "string"
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
        "description": "Lists repositories for the specified organization.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- repo:list",
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
                            "description": "The ID of the repository",
                            "default": ""
                          },
                          "created_at": {
                            "type": "string",
                            "description": "The creation date of the repository",
                            "default": ""
                          },
                          "updated_at": {
                            "type": "string",
                            "description": "The last update date of the repository",
                            "default": ""
                          },
                          "slug": {
                            "type": "string",
                            "description": "The slug of the repository",
                            "default": ""
                          },
                          "head_full_scan_id": {
                            "type": "string",
                            "description": "The ID of the head full scan of the repository",
                            "default": "",
                            "nullable": true
                          },
                          "integration_meta": {
                            "anyOf": [
                              {
                                "type": "object",
                                "additionalProperties": false,
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "enum": [
                                      "github"
                                    ]
                                  },
                                  "value": {
                                    "type": "object",
                                    "additionalProperties": false,
                                    "description": "",
                                    "properties": {
                                      "installation_id": {
                                        "type": "string",
                                        "description": "The GitHub installation_id of the active associated Socket GitHub App",
                                        "default": ""
                                      },
                                      "installation_login": {
                                        "type": "string",
                                        "description": "The GitHub login name that the active Socket GitHub App installation is installed to",
                                        "default": ""
                                      },
                                      "repo_name": {
                                        "type": "string",
                                        "description": "The name of the associated GitHub repo.",
                                        "default": "",
                                        "nullable": true
                                      },
                                      "repo_id": {
                                        "type": "string",
                                        "description": "The id of the associated GitHub repo.",
                                        "default": "",
                                        "nullable": true
                                      }
                                    },
                                    "required": [
                                      "installation_id",
                                      "installation_login",
                                      "repo_id",
                                      "repo_name"
                                    ]
                                  }
                                }
                              }
                            ],
                            "nullable": true
                          },
                          "name": {
                            "type": "string",
                            "description": "The name of the repository",
                            "default": ""
                          },
                          "description": {
                            "type": "string",
                            "description": "The description of the repository",
                            "default": "",
                            "nullable": true
                          },
                          "homepage": {
                            "type": "string",
                            "description": "The homepage URL of the repository",
                            "default": "",
                            "nullable": true
                          },
                          "visibility": {
                            "type": "string",
                            "enum": [
                              "public",
                              "private"
                            ],
                            "description": "The visibility of the repository",
                            "default": "private"
                          },
                          "archived": {
                            "type": "boolean",
                            "default": false,
                            "description": "Whether the repository is archived or not"
                          },
                          "default_branch": {
                            "type": "string",
                            "description": "The default branch of the repository",
                            "default": "main",
                            "nullable": true
                          },
                          "workspace": {
                            "type": "string",
                            "description": "The workspace of the repository",
                            "default": ""
                          }
                        },
                        "description": ""
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
                    "results"
                  ]
                }
              }
            },
            "description": "Lists repositories for the specified organization. The authenticated user must be a member of the organization."
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