# Source: https://docs.socket.dev/reference/historicalsnapshotslist.md

# List details of periodic historical data snapshots (Beta)

This API endpoint is used to list the details of historical snapshots.
Snapshots of organization data are taken periodically, and each historical snapshot record contains high-level overview metrics about the data that was collected.
Other [Historical Data Endpoints](/reference/historical-data-endpoints) can be used to fetch the raw data associated with each snapshot.

Historical snapshots contain details and raw data for the following resources:

- Repositories
- Alerts
- Dependencies
- Artifacts
- Users
- Settings

Daily snapshot data is bucketed to the nearest day which is described in more detail at: [Historical Data Endpoints](/reference/historical-data-endpoints)

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- historical:snapshots-list

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
      "name": "org-snapshots"
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
    "/orgs/{org_slug}/historical/snapshots": {
      "get": {
        "tags": [
          "org-snapshots"
        ],
        "summary": "List details of periodic historical data snapshots (Beta)",
        "operationId": "historicalSnapshotsList",
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
            "name": "date",
            "in": "query",
            "required": false,
            "description": "The UTC date in YYYY-MM-DD format for which to fetch snapshots",
            "schema": {
              "type": "string",
              "default": "CURRENT_DATE"
            }
          },
          {
            "name": "range",
            "in": "query",
            "required": false,
            "description": "The number of days of data to fetch as an offset from input date (e.g. \"-7d\" or \"7d\") or use \"latest\" to query for latest snapshots for each repo",
            "schema": {
              "type": "string",
              "default": "-7d"
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Specify the maximum number of results to return per page (intermediate pages may have fewer than this limit and callers should always check \"endCursor\" in response body to know if there are more pages)",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 10000,
              "default": 10000
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
            "name": "filters.status",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of historical snapshot statuses that should be included (allowed: \"in-progress\", \"success\", \"failure\", \"timeout\", \"skipped\")",
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "filters.requestId",
            "in": "query",
            "required": false,
            "description": "Comma-separated list of requestId values that were used to start the historical snapshot job",
            "schema": {
              "type": "string",
              "default": ""
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "historical:snapshots-list"
            ]
          },
          {
            "basicAuth": [
              "historical:snapshots-list"
            ]
          }
        ],
        "description": "This API endpoint is used to list the details of historical snapshots.\nSnapshots of organization data are taken periodically, and each historical snapshot record contains high-level overview metrics about the data that was collected.\nOther [Historical Data Endpoints](/reference/historical-data-endpoints) can be used to fetch the raw data associated with each snapshot.\n\nHistorical snapshots contain details and raw data for the following resources:\n\n- Repositories\n- Alerts\n- Dependencies\n- Artifacts\n- Users\n- Settings\n\nDaily snapshot data is bucketed to the nearest day which is described in more detail at: [Historical Data Endpoints](/reference/historical-data-endpoints)\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- historical:snapshots-list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
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
                        },
                        "filters": {
                          "type": "object",
                          "additionalProperties": false,
                          "properties": {
                            "status": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "description": "",
                                "default": ""
                              },
                              "description": ""
                            },
                            "requestId": {
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
                      },
                      "required": [
                        "endDateInclusive",
                        "filters",
                        "organizationId",
                        "queryStartTimestamp",
                        "startDateInclusive"
                      ]
                    },
                    "items": {
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
                          "requestId": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "requestedBy": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "requestedAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "startedAt": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "finishedAt": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "durationMs": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "status": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "numReposScanned": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numSbomsScanned": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numLowAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numHighAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numMediumAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numCriticalAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numIgnoredLowAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numIgnoredHighAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numIgnoredMediumAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          },
                          "numIgnoredCriticalAlerts": {
                            "type": "integer",
                            "description": "",
                            "default": 0
                          }
                        },
                        "required": [
                          "durationMs",
                          "finishedAt",
                          "id",
                          "numCriticalAlerts",
                          "numHighAlerts",
                          "numIgnoredCriticalAlerts",
                          "numIgnoredHighAlerts",
                          "numIgnoredLowAlerts",
                          "numIgnoredMediumAlerts",
                          "numLowAlerts",
                          "numMediumAlerts",
                          "numReposScanned",
                          "numSbomsScanned",
                          "requestId",
                          "requestedAt",
                          "requestedBy",
                          "startedAt",
                          "status"
                        ]
                      },
                      "description": ""
                    },
                    "endCursor": {
                      "type": "string",
                      "description": "",
                      "default": "",
                      "nullable": true
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
            "description": "The historical snapshots."
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