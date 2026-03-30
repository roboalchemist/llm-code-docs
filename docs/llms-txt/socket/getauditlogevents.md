# Source: https://docs.socket.dev/reference/getauditlogevents.md

# Get Audit Log Events

Paginated list of audit log events.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- audit-log:list

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
      "name": "audit-log"
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
    "/orgs/{org_slug}/audit-log": {
      "get": {
        "tags": [
          "audit-log"
        ],
        "summary": "Get Audit Log Events",
        "operationId": "getAuditLogEvents",
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
            "name": "type",
            "in": "query",
            "required": false,
            "description": "Filter audit log events by type. Omit for all types.",
            "schema": {
              "type": "string",
              "enum": [
                "AddLicenseOverlayNote",
                "AssociateLabel",
                "CancelInvitation",
                "ChangeMemberRole",
                "ChangePlanSubscriptionSeats",
                "CreateApiToken",
                "CreateArtifact",
                "CreateLabel",
                "CreateOauthRefreshToken",
                "CreateRepoAccessRule",
                "CreateWebhook",
                "CreateTicket",
                "DeleteAlertTriage",
                "DeleteApiToken",
                "DeleteFullScan",
                "DeleteLabel",
                "DeleteLabelSetting",
                "DeleteRepoAccessRule",
                "DeleteReport",
                "DeleteRepository",
                "DeleteWebhook",
                "DisassociateLabel",
                "DisconnectJiraIntegration",
                "DowngradeOrganizationPlan",
                "JoinOrganization",
                "JiraIntegrationConnected",
                "MemberAdded",
                "MemberRemoved",
                "MemberRoleChanged",
                "RemoveLicenseOverlay",
                "RemoveMember",
                "ResetInvitationLink",
                "ResetOrganizationSettingToDefault",
                "RotateOauthRefreshToken",
                "RevokeApiToken",
                "RotateApiToken",
                "SendInvitation",
                "SetLabelSettingToDefault",
                "SyncOrganization",
                "TransferOwnership",
                "UpdateAlertTriage",
                "UpdateApiTokenCommitter",
                "UpdateApiTokenMaxQuota",
                "UpdateApiTokenName",
                "UpdateApiTokenScopes",
                "UpdateApiTokenVisibility",
                "UpdateAutopatchCurated",
                "UpdateLabel",
                "UpdateLabelSetting",
                "UpdateLicenseOverlay",
                "UpdateOrganizationSetting",
                "UpdateRepoAccessRule",
                "UpdateWebhook",
                "UpgradeOrganizationPlan"
              ]
            }
          },
          {
            "name": "per_page",
            "in": "query",
            "required": false,
            "description": "Number of events per page",
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
            "description": "Page token",
            "schema": {
              "type": "string",
              "default": "1"
            }
          },
          {
            "name": "from",
            "in": "query",
            "required": false,
            "description": "A Unix timestamp in seconds to filter results prior to this date.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "audit-log:list"
            ]
          },
          {
            "basicAuth": [
              "audit-log:list"
            ]
          }
        ],
        "description": "Paginated list of audit log events.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- audit-log:list",
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
                          "event_id": {
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
                          "country_code": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "organization_id": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "ip_address": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "payload": {
                            "type": "object",
                            "description": "",
                            "default": null,
                            "nullable": true
                          },
                          "status_code": {
                            "type": "integer",
                            "description": "",
                            "default": 0,
                            "nullable": true
                          },
                          "type": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "user_agent": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "user_id": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "user_email": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "user_image": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "organization_name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "description": ""
                      },
                      "description": ""
                    },
                    "nextPage": {
                      "type": "string",
                      "description": "",
                      "default": "",
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
            "description": "The paginated list of events in an organizations audit log and the next page querystring token."
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