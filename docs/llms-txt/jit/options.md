# Source: https://docs.jit.io/reference/options.md

# Fetch Steps Options

Retrieve the available steps options for a workflow.

**Requires the following permission:**
`jit.workflows.read`

This feature is exclusive to premium users. To access it, upgrade to the Premium users pricing plan.

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
  "paths": {
    "/workflows/options": {
      "get": {
        "summary": "Fetch Steps Options",
        "description": "Retrieve the available steps options for a workflow.\n\n**Requires the following permission:**\n`jit.workflows.read`\n\nThis feature is exclusive to premium users. To access it, upgrade to the Premium users pricing plan.",
        "operationId": "options",
        "parameters": [],
        "tags": [
          "Workflows"
        ],
        "responses": {
          "200": {
            "description": "A list of steps options per step type (trigger, condition, action)",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetStepsOptionsResponse"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
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
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
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
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
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
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
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
      "Access-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Credentials": {
        "type": "boolean",
        "default": true
      },
      "GetStepsOptionsResponse": {
        "title": "GetStepsOptionsResponse",
        "type": "object",
        "properties": {
          "trigger_options": {
            "title": "Trigger Options",
            "default": [
              {
                "step_type": "trigger",
                "type": "findings-created",
                "label": "Backlog Finding Created",
                "description": "Triggered when new finding is created",
                "input": [],
                "output": [
                  "finding"
                ]
              },
              {
                "step_type": "trigger",
                "type": "findings-fixed",
                "label": "Backlog Finding Fixed",
                "description": "Triggered when finding is fixed",
                "input": [],
                "output": [
                  "finding"
                ]
              },
              {
                "step_type": "trigger",
                "type": "findings-ignored",
                "label": "Backlog Finding Ignored",
                "description": "Triggered when finding is ignored",
                "input": [],
                "output": [
                  "finding"
                ]
              }
            ],
            "type": "array",
            "items": {
              "title": "TriggerOption",
              "type": "object",
              "properties": {
                "step_type": {
                  "allOf": [
                    {
                      "title": "StepType",
                      "description": "An enumeration.",
                      "enum": [
                        "condition",
                        "action",
                        "trigger"
                      ],
                      "type": "string",
                      "default": "action"
                    }
                  ]
                },
                "type": {
                  "title": "Type",
                  "description": "The unique type identifier of the option",
                  "type": "string"
                },
                "label": {
                  "title": "Label",
                  "description": "Display name of the option",
                  "type": "string"
                },
                "description": {
                  "title": "Description",
                  "description": "Description of the option",
                  "type": "string"
                },
                "input": {
                  "description": "Triggers do not accept any input, always an empty list",
                  "default": [],
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                },
                "output": {
                  "description": "The output entities for this option",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                }
              },
              "required": [
                "type",
                "label",
                "description",
                "output"
              ]
            }
          },
          "condition_options": {
            "title": "Condition Options",
            "default": [
              {
                "step_type": "condition",
                "type": "FindingCondition",
                "label": "Finding Condition",
                "description": "Condition based on finding attributes",
                "input": [
                  "finding"
                ],
                "output": [
                  "asset",
                  "finding"
                ],
                "prerequisites": [
                  "asset"
                ],
                "config_schema": {
                  "filter_conditions": "when {condition_entity} has {condition_attribute} {condition_operator} {condition_value}",
                  "inputs": {
                    "condition_entity": {
                      "label": "Condition Entity",
                      "input_type": "select",
                      "options": [
                        {
                          "value": "finding",
                          "label": "Finding"
                        },
                        {
                          "value": "asset",
                          "label": "Resource"
                        }
                      ],
                      "required": true,
                      "placeholder": "Select",
                      "default_value": null,
                      "multi": null,
                      "depends_on": null,
                      "dynamic_config": null,
                      "options_callback": null
                    },
                    "condition_attribute": {
                      "label": "Condition Attribute",
                      "input_type": "select",
                      "required": true,
                      "depends_on": "condition_entity",
                      "dynamic_config": {
                        "finding": {
                          "options": [
                            {
                              "value": "priority_factors",
                              "label": "Priority Factor"
                            },
                            {
                              "value": "issue_severity",
                              "label": "Severity"
                            },
                            {
                              "value": "priority_score",
                              "label": "Priority Score"
                            },
                            {
                              "value": "vulnerability_type",
                              "label": "Finding Type"
                            },
                            {
                              "value": "teams",
                              "label": "Team"
                            },
                            {
                              "value": "cwes",
                              "label": "CWE"
                            }
                          ]
                        },
                        "asset": {
                          "options": [
                            {
                              "value": "asset_type",
                              "label": "Type"
                            },
                            {
                              "value": "asset_name",
                              "label": "Name"
                            },
                            {
                              "value": "score",
                              "label": "Risk Score"
                            },
                            {
                              "value": "priority_factors",
                              "label": "Priority Factor"
                            }
                          ]
                        }
                      },
                      "placeholder": "Select",
                      "options": null,
                      "default_value": null,
                      "multi": null,
                      "options_callback": null
                    },
                    "condition_operator": {
                      "label": "Condition Operator",
                      "input_type": "select",
                      "required": true,
                      "depends_on": "condition_attribute",
                      "dynamic_config": {
                        "finding": {
                          "priority_factors": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "issue_severity": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "priority_score": {
                            "options": [
                              {
                                "value": "above",
                                "label": "Above"
                              },
                              {
                                "value": "below",
                                "label": "Below"
                              },
                              {
                                "value": "equal",
                                "label": "Equal"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "vulnerability_type": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "teams": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "cwes": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          }
                        },
                        "asset": {
                          "asset_type": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "asset_name": {
                            "options": [
                              {
                                "value": "equal",
                                "label": "Equal"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "score": {
                            "options": [
                              {
                                "value": "above",
                                "label": "Above"
                              },
                              {
                                "value": "below",
                                "label": "Below"
                              },
                              {
                                "value": "equal",
                                "label": "Equal"
                              }
                            ],
                            "placeholder": "Select"
                          },
                          "priority_factors": {
                            "options": [
                              {
                                "value": "contain",
                                "label": "Contain"
                              }
                            ],
                            "placeholder": "Select"
                          }
                        }
                      },
                      "options": null,
                      "default_value": null,
                      "multi": null,
                      "placeholder": null,
                      "options_callback": null
                    },
                    "condition_value": {
                      "label": "Condition Value",
                      "required": true,
                      "multi": true,
                      "depends_on": "condition_operator",
                      "dynamic_config": {
                        "finding": {
                          "priority_factors": {
                            "input_type": "select",
                            "placeholder": "Select priority factors",
                            "options_callback": "fetchFindingPriorityFactorsOptions"
                          },
                          "issue_severity": {
                            "input_type": "select",
                            "options": [
                              {
                                "value": "CRITICAL",
                                "label": "Critical"
                              },
                              {
                                "value": "HIGH",
                                "label": "High"
                              },
                              {
                                "value": "MEDIUM",
                                "label": "Medium"
                              },
                              {
                                "value": "LOW",
                                "label": "Low"
                              }
                            ]
                          },
                          "priority_score": {
                            "input_type": "number",
                            "placeholder": "Enter a priority score",
                            "validation": {
                              "min": 0,
                              "max": 100
                            }
                          },
                          "vulnerability_type": {
                            "input_type": "select",
                            "placeholder": "Select finding types",
                            "options_callback": "fetchFindingTypesOptions"
                          },
                          "teams": {
                            "input_type": "select",
                            "placeholder": "Select team names",
                            "options_callback": "fetchFindingTeamsOptions"
                          },
                          "cwes": {
                            "input_type": "text",
                            "placeholder": "Enter CWES"
                          }
                        },
                        "asset": {
                          "asset_type": {
                            "input_type": "select",
                            "placeholder": "Select asset types",
                            "options_callback": "fetchAssetTypesOptions"
                          },
                          "asset_name": {
                            "input_type": "select",
                            "placeholder": "Select resource names",
                            "options_callback": "fetchAssetNamesOptions"
                          },
                          "score": {
                            "input_type": "number",
                            "placeholder": "Enter a risk score",
                            "validation": {
                              "min": 0,
                              "max": 100
                            }
                          },
                          "priority_factors": {
                            "input_type": "select",
                            "placeholder": "Select priority factors",
                            "options_callback": "fetchAssetPriorityFactorsOptions"
                          }
                        }
                      },
                      "input_type": null,
                      "options": null,
                      "default_value": null,
                      "placeholder": null,
                      "options_callback": null
                    },
                    "user_identity_type": null,
                    "user_identity_value": null
                  },
                  "slug": "finding_condition",
                  "base_condition": ""
                }
              }
            ],
            "type": "array",
            "items": {
              "title": "ConditionOption",
              "type": "object",
              "properties": {
                "step_type": {
                  "allOf": [
                    {
                      "title": "StepType",
                      "description": "An enumeration.",
                      "enum": [
                        "condition",
                        "action",
                        "trigger"
                      ],
                      "type": "string",
                      "default": "action"
                    }
                  ]
                },
                "type": {
                  "title": "Type",
                  "description": "The unique type identifier of the option",
                  "type": "string"
                },
                "label": {
                  "title": "Label",
                  "description": "Display name of the option",
                  "type": "string"
                },
                "description": {
                  "title": "Description",
                  "description": "Description of the option",
                  "type": "string"
                },
                "input": {
                  "description": "The input entities for this option",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                },
                "output": {
                  "description": "The output entities for this option",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                },
                "prerequisites": {
                  "description": "list of entities required as prerequisites",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                },
                "config_schema": {
                  "title": "Config Schema",
                  "description": "Schema defining condition details",
                  "type": "object"
                }
              },
              "required": [
                "type",
                "label",
                "description",
                "input",
                "output",
                "prerequisites",
                "config_schema"
              ]
            }
          },
          "action_options": {
            "title": "Action Options",
            "default": [
              {
                "step_type": "action",
                "type": "SendFindingMessage",
                "label": "Send Notification",
                "description": "Send a finding change notification to channel",
                "input": [
                  "finding"
                ],
                "output": [
                  "channel_name"
                ],
                "config_schema": [
                  {
                    "key": "vendor",
                    "type": "VendorPicker",
                    "enum": [
                      "slack"
                    ],
                    "description": "Choose a Messaging system to use"
                  },
                  {
                    "key": "channel",
                    "type": "SlackChannelPicker",
                    "depends_on": {
                      "vendor": "slack"
                    },
                    "description": "Choose Slack channel to notify team members"
                  }
                ],
                "prerequisites": [
                  "asset"
                ]
              },
              {
                "step_type": "action",
                "type": "CreateTicketForFinding",
                "label": "Create Ticket",
                "description": "Creates a ticket for the finding",
                "input": [
                  "finding"
                ],
                "output": [],
                "config_schema": [
                  {
                    "key": "vendor",
                    "type": "VendorPicker",
                    "enum": [],
                    "description": "Choose a Ticket Management System to use"
                  },
                  {
                    "key": "project",
                    "type": "ProjectPicker",
                    "description": "Choose a project to create tickets"
                  }
                ],
                "prerequisites": []
              },
              {
                "step_type": "action",
                "type": "SendFindingToSIEM",
                "label": "Send Finding to SIEM",
                "description": "Sends all findings to a Security Information and Event Management (SIEM) system",
                "input": [
                  "finding"
                ],
                "output": [],
                "config_schema": [
                  {
                    "key": "vendor",
                    "type": "VendorPicker",
                    "enum": [],
                    "description": "Choose a centralized logging system to send findings"
                  }
                ],
                "prerequisites": []
              }
            ],
            "type": "array",
            "items": {
              "title": "ActionOption",
              "type": "object",
              "properties": {
                "step_type": {
                  "allOf": [
                    {
                      "title": "StepType",
                      "description": "An enumeration.",
                      "enum": [
                        "condition",
                        "action",
                        "trigger"
                      ],
                      "type": "string",
                      "default": "action"
                    }
                  ]
                },
                "type": {
                  "title": "Type",
                  "description": "The unique type identifier of the option",
                  "type": "string"
                },
                "label": {
                  "title": "Label",
                  "description": "Display name of the option",
                  "type": "string"
                },
                "description": {
                  "title": "Description",
                  "description": "Description of the option",
                  "type": "string"
                },
                "input": {
                  "description": "The input entities for this option",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                },
                "output": {
                  "description": "The output entities for this option",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  },
                  "uniqueItems": true
                },
                "config_schema": {
                  "title": "Config Schema",
                  "description": "Configuration schema for the action",
                  "type": "array",
                  "items": {
                    "type": "object"
                  }
                },
                "prerequisites": {
                  "description": "list of entities required as prerequisites",
                  "type": "array",
                  "items": {
                    "title": "EntityType",
                    "description": "An enumeration.",
                    "enum": [
                      "finding",
                      "asset",
                      "channel_name",
                      "ticket_url"
                    ],
                    "type": "string"
                  }
                }
              },
              "required": [
                "type",
                "label",
                "description",
                "input",
                "output",
                "config_schema",
                "prerequisites"
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