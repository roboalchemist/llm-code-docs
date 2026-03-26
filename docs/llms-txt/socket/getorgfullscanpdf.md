# Source: https://docs.socket.dev/reference/getorgfullscanpdf.md

# Generate PDF report for full scan

Generate a PDF report for all alerts in a full scan.

This endpoint streams a PDF document containing all alerts found in the full scan,
with optional filtering and grouping options.

Supported request body filter IDs include:
- alert.action (error|warn|monitor|ignore)
- alert.type
- alert.category
- alert.severity (low|medium|middle|high|critical or 0-3)
- artifact.type (purl type, e.g. npm, pypi)
- dependency.type (direct|transitive)
- dependency.scope (dev|normal)
- dependency.usage (used|unused)
- manifest.file

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
    "/orgs/{org_slug}/full-scans/{full_scan_id}/format/pdf": {
      "post": {
        "tags": [
          "full-scans"
        ],
        "summary": "Generate PDF report for full scan",
        "operationId": "getOrgFullScanPdf",
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
          },
          {
            "name": "include_alert_priority_details",
            "in": "query",
            "required": false,
            "description": "Control which alert priority fields to include in the response. Set to \"true\" to include all fields, \"false\" to exclude all fields, or specify individual fields like \"components,formula\" to include only those fields.",
            "schema": {
              "oneOf": [
                {
                  "type": "boolean",
                  "default": false
                },
                {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "enum": [
                      "component",
                      "formula"
                    ]
                  }
                }
              ],
              "default": false
            }
          },
          {
            "name": "include_license_details",
            "in": "query",
            "required": true,
            "description": "Include license details in the response.",
            "schema": {
              "type": "boolean",
              "default": false
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
                  "filters": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "id": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "value": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": ""
                        }
                      },
                      "required": [
                        "id",
                        "value"
                      ]
                    },
                    "description": ""
                  },
                  "groupBy": {
                    "type": "string",
                    "description": "",
                    "default": ""
                  },
                  "additionalInformation": {
                    "type": "string",
                    "description": "",
                    "default": ""
                  }
                }
              }
            }
          },
          "required": false
        },
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
        "description": "Generate a PDF report for all alerts in a full scan.\n\nThis endpoint streams a PDF document containing all alerts found in the full scan,\nwith optional filtering and grouping options.\n\nSupported request body filter IDs include:\n- alert.action (error|warn|monitor|ignore)\n- alert.type\n- alert.category\n- alert.severity (low|medium|middle|high|critical or 0-3)\n- artifact.type (purl type, e.g. npm, pypi)\n- dependency.type (direct|transitive)\n- dependency.scope (dev|normal)\n- dependency.usage (used|unused)\n- manifest.file\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- full-scans:list",
        "responses": {
          "200": {
            "content": {
              "application/pdf": {}
            },
            "description": "PDF report of alerts"
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