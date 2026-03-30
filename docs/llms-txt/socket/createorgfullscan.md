# Source: https://docs.socket.dev/reference/createorgfullscan.md

# Create full scan

Create a full scan from a set of package manifest files. Returns a full scan including all SBOM artifacts.

To get a list of supported filetypes that can be uploaded in a full-scan, see the [Get supported file types](/reference/getsupportedfiles) endpoint.

The maximum number of files you can upload at a time is 5000 and each file can be no bigger than 268 MB.

**Query Parameters:**
- `scan_type` (optional): The type of scan to perform. Defaults to 'socket'. Must be 32 characters or less. Used for categorizing multiple SBOM heads per repository branch.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- full-scans:create

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
    "/orgs/{org_slug}/full-scans": {
      "post": {
        "tags": [
          "full-scans"
        ],
        "summary": "Create full scan",
        "operationId": "CreateOrgFullScan",
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
            "name": "repo",
            "in": "query",
            "required": true,
            "description": "The slug of the repository to associate the full-scan with.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "workspace",
            "in": "query",
            "required": false,
            "description": "The workspace of the repository to associate the full-scan with.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "branch",
            "in": "query",
            "required": false,
            "description": "The branch name to associate the full-scan with. Branch names must follow Git branch name rules: be 1–255 characters long; cannot be exactly @;  cannot begin or end with /, ., or .lock; cannot contain \"//\", \"..\", or \"@{\"; and cannot include control characters, spaces, or any of ~^:?*[.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "commit_message",
            "in": "query",
            "required": false,
            "description": "The commit message to associate the full-scan with.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "commit_hash",
            "in": "query",
            "required": false,
            "description": "The commit hash to associate the full-scan with.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "pull_request",
            "in": "query",
            "required": false,
            "description": "The pull request number to associate the full-scan with.",
            "schema": {
              "type": "integer",
              "minimum": 1
            }
          },
          {
            "name": "committers",
            "in": "query",
            "required": false,
            "description": "The committers to associate with the full-scan. Set query more than once to set multiple.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "integration_type",
            "in": "query",
            "required": false,
            "description": "The integration type to associate the full-scan with. Defaults to \"Api\" if omitted.",
            "schema": {
              "type": "string",
              "enum": [
                "api",
                "github",
                "gitlab",
                "bitbucket",
                "azure",
                "web"
              ]
            }
          },
          {
            "name": "integration_org_slug",
            "in": "query",
            "required": false,
            "description": "The integration org slug to associate the full-scan with. If omitted, the Socket org name will be used. This is used to generate links and badges.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "make_default_branch",
            "in": "query",
            "required": false,
            "description": "Set the default branch of the repository to the branch of this full-scan. A branch name is required with this option.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "set_as_pending_head",
            "in": "query",
            "required": false,
            "description": "Designate this full-scan as the latest scan of a given branch. Default branch head scans are included in org alerts. This is only supported on the default branch. A branch name is required with this option.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "tmp",
            "in": "query",
            "required": false,
            "description": "Create a temporary full-scan that is not listed in the reports dashboard. Cannot be used when set_as_pending_head=true.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "scan_type",
            "in": "query",
            "required": false,
            "description": "The type of scan to perform. Defaults to 'socket'. Must be 32 characters or less. Used for categorizing multiple SBOM heads per repository branch.",
            "schema": {
              "type": "string",
              "default": "socket"
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "additionalProperties": {
                  "type": "string",
                  "default": {
                    "type": "Buffer",
                    "data": []
                  },
                  "format": "binary",
                  "description": ""
                },
                "properties": {},
                "description": ""
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "full-scans:create"
            ]
          },
          {
            "basicAuth": [
              "full-scans:create"
            ]
          }
        ],
        "description": "Create a full scan from a set of package manifest files. Returns a full scan including all SBOM artifacts.\n\nTo get a list of supported filetypes that can be uploaded in a full-scan, see the [Get supported file types](/reference/getsupportedfiles) endpoint.\n\nThe maximum number of files you can upload at a time is 5000 and each file can be no bigger than 268 MB.\n\n**Query Parameters:**\n- `scan_type` (optional): The type of scan to perform. Defaults to 'socket'. Must be 32 characters or less. Used for categorizing multiple SBOM heads per repository branch.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- full-scans:create",
        "responses": {
          "201": {
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
                    },
                    "unmatchedFiles": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "description": ""
                    }
                  },
                  "description": ""
                }
              }
            },
            "description": "The details of the created full scan."
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