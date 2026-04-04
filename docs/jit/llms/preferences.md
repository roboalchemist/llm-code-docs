# Source: https://docs.jit.io/reference/preferences.md

# Return all preferences

Retrieves system preferences at various scopes. Users can specify 'tenant' for organizational-level settings, 'user' for individual settings, or 'merged' for a combination.

**Requires the following permission:**
`jit.preferences.read`

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Jit Public APIs",
    "description": "Jit Public APIs.\n\nThe API requires that you log in first and obtain a JWT authentication bearer token:\n\nJIT Platform generates CLIENT_ID and SECRET under `Settings -> Users & Permissions -> API Tokens`\n\n For more information, refer to [Users and Permissions](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
    "version": "1",
    "termsOfService": "https://www.jit.io/legal/terms"
  },
  "servers": [
    {
      "url": "https://api.jit.io",
      "description": "Jit API domain"
    }
  ],
  "externalDocs": {
    "url": "https://docs.jit.io/docs",
    "description": "Jit docs"
  },
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "tags": [
    {
      "name": "Tenant",
      "description": "Returns, adds, edits, or remove tenant and preferences data.",
      "externalDocs": {
        "url": "https://docs.jit.io/docs",
        "description": "Learn about managing your tenant in JIT"
      }
    }
  ],
  "paths": {
    "/tenant/preferences": {
      "get": {
        "summary": "Return all preferences",
        "description": "Retrieves system preferences at various scopes. Users can specify 'tenant' for organizational-level settings, 'user' for individual settings, or 'merged' for a combination.\n\n**Requires the following permission:**\n`jit.preferences.read`",
        "operationId": "preferences",
        "parameters": [
          {
            "name": "scope",
            "in": "query",
            "description": "Specifies the preference scope: 'tenant' (default) for organization-level settings, 'user' for individual user settings, or 'both', which merges tenant and user preferences.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/scope"
            }
          }
        ],
        "tags": [
          "Tenant"
        ],
        "responses": {
          "200": {
            "description": "Get tenant and user preferences by scope",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MergedPreferences"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TenantAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "400": {
            "description": "Bad request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BadRequest"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TenantAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UnauthorizedAuthorizerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TenantAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ForbiddenError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TenantAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalServerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/TenantAccess-Control-Allow-Origin"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BadRequest": {
        "title": "ValidationErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INVALID_INPUT",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable message containing fields that failed validation.",
            "example": "sample_field1: ensure this value is greater than or equal to 5\ninner_object -> sample_field2: field required",
            "type": "string"
          },
          "invalid_parameters": {
            "title": "Input parameters to errors map",
            "description": "Dictionary mapping input parameter for their corresponding error messages for programmatic use.\n\n**Important**: This dictionary should match your input. Parameters with invalid inputs display their respective messages.",
            "nullable": true,
            "example": {
              "sample_field1": "ensure this value is greater than or equal to 5",
              "inner_object": {
                "sample_field2": "field required"
              }
            },
            "type": "object"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "ForbiddenError": {
        "title": "ForbiddenErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "FORBIDDEN",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Request is missing the required permissions.",
            "type": "string"
          },
          "missing_permissions": {
            "title": "Missing permissions",
            "description": "List of missing permissions.",
            "nullable": true,
            "example": [
              "jit.category.write",
              "jit.category.read"
            ],
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "InternalServerError": {
        "title": "InternalErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INTERNAL_SERVER_ERROR",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Some error message indicating the issue that occurred",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "UnauthorizedAuthorizerError": {
        "title": "UnauthorizedAuthorizerErrorResponse",
        "type": "object",
        "properties": {
          "Message": {
            "title": "Error message",
            "description": "Human readable error message.\n\n**Important**: This schema does not contain `error` field.",
            "example": "Unauthorized",
            "type": "string"
          }
        },
        "required": [
          "Message"
        ]
      },
      "MergedPreferences": {
        "title": "MergedPreferences",
        "type": "object",
        "properties": {
          "display": {
            "title": "Display Preferences",
            "description": "Controls the display settings of the user interface. This includes layout preferences, theme settings, etc.",
            "allOf": [
              {
                "title": "DisplayPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "show_set_as_goal_modal": {
                    "title": "Show Set Goal Modal",
                    "description": "Indicates whether the 'Set Goal' modal is displayed to the user.",
                    "default": true,
                    "example": true,
                    "type": "boolean"
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          },
          "notifications": {
            "title": "Notification Preferences",
            "description": "Enable control of notifications preferences.",
            "allOf": [
              {
                "title": "NotificationsPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "ignore_findings": {
                    "title": "Ignore Findings",
                    "description": "Notifications about ignored findings.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  },
                  "deployment_with_vulnerabilities": {
                    "title": "Deployment with Vulnerabilities",
                    "description": "Notifications about deployments with vulnerabilities.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  },
                  "findings_on_saved_views": {
                    "title": "Findings on Saved Views",
                    "description": "Notifications about new findings on saved views.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  },
                  "new_action_created": {
                    "title": "New Action Created",
                    "description": "Notifications about new actions.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  },
                  "high_severity_findings": {
                    "title": "High Severity Findings",
                    "description": "Notifications about new high severity findings.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  },
                  "period_report": {
                    "title": "Bi-Weekly Period Report",
                    "description": "Notifications about bi-weekly reports.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  },
                  "security_plan_failures": {
                    "title": "Security Plan Failures",
                    "description": "Notifications about security plan failure.",
                    "allOf": [
                      {
                        "title": "NotificationsPreference",
                        "type": "object",
                        "properties": {
                          "enabled": {
                            "title": "Enabled",
                            "description": "Indicates whether the preference is enabled.",
                            "example": true,
                            "type": "boolean"
                          },
                          "channel": {
                            "title": "Notification Channel",
                            "description": "The communication channel used for notifications.",
                            "example": "Some Channel",
                            "type": "string"
                          }
                        }
                      }
                    ]
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          },
          "deployment": {
            "title": "Deployment Preferences",
            "description": "Enable control of deployment preferences.",
            "allOf": [
              {
                "title": "DeploymentPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "environments": {
                    "title": "Environments",
                    "description": "List of environments where Jit scans deployment.",
                    "default": [],
                    "example": [
                      "Staging",
                      "Production"
                    ],
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          },
          "pr_check": {
            "title": "PR Check Preferences",
            "description": "Enable control of PR check preferences.",
            "allOf": [
              {
                "title": "PrCheckPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "is_enabled": {
                    "title": "Enabled",
                    "description": "Indicates whether the preference is enabled.",
                    "example": true,
                    "type": "boolean"
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          },
          "thresholds": {
            "title": "Thresholds Preferences",
            "description": "Enable control of thresholds preferences.",
            "allOf": [
              {
                "title": "ThresholdsPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "score": {
                    "title": "Score Threshold",
                    "description": "The score threshold for the tenant.",
                    "default": 80,
                    "type": "integer"
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          },
          "teams_sync": {
            "title": "Teams Sync Preferences",
            "description": "Enable control of teams sync preferences.",
            "allOf": [
              {
                "title": "TeamsSyncPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "sync_type": {
                    "title": "Sync Type",
                    "description": "The type of sync for the tenant.",
                    "allOf": [
                      {
                        "title": "SyncType",
                        "description": "An enumeration.",
                        "enum": [
                          "manual",
                          "auto"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "provider": {
                    "title": "Provider",
                    "description": "In case of auto sync, the provider to sync with.",
                    "type": "string"
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          },
          "backlog_branches": {
            "title": "Backlog Branches Preferences",
            "description": "Enable control of backlog branches preferences.",
            "allOf": [
              {
                "title": "BacklogBranchesPreferences",
                "type": "object",
                "properties": {
                  "created_at": {
                    "title": "Created At",
                    "description": "Creation date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "modified_at": {
                    "title": "Modified At",
                    "description": "Last modification date of the preference.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                    "example": "2023-10-17 19:09:40.236710",
                    "format": "date-time",
                    "type": "string"
                  },
                  "scope": {
                    "title": "Preference Scope",
                    "description": "The scope to which this preference applies.",
                    "example": "tenant",
                    "allOf": [
                      {
                        "title": "PreferencesScope",
                        "description": "An enumeration.",
                        "enum": [
                          "tenant",
                          "user"
                        ],
                        "type": "string"
                      }
                    ]
                  },
                  "backlog_branches": {
                    "title": "Backlog Branches",
                    "description": "List of all the backlog branches which by this setting, make them scanned by Jit in Non-PR events",
                    "example": [
                      "develop"
                    ],
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "required": [
                  "scope"
                ]
              }
            ]
          }
        }
      },
      "scope": {
        "default": "tenant",
        "example": "tenant",
        "title": "RequestPreferenceScope",
        "description": "An enumeration.",
        "enum": [
          "tenant",
          "user",
          "merged"
        ],
        "type": "string"
      },
      "TenantAccess-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "*"
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 103,
      "1": 96,
      "2": 119,
      "3": 178,
      "4": 114,
      "5": 109,
      "6": 158,
      "7": 128,
      "8": 238,
      "9": 252,
      "10": 241,
      "11": 194
    }
  }
}
```