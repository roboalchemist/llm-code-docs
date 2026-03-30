# Source: https://docs.firehydrant.com/reference/update_team_escalation_policy.md

# Update an escalation policy for a team

Update a Signals escalation policy by ID

# OpenAPI definition

````json
{
  "openapi": "3.0.1",
  "info": {
    "title": "FireHydrant API",
    "description": "The FireHydrant API is based around REST. It uses Bearer token authentication and returns JSON responses. You can use the FireHydrant API to configure integrations, define incidents, and set up webhooks--anything you can do on the FireHydrant UI.\n\n* [Dig into our API endpoints](https://developers.firehydrant.io/docs/api)\n* [View your bot users](https://app.firehydrant.io/organizations/bots)\n\n## Base API endpoint\n\n[https://api.firehydrant.io/v1](https://api.firehydrant.io/v1)\n\n## Current version\n\nv1\n\n## Authentication\n\nAll requests to the FireHydrant API require an `Authorization` header with the value set to `Bearer {token}`. FireHydrant supports bot tokens to act on behalf of a computer instead of a user's account. This prevents integrations from breaking when people leave your organization or their token is revoked. See the Bot tokens section (below) for more information on this.\n\nAn example of a header to authenticate against FireHydrant would look like:\n\n```\nAuthorization: Bearer fhb-thisismytoken\n```\n\n## Bot tokens\n\nTo access the FireHydrant API, you must authenticate with a bot token. (You must have owner permissions on your organization to see bot tokens.) Bot users allow you to interact with the FireHydrant API by using token-based authentication. To create bot tokens, log in to your organization and refer to the **Bot users** [page](https://app.firehydrant.io/organizations/bots).\n\nBot tokens enable you to create a bot that has no ties to any user. Normally, all actions associated with an API token are associated with the user who created it. Bot tokens attribute all actions to the bot user itself. This way, all data associated with the token actions can be performed against the FireHydrant API without a user.\n\nEvery request to the API is authenticated unless specified otherwise.\n\n### Rate Limiting\n\nCurrently, requests made with bot tokens are rate limited on a per-account level. If your account has multiple bot token then the rate limit is shared across all of them. As of February 7th, 2023, the rate limit is at least 50 requests per account every 10 seconds, or 300 requests per minute.\n\nRate limited responses will be served with a `429` status code and a JSON body of:\n\n```json\n{\"error\": \"rate limit exceeded\"}\n```\nand headers of:\n```\n\"RateLimit-Limit\" -> the maximum number of requests in the rate limit pool\n\"Retry-After\" -> the number of seconds to wait before trying again\n```\n\n## How lists are returned\n\nAPI lists are returned as arrays. A paginated entity in FireHydrant will return two top-level keys in the response object: a data key and a pagination key.\n\n### Paginated requests\n\nThe `data` key is returned as an array. Each item in the array includes all of the entity data specified in the API endpoint. (The per-page default for the array is 20 items.)\n\nPagination is the second key (`pagination`) returned in the overall response body. It includes medtadata around the current page, total count of items, and options to go to the next and previous page. All of the specifications returned in the pagination object are available as URL parameters. So if you want to specify, for example, going to the second page of a response, you can send a request to the same endpoint but pass the URL parameter **page=2**.\n\nFor example, you might request **https://api.firehydrant.io/v1/environments/** to retrieve environments data. The JSON returned contains the above-mentioned data section and pagination section. The data section includes various details about an incident, such as the environment name, description, and when it was created.\n\n```\n{\n  \"data\": [\n    {\n      \"id\": \"f8125cf4-b3a7-4f88-b5ab-57a60b9ed89b\",\n      \"name\": \"Production - GCP\",\n      \"description\": \"\",\n      \"created_at\": \"2021-02-17T20:02:10.679Z\"\n    },\n    {\n      \"id\": \"a69f1f58-af77-4708-802d-7e73c0bf261c\",\n      \"name\": \"Staging\",\n      \"description\": \"\",\n      \"created_at\": \"2021-04-16T13:41:59.418Z\"\n    }\n  ],\n  \"pagination\": {\n    \"count\": 2,\n    \"page\": 1,\n    \"items\": 2,\n    \"pages\": 1,\n    \"last\": 1,\n    \"prev\": null,\n    \"next\": null\n  }\n}\n```\n\nTo request the second page, you'd request the same endpoint with the additional query parameter of `page` in the URL:\n\n```\nGET https://api.firehydrant.io/v1/environments?page=2\n```\n\nIf you need to modify the number of records coming back from FireHydrant, you can use the `per_page` parameter (max is 200):\n\n```\nGET https://api.firehydrant.io/v1/environments?per_page=50\n```",
    "version": "0.0.1"
  },
  "servers": [
    {
      "url": "https://api.firehydrant.io/"
    }
  ],
  "security": [
    {
      "api_key": []
    }
  ],
  "tags": [
    {
      "name": "Signals",
      "description": "Operations related to Signals"
    }
  ],
  "paths": {
    "/v1/teams/{team_id}/escalation_policies/{id}": {
      "patch": {
        "tags": [
          "Signals"
        ],
        "summary": "Update an escalation policy for a team",
        "description": "Update a Signals escalation policy by ID",
        "operationId": "update_team_escalation_policy",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/update_team_escalation_policy"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Update a Signals escalation policy by ID",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Signals_API_EscalationPolicyEntity"
                }
              }
            }
          }
        },
        "x-codegen-request-body-name": "update_team_escalation_policy"
      }
    }
  },
  "components": {
    "schemas": {
      "AuthorEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "source": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          }
        }
      },
      "Signals_API_TargetEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
          },
          "team_id": {
            "type": "string",
            "nullable": true
          },
          "is_pageable": {
            "type": "boolean",
            "nullable": true
          }
        }
      },
      "Signals_API_EscalationPolicyEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "default": {
            "type": "boolean",
            "nullable": true
          },
          "repetitions": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "steps": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Signals_API_EscalationPolicyStepEntity"
            }
          },
          "handoff_step": {
            "$ref": "#/components/schemas/NullableSignals_API_EscalationPolicyHandoffStepEntity"
          },
          "created_by": {
            "$ref": "#/components/schemas/NullableAuthorEntity"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "step_strategy": {
            "type": "string",
            "nullable": true
          },
          "notification_priority_policies": {
            "type": "array",
            "description": "Priority-specific policies for dynamic escalation policies",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Signals_API_NotificationPriorityPolicyEntity"
            }
          }
        },
        "description": "Signals_API_EscalationPolicyEntity model"
      },
      "Signals_API_EscalationPolicyStepEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "parent_position": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "targets": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Signals_API_TargetEntity"
            }
          },
          "timeout": {
            "type": "string",
            "nullable": true
          },
          "distribution_type": {
            "type": "string",
            "description": "The distribution type for the step",
            "nullable": true,
            "enum": [
              "unspecified",
              "round_robin_by_alert",
              "round_robin_by_escalation_policy"
            ]
          },
          "next_target_for_round_robin": {
            "$ref": "#/components/schemas/NullableSignals_API_TargetEntity"
          },
          "priorities": {
            "type": "array",
            "description": "The notification priorities that this step is assigned to. Valid values are HIGH, MEDIUM, and LOW.",
            "nullable": true,
            "items": {
              "type": "string"
            }
          }
        }
      },
      "Signals_API_EscalationPolicyHandoffStepEntity": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "target": {
            "$ref": "#/components/schemas/NullableSignals_API_TargetEntity"
          }
        }
      },
      "Signals_API_NotificationPriorityPolicyEntity": {
        "type": "object",
        "properties": {
          "notification_priority": {
            "type": "string",
            "description": "The notification priority this policy handles (HIGH, MEDIUM, or LOW)",
            "nullable": true
          },
          "repetitions": {
            "type": "integer",
            "description": "Number of repetitions for this priority",
            "format": "int32",
            "nullable": true
          },
          "handoff_step": {
            "$ref": "#/components/schemas/NullableSignals_API_EscalationPolicyHandoffStepEntity"
          },
          "steps": {
            "type": "array",
            "description": "Steps for this priority",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/Signals_API_EscalationPolicyStepEntity"
            }
          }
        }
      },
      "update_team_escalation_policy": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The escalation policy's name.",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "A detailed description of the escalation policy.",
            "nullable": true
          },
          "repetitions": {
            "type": "integer",
            "description": "The number of times that the escalation policy should repeat before an alert is dropped.",
            "format": "int32",
            "nullable": true,
            "default": 0
          },
          "default": {
            "type": "boolean",
            "description": "Whether this escalation policy should be the default for the team.",
            "nullable": true,
            "default": false
          },
          "step_strategy": {
            "type": "string",
            "description": "The strategy for handling steps in the escalation policy. Can be \"static\" or \"dynamic_by_priority\".",
            "nullable": true
          },
          "steps": {
            "type": "array",
            "description": "A list of steps that define how an alert should escalate through the policy.",
            "nullable": true,
            "items": {
              "required": [
                "timeout"
              ],
              "type": "object",
              "properties": {
                "targets": {
                  "type": "array",
                  "description": "A list of targets that the step will notify. You can specify up to 15 targets per step.",
                  "nullable": true,
                  "items": {
                    "required": [
                      "id",
                      "type"
                    ],
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "description": "The type of target that the step will notify.",
                        "enum": [
                          "OnCallSchedule",
                          "User",
                          "SlackChannel",
                          "MicrosoftTeamsChannel",
                          "EntireTeam",
                          "Webhook"
                        ]
                      },
                      "id": {
                        "type": "string",
                        "description": "The ID of the target that the step will notify."
                      }
                    }
                  }
                },
                "timeout": {
                  "type": "string",
                  "description": "An ISO8601 duration string specifying how long to wait before moving on to the next step. For the last step, this value specifies how long to wait before the escalation policy should repeat, if it repeats."
                },
                "distribution_type": {
                  "type": "string",
                  "description": "The round robin configuration for the step. One of 'unspecified', 'round_robin_by_alert', or 'round_robin_by_escalation_policy'.",
                  "nullable": true,
                  "enum": [
                    "unspecified",
                    "round_robin_by_alert",
                    "round_robin_by_escalation_policy"
                  ]
                },
                "priorities": {
                  "type": "array",
                  "description": "A list of priorities (HIGH, MEDIUM, LOW) to which the step applies when using a dynamic escalation policy.",
                  "nullable": true,
                  "items": {
                    "type": "string"
                  }
                }
              }
            }
          },
          "handoff_step": {
            "required": [
              "target_id",
              "target_type"
            ],
            "type": "object",
            "properties": {
              "target_type": {
                "type": "string",
                "description": "The type of target to which the policy will hand off.",
                "enum": [
                  "EscalationPolicy",
                  "Team"
                ]
              },
              "target_id": {
                "type": "string",
                "description": "The ID of the target to which the policy will hand off."
              }
            },
            "description": "A step that defines where an alert should be sent when the policy is exhausted and the alert is still unacknowledged.",
            "nullable": true
          },
          "prioritized_settings": {
            "type": "object",
            "properties": {
              "high": {
                "type": "object",
                "properties": {
                  "repetitions": {
                    "type": "integer",
                    "description": "Number of repetitions for HIGH priority alerts",
                    "format": "int32",
                    "nullable": true
                  },
                  "handoff_step": {
                    "required": [
                      "target_id",
                      "target_type"
                    ],
                    "type": "object",
                    "properties": {
                      "target_type": {
                        "type": "string",
                        "enum": [
                          "EscalationPolicy",
                          "Team"
                        ]
                      },
                      "target_id": {
                        "type": "string"
                      }
                    },
                    "description": "Handoff step for HIGH priority alerts",
                    "nullable": true
                  }
                },
                "description": "Settings for HIGH priority alerts",
                "nullable": true
              },
              "medium": {
                "type": "object",
                "properties": {
                  "repetitions": {
                    "type": "integer",
                    "description": "Number of repetitions for MEDIUM priority alerts",
                    "format": "int32",
                    "nullable": true
                  },
                  "handoff_step": {
                    "required": [
                      "target_id",
                      "target_type"
                    ],
                    "type": "object",
                    "properties": {
                      "target_type": {
                        "type": "string",
                        "enum": [
                          "EscalationPolicy",
                          "Team"
                        ]
                      },
                      "target_id": {
                        "type": "string"
                      }
                    },
                    "description": "Handoff step for MEDIUM priority alerts",
                    "nullable": true
                  }
                },
                "description": "Settings for MEDIUM priority alerts",
                "nullable": true
              },
              "low": {
                "type": "object",
                "properties": {
                  "repetitions": {
                    "type": "integer",
                    "description": "Number of repetitions for LOW priority alerts",
                    "format": "int32",
                    "nullable": true
                  },
                  "handoff_step": {
                    "required": [
                      "target_id",
                      "target_type"
                    ],
                    "type": "object",
                    "properties": {
                      "target_type": {
                        "type": "string",
                        "enum": [
                          "EscalationPolicy",
                          "Team"
                        ]
                      },
                      "target_id": {
                        "type": "string"
                      }
                    },
                    "description": "Handoff step for LOW priority alerts",
                    "nullable": true
                  }
                },
                "description": "Settings for LOW priority alerts",
                "nullable": true
              }
            },
            "description": "Priority-specific settings for dynamic escalation policies",
            "nullable": true
          }
        },
        "description": "Update a Signals escalation policy by ID"
      },
      "NullableAuthorEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/AuthorEntity"
          }
        ]
      },
      "NullableSignals_API_TargetEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Signals_API_TargetEntity"
          }
        ]
      },
      "NullableSignals_API_EscalationPolicyHandoffStepEntity": {
        "nullable": true,
        "allOf": [
          {
            "$ref": "#/components/schemas/Signals_API_EscalationPolicyHandoffStepEntity"
          }
        ]
      }
    },
    "securitySchemes": {
      "api_key": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
      }
    }
  },
  "x-original-swagger-version": "2.0"
}
````