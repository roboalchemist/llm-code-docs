# Source: https://docs.jit.io/reference/runs.md

# Get workflow runs

Retrieve workflow runs with pagination and the associated workflow

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
    "/workflows/{workflow_id}/runs": {
      "get": {
        "summary": "Get workflow runs",
        "description": "Retrieve workflow runs with pagination and the associated workflow\n\n**Requires the following permission:**\n`jit.workflows.read`\n\nThis feature is exclusive to premium users. To access it, upgrade to the Premium users pricing plan.",
        "operationId": "runs",
        "parameters": [
          {
            "name": "workflow_id",
            "in": "path",
            "description": "The ID of the workflow to retrieve runs for.",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/workflow_id"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "The maximum number of workflow runs to return. Must be positive and <= 100",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/limit-989ced22-7fc1-409d-904f-8475c2d493f0"
            }
          },
          {
            "name": "after",
            "in": "query",
            "description": "The token to start the next page of results.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/Workflowsafter"
            }
          },
          {
            "name": "workflow_version",
            "in": "query",
            "description": "The version of the workflow to fetch. If not provided, fetches the latest version.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/workflow_version"
            }
          }
        ],
        "tags": [
          "Workflows"
        ],
        "responses": {
          "200": {
            "description": "Workflow runs retrieved successfully with the associated workflow.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetWorkflowRunsResponse"
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
          "400": {
            "description": "Get Workflows Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetWorkflowsBadRequest"
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
          "404": {
            "description": "Workflow Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WorkflowNotFound"
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
      "GetWorkflowRunsResponse": {
        "title": "GetWorkflowRunsResponse",
        "type": "object",
        "properties": {
          "runs": {
            "title": "PaginatedResponse[WorkflowRunResponse]",
            "type": "object",
            "properties": {
              "metadata": {
                "title": "Metadata",
                "description": "Required fields to paginate over the response",
                "example": {
                  "limit": 5,
                  "count": 1,
                  "after": "CURSOR"
                },
                "allOf": [
                  {
                    "title": "PaginatedResponseMetadata",
                    "type": "object",
                    "properties": {
                      "limit": {
                        "title": "Results limit",
                        "description": "Maximum number of requested results.",
                        "example": 5,
                        "type": "integer"
                      },
                      "count": {
                        "title": "Number of results",
                        "description": "Number of results in the data field.",
                        "example": 3,
                        "type": "integer"
                      },
                      "after": {
                        "title": "Cursor",
                        "description": "Cursor for next request to get the results page. Null means no more results.",
                        "example": "CURSOR",
                        "type": "string"
                      }
                    },
                    "required": [
                      "limit",
                      "count"
                    ]
                  }
                ]
              },
              "data": {
                "title": "Data",
                "description": "List of JSONs holding the requested data.",
                "type": "array",
                "items": {
                  "title": "WorkflowRunResponse",
                  "type": "object",
                  "properties": {
                    "tenant_id": {
                      "title": "Tenant Id",
                      "type": "string"
                    },
                    "id": {
                      "title": "Id",
                      "type": "string"
                    },
                    "execution_name": {
                      "title": "Execution Name",
                      "type": "string"
                    },
                    "item_id": {
                      "title": "Item Id",
                      "type": "string"
                    },
                    "workflow_id": {
                      "title": "Workflow Id",
                      "type": "string"
                    },
                    "workflow_version": {
                      "title": "Workflow Version",
                      "type": "integer"
                    },
                    "status": {
                      "title": "Status",
                      "enum": [
                        "running",
                        "success",
                        "failure"
                      ],
                      "type": "string"
                    },
                    "started_at": {
                      "title": "Started At",
                      "type": "string"
                    },
                    "completed_at": {
                      "title": "Completed At",
                      "type": "string"
                    },
                    "workflow_steps": {
                      "title": "Workflow Steps",
                      "type": "object",
                      "additionalProperties": {
                        "title": "WorkflowStepResult",
                        "type": "object",
                        "properties": {
                          "status": {
                            "title": "Status",
                            "anyOf": [
                              {
                                "title": "ActionResultStatus",
                                "description": "An enumeration.",
                                "enum": [
                                  "success",
                                  "failure"
                                ],
                                "type": "string"
                              },
                              {
                                "title": "ConditionResultStatus",
                                "description": "An enumeration.",
                                "enum": [
                                  "passed",
                                  "skipped"
                                ],
                                "type": "string"
                              }
                            ]
                          },
                          "message": {
                            "title": "Message",
                            "type": "string"
                          }
                        },
                        "required": [
                          "status"
                        ]
                      }
                    }
                  },
                  "required": [
                    "tenant_id",
                    "id",
                    "execution_name",
                    "item_id",
                    "workflow_id",
                    "workflow_version",
                    "status",
                    "started_at",
                    "workflow_steps"
                  ]
                }
              }
            },
            "required": [
              "metadata",
              "data"
            ]
          },
          "workflow": {
            "title": "WorkflowApiResponse",
            "type": "object",
            "properties": {
              "id": {
                "title": "Id",
                "type": "string"
              },
              "name": {
                "title": "Name",
                "type": "string"
              },
              "description": {
                "title": "Description",
                "default": "",
                "type": "string"
              },
              "tenant_id": {
                "title": "Tenant Id",
                "type": "string"
              },
              "created_at": {
                "title": "Created At",
                "type": "string"
              },
              "updated_at": {
                "title": "Updated At",
                "type": "string"
              },
              "creator_user_id": {
                "title": "Creator User Id",
                "type": "string"
              },
              "creator_user_name": {
                "title": "Creator User Name",
                "type": "string"
              },
              "is_enabled": {
                "title": "Is Enabled",
                "type": "boolean"
              },
              "trigger": {
                "title": "Trigger",
                "type": "object",
                "properties": {
                  "step_type": {
                    "title": "Step Type",
                    "default": "trigger",
                    "enum": [
                      "trigger"
                    ],
                    "type": "string"
                  },
                  "id": {
                    "title": "Id",
                    "type": "string"
                  },
                  "name": {
                    "title": "Name",
                    "type": "string"
                  },
                  "next": {
                    "title": "Next",
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "type": {
                    "title": "Type",
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "name",
                  "next",
                  "type"
                ]
              },
              "steps": {
                "title": "Steps",
                "type": "array",
                "items": {
                  "discriminator": {
                    "propertyName": "step_type",
                    "mapping": {
                      "action": "#/definitions/ActionStep",
                      "condition": "#/definitions/ConditionStep"
                    }
                  },
                  "oneOf": [
                    {
                      "title": "ActionStep",
                      "type": "object",
                      "properties": {
                        "step_type": {
                          "title": "Step Type",
                          "default": "action",
                          "enum": [
                            "action"
                          ],
                          "type": "string"
                        },
                        "id": {
                          "title": "Id",
                          "type": "string"
                        },
                        "name": {
                          "title": "Name",
                          "type": "string"
                        },
                        "next": {
                          "title": "Next",
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "type": {
                          "title": "Type",
                          "type": "string"
                        },
                        "config": {
                          "title": "Config",
                          "type": "object"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "next",
                        "type",
                        "config"
                      ]
                    },
                    {
                      "title": "ConditionStep",
                      "type": "object",
                      "properties": {
                        "step_type": {
                          "title": "Step Type",
                          "default": "condition",
                          "enum": [
                            "condition"
                          ],
                          "type": "string"
                        },
                        "id": {
                          "title": "Id",
                          "type": "string"
                        },
                        "name": {
                          "title": "Name",
                          "type": "string"
                        },
                        "next": {
                          "title": "Next",
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "type": {
                          "title": "Type",
                          "type": "string"
                        },
                        "config": {
                          "title": "Config",
                          "type": "object"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "next",
                        "type",
                        "config"
                      ]
                    }
                  ]
                }
              },
              "version": {
                "title": "Version",
                "type": "integer"
              },
              "last_run_at": {
                "title": "Last Run At",
                "type": "string"
              },
              "last_run_status": {
                "title": "Last Run Status",
                "enum": [
                  "running",
                  "success",
                  "failure"
                ],
                "type": "string"
              }
            },
            "required": [
              "id",
              "name",
              "tenant_id",
              "created_at",
              "updated_at",
              "creator_user_id",
              "creator_user_name",
              "is_enabled",
              "trigger",
              "steps",
              "version"
            ]
          }
        },
        "required": [
          "runs",
          "workflow"
        ]
      },
      "GetWorkflowsBadRequest": {
        "title": "GetWorkflowsBadRequestErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "BAD_REQUEST",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error description.",
            "example": "Limit must be greater than 0",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "WorkflowNotFound": {
        "title": "WorkflowNotFoundErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "WORKFLOW_NOT_FOUND",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error description.",
            "example": "Workflow not found.",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "Workflowsafter": {
        "example": "eyJ0b2tlbi",
        "title": "After",
        "type": "string"
      },
      "workflow_id": {
        "title": "Workflow ID",
        "type": "string"
      },
      "limit-989ced22-7fc1-409d-904f-8475c2d493f0": {
        "default": 20,
        "example": 20,
        "maximum": 100,
        "minimum": 1,
        "title": "Limit",
        "type": "integer"
      },
      "workflow_version": {
        "example": 1,
        "title": "Workflow Version",
        "type": "integer"
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