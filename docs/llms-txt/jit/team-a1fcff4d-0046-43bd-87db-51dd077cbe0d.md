# Source: https://docs.jit.io/reference/team-a1fcff4d-0046-43bd-87db-51dd077cbe0d.md

# Create a new team

Creating a new team with an optional parent Team ID for hierarchical structuring.

By default the team is initialized with a `manual` source.

Use the **/teams** endpoint to retrieve all teams the authenticated user has access to.

**Requires the following permission:**
`jit.teams.write`

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
      "name": "Teams",
      "description": "Returns, adds, edits, or removes teams and their members",
      "externalDocs": {
        "url": "https://docs.jit.io/docs/teams",
        "description": "Learn about managing teams in JIT"
      }
    }
  ],
  "paths": {
    "/teams/": {
      "post": {
        "summary": "Create a new team",
        "description": "Creating a new team with an optional parent Team ID for hierarchical structuring.\n\nBy default the team is initialized with a `manual` source.\n\nUse the **/teams** endpoint to retrieve all teams the authenticated user has access to.\n\n**Requires the following permission:**\n`jit.teams.write`",
        "operationId": "team-a1fcff4d-0046-43bd-87db-51dd077cbe0d",
        "parameters": [],
        "tags": [
          "Teams"
        ],
        "requestBody": {
          "description": "The fields describing the new team.",
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateTeamRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "The team was created successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ManualTeamResponse"
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
          "409": {
            "description": "Team already exists",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TeamExistsConflict"
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
          "422": {
            "description": "Parent team not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ParentTeamNotFound"
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
      "Access-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Credentials": {
        "type": "boolean",
        "default": true
      },
      "CreateTeamRequest": {
        "title": "CreateTeamRequest",
        "type": "object",
        "properties": {
          "name": {
            "title": "Team Name",
            "description": "Team Name. This name must be unique in the organization",
            "minLength": 1,
            "example": "My Awesome Team",
            "type": "string"
          },
          "description": {
            "title": "Description",
            "description": "Description of the team.",
            "default": "",
            "example": "This is my awesome team that represents my dev team",
            "type": "string"
          },
          "hidden": {
            "title": "Hidden",
            "description": "Indicates whether the team is visible in the platform.",
            "default": false,
            "example": false,
            "type": "boolean"
          },
          "parent_team_id": {
            "title": "Parent Team ID",
            "description": "Unique ID of the parent team associated with this team.\n\nUse the **/teams** endpoint to retrieve all teams the authenticated user has access to.",
            "minLength": 1,
            "example": "eb2990b6-b4d3-4931-9525-033c57168858",
            "type": "string"
          },
          "members": {
            "title": "Team Members",
            "description": "List of member names to set for this team. If provided, will replace all existing members.",
            "example": [
              "user1",
              "user2",
              "user3"
            ],
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "assets": {
            "title": "Assets",
            "description": "List of assets to associate with this team. If provided, will sync team assets.",
            "example": [],
            "type": "array",
            "items": {
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
                    "image"
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
            }
          }
        },
        "required": [
          "name"
        ]
      },
      "ManualTeamResponse": {
        "title": "ManualTeamResponse",
        "type": "object",
        "properties": {
          "tenant_id": {
            "title": "Tenant ID",
            "description": "Unique ID representing the Tenant ID.",
            "example": "c7a1c231-f2d1-4352-9ca0-fa2da8bf623c",
            "readOnly": true,
            "type": "string"
          },
          "id": {
            "title": "Team ID",
            "description": "Unique ID that represents team ID. Use the **/teams** endpoint to retrieve all teams the authenticated user has access to.",
            "minLength": 1,
            "example": "eb2990b6-b4d3-4931-9525-033c57168858",
            "readOnly": true,
            "type": "string"
          },
          "created_at": {
            "title": "Creation Date",
            "description": "Date and time the team was created.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
            "example": "2023-10-17 19:09:40.236710",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "modified_at": {
            "title": "Modified Date",
            "description": "Date and time the team was updated.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
            "example": "2023-10-17 19:09:40.236710",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "name": {
            "title": "Team Name",
            "description": "Team Name. This name must be unique in the organization",
            "minLength": 1,
            "example": "My Awesome Team",
            "type": "string"
          },
          "description": {
            "title": "Description",
            "description": "Description of the team.",
            "default": "",
            "example": "This is my awesome team that represents my dev team",
            "type": "string"
          },
          "parent_team_id": {
            "title": "Parent Team ID",
            "description": "Unique ID representing the parent team associated with this team.\n\nUse the **/teams** endpoint to retrieve all teams the authenticated user has access to.",
            "minLength": 1,
            "example": "eb2990b6-b4d3-4931-9525-033c57168858",
            "readOnly": true,
            "type": "string"
          },
          "children_team_ids": {
            "title": "Child teams IDs",
            "description": "List of unique GUIDs representing child teams associated with this team.\n\nUse the **/teams** endpoint to retrieve all teams the authenticated user has access to.",
            "default": [],
            "example": [
              "31e625fc-d138-48f9-bb5e-811397c27cbe",
              "75d2b1c0-e7c5-4430-939e-4b865613440f"
            ],
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "score": {
            "title": "Score",
            "description": "Aggregated security score of the team. 0 indicates that all related security checks failed. 100 indicates that all related security checks passed.",
            "default": 0,
            "minimum": 0,
            "maximum": 100,
            "example": 0,
            "readOnly": true,
            "type": "integer"
          },
          "source": {
            "title": "Source",
            "description": "The source of who created the team. `manual` indicates the team was created by an API. `github` indicates the team was synced from GitHub.",
            "default": "manual",
            "example": "manual",
            "enum": [
              "manual"
            ],
            "readOnly": true,
            "type": "string"
          },
          "hidden": {
            "title": "Hidden",
            "description": "Indicates whether the team is visible in the platform.",
            "default": false,
            "example": false,
            "readOnly": true,
            "type": "boolean"
          },
          "is_pr_check_enabled": {
            "title": "Is PR Check Enabled",
            "description": "Indicates whether PR check is enabled for the team's repos.",
            "example": false,
            "type": "boolean"
          },
          "is_activated": {
            "title": "Is Activated",
            "description": "Indicates whether the team is activated.",
            "default": false,
            "example": false,
            "type": "boolean"
          },
          "project": {
            "title": "Project",
            "type": "object"
          }
        },
        "required": [
          "tenant_id",
          "id",
          "created_at",
          "modified_at",
          "name"
        ]
      },
      "ParentTeamNotFound": {
        "title": "ParentTeamNotFoundSchema",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "PARENT_TEAM_NOT_EXIST",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error description.",
            "example": "Parent team with id 'eb2990b6-b4d3-4931-9525-033c57168858' does not exist",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "TeamExistsConflict": {
        "title": "TeamAlreadyExistsSchema",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "TEAM_ALREADY_EXISTS",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error description.",
            "example": "Team with name 'My Awesome Team' already exists",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
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