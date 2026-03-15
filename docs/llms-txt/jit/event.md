# Source: https://docs.jit.io/reference/event.md

# Trigger synchronous execution.

Trigger synchronous execution for local environments. This endpoint can be used to trigger executions initiated by our controls CLI or by users in their local environments.

**Requires the following permission:**
`jit.trigger.write`

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
      "name": "Executions",
      "description": "Executions management endpoints"
    }
  ],
  "paths": {
    "/trigger/sync_event": {
      "post": {
        "summary": "Trigger synchronous execution.",
        "description": "Trigger synchronous execution for local environments. This endpoint can be used to trigger executions initiated by our controls CLI or by users in their local environments.\n\n**Requires the following permission:**\n`jit.trigger.write`",
        "operationId": "event",
        "parameters": [],
        "tags": [
          "Executions"
        ],
        "requestBody": {
          "description": "The fields describing the synchronous execution request.",
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TriggerSyncEventRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Synchronous execution response with download link",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SyncExecutionResponse"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin-6ee369c9-118c-44b2-85a3-df221c4db09c"
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
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin-417f96a2-f643-4c6b-a929-687197c07ef4"
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
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin-d790d85f-35ac-4ba5-87bc-09c6eff36a06"
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
          "422": {
            "description": "Unprocessable Entity",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TriggerUnprocessableEntity"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin-0bb23a04-26b8-411b-8ca6-e8cee4acf8c7"
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
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin-50c3f722-d7b0-4a53-b8ed-b0745bde3812"
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
      "Access-Control-Allow-Credentials": {
        "type": "boolean",
        "default": true
      },
      "SyncExecutionResponse": {
        "title": "DispatchEventWithDownloadLink",
        "type": "object",
        "properties": {
          "dispatch_execution_event": {
            "title": "Dispatch Execution Event",
            "description": "The dispatch execution event details containing execution metadata",
            "allOf": [
              {
                "title": "DispatchExecutionEvent",
                "type": "object",
                "properties": {
                  "context": {
                    "title": "ExecutionContext",
                    "description": "The context of the execution. Basically things that are needed for the execution.\nThe attributes added here might be change between the trigger to the actual execution.",
                    "type": "object",
                    "properties": {
                      "jit_event": {
                        "title": "Jit Event",
                        "anyOf": [
                          {
                            "title": "OpenPRJitEvent",
                            "description": "This class represents JitEvent of Open Fix PR by Jit on the users repo",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "centralized_repo_asset_id": {
                                "title": "Centralized Repo Asset Id",
                                "type": "string"
                              },
                              "centralized_repo_asset_name": {
                                "title": "Centralized Repo Asset Name",
                                "type": "string"
                              },
                              "centralized_repo_files_location": {
                                "title": "Centralized Repo Files Location",
                                "type": "string"
                              },
                              "ci_workflow_files_path": {
                                "title": "Ci Workflow Files Path",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "finding_id": {
                                "title": "Finding Id",
                                "type": "string"
                              },
                              "action_id": {
                                "title": "Action Id",
                                "type": "string"
                              },
                              "fix_suggestion": {
                                "title": "Fix Suggestion",
                                "type": "object"
                              },
                              "app_id": {
                                "title": "App Id",
                                "type": "string"
                              },
                              "installation_id": {
                                "title": "Installation Id",
                                "type": "string"
                              },
                              "owner": {
                                "title": "Owner",
                                "type": "string"
                              },
                              "original_repository": {
                                "title": "Original Repository",
                                "type": "string"
                              },
                              "defined_backlog_branches": {
                                "title": "Defined Backlog Branches",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "finding_id",
                              "fix_suggestion",
                              "app_id",
                              "installation_id",
                              "owner",
                              "original_repository"
                            ]
                          },
                          {
                            "title": "ManualExecutionJitEvent",
                            "description": "This is a special case of JitEvent that is used to trigger a manual execution of a JitEvent.\nWe don't need to specify a branch in case of code plan item, the system will default to the default branch.\nUsers must provide a plan item & list of asset ids to execute the JitEvent on.",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "asset_ids_filter": {
                                "title": "Asset Ids Filter",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "plan_item_slug": {
                                "title": "Plan Item Slug",
                                "type": "string"
                              },
                              "priority": {
                                "title": "ExecutionPriority",
                                "description": "An enumeration.",
                                "enum": [
                                  1,
                                  3
                                ],
                                "type": "integer"
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "asset_ids_filter",
                              "plan_item_slug"
                            ]
                          },
                          {
                            "title": "ResourceAddedJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "created_asset_ids": {
                                "title": "Created Asset Ids",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                },
                                "uniqueItems": true
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "created_asset_ids"
                            ]
                          },
                          {
                            "title": "ItemActivatedJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "activated_plan_slug": {
                                "title": "Activated Plan Slug",
                                "type": "string"
                              },
                              "activated_plan_item_slugs": {
                                "title": "Activated Plan Item Slugs",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                },
                                "uniqueItems": true
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "activated_plan_slug",
                              "activated_plan_item_slugs"
                            ]
                          },
                          {
                            "title": "DeploymentJitEvent",
                            "type": "object",
                            "properties": {
                              "app_id": {
                                "title": "App Id",
                                "type": "string"
                              },
                              "installation_id": {
                                "title": "Installation Id",
                                "type": "string"
                              },
                              "deployment_id": {
                                "title": "Deployment Id",
                                "type": "string"
                              },
                              "environment": {
                                "title": "Environment",
                                "type": "string"
                              },
                              "vendor": {
                                "title": "Vendor",
                                "type": "string"
                              },
                              "owner": {
                                "title": "Owner",
                                "type": "string"
                              },
                              "original_repository": {
                                "title": "Original Repository",
                                "type": "string"
                              },
                              "sender": {
                                "title": "DeploymentSender",
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "title": "Id",
                                    "type": "string"
                                  },
                                  "login": {
                                    "title": "Login",
                                    "type": "string"
                                  },
                                  "avatar_url": {
                                    "title": "Avatar Url",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "id",
                                  "login"
                                ]
                              },
                              "branch_name": {
                                "title": "Branch Name",
                                "type": "string"
                              },
                              "commit_sha": {
                                "title": "Commit Sha",
                                "type": "string"
                              },
                              "created_at": {
                                "title": "Created At",
                                "type": "string"
                              },
                              "user_vendor_id": {
                                "title": "User Vendor Id",
                                "type": "string"
                              },
                              "user_vendor_name": {
                                "title": "User Vendor Name",
                                "type": "string"
                              },
                              "deployment_type": {
                                "allOf": [
                                  {
                                    "title": "JitDeploymentType",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "non_production",
                                      "production"
                                    ],
                                    "type": "string",
                                    "default": "non_production"
                                  }
                                ]
                              },
                              "deployment_action": {
                                "title": "DeploymentAction",
                                "type": "object",
                                "properties": {
                                  "name": {
                                    "title": "Name",
                                    "type": "string"
                                  },
                                  "status": {
                                    "title": "Status",
                                    "type": "string"
                                  },
                                  "conclusion": {
                                    "title": "Conclusion",
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
                                  "url": {
                                    "title": "Url",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "name",
                                  "status",
                                  "url"
                                ]
                              },
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "DEPLOYMENT_WORKFLOW_TRIGGER": {
                                "title": "Deployment Workflow Trigger",
                                "default": "deployment",
                                "type": "string"
                              }
                            },
                            "required": [
                              "app_id",
                              "installation_id",
                              "deployment_id",
                              "environment",
                              "vendor",
                              "owner",
                              "original_repository",
                              "sender",
                              "branch_name",
                              "commit_sha",
                              "created_at",
                              "tenant_id",
                              "jit_event_id"
                            ]
                          },
                          {
                            "title": "ManualBranchScanJitEvent",
                            "description": "Event for manually triggering a scan for a specific branch of a repository.\nAll findings from this scan are considered backlog findings.",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "centralized_repo_asset_id": {
                                "title": "Centralized Repo Asset Id",
                                "type": "string"
                              },
                              "centralized_repo_asset_name": {
                                "title": "Centralized Repo Asset Name",
                                "type": "string"
                              },
                              "centralized_repo_files_location": {
                                "title": "Centralized Repo Files Location",
                                "type": "string"
                              },
                              "ci_workflow_files_path": {
                                "title": "Ci Workflow Files Path",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "app_id": {
                                "title": "App Id",
                                "type": "string"
                              },
                              "installation_id": {
                                "title": "Installation Id",
                                "type": "string"
                              },
                              "original_repository": {
                                "title": "Original Repository",
                                "default": "",
                                "type": "string"
                              },
                              "vendor": {
                                "title": "Vendor",
                                "type": "string"
                              },
                              "owner": {
                                "title": "Owner",
                                "type": "string"
                              },
                              "branch": {
                                "title": "Branch",
                                "type": "string"
                              },
                              "pull_request_number": {
                                "title": "Pull Request Number",
                                "type": "string"
                              },
                              "pull_request_title": {
                                "title": "Pull Request Title",
                                "type": "string"
                              },
                              "commits": {
                                "title": "Commits",
                                "type": "object",
                                "properties": {
                                  "base_sha": {
                                    "title": "Base Sha",
                                    "type": "string"
                                  },
                                  "head_sha": {
                                    "title": "Head Sha",
                                    "type": "string"
                                  },
                                  "last_pr_commit_head_sha": {
                                    "title": "Last Pr Commit Head Sha",
                                    "type": "string"
                                  }
                                }
                              },
                              "user_vendor_id": {
                                "title": "User Vendor Id",
                                "type": "string"
                              },
                              "user_vendor_name": {
                                "title": "User Vendor Name",
                                "type": "string"
                              },
                              "languages": {
                                "title": "Languages",
                                "default": [],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "is_backlog": {
                                "title": "Is Backlog",
                                "type": "boolean"
                              },
                              "asset_ids_filter": {
                                "title": "Asset Ids Filter",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "vendor",
                              "branch",
                              "commits",
                              "is_backlog"
                            ]
                          },
                          {
                            "title": "PullRequestWebhookEvent",
                            "description": "This Event used for the PR translators from the SCM.",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "title": "JitEventName",
                                "description": "An enumeration.",
                                "enum": [
                                  "full_scan",
                                  "pull_request_created",
                                  "pull_request_updated",
                                  "open_fix_pull_request",
                                  "merge_default_branch",
                                  "register_scheduled_tasks",
                                  "unregister_scheduled_tasks",
                                  "trigger_scheduled_task",
                                  "non_production_deployment",
                                  "production_deployment",
                                  "item_activated",
                                  "resource_added",
                                  "manual_execution",
                                  "jit_branch_changed",
                                  "sync",
                                  "manual_branch_scan"
                                ],
                                "type": "string",
                                "default": "jit_branch_changed"
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "centralized_repo_asset_id": {
                                "title": "Centralized Repo Asset Id",
                                "type": "string"
                              },
                              "centralized_repo_asset_name": {
                                "title": "Centralized Repo Asset Name",
                                "type": "string"
                              },
                              "centralized_repo_files_location": {
                                "title": "Centralized Repo Files Location",
                                "type": "string"
                              },
                              "ci_workflow_files_path": {
                                "title": "Ci Workflow Files Path",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "app_id": {
                                "title": "App Id",
                                "type": "string"
                              },
                              "installation_id": {
                                "title": "Installation Id",
                                "type": "string"
                              },
                              "original_repository": {
                                "title": "Original Repository",
                                "type": "string"
                              },
                              "vendor": {
                                "title": "Vendor",
                                "type": "string"
                              },
                              "owner": {
                                "title": "Owner",
                                "type": "string"
                              },
                              "branch": {
                                "title": "Branch",
                                "type": "string"
                              },
                              "pull_request_number": {
                                "title": "Pull Request Number",
                                "type": "string"
                              },
                              "pull_request_title": {
                                "title": "Pull Request Title",
                                "type": "string"
                              },
                              "commits": {
                                "title": "Commits",
                                "type": "object",
                                "properties": {
                                  "base_sha": {
                                    "title": "Base Sha",
                                    "type": "string"
                                  },
                                  "head_sha": {
                                    "title": "Head Sha",
                                    "type": "string"
                                  },
                                  "last_pr_commit_head_sha": {
                                    "title": "Last Pr Commit Head Sha",
                                    "type": "string"
                                  }
                                }
                              },
                              "user_vendor_id": {
                                "title": "User Vendor Id",
                                "type": "string"
                              },
                              "user_vendor_name": {
                                "title": "User Vendor Name",
                                "type": "string"
                              },
                              "languages": {
                                "title": "Languages",
                                "default": [],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "url": {
                                "title": "Url",
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
                              "user_vendor_avatar_url": {
                                "title": "User Vendor Avatar Url",
                                "type": "string"
                              },
                              "source_branch": {
                                "title": "Source Branch",
                                "type": "string"
                              },
                              "commits_url": {
                                "title": "Commits Url",
                                "type": "string"
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_name",
                              "jit_event_id",
                              "original_repository",
                              "vendor",
                              "commits",
                              "url",
                              "created_at",
                              "updated_at",
                              "user_vendor_avatar_url",
                              "source_branch"
                            ]
                          },
                          {
                            "title": "CodeRelatedJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "title": "JitEventName",
                                "description": "An enumeration.",
                                "enum": [
                                  "full_scan",
                                  "pull_request_created",
                                  "pull_request_updated",
                                  "open_fix_pull_request",
                                  "merge_default_branch",
                                  "register_scheduled_tasks",
                                  "unregister_scheduled_tasks",
                                  "trigger_scheduled_task",
                                  "non_production_deployment",
                                  "production_deployment",
                                  "item_activated",
                                  "resource_added",
                                  "manual_execution",
                                  "jit_branch_changed",
                                  "sync",
                                  "manual_branch_scan"
                                ],
                                "type": "string",
                                "default": "jit_branch_changed"
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "centralized_repo_asset_id": {
                                "title": "Centralized Repo Asset Id",
                                "type": "string"
                              },
                              "centralized_repo_asset_name": {
                                "title": "Centralized Repo Asset Name",
                                "type": "string"
                              },
                              "centralized_repo_files_location": {
                                "title": "Centralized Repo Files Location",
                                "type": "string"
                              },
                              "ci_workflow_files_path": {
                                "title": "Ci Workflow Files Path",
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "app_id": {
                                "title": "App Id",
                                "type": "string"
                              },
                              "installation_id": {
                                "title": "Installation Id",
                                "type": "string"
                              },
                              "original_repository": {
                                "title": "Original Repository",
                                "type": "string"
                              },
                              "vendor": {
                                "title": "Vendor",
                                "type": "string"
                              },
                              "owner": {
                                "title": "Owner",
                                "type": "string"
                              },
                              "branch": {
                                "title": "Branch",
                                "type": "string"
                              },
                              "pull_request_number": {
                                "title": "Pull Request Number",
                                "type": "string"
                              },
                              "pull_request_title": {
                                "title": "Pull Request Title",
                                "type": "string"
                              },
                              "commits": {
                                "title": "Commits",
                                "type": "object",
                                "properties": {
                                  "base_sha": {
                                    "title": "Base Sha",
                                    "type": "string"
                                  },
                                  "head_sha": {
                                    "title": "Head Sha",
                                    "type": "string"
                                  },
                                  "last_pr_commit_head_sha": {
                                    "title": "Last Pr Commit Head Sha",
                                    "type": "string"
                                  }
                                }
                              },
                              "user_vendor_id": {
                                "title": "User Vendor Id",
                                "type": "string"
                              },
                              "user_vendor_name": {
                                "title": "User Vendor Name",
                                "type": "string"
                              },
                              "languages": {
                                "title": "Languages",
                                "default": [],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_name",
                              "jit_event_id",
                              "original_repository",
                              "vendor",
                              "commits"
                            ]
                          },
                          {
                            "title": "RegisterScheduledTasksJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "tasks": {
                                "title": "Tasks",
                                "type": "array",
                                "items": {
                                  "title": "ScheduledTask",
                                  "type": "object",
                                  "properties": {
                                    "tenant_id": {
                                      "title": "Tenant Id",
                                      "type": "string"
                                    },
                                    "task_id": {
                                      "title": "Task Id",
                                      "type": "string"
                                    },
                                    "workflow_name": {
                                      "title": "Workflow Name",
                                      "type": "string"
                                    },
                                    "workflow_slug": {
                                      "title": "Workflow Slug",
                                      "type": "string"
                                    },
                                    "plan_item_slug": {
                                      "title": "Plan Item Slug",
                                      "type": "string"
                                    },
                                    "plan_item_slugs": {
                                      "title": "Plan Item Slugs",
                                      "default": [],
                                      "type": "array",
                                      "items": {
                                        "type": "string"
                                      }
                                    },
                                    "plan_item_template_slug": {
                                      "title": "Plan Item Template Slug",
                                      "type": "string"
                                    },
                                    "plan_item_template_name": {
                                      "title": "Plan Item Template Name",
                                      "type": "string"
                                    },
                                    "cron_expression": {
                                      "title": "Cron Expression",
                                      "type": "string"
                                    },
                                    "single_execution_time": {
                                      "title": "Single Execution Time",
                                      "type": "string",
                                      "format": "date-time"
                                    }
                                  },
                                  "required": [
                                    "tenant_id",
                                    "workflow_name",
                                    "workflow_slug",
                                    "plan_item_slug",
                                    "plan_item_template_slug",
                                    "plan_item_template_name"
                                  ]
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "tasks"
                            ]
                          },
                          {
                            "title": "UnregisterScheduledTasksJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "tasks": {
                                "title": "Tasks",
                                "type": "array",
                                "items": {
                                  "title": "ScheduledTask",
                                  "type": "object",
                                  "properties": {
                                    "tenant_id": {
                                      "title": "Tenant Id",
                                      "type": "string"
                                    },
                                    "task_id": {
                                      "title": "Task Id",
                                      "type": "string"
                                    },
                                    "workflow_name": {
                                      "title": "Workflow Name",
                                      "type": "string"
                                    },
                                    "workflow_slug": {
                                      "title": "Workflow Slug",
                                      "type": "string"
                                    },
                                    "plan_item_slug": {
                                      "title": "Plan Item Slug",
                                      "type": "string"
                                    },
                                    "plan_item_slugs": {
                                      "title": "Plan Item Slugs",
                                      "default": [],
                                      "type": "array",
                                      "items": {
                                        "type": "string"
                                      }
                                    },
                                    "plan_item_template_slug": {
                                      "title": "Plan Item Template Slug",
                                      "type": "string"
                                    },
                                    "plan_item_template_name": {
                                      "title": "Plan Item Template Name",
                                      "type": "string"
                                    },
                                    "cron_expression": {
                                      "title": "Cron Expression",
                                      "type": "string"
                                    },
                                    "single_execution_time": {
                                      "title": "Single Execution Time",
                                      "type": "string",
                                      "format": "date-time"
                                    }
                                  },
                                  "required": [
                                    "tenant_id",
                                    "workflow_name",
                                    "workflow_slug",
                                    "plan_item_slug",
                                    "plan_item_template_slug",
                                    "plan_item_template_name"
                                  ]
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "tasks"
                            ]
                          },
                          {
                            "title": "TriggerScheduledTaskJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "task_id": {
                                "title": "Task Id",
                                "type": "string"
                              },
                              "workflow_name": {
                                "title": "Workflow Name",
                                "type": "string"
                              },
                              "workflow_slug": {
                                "title": "Workflow Slug",
                                "type": "string"
                              },
                              "plan_item_slug": {
                                "title": "Plan Item Slug",
                                "type": "string"
                              },
                              "plan_item_slugs": {
                                "title": "Plan Item Slugs",
                                "default": [],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "plan_item_template_slug": {
                                "title": "Plan Item Template Slug",
                                "type": "string"
                              },
                              "plan_item_template_name": {
                                "title": "Plan Item Template Name",
                                "type": "string"
                              },
                              "cron_expression": {
                                "title": "Cron Expression",
                                "type": "string"
                              },
                              "single_execution_time": {
                                "title": "Single Execution Time",
                                "type": "string",
                                "format": "date-time"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "workflow_name",
                              "workflow_slug",
                              "plan_item_slug",
                              "plan_item_template_slug",
                              "plan_item_template_name",
                              "jit_event_id"
                            ]
                          },
                          {
                            "title": "SynchronousJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              },
                              "plan_item_slug": {
                                "title": "Plan Item Slug",
                                "type": "string"
                              },
                              "is_backlog": {
                                "title": "Is Backlog",
                                "type": "boolean"
                              },
                              "dispatch_args": {
                                "title": "Dispatch Args",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "string"
                                }
                              },
                              "os": {
                                "title": "OsTypes",
                                "description": "Enumeration of supported operating system distribution types.",
                                "enum": [
                                  "slim",
                                  "alpine"
                                ],
                                "type": "string"
                              },
                              "arch": {
                                "title": "ArchTypes",
                                "description": "Enumeration of supported architecture types.",
                                "enum": [
                                  "amd64",
                                  "arm64"
                                ],
                                "type": "string"
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id",
                              "asset_id",
                              "plan_item_slug",
                              "is_backlog",
                              "dispatch_args",
                              "os",
                              "arch"
                            ]
                          },
                          {
                            "title": "JitBranchChangedJitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "allOf": [
                                  {
                                    "title": "JitEventName",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "full_scan",
                                      "pull_request_created",
                                      "pull_request_updated",
                                      "open_fix_pull_request",
                                      "merge_default_branch",
                                      "register_scheduled_tasks",
                                      "unregister_scheduled_tasks",
                                      "trigger_scheduled_task",
                                      "non_production_deployment",
                                      "production_deployment",
                                      "item_activated",
                                      "resource_added",
                                      "manual_execution",
                                      "jit_branch_changed",
                                      "sync",
                                      "manual_branch_scan"
                                    ],
                                    "type": "string",
                                    "default": "jit_branch_changed"
                                  }
                                ]
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_id"
                            ]
                          },
                          {
                            "title": "JitEvent",
                            "type": "object",
                            "properties": {
                              "tenant_id": {
                                "title": "Tenant Id",
                                "type": "string"
                              },
                              "jit_event_name": {
                                "title": "JitEventName",
                                "description": "An enumeration.",
                                "enum": [
                                  "full_scan",
                                  "pull_request_created",
                                  "pull_request_updated",
                                  "open_fix_pull_request",
                                  "merge_default_branch",
                                  "register_scheduled_tasks",
                                  "unregister_scheduled_tasks",
                                  "trigger_scheduled_task",
                                  "non_production_deployment",
                                  "production_deployment",
                                  "item_activated",
                                  "resource_added",
                                  "manual_execution",
                                  "jit_branch_changed",
                                  "sync",
                                  "manual_branch_scan"
                                ],
                                "type": "string",
                                "default": "jit_branch_changed"
                              },
                              "jit_event_id": {
                                "title": "Jit Event Id",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset Id",
                                "type": "string"
                              },
                              "workflows": {
                                "title": "Workflows",
                                "type": "object",
                                "additionalProperties": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              }
                            },
                            "required": [
                              "tenant_id",
                              "jit_event_name",
                              "jit_event_id"
                            ]
                          }
                        ]
                      },
                      "installation_id": {
                        "title": "Installation Id",
                        "type": "string"
                      },
                      "owner": {
                        "title": "Owner",
                        "type": "string"
                      },
                      "asset_id": {
                        "title": "Asset Id",
                        "type": "string"
                      },
                      "asset_name": {
                        "title": "Asset Name",
                        "type": "string"
                      },
                      "asset_type": {
                        "title": "Asset Type",
                        "type": "string"
                      },
                      "vendor": {
                        "title": "Vendor",
                        "type": "string"
                      },
                      "job": {
                        "title": "WorkflowJob",
                        "type": "object",
                        "properties": {
                          "runner": {
                            "title": "RunnerConfig",
                            "type": "object",
                            "properties": {
                              "type": {
                                "title": "Runner",
                                "description": "An enumeration.",
                                "enum": [
                                  "jit",
                                  "ci",
                                  "sync"
                                ],
                                "type": "string"
                              },
                              "setup": {
                                "title": "RunnerSetup",
                                "type": "object",
                                "properties": {
                                  "mount": {
                                    "title": "Mount",
                                    "type": "boolean"
                                  },
                                  "checkout": {
                                    "title": "Checkout",
                                    "type": "boolean"
                                  },
                                  "assume_role": {
                                    "title": "Assume Role",
                                    "type": "boolean"
                                  },
                                  "account_id": {
                                    "title": "Account Id",
                                    "type": "string"
                                  },
                                  "auth_type": {
                                    "title": "AuthType",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "no_auth",
                                      "aws_iam_role",
                                      "scm_token",
                                      "integrations"
                                    ],
                                    "type": "string"
                                  },
                                  "timeout_minutes": {
                                    "title": "Timeout Minutes",
                                    "type": "integer"
                                  },
                                  "extended_clone": {
                                    "title": "Extended Clone",
                                    "type": "boolean"
                                  }
                                }
                              }
                            },
                            "required": [
                              "type"
                            ]
                          },
                          "job_name": {
                            "title": "Job Name",
                            "type": "string"
                          },
                          "condition": {
                            "title": "Condition",
                            "type": "object",
                            "additionalProperties": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            }
                          },
                          "integrations": {
                            "title": "Integrations",
                            "type": "array",
                            "items": {
                              "title": "JobIntegration",
                              "type": "object",
                              "properties": {
                                "name": {
                                  "title": "Name",
                                  "type": "string"
                                },
                                "required": {
                                  "title": "Required",
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "name",
                                "required"
                              ]
                            }
                          },
                          "steps": {
                            "title": "Steps",
                            "type": "array",
                            "items": {
                              "title": "Step",
                              "type": "object",
                              "properties": {
                                "name": {
                                  "title": "Name",
                                  "type": "string"
                                },
                                "uses": {
                                  "title": "Uses",
                                  "type": "string"
                                },
                                "executable": {
                                  "title": "Executable",
                                  "type": "string"
                                },
                                "params": {
                                  "title": "Params",
                                  "default": {},
                                  "type": "object"
                                }
                              },
                              "required": [
                                "name",
                                "uses"
                              ]
                            }
                          }
                        },
                        "required": [
                          "runner",
                          "job_name",
                          "steps"
                        ]
                      },
                      "workflow": {
                        "title": "ExecutionContextWorkflow",
                        "description": "This is the model without the parsed content\nparsed_content and content violates the DRY principle and create drifts in our backend\nHowever, we need to keep the parsed content in the plan-service for the UI",
                        "type": "object",
                        "properties": {
                          "slug": {
                            "title": "Slug",
                            "type": "string"
                          },
                          "name": {
                            "title": "Name",
                            "type": "string"
                          },
                          "type": {
                            "allOf": [
                              {
                                "title": "TemplateType",
                                "description": "An enumeration.",
                                "enum": [
                                  "plan",
                                  "workflow",
                                  "plan_item"
                                ],
                                "type": "string",
                                "default": "workflow"
                              }
                            ]
                          },
                          "default": {
                            "title": "Default",
                            "type": "boolean"
                          },
                          "content": {
                            "title": "Content",
                            "type": "string"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "default": [],
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "params": {
                            "title": "Params",
                            "type": "object"
                          },
                          "plan_item_template_slug": {
                            "title": "Plan Item Template Slug",
                            "type": "string"
                          },
                          "asset_types": {
                            "title": "Asset Types",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "workflow_type": {
                            "title": "Workflow Type",
                            "type": "string"
                          }
                        },
                        "required": [
                          "slug",
                          "name"
                        ]
                      },
                      "enrichment_result": {
                        "title": "RepoEnrichmentResult",
                        "type": "object",
                        "properties": {
                          "mime_types": {
                            "title": "Mime Types",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "languages": {
                            "title": "Languages",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "frameworks": {
                            "title": "Frameworks",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "package_managers": {
                            "title": "Package Managers",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "content_size": {
                            "title": "ContentSize",
                            "description": "T-shirt size for the repository content.\nThis is used to determine the size of the repository content.",
                            "enum": [
                              "x-small",
                              "small",
                              "medium",
                              "large",
                              "x-large"
                            ],
                            "type": "string"
                          },
                          "dependency_size": {
                            "title": "ContentSize",
                            "description": "T-shirt size for the repository content.\nThis is used to determine the size of the repository content.",
                            "enum": [
                              "x-small",
                              "small",
                              "medium",
                              "large",
                              "x-large"
                            ],
                            "type": "string"
                          }
                        },
                        "required": [
                          "mime_types",
                          "languages",
                          "frameworks",
                          "package_managers"
                        ]
                      },
                      "is_temp_asset_created": {
                        "title": "Is Temp Asset Created",
                        "default": false,
                        "type": "boolean"
                      },
                      "auth": {
                        "title": "Auth",
                        "type": "object",
                        "properties": {
                          "type": {
                            "title": "AuthType",
                            "description": "An enumeration.",
                            "enum": [
                              "no_auth",
                              "aws_iam_role",
                              "scm_token",
                              "integrations"
                            ],
                            "type": "string"
                          },
                          "config": {
                            "title": "Config",
                            "type": "object",
                            "additionalProperties": {
                              "type": "string"
                            }
                          }
                        },
                        "required": [
                          "type",
                          "config"
                        ]
                      },
                      "asset": {
                        "title": "Asset",
                        "type": "object",
                        "properties": {
                          "aws_account_id": {
                            "title": "AWS Account ID",
                            "description": "The AWS account ID of the asset.",
                            "example": "123456789012",
                            "type": "string"
                          },
                          "aws_stack_arn": {
                            "title": "AWS Stack ARN",
                            "description": "The Amazon Resource Name (ARN) of the AWS CloudFormation stack.",
                            "example": "arn:aws:cloudformation:us-east-1:123456789012:stack/stack-name/guid",
                            "type": "string"
                          },
                          "aws_jit_role_name": {
                            "title": "AWS JIT Role Name",
                            "description": "The name of the jit role in AWS",
                            "example": "jit-role",
                            "type": "string"
                          },
                          "aws_regions_to_scan": {
                            "title": "AWS Regions to Scan",
                            "description": "The AWS regions to scan.",
                            "example": [
                              "us-east-1",
                              "us-west-2"
                            ],
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "aws_jit_role_external_id": {
                            "title": "Aws Jit Role External Id",
                            "type": "string"
                          },
                          "account_id": {
                            "title": "Account ID",
                            "description": "The account ID of the asset.",
                            "example": "123456789012",
                            "type": "string"
                          },
                          "target_url": {
                            "title": "Target URL",
                            "description": "The target URL for ZAP scanning.",
                            "example": "https://example.com",
                            "type": "string"
                          },
                          "exclude_paths": {
                            "title": "Exclude Paths",
                            "description": "Paths to exclude from ZAP scanning.",
                            "example": [
                              "/api/health",
                              "/api/status"
                            ],
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "authentication_mode": {
                            "title": "Authentication Mode",
                            "description": "The authentication mode to be used for ZAP scanning.",
                            "example": "formBasedAuthentication",
                            "type": "string"
                          },
                          "authentication_key": {
                            "title": "Authentication Key",
                            "description": "The key used for authentication in ZAP scanning.",
                            "example": "authKey123",
                            "type": "string"
                          },
                          "authentication_value": {
                            "title": "Authentication Value",
                            "description": "The value used for authentication in ZAP scanning.",
                            "example": "secretValue",
                            "type": "string"
                          },
                          "auth_header_name": {
                            "title": "Auth Header Name",
                            "description": "The name of the authentication header used in ZAP scanning.",
                            "example": "Authorization",
                            "type": "string"
                          },
                          "auth_header_value": {
                            "title": "Auth Header Value",
                            "description": "The value of the authentication header used in ZAP scanning.",
                            "example": "Bearer token",
                            "type": "string"
                          },
                          "login_page_url": {
                            "title": "Login Page URL",
                            "description": "The URL of the login page for authentication in ZAP scanning.",
                            "example": "https://example.com/login",
                            "type": "string"
                          },
                          "username": {
                            "title": "Username",
                            "description": "The username used for authentication in ZAP scanning.",
                            "example": "admin",
                            "type": "string"
                          },
                          "username_css_selector": {
                            "title": "Username CSS Selector",
                            "description": "The CSS selector used to locate the username field on the login page.",
                            "example": "#username",
                            "type": "string"
                          },
                          "password": {
                            "title": "Password",
                            "description": "The password used for authentication in ZAP scanning.",
                            "example": "secretPassword",
                            "type": "string"
                          },
                          "password_ref": {
                            "title": "Password Reference",
                            "description": "A reference to the password, used for authentication in ZAP scanning.",
                            "example": "passwordRef123",
                            "type": "string"
                          },
                          "password_css_selector": {
                            "title": "Password CSS Selector",
                            "description": "The CSS selector used to locate the password field on the login page.",
                            "example": "#password",
                            "type": "string"
                          },
                          "api_domain": {
                            "title": "API Domain",
                            "description": "The domain of the API to be scanned by ZAP.",
                            "example": "api.example.com",
                            "type": "string"
                          },
                          "external_id": {
                            "title": "External ID",
                            "description": "The external ID of the asset.",
                            "example": "12345678901234567890123456789012",
                            "type": "string"
                          },
                          "asset_id": {
                            "title": "Asset ID",
                            "description": "The unique identifier for the asset.",
                            "example": "727395ab-4cac-4216-998d-7f212c2cf389",
                            "type": "string"
                          },
                          "tenant_id": {
                            "title": "Tenant ID",
                            "description": "The tenant's unique identifier.",
                            "example": "f8c2f72c-4fc3-4048-a885-6c0208777644",
                            "type": "string"
                          },
                          "asset_type": {
                            "title": "Asset Type",
                            "description": "The type of the asset.",
                            "example": "repo",
                            "enum": [
                              "repo",
                              "org",
                              "aws_account",
                              "gcp_account",
                              "azure_account",
                              "web",
                              "api",
                              "image",
                              "external_integ"
                            ],
                            "type": "string"
                          },
                          "vendor": {
                            "title": "Vendor",
                            "description": "The vendor associated with the asset.",
                            "example": "github",
                            "type": "string"
                          },
                          "owner": {
                            "title": "Owner",
                            "description": "The owner of the asset.",
                            "example": "owner",
                            "type": "string"
                          },
                          "asset_name": {
                            "title": "Asset Name",
                            "description": "The name of the asset.",
                            "example": "asset-name",
                            "type": "string"
                          },
                          "asset_display_name": {
                            "title": "Asset Display Name",
                            "description": "The display name of the asset.",
                            "example": "asset-name",
                            "type": "string"
                          },
                          "is_active": {
                            "title": "Is Active",
                            "description": "Indicates whether the asset is active.",
                            "example": true,
                            "type": "boolean"
                          },
                          "is_covered": {
                            "title": "Is Covered",
                            "description": "Indicates whether the asset is covered.",
                            "default": true,
                            "example": true,
                            "type": "boolean"
                          },
                          "is_archived": {
                            "title": "Is Archived",
                            "description": "Indicates whether the asset is archived.",
                            "example": false,
                            "type": "boolean"
                          },
                          "created_at": {
                            "title": "Created At",
                            "description": "Creation date of the asset.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                            "example": "2023-10-17 19:09:40.236710",
                            "format": "date-time",
                            "type": "string"
                          },
                          "modified_at": {
                            "title": "Modified At",
                            "description": "Last modification date of the asset.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                            "example": "2023-10-17 19:09:40.236710",
                            "format": "date-time",
                            "type": "string"
                          },
                          "environment": {
                            "title": "Environment",
                            "description": "The environment where the asset is located.",
                            "example": "production",
                            "type": "string"
                          },
                          "is_branch_protected_by_jit": {
                            "title": "Is Branch Protected by JIT",
                            "description": "Indicates whether the branch is protected by JIT.",
                            "example": true,
                            "type": "boolean"
                          },
                          "status": {
                            "title": "Status",
                            "description": "The status of the asset.",
                            "example": "connected",
                            "allOf": [
                              {
                                "title": "AssetStatus",
                                "description": "An enumeration.",
                                "enum": [
                                  "connected",
                                  "failed"
                                ],
                                "type": "string"
                              }
                            ]
                          },
                          "status_details": {
                            "title": "Status Details",
                            "description": "Detailed information about the asset's status.",
                            "example": "The asset is connected.",
                            "type": "string"
                          },
                          "tags": {
                            "title": "Tags",
                            "description": "A list of tags associated with the asset.",
                            "default": [],
                            "example": [
                              {
                                "name": "team",
                                "value": "security"
                              },
                              {
                                "name": "team",
                                "value": "devops"
                              }
                            ],
                            "type": "array",
                            "items": {
                              "title": "Tag",
                              "type": "object",
                              "properties": {
                                "name": {
                                  "title": "Name",
                                  "type": "string"
                                },
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "name",
                                "value"
                              ]
                            }
                          },
                          "score": {
                            "title": "Score",
                            "description": "The score assigned to the asset.",
                            "default": 0,
                            "example": 0,
                            "type": "integer"
                          },
                          "is_pr_check_enabled": {
                            "title": "Is PR Check Enabled",
                            "description": "Indicates whether Pull Request checks are enabled for this asset.",
                            "example": true,
                            "type": "boolean"
                          },
                          "plan_items": {
                            "title": "Plan Items",
                            "description": "The slugs of the plan items that scan the asset.",
                            "default": [],
                            "example": [
                              "item-code-vulnerability",
                              "item-dependency-check"
                            ],
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "priority_factors": {
                            "title": "Priority Factors",
                            "description": "List of factors that contribute to the asset's priority score.",
                            "default": [],
                            "example": [
                              "Production",
                              "Externally Accessible"
                            ],
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "priority_score": {
                            "title": "Priority Score",
                            "description": "The priority score of the asset.",
                            "default": 0,
                            "example": 0,
                            "type": "integer"
                          },
                          "priority_context": {
                            "title": "Priority Context",
                            "description": "The active context of the asset's priority.",
                            "example": {
                              "Production": {
                                "description": "Production environment",
                                "weight": 10
                              }
                            },
                            "type": "object",
                            "additionalProperties": {
                              "title": "PriorityFactorContext",
                              "type": "object",
                              "properties": {
                                "description": {
                                  "title": "Description",
                                  "type": "string"
                                },
                                "vendor": {
                                  "allOf": [
                                    {
                                      "title": "PriorityFactorVendor",
                                      "description": "An enumeration.",
                                      "enum": [
                                        "jit",
                                        "wiz"
                                      ],
                                      "type": "string",
                                      "default": "jit"
                                    }
                                  ]
                                },
                                "weight": {
                                  "title": "Weight",
                                  "type": "integer"
                                },
                                "static_description": {
                                  "title": "Static Description",
                                  "type": "string"
                                }
                              }
                            }
                          },
                          "original_priority_factors": {
                            "title": "Priority Factors",
                            "description": "List of factors that contribute to the asset's priority score.",
                            "default": [],
                            "example": [
                              "Production",
                              "Externally Accessible"
                            ],
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "original_priority_context": {
                            "title": "Priority Context",
                            "description": "The active context of the asset's priority.",
                            "example": {
                              "Production": {
                                "description": "Production environment",
                                "weight": 10
                              }
                            },
                            "type": "object",
                            "additionalProperties": {
                              "title": "PriorityFactorContext",
                              "type": "object",
                              "properties": {
                                "description": {
                                  "title": "Description",
                                  "type": "string"
                                },
                                "vendor": {
                                  "allOf": [
                                    {
                                      "title": "PriorityFactorVendor",
                                      "description": "An enumeration.",
                                      "enum": [
                                        "jit",
                                        "wiz"
                                      ],
                                      "type": "string",
                                      "default": "jit"
                                    }
                                  ]
                                },
                                "weight": {
                                  "title": "Weight",
                                  "type": "integer"
                                },
                                "static_description": {
                                  "title": "Static Description",
                                  "type": "string"
                                }
                              }
                            }
                          },
                          "manual_factors": {
                            "title": "Manual Factors",
                            "allOf": [
                              {
                                "title": "ManualFactors",
                                "type": "object",
                                "properties": {
                                  "added": {
                                    "title": "Added",
                                    "default": [],
                                    "type": "array",
                                    "items": {
                                      "title": "ManualFactorItem",
                                      "type": "object",
                                      "properties": {
                                        "factor": {
                                          "title": "Factor",
                                          "type": "string"
                                        },
                                        "user_explanation": {
                                          "title": "User Explanation",
                                          "type": "string"
                                        },
                                        "source": {
                                          "title": "Source",
                                          "default": "finding",
                                          "enum": [
                                            "finding",
                                            "asset"
                                          ],
                                          "type": "string"
                                        }
                                      },
                                      "required": [
                                        "factor"
                                      ]
                                    }
                                  },
                                  "removed": {
                                    "title": "Removed",
                                    "default": [],
                                    "type": "array",
                                    "items": {
                                      "title": "ManualFactorItem",
                                      "type": "object",
                                      "properties": {
                                        "factor": {
                                          "title": "Factor",
                                          "type": "string"
                                        },
                                        "user_explanation": {
                                          "title": "User Explanation",
                                          "type": "string"
                                        },
                                        "source": {
                                          "title": "Source",
                                          "default": "finding",
                                          "enum": [
                                            "finding",
                                            "asset"
                                          ],
                                          "type": "string"
                                        }
                                      },
                                      "required": [
                                        "factor"
                                      ]
                                    }
                                  }
                                },
                                "default": {
                                  "added": [],
                                  "removed": []
                                }
                              }
                            ]
                          }
                        },
                        "required": [
                          "asset_id",
                          "tenant_id",
                          "asset_type",
                          "vendor",
                          "owner",
                          "asset_name",
                          "is_active",
                          "created_at",
                          "modified_at"
                        ]
                      },
                      "installation": {
                        "title": "Installation",
                        "type": "object",
                        "properties": {
                          "tenant_id": {
                            "title": "Tenant Id",
                            "type": "string"
                          },
                          "app_id": {
                            "title": "App Id",
                            "type": "string"
                          },
                          "owner": {
                            "title": "Owner",
                            "type": "string"
                          },
                          "installation_id": {
                            "title": "Installation Id",
                            "type": "string"
                          },
                          "is_active": {
                            "title": "Is Active",
                            "type": "boolean"
                          },
                          "creator": {
                            "title": "Creator",
                            "type": "string"
                          },
                          "vendor": {
                            "title": "Vendor",
                            "type": "string"
                          },
                          "name": {
                            "title": "Name",
                            "type": "string"
                          },
                          "created_at": {
                            "title": "Created At",
                            "type": "string"
                          },
                          "modified_at": {
                            "title": "Modified At",
                            "type": "string"
                          },
                          "status": {
                            "title": "InstallationStatus",
                            "description": "An enumeration.",
                            "enum": [
                              "connected",
                              "connecting",
                              "disconnected",
                              "disconnecting",
                              "updating",
                              "updated",
                              "warning",
                              "pending",
                              "error"
                            ],
                            "type": "string"
                          },
                          "status_details": {
                            "title": "Status Details",
                            "type": "object"
                          },
                          "installation_type": {
                            "title": "Installation Type",
                            "type": "string"
                          },
                          "vendor_response": {
                            "title": "Vendor Response",
                            "type": "object"
                          },
                          "vendor_attributes": {
                            "title": "Vendor Attributes",
                            "type": "object"
                          },
                          "external_id": {
                            "title": "External Id",
                            "type": "string"
                          },
                          "aws_regions_to_monitor": {
                            "title": "Aws Regions To Monitor",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "integration_version": {
                            "title": "Integration Version",
                            "type": "string"
                          },
                          "centralized_repo_asset_id": {
                            "title": "Centralized Repo Asset Id",
                            "type": "string"
                          },
                          "centralized_repo_asset": {
                            "title": "LimitedAsset",
                            "type": "object",
                            "properties": {
                              "account_id": {
                                "title": "Account ID",
                                "description": "The account ID of the asset.",
                                "example": "123456789012",
                                "type": "string"
                              },
                              "aws_account_id": {
                                "title": "AWS Account ID",
                                "description": "The AWS account ID of the asset.",
                                "example": "123456789012",
                                "type": "string"
                              },
                              "aws_stack_arn": {
                                "title": "AWS Stack ARN",
                                "description": "The Amazon Resource Name (ARN) of the AWS CloudFormation stack.",
                                "example": "arn:aws:cloudformation:us-east-1:123456789012:stack/stack-name/guid",
                                "type": "string"
                              },
                              "aws_jit_role_name": {
                                "title": "AWS JIT Role Name",
                                "description": "The name of the jit role in AWS",
                                "example": "jit-role",
                                "type": "string"
                              },
                              "aws_regions_to_scan": {
                                "title": "AWS Regions to Scan",
                                "description": "The AWS regions to scan.",
                                "example": [
                                  "us-east-1",
                                  "us-west-2"
                                ],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "target_url": {
                                "title": "Target URL",
                                "description": "The target URL for ZAP scanning.",
                                "example": "https://example.com",
                                "type": "string"
                              },
                              "exclude_paths": {
                                "title": "Exclude Paths",
                                "description": "Paths to exclude from ZAP scanning.",
                                "example": [
                                  "/api/health",
                                  "/api/status"
                                ],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "authentication_mode": {
                                "title": "Authentication Mode",
                                "description": "The authentication mode to be used for ZAP scanning.",
                                "example": "formBasedAuthentication",
                                "type": "string"
                              },
                              "authentication_key": {
                                "title": "Authentication Key",
                                "description": "The key used for authentication in ZAP scanning.",
                                "example": "authKey123",
                                "type": "string"
                              },
                              "authentication_value": {
                                "title": "Authentication Value",
                                "description": "The value used for authentication in ZAP scanning.",
                                "example": "secretValue",
                                "type": "string"
                              },
                              "auth_header_name": {
                                "title": "Auth Header Name",
                                "description": "The name of the authentication header used in ZAP scanning.",
                                "example": "Authorization",
                                "type": "string"
                              },
                              "auth_header_value": {
                                "title": "Auth Header Value",
                                "description": "The value of the authentication header used in ZAP scanning.",
                                "example": "Bearer token",
                                "type": "string"
                              },
                              "login_page_url": {
                                "title": "Login Page URL",
                                "description": "The URL of the login page for authentication in ZAP scanning.",
                                "example": "https://example.com/login",
                                "type": "string"
                              },
                              "username": {
                                "title": "Username",
                                "description": "The username used for authentication in ZAP scanning.",
                                "example": "admin",
                                "type": "string"
                              },
                              "username_css_selector": {
                                "title": "Username CSS Selector",
                                "description": "The CSS selector used to locate the username field on the login page.",
                                "example": "#username",
                                "type": "string"
                              },
                              "password": {
                                "title": "Password",
                                "description": "The password used for authentication in ZAP scanning.",
                                "example": "secretPassword",
                                "type": "string"
                              },
                              "password_ref": {
                                "title": "Password Reference",
                                "description": "A reference to the password, used for authentication in ZAP scanning.",
                                "example": "passwordRef123",
                                "type": "string"
                              },
                              "password_css_selector": {
                                "title": "Password CSS Selector",
                                "description": "The CSS selector used to locate the password field on the login page.",
                                "example": "#password",
                                "type": "string"
                              },
                              "api_domain": {
                                "title": "API Domain",
                                "description": "The domain of the API to be scanned by ZAP.",
                                "example": "api.example.com",
                                "type": "string"
                              },
                              "external_id": {
                                "title": "External ID",
                                "description": "The external ID of the asset.",
                                "example": "12345678901234567890123456789012",
                                "type": "string"
                              },
                              "asset_id": {
                                "title": "Asset ID",
                                "description": "The unique identifier for the asset.",
                                "example": "727395ab-4cac-4216-998d-7f212c2cf389",
                                "type": "string"
                              },
                              "tenant_id": {
                                "title": "Tenant ID",
                                "description": "The tenant's unique identifier.",
                                "example": "f8c2f72c-4fc3-4048-a885-6c0208777644",
                                "type": "string"
                              },
                              "asset_type": {
                                "title": "Asset Type",
                                "description": "The type of the asset.",
                                "example": "repo",
                                "enum": [
                                  "repo",
                                  "org",
                                  "aws_account",
                                  "gcp_account",
                                  "azure_account",
                                  "web",
                                  "api",
                                  "image",
                                  "external_integ"
                                ],
                                "type": "string"
                              },
                              "vendor": {
                                "title": "Vendor",
                                "description": "The vendor associated with the asset.",
                                "example": "github",
                                "type": "string"
                              },
                              "owner": {
                                "title": "Owner",
                                "description": "The owner of the asset.",
                                "example": "owner",
                                "type": "string"
                              },
                              "asset_name": {
                                "title": "Asset Name",
                                "description": "The name of the asset.",
                                "example": "asset-name",
                                "type": "string"
                              },
                              "asset_display_name": {
                                "title": "Asset Display Name",
                                "description": "The display name of the asset.",
                                "example": "asset-name",
                                "type": "string"
                              },
                              "is_active": {
                                "title": "Is Active",
                                "description": "Indicates whether the asset is active.",
                                "example": true,
                                "type": "boolean"
                              },
                              "is_covered": {
                                "title": "Is Covered",
                                "description": "Indicates whether the asset is covered.",
                                "default": true,
                                "example": true,
                                "type": "boolean"
                              },
                              "is_archived": {
                                "title": "Is Archived",
                                "description": "Indicates whether the asset is archived.",
                                "example": false,
                                "type": "boolean"
                              },
                              "created_at": {
                                "title": "Created At",
                                "description": "Creation date of the asset.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                                "example": "2023-10-17 19:09:40.236710",
                                "format": "date-time",
                                "type": "string"
                              },
                              "modified_at": {
                                "title": "Modified At",
                                "description": "Last modification date of the asset.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                                "example": "2023-10-17 19:09:40.236710",
                                "format": "date-time",
                                "type": "string"
                              },
                              "environment": {
                                "title": "Environment",
                                "description": "The environment where the asset is located.",
                                "example": "production",
                                "type": "string"
                              },
                              "is_branch_protected_by_jit": {
                                "title": "Is Branch Protected by JIT",
                                "description": "Indicates whether the branch is protected by JIT.",
                                "example": true,
                                "type": "boolean"
                              },
                              "status": {
                                "title": "Status",
                                "description": "The status of the asset.",
                                "example": "connected",
                                "allOf": [
                                  {
                                    "title": "AssetStatus",
                                    "description": "An enumeration.",
                                    "enum": [
                                      "connected",
                                      "failed"
                                    ],
                                    "type": "string"
                                  }
                                ]
                              },
                              "status_details": {
                                "title": "Status Details",
                                "description": "Detailed information about the asset's status.",
                                "example": "The asset is connected.",
                                "type": "string"
                              },
                              "tags": {
                                "title": "Tags",
                                "description": "A list of tags associated with the asset.",
                                "default": [],
                                "example": [
                                  {
                                    "name": "team",
                                    "value": "security"
                                  },
                                  {
                                    "name": "team",
                                    "value": "devops"
                                  }
                                ],
                                "type": "array",
                                "items": {
                                  "title": "Tag",
                                  "type": "object",
                                  "properties": {
                                    "name": {
                                      "title": "Name",
                                      "type": "string"
                                    },
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "name",
                                    "value"
                                  ]
                                }
                              },
                              "score": {
                                "title": "Score",
                                "description": "The score assigned to the asset.",
                                "default": 0,
                                "example": 0,
                                "type": "integer"
                              },
                              "is_pr_check_enabled": {
                                "title": "Is PR Check Enabled",
                                "description": "Indicates whether Pull Request checks are enabled for this asset.",
                                "example": true,
                                "type": "boolean"
                              },
                              "plan_items": {
                                "title": "Plan Items",
                                "description": "The slugs of the plan items that scan the asset.",
                                "default": [],
                                "example": [
                                  "item-code-vulnerability",
                                  "item-dependency-check"
                                ],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "priority_factors": {
                                "title": "Priority Factors",
                                "description": "List of factors that contribute to the asset's priority score.",
                                "default": [],
                                "example": [
                                  "Production",
                                  "Externally Accessible"
                                ],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "priority_score": {
                                "title": "Priority Score",
                                "description": "The priority score of the asset.",
                                "default": 0,
                                "example": 0,
                                "type": "integer"
                              },
                              "priority_context": {
                                "title": "Priority Context",
                                "description": "The active context of the asset's priority.",
                                "example": {
                                  "Production": {
                                    "description": "Production environment",
                                    "weight": 10
                                  }
                                },
                                "type": "object",
                                "additionalProperties": {
                                  "title": "PriorityFactorContext",
                                  "type": "object",
                                  "properties": {
                                    "description": {
                                      "title": "Description",
                                      "type": "string"
                                    },
                                    "vendor": {
                                      "allOf": [
                                        {
                                          "title": "PriorityFactorVendor",
                                          "description": "An enumeration.",
                                          "enum": [
                                            "jit",
                                            "wiz"
                                          ],
                                          "type": "string",
                                          "default": "jit"
                                        }
                                      ]
                                    },
                                    "weight": {
                                      "title": "Weight",
                                      "type": "integer"
                                    },
                                    "static_description": {
                                      "title": "Static Description",
                                      "type": "string"
                                    }
                                  }
                                }
                              },
                              "original_priority_factors": {
                                "title": "Priority Factors",
                                "description": "List of factors that contribute to the asset's priority score.",
                                "default": [],
                                "example": [
                                  "Production",
                                  "Externally Accessible"
                                ],
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              },
                              "original_priority_context": {
                                "title": "Priority Context",
                                "description": "The active context of the asset's priority.",
                                "example": {
                                  "Production": {
                                    "description": "Production environment",
                                    "weight": 10
                                  }
                                },
                                "type": "object",
                                "additionalProperties": {
                                  "title": "PriorityFactorContext",
                                  "type": "object",
                                  "properties": {
                                    "description": {
                                      "title": "Description",
                                      "type": "string"
                                    },
                                    "vendor": {
                                      "allOf": [
                                        {
                                          "title": "PriorityFactorVendor",
                                          "description": "An enumeration.",
                                          "enum": [
                                            "jit",
                                            "wiz"
                                          ],
                                          "type": "string",
                                          "default": "jit"
                                        }
                                      ]
                                    },
                                    "weight": {
                                      "title": "Weight",
                                      "type": "integer"
                                    },
                                    "static_description": {
                                      "title": "Static Description",
                                      "type": "string"
                                    }
                                  }
                                }
                              },
                              "manual_factors": {
                                "title": "Manual Factors",
                                "allOf": [
                                  {
                                    "title": "ManualFactors",
                                    "type": "object",
                                    "properties": {
                                      "added": {
                                        "title": "Added",
                                        "default": [],
                                        "type": "array",
                                        "items": {
                                          "title": "ManualFactorItem",
                                          "type": "object",
                                          "properties": {
                                            "factor": {
                                              "title": "Factor",
                                              "type": "string"
                                            },
                                            "user_explanation": {
                                              "title": "User Explanation",
                                              "type": "string"
                                            },
                                            "source": {
                                              "title": "Source",
                                              "default": "finding",
                                              "enum": [
                                                "finding",
                                                "asset"
                                              ],
                                              "type": "string"
                                            }
                                          },
                                          "required": [
                                            "factor"
                                          ]
                                        }
                                      },
                                      "removed": {
                                        "title": "Removed",
                                        "default": [],
                                        "type": "array",
                                        "items": {
                                          "title": "ManualFactorItem",
                                          "type": "object",
                                          "properties": {
                                            "factor": {
                                              "title": "Factor",
                                              "type": "string"
                                            },
                                            "user_explanation": {
                                              "title": "User Explanation",
                                              "type": "string"
                                            },
                                            "source": {
                                              "title": "Source",
                                              "default": "finding",
                                              "enum": [
                                                "finding",
                                                "asset"
                                              ],
                                              "type": "string"
                                            }
                                          },
                                          "required": [
                                            "factor"
                                          ]
                                        }
                                      }
                                    },
                                    "default": {
                                      "added": [],
                                      "removed": []
                                    }
                                  }
                                ]
                              }
                            },
                            "required": [
                              "asset_id",
                              "tenant_id",
                              "asset_type",
                              "vendor",
                              "owner",
                              "asset_name",
                              "is_active",
                              "created_at",
                              "modified_at"
                            ]
                          },
                          "oauth_context": {
                            "title": "Oauth Context",
                            "type": "object"
                          }
                        },
                        "required": [
                          "tenant_id",
                          "app_id",
                          "owner",
                          "installation_id",
                          "is_active",
                          "creator",
                          "vendor",
                          "name",
                          "created_at",
                          "modified_at"
                        ]
                      },
                      "config": {
                        "title": "Config",
                        "type": "object"
                      },
                      "integration": {
                        "title": "Integration",
                        "default": {},
                        "type": "object"
                      },
                      "centralized": {
                        "title": "Centralized",
                        "type": "object",
                        "properties": {
                          "centralized_repo_files_location": {
                            "title": "Centralized Repo Files Location",
                            "type": "string"
                          },
                          "ci_workflow_files_path": {
                            "title": "Ci Workflow Files Path",
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "required": [
                      "jit_event",
                      "owner",
                      "asset_id",
                      "asset_name",
                      "asset_type",
                      "vendor",
                      "job",
                      "workflow",
                      "asset",
                      "config"
                    ]
                  },
                  "secrets": {
                    "title": "Secrets",
                    "type": "object",
                    "additionalProperties": {
                      "type": "string"
                    }
                  },
                  "execution_data": {
                    "title": "ControlExecutionData",
                    "type": "object",
                    "properties": {
                      "execution_id": {
                        "title": "Execution Id",
                        "type": "string"
                      }
                    },
                    "required": [
                      "execution_id"
                    ]
                  },
                  "operational_data": {
                    "title": "ControlOperationalData",
                    "type": "object",
                    "properties": {
                      "callback_urls": {
                        "title": "CallbackUrls",
                        "description": "The callback urls that been sent to the control",
                        "type": "object",
                        "properties": {
                          "execution": {
                            "title": "Execution",
                            "type": "string"
                          },
                          "presigned_logs_upload_url": {
                            "title": "Presigned Logs Upload Url",
                            "type": "string"
                          },
                          "presigned_findings_upload_url": {
                            "title": "Presigned Findings Upload Url",
                            "type": "string"
                          },
                          "ignores": {
                            "title": "Ignores",
                            "type": "string"
                          },
                          "actions": {
                            "title": "Actions",
                            "type": "string"
                          },
                          "finding_schema": {
                            "title": "Finding Schema",
                            "type": "string"
                          },
                          "base_api": {
                            "title": "Base Api",
                            "type": "string"
                          },
                          "update_finding_url": {
                            "title": "Update Finding Url",
                            "type": "string"
                          }
                        },
                        "required": [
                          "execution",
                          "presigned_logs_upload_url"
                        ]
                      },
                      "callback_token": {
                        "title": "Callback Token",
                        "type": "string"
                      },
                      "control_name": {
                        "title": "Control Name",
                        "type": "string"
                      },
                      "control_image": {
                        "title": "Control Image",
                        "type": "string"
                      },
                      "control_timeout_seconds": {
                        "title": "Control Timeout Seconds",
                        "type": "integer"
                      },
                      "feature_flags_api_key": {
                        "title": "Feature Flags Api Key",
                        "type": "string"
                      }
                    },
                    "required": [
                      "callback_urls",
                      "callback_token",
                      "control_name",
                      "control_image",
                      "control_timeout_seconds",
                      "feature_flags_api_key"
                    ]
                  }
                },
                "required": [
                  "context",
                  "secrets",
                  "execution_data",
                  "operational_data"
                ]
              }
            ]
          },
          "executable_url": {
            "title": "Executable Download URL",
            "description": "Presigned S3 URL for downloading the executable. URL expires after a set duration.",
            "minLength": 1,
            "example": "https://s3.amazonaws.com/bucket/executable?token=xyz",
            "type": "string"
          }
        },
        "required": [
          "dispatch_execution_event",
          "executable_url"
        ]
      },
      "TriggerSyncEventRequest": {
        "title": "TriggerSyncEventRequest",
        "type": "object",
        "properties": {
          "plan_item_slug": {
            "title": "Plan Item Slug",
            "description": "The plan item slug",
            "minLength": 1,
            "example": "plan-item-cotainer-scanning-on-build",
            "type": "string"
          },
          "asset_type": {
            "title": "Asset Type",
            "description": "The type of asset to be scanned",
            "example": "image",
            "type": "string"
          },
          "vendor": {
            "title": "Vendor",
            "description": "The vendor type for the asset",
            "example": "docker",
            "type": "string"
          },
          "owner": {
            "title": "Owner",
            "description": "The owner of the asset",
            "minLength": 1,
            "example": "jit-platform",
            "type": "string"
          },
          "asset_name": {
            "title": "Asset Name",
            "description": "The asset_name to scan",
            "minLength": 1,
            "example": "security-control-image",
            "type": "string"
          },
          "is_backlog": {
            "title": "Is Backlog",
            "description": "Whether this is a backlog execution",
            "default": false,
            "example": false,
            "type": "boolean"
          },
          "dispatch_args": {
            "title": "Dispatch Args",
            "description": "Additional arguments for dispatch execution",
            "example": {
              "branch": "main",
              "commit": "abc123"
            },
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "os": {
            "title": "Operating System",
            "description": "Operating system type for the executable",
            "example": "alpine",
            "allOf": [
              {
                "title": "OsTypes",
                "description": "Enumeration of supported operating system distribution types.",
                "enum": [
                  "slim",
                  "alpine"
                ],
                "type": "string"
              }
            ]
          },
          "arch": {
            "title": "Architecture",
            "description": "Architecture type for the executable",
            "example": "amd64",
            "allOf": [
              {
                "title": "ArchTypes",
                "description": "Enumeration of supported architecture types.",
                "enum": [
                  "amd64",
                  "arm64"
                ],
                "type": "string"
              }
            ]
          }
        },
        "required": [
          "plan_item_slug",
          "asset_type",
          "vendor",
          "owner",
          "asset_name",
          "dispatch_args",
          "os",
          "arch"
        ]
      },
      "TriggerUnprocessableEntity": {
        "title": "UnprocessableEntityErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "UNPROCESSABLE_ENTITY",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Could not trigger execution",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "Access-Control-Allow-Origin-6ee369c9-118c-44b2-85a3-df221c4db09c": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Origin-0bb23a04-26b8-411b-8ca6-e8cee4acf8c7": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Origin-d790d85f-35ac-4ba5-87bc-09c6eff36a06": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Origin-417f96a2-f643-4c6b-a929-687197c07ef4": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Origin-50c3f722-d7b0-4a53-b8ed-b0745bde3812": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
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