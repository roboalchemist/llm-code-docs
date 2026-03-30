# Source: https://docs.jit.io/reference/teams-2.md

# Return all teams

Returns all teams together with Parent and Child IDs. **Optional**: return team members as additional metadata.

**Requires the following permission:**
`jit.teams.read`

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
      "get": {
        "summary": "Return all teams",
        "description": "Returns all teams together with Parent and Child IDs. **Optional**: return team members as additional metadata.\n\n**Requires the following permission:**\n`jit.teams.read`",
        "operationId": "teams",
        "parameters": [
          {
            "name": "include_members",
            "in": "query",
            "description": "Should or should not return team members.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/include_members"
            }
          },
          {
            "name": "include_image",
            "in": "query",
            "description": "Should or should not return image details.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/include_image"
            }
          },
          {
            "name": "hidden",
            "in": "query",
            "description": "Should or should not return hidden teams.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/hidden"
            }
          },
          {
            "name": "team_ids",
            "in": "query",
            "description": "Return a list of team IDs, with a limit of up to 10 IDs.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/team_ids"
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
          }
        ],
        "tags": [
          "Teams"
        ],
        "responses": {
          "200": {
            "description": "Paginated list of teams returned successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetTeamsResponse"
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
      "GetTeamsResponse": {
        "title": "GetTeamsResponse",
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
              "title": "TeamWithMetadata",
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
                  "title": "Creation Source",
                  "description": "The source of who created the team. `manual` indicates the team was created by an API. `github` indicates the team was synced from GitHub.",
                  "example": "manual",
                  "enum": [
                    "manual",
                    "github"
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
                "members": {
                  "title": "List of team members",
                  "description": "List of all team members and their details.",
                  "nullable": true,
                  "type": "array",
                  "items": {
                    "title": "Member",
                    "type": "object",
                    "properties": {
                      "id": {
                        "title": "ID",
                        "description": "ID of the team member.",
                        "example": "440032d5-7728-457f-8f19-15c8c7a6697f",
                        "readOnly": true,
                        "type": "string"
                      },
                      "name": {
                        "title": "Name",
                        "description": "Name of the team member.",
                        "example": "Jitey JIT",
                        "readOnly": true,
                        "type": "string"
                      },
                      "team_id": {
                        "title": "Team ID",
                        "description": "Unique ID that represents team ID. Use the **/teams** endpoint to retrieve all teams the authenticated user has access to.",
                        "minLength": 1,
                        "example": "eb2990b6-b4d3-4931-9525-033c57168858",
                        "readOnly": true,
                        "type": "string"
                      },
                      "created_at": {
                        "title": "Creation Date",
                        "description": "Date and time the team member was created.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                        "example": "2023-10-17 19:09:40.236710",
                        "format": "date-time",
                        "readOnly": true,
                        "type": "string"
                      },
                      "modified_at": {
                        "title": "Modified Date",
                        "description": "Date and time the team member was modified.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                        "example": "2023-10-17 19:09:40.236710",
                        "format": "date-time",
                        "readOnly": true,
                        "type": "string"
                      },
                      "source": {
                        "title": "Member Source",
                        "description": "Source of the team member.",
                        "example": "github|manual",
                        "readOnly": true,
                        "type": "string"
                      },
                      "avatar_url": {
                        "title": "Member Avatar URL",
                        "description": "Avatar URL of the team member in the 3rd party vendor.",
                        "example": "https://avatars.githubusercontent.com/u/0000?v=4",
                        "minLength": 1,
                        "maxLength": 2083,
                        "format": "uri",
                        "type": "string",
                        "readOnly": true
                      },
                      "vendor_id": {
                        "title": "Vendor ID",
                        "description": "Identifier representing the vendor who created the user.",
                        "example": "1234567",
                        "readOnly": true,
                        "type": "string"
                      },
                      "url": {
                        "title": "Member programmatic URL",
                        "description": "Programmatic URL of the team member in the 3rd party vendor.",
                        "example": "https://api.github.com/users/JiteyJIT",
                        "minLength": 1,
                        "maxLength": 2083,
                        "format": "uri",
                        "type": "string",
                        "readOnly": true
                      },
                      "html_url": {
                        "title": "Member HTML URL",
                        "description": "HTTP URL of the team member in the 3rd party vendor.",
                        "example": "https://github.com/users/JiteyJIT",
                        "minLength": 1,
                        "maxLength": 2083,
                        "format": "uri",
                        "type": "string",
                        "readOnly": true
                      }
                    },
                    "required": [
                      "id",
                      "name",
                      "team_id",
                      "created_at",
                      "modified_at",
                      "avatar_url"
                    ]
                  }
                },
                "image_details": {
                  "title": "Image Details",
                  "description": "Details of the image associated with the team",
                  "allOf": [
                    {
                      "title": "ImageResponse",
                      "type": "object",
                      "properties": {
                        "background_image_url": {
                          "title": "Background Image URL",
                          "description": "URL of the background image associated with the team",
                          "example": "https://www.example.com/image.png",
                          "type": "string"
                        },
                        "shape": {
                          "title": "Shape",
                          "description": "Shape of the image associated with the team, options are: `polygon`, `star`, `circle`, `square`, `diamond`, `pentagon`",
                          "example": "star",
                          "type": "string"
                        }
                      },
                      "required": [
                        "background_image_url",
                        "shape"
                      ]
                    }
                  ]
                }
              },
              "required": [
                "tenant_id",
                "id",
                "created_at",
                "modified_at",
                "name",
                "source"
              ]
            }
          }
        },
        "required": [
          "metadata",
          "data"
        ]
      },
      "include_members": {
        "default": false,
        "example": false,
        "title": "Include Members",
        "type": "boolean"
      },
      "include_image": {
        "default": false,
        "example": false,
        "title": "Include Image details",
        "type": "boolean"
      },
      "hidden": {
        "default": false,
        "example": false,
        "title": "Include hidden teams",
        "type": "boolean"
      },
      "team_ids": {
        "example": "1ca16da7-62f0-4150-9fa0-9d9ff98d8541,60da519c-9fcd-4633-86d1-6960c65631f8",
        "title": "Team IDs",
        "type": "string"
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