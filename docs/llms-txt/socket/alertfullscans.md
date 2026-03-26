# Source: https://docs.socket.dev/reference/alertfullscans.md

# List full scans associated with alert (Beta)

List full scans associated with alert.

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- alerts:list

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
      "name": "alerts"
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
    "/orgs/{org_slug}/alert-full-scan-search": {
      "get": {
        "tags": [
          "alerts"
        ],
        "summary": "List full scans associated with alert (Beta)",
        "operationId": "alertFullScans",
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
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Specify the maximum number of items to return per page (intermediate pages may have fewer than this limit and callers should always check \"endCursor\" in response body to know if there are more pages)",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 5000,
              "default": 1000
            }
          },
          {
            "name": "startAfterCursor",
            "in": "query",
            "required": false,
            "description": "The pagination cursor that was returned as the \"endCursor\" property in previous request",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "alertKey",
            "in": "query",
            "required": true,
            "description": "One or more alert keys for which to find associated full scans",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "range",
            "in": "query",
            "required": false,
            "description": "The number of days of data to fetch as an offset from current date (e.g. \"-7d\" for past 7 days)",
            "schema": {
              "type": "string",
              "default": "-7d"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "alerts:list"
            ]
          },
          {
            "basicAuth": [
              "alerts:list"
            ]
          }
        ],
        "description": "List full scans associated with alert.\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- alerts:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "endCursor": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
                    },
                    "items": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "fullScanId": {
                            "type": "string",
                            "description": "ID of full scan",
                            "default": ""
                          },
                          "branchName": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "branchType": {
                            "type": "string",
                            "enum": [
                              "default",
                              "non-default",
                              "tracked",
                              "untracked",
                              ""
                            ],
                            "description": "Type of branch that was scanned",
                            "default": ""
                          },
                          "repoFullName": {
                            "type": "string",
                            "description": "Full name of repo which contains repo workspace and repo slug",
                            "default": "",
                            "nullable": true
                          },
                          "sbomCreatedAt": {
                            "type": "string",
                            "description": "ISO date when SBOM was created",
                            "default": ""
                          },
                          "scannedAt": {
                            "type": "string",
                            "description": "ISO date when SBOM was scanned",
                            "default": ""
                          },
                          "alertKeys": {
                            "type": "array",
                            "items": {
                              "type": "string",
                              "description": "Alert keys associated with scan",
                              "default": ""
                            },
                            "description": ""
                          }
                        },
                        "required": [
                          "alertKeys",
                          "branchName",
                          "branchType",
                          "fullScanId",
                          "repoFullName",
                          "sbomCreatedAt",
                          "scannedAt"
                        ]
                      },
                      "description": ""
                    },
                    "meta": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "organizationId": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "alertKeys": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "description": ""
                        },
                        "queryStartTimestamp": {
                          "type": "number",
                          "description": "",
                          "default": 0
                        },
                        "startDateInclusive": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "endDateInclusive": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        }
                      },
                      "required": [
                        "alertKeys",
                        "endDateInclusive",
                        "organizationId",
                        "queryStartTimestamp",
                        "startDateInclusive"
                      ]
                    }
                  },
                  "required": [
                    "endCursor",
                    "items",
                    "meta"
                  ]
                }
              }
            },
            "description": "The paginated array of full scans associated with alert for the organization and related metadata."
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