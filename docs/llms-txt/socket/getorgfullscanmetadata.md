# Source: https://docs.socket.dev/reference/getorgfullscanmetadata.md

# Get full scan metadata

Get metadata for a single full scan

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- full-scans:list

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
      "name": "full-scans"
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
    "/orgs/{org_slug}/full-scans/{full_scan_id}/metadata": {
      "get": {
        "tags": [
          "full-scans"
        ],
        "summary": "Get full scan metadata",
        "operationId": "getOrgFullScanMetadata",
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
            "name": "full_scan_id",
            "in": "path",
            "required": true,
            "description": "The ID of the full scan",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "full-scans:list"
            ]
          },
          {
            "basicAuth": [
              "full-scans:list"
            ]
          }
        ],
        "description": "Get metadata for a single full scan\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- full-scans:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
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
                    "organization_id": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "organization_slug": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "repository_id": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "repository_slug": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "branch": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "commit_message": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "commit_hash": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "pull_request": {
                      "type": "integer",
                      "description": "",
                      "default": 0,
                      "nullable": true
                    },
                    "committers": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "description": ""
                    },
                    "html_url": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "api_url": {
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
                    "repo": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "html_report_url": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "integration_type": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "integration_repo_url": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "integration_branch_url": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "integration_commit_url": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "integration_pull_request_url": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "scan_type": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "scan_state": {
                      "type": "string",
                      "enum": [
                        "pending",
                        "precrawl",
                        "resolve",
                        "scan"
                      ],
                      "description": "The current processing status of the SBOM",
                      "default": "pending",
                      "nullable": true
                    }
                  },
                  "description": ""
                }
              }
            },
            "description": "The data from the full scan"
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