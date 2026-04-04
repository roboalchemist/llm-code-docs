# Source: https://docs.jit.io/reference/policy.md

# Return policy rules

Returns a paginated list of rules configured for a specific policy identified by its slug

**Requires the following permission:**
`jit.policies.read`

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
    "/policies/{policy_slug}/rules": {
      "get": {
        "summary": "Return policy rules",
        "description": "Returns a paginated list of rules configured for a specific policy identified by its slug\n\n**Requires the following permission:**\n`jit.policies.read`",
        "operationId": "policy",
        "parameters": [
          {
            "name": "policy_slug",
            "in": "path",
            "description": "Unique identifier (slug) of the policy",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/policy_slug"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "The maximum number of results to be returned per page.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/limit"
            }
          },
          {
            "name": "after",
            "in": "query",
            "description": "Cursor for next request to get the results page. Null means no more results.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/after"
            }
          },
          {
            "name": "enabled",
            "in": "query",
            "description": "Filter rules by enabled status",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/enabled"
            }
          }
        ],
        "tags": [
          "Policies"
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved paginated list of policy rules",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedRules"
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
      "limit": {
        "default": 100,
        "example": 4,
        "title": "Results limit",
        "type": "integer"
      },
      "after": {
        "example": "CURSOR",
        "title": "Cursor",
        "type": "string"
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
      "PaginatedRules": {
        "title": "PaginatedResponse[Rule]",
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
              "title": "Rule",
              "type": "object",
              "properties": {
                "id": {
                  "title": "Id",
                  "type": "string"
                },
                "created_at": {
                  "title": "Created At",
                  "type": "string"
                },
                "created_by": {
                  "title": "Created By",
                  "type": "string"
                },
                "updated_at": {
                  "title": "Updated At",
                  "type": "string"
                },
                "updated_by": {
                  "title": "Updated By",
                  "type": "string"
                },
                "type": {
                  "title": "Type",
                  "description": "The type of the entity.",
                  "allOf": [
                    {
                      "title": "RuleCollectionEntityType",
                      "description": "An enumeration.",
                      "enum": [
                        "rule"
                      ],
                      "type": "string",
                      "default": "rule"
                    }
                  ]
                },
                "rule_slug": {
                  "title": "Rule Slug",
                  "type": "string"
                },
                "tenant_id": {
                  "title": "Tenant Id",
                  "type": "string"
                },
                "policy_slug": {
                  "title": "Related Policy Slug",
                  "description": "The name of the Policy associated with the Rule.",
                  "type": "string"
                },
                "enabled": {
                  "title": "Enabled",
                  "description": "Indicates whether the policy is enabled.",
                  "type": "boolean"
                },
                "response_type": {
                  "title": "Response Type",
                  "description": "The type of response returned from the rule evaluation.",
                  "allOf": [
                    {
                      "title": "PolicyResponseType",
                      "description": "An enumeration.",
                      "enum": [
                        "boolean"
                      ],
                      "type": "string"
                    }
                  ]
                },
                "settings": {
                  "title": "Policy Settings",
                  "description": "The settings for the policy.",
                  "anyOf": [
                    {
                      "title": "AllowIgnorePlatformFindingsSettings",
                      "type": "object",
                      "properties": {
                        "conditions": {
                          "title": "Conditions",
                          "description": "List of conditions to be applied to the rule",
                          "type": "array",
                          "items": {
                            "anyOf": [
                              {
                                "title": "FindingPriorityFactorsCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "priority_factors",
                                    "enum": [
                                      "priority_factors"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingPriorityScoreCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "priority_score",
                                    "enum": [
                                      "priority_score"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "equal",
                                    "enum": [
                                      "above",
                                      "below",
                                      "equal"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "description": "The value of the attribute must be between 0 and 100",
                                    "minimum": 0,
                                    "maximum": 100,
                                    "type": "integer"
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingSeverityAttributeCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "issue_severity",
                                    "enum": [
                                      "issue_severity"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "type": "array",
                                    "items": {
                                      "title": "Severity",
                                      "description": "An enumeration.",
                                      "enum": [
                                        "Critical",
                                        "High",
                                        "Medium",
                                        "Low"
                                      ],
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingTypeCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "vulnerability_type",
                                    "enum": [
                                      "vulnerability_type"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingTeamsCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "teams",
                                    "enum": [
                                      "teams"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingCWESCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "cwes",
                                    "enum": [
                                      "cwes"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetTypeCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "asset_type",
                                    "enum": [
                                      "asset_type"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetNameCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "asset_name",
                                    "enum": [
                                      "asset_name"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetRiskScoreCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "score",
                                    "enum": [
                                      "score"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "equal",
                                    "enum": [
                                      "above",
                                      "below",
                                      "equal"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "description": "The value of the attribute must be between 0 and 100",
                                    "minimum": 0,
                                    "maximum": 100,
                                    "type": "integer"
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetPriorityFactorCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "priority_factors",
                                    "enum": [
                                      "priority_factors"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              }
                            ]
                          }
                        },
                        "user_identity_type": {
                          "description": "Specifies the user identity type, identifier for user email and role for user role.",
                          "allOf": [
                            {
                              "title": "UserIdentityType",
                              "description": "An enumeration.",
                              "enum": [
                                "identifier",
                                "role"
                              ],
                              "type": "string",
                              "default": "identifier"
                            }
                          ]
                        },
                        "user_identity_value": {
                          "title": "User Identity Value",
                          "description": "List of user emails.",
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        }
                      },
                      "required": [
                        "user_identity_type",
                        "user_identity_value"
                      ]
                    },
                    {
                      "title": "AllowIgnoreSCMFindingsSettings",
                      "type": "object",
                      "properties": {
                        "conditions": {
                          "title": "Conditions",
                          "description": "List of conditions to be applied to the rule",
                          "type": "array",
                          "items": {
                            "anyOf": [
                              {
                                "title": "FindingSeverityAttributeCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "issue_severity",
                                    "enum": [
                                      "issue_severity"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "type": "array",
                                    "items": {
                                      "title": "Severity",
                                      "description": "An enumeration.",
                                      "enum": [
                                        "Critical",
                                        "High",
                                        "Medium",
                                        "Low"
                                      ],
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingTypeCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "vulnerability_type",
                                    "enum": [
                                      "vulnerability_type"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingTeamsCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "teams",
                                    "enum": [
                                      "teams"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "FindingCWESCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "finding",
                                    "enum": [
                                      "finding"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "cwes",
                                    "enum": [
                                      "cwes"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetTypeCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "asset_type",
                                    "enum": [
                                      "asset_type"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetNameCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "asset_name",
                                    "enum": [
                                      "asset_name"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetRiskScoreCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "score",
                                    "enum": [
                                      "score"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "equal",
                                    "enum": [
                                      "above",
                                      "below",
                                      "equal"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "description": "The value of the attribute must be between 0 and 100",
                                    "minimum": 0,
                                    "maximum": 100,
                                    "type": "integer"
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              },
                              {
                                "title": "AssetPriorityFactorCondition",
                                "type": "object",
                                "properties": {
                                  "condition_entity": {
                                    "title": "Condition Entity",
                                    "default": "asset",
                                    "enum": [
                                      "asset"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_attribute": {
                                    "title": "Condition Attribute",
                                    "default": "priority_factors",
                                    "enum": [
                                      "priority_factors"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_operator": {
                                    "title": "Condition Operator",
                                    "default": "contain",
                                    "enum": [
                                      "contain"
                                    ],
                                    "type": "string"
                                  },
                                  "condition_value": {
                                    "title": "Condition Value",
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "condition_value"
                                ]
                              }
                            ]
                          }
                        },
                        "user_identity_type": {
                          "allOf": [
                            {
                              "title": "UserIdentityType",
                              "description": "An enumeration.",
                              "enum": [
                                "identifier",
                                "role"
                              ],
                              "type": "string",
                              "default": "identifier"
                            }
                          ]
                        },
                        "user_identity_value": {
                          "title": "User Identity Value",
                          "description": "List of SCM usernames.",
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        }
                      },
                      "required": [
                        "user_identity_value"
                      ]
                    },
                    {
                      "title": "AllowBypassSCMCommandSettings",
                      "type": "object",
                      "properties": {
                        "conditions": {
                          "title": "Conditions",
                          "description": "List of conditions to be applied to the rule",
                          "type": "array",
                          "items": {
                            "title": "BaseCondition",
                            "type": "object",
                            "properties": {
                              "condition_entity": {
                                "title": "Condition Entity",
                                "type": "string"
                              },
                              "condition_attribute": {
                                "title": "Condition Attribute",
                                "type": "string"
                              },
                              "condition_operator": {
                                "title": "ConditionOperation",
                                "description": "An enumeration.",
                                "enum": [
                                  "equal",
                                  "contain",
                                  "above",
                                  "below"
                                ],
                                "type": "string"
                              },
                              "condition_value": {
                                "title": "Condition Value"
                              }
                            },
                            "required": [
                              "condition_entity",
                              "condition_attribute"
                            ]
                          }
                        },
                        "user_identity_type": {
                          "allOf": [
                            {
                              "title": "UserIdentityType",
                              "description": "An enumeration.",
                              "enum": [
                                "identifier",
                                "role"
                              ],
                              "type": "string",
                              "default": "identifier"
                            }
                          ]
                        },
                        "user_identity_value": {
                          "title": "User Identity Value",
                          "description": "List of SCM usernames.",
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        }
                      },
                      "required": [
                        "user_identity_value"
                      ]
                    },
                    {
                      "title": "SLAEnforcementRuleSettings",
                      "description": "Settings for SLA Enforcement policy on pull requests.\n\nNote: TEMPLATE_CONFIG is not used for this policy. The template is defined\ndirectly in policies_template.py using Policy.construct() to bypass validation,\nas RuleTemplateInputs in jit-utils doesn't support SLA-specific fields.",
                      "type": "object",
                      "properties": {
                        "conditions": {
                          "title": "Conditions",
                          "description": "List of conditions to be applied to the rule",
                          "type": "array",
                          "items": {
                            "title": "BaseCondition",
                            "type": "object",
                            "properties": {
                              "condition_entity": {
                                "title": "Condition Entity",
                                "type": "string"
                              },
                              "condition_attribute": {
                                "title": "Condition Attribute",
                                "type": "string"
                              },
                              "condition_operator": {
                                "title": "ConditionOperation",
                                "description": "An enumeration.",
                                "enum": [
                                  "equal",
                                  "contain",
                                  "above",
                                  "below"
                                ],
                                "type": "string"
                              },
                              "condition_value": {
                                "title": "Condition Value"
                              }
                            },
                            "required": [
                              "condition_entity",
                              "condition_attribute"
                            ]
                          }
                        },
                        "enforcement_mode": {
                          "description": "The enforcement mode: 'warn' shows a warning, 'block' fails the PR check",
                          "allOf": [
                            {
                              "title": "SLAEnforcementMode",
                              "description": "Enforcement mode for SLA policy on pull requests.",
                              "enum": [
                                "warn",
                                "block"
                              ],
                              "type": "string"
                            }
                          ]
                        },
                        "repository_scope": {
                          "description": "The scope of repositories: 'all' applies to all repos, 'selected' applies to specific repos",
                          "allOf": [
                            {
                              "title": "SLARepositoryScope",
                              "description": "Repository scope for SLA policy.",
                              "enum": [
                                "all",
                                "selected"
                              ],
                              "type": "string"
                            }
                          ]
                        },
                        "selected_asset_ids": {
                          "title": "Selected Asset Ids",
                          "description": "List of asset IDs when repository_scope is 'selected'",
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "sla_by_severity": {
                          "title": "Sla By Severity",
                          "description": "SLA thresholds per severity level",
                          "type": "array",
                          "items": {
                            "title": "SLASeverityConfig",
                            "description": "Configuration for SLA threshold per severity level.",
                            "type": "object",
                            "properties": {
                              "severity": {
                                "description": "The severity level for this SLA configuration",
                                "allOf": [
                                  {
                                    "title": "SLASeverity",
                                    "description": "Finding severity levels for SLA configuration.",
                                    "enum": [
                                      "critical",
                                      "high",
                                      "medium",
                                      "low"
                                    ],
                                    "type": "string"
                                  }
                                ]
                              },
                              "max_age_days": {
                                "title": "Max Age Days",
                                "description": "Maximum age in days before a finding is considered overdue (1-365)",
                                "minimum": 1,
                                "maximum": 365,
                                "type": "integer"
                              }
                            },
                            "required": [
                              "severity",
                              "max_age_days"
                            ]
                          }
                        }
                      },
                      "required": [
                        "enforcement_mode",
                        "repository_scope",
                        "sla_by_severity"
                      ]
                    }
                  ]
                }
              },
              "required": [
                "id",
                "created_at",
                "created_by",
                "rule_slug",
                "tenant_id",
                "policy_slug",
                "enabled",
                "response_type",
                "settings"
              ]
            }
          }
        },
        "required": [
          "metadata",
          "data"
        ]
      },
      "policy_slug": {
        "title": "Policy Slug",
        "type": "string"
      },
      "enabled": {
        "title": "ParsingModel[bool]",
        "type": "boolean"
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