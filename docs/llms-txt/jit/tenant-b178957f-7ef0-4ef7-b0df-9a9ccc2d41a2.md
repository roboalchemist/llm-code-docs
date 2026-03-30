# Source: https://docs.jit.io/reference/tenant-b178957f-7ef0-4ef7-b0df-9a9ccc2d41a2.md

# Update configuration file

Updates the configuration file content. The configuration file content must be a valid YAML string, representing a dictionary object.

The `file_sha` parameter is required to ensure the file being updated has not changed since the last read operation. If the file has changed, the update will fail to prevent overwriting changes. To forcefully update the configuration file content, you may provide a commit hash in the `file_sha` parameter.

**Important**: This API overwrites the entire configuration. Please call the `Get configuration file` API to retrieve the current configuration content first, and append the new configuration to the existing content.
For details on the structure of specific configurations, please refer to the [Security As Code Documentation](https://docs.jit.io/docs/security-as-code-configuration).

**Usage Example**

1. Retrieve the current configuration content using the get configuration API:

```
curl -X GET \
  –url https://api.jit.io/plans/configuration-file \
  –header ‘accept: application/json’ \
  –header ‘Authorization: Bearer ’
```

A potential response might be:

```
{
  "content": {
    "folders": [
      {
        "exclude": [
          "/tests/*"
        ],
        "path": "/"
      }
    ]
  },
  "sha": "c548d1f6410fa66f1222678eef84a26dd042fc0f"
}
```

2. Update the configuration file content:

For instance, to add a new exclude folder to the current content, append it and use the following curl command:

```
curl -X PUT \
  –url https://api.jit.io/plans/configuration-file \
  –header 'accept: application/json' \
  –header 'Authorization: Bearer ' \
  –data '{
  "payload": {
    "folders": [
      {
        "exclude": [
          "/tests/*",
          "/cypress/*"
        ],
        "path": "/"
      }
    ]
  },
  "file_sha": "c548d1f6410fa66f1222678eef84a26dd042fc0f"
}'
```


**Requires the following permission:**
`jit.preferences.write`

# OpenAPI definition

````json
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
      "name": "Plans",
      "description": "Returns, adds, edits, or removes plans and their items",
      "externalDocs": {
        "url": "https://docs.jit.io/docs/my-plan-tab",
        "description": "Learn about managing plans in JIT"
      }
    }
  ],
  "paths": {
    "/plan/configuration-file": {
      "put": {
        "summary": "Update configuration file",
        "description": "\nUpdates the configuration file content. The configuration file content must be a valid YAML string, representing a dictionary object.\n\nThe `file_sha` parameter is required to ensure the file being updated has not changed since the last read operation. If the file has changed, the update will fail to prevent overwriting changes. To forcefully update the configuration file content, you may provide a commit hash in the `file_sha` parameter.\n\n**Important**: This API overwrites the entire configuration. Please call the `Get configuration file` API to retrieve the current configuration content first, and append the new configuration to the existing content.\nFor details on the structure of specific configurations, please refer to the [Security As Code Documentation](https://docs.jit.io/docs/security-as-code-configuration).\n\n**Usage Example**\n\n1. Retrieve the current configuration content using the get configuration API:\n\n```\ncurl -X GET \\\n  –url https://api.jit.io/plans/configuration-file \\\n  –header ‘accept: application/json’ \\\n  –header ‘Authorization: Bearer ’\n```\n\nA potential response might be:\n\n```\n{\n  \"content\": {\n    \"folders\": [\n      {\n        \"exclude\": [\n          \"/tests/*\"\n        ],\n        \"path\": \"/\"\n      }\n    ]\n  },\n  \"sha\": \"c548d1f6410fa66f1222678eef84a26dd042fc0f\"\n}\n```\n\n2. Update the configuration file content:\n\nFor instance, to add a new exclude folder to the current content, append it and use the following curl command:\n\n```\ncurl -X PUT \\\n  –url https://api.jit.io/plans/configuration-file \\\n  –header 'accept: application/json' \\\n  –header 'Authorization: Bearer ' \\\n  –data '{\n  \"payload\": {\n    \"folders\": [\n      {\n        \"exclude\": [\n          \"/tests/*\",\n          \"/cypress/*\"\n        ],\n        \"path\": \"/\"\n      }\n    ]\n  },\n  \"file_sha\": \"c548d1f6410fa66f1222678eef84a26dd042fc0f\"\n}'\n```\n\n\n**Requires the following permission:**\n`jit.preferences.write`",
        "operationId": "tenant-b178957f-7ef0-4ef7-b0df-9a9ccc2d41a2",
        "parameters": [],
        "tags": [
          "Plans"
        ],
        "requestBody": {
          "required": false,
          "description": "New configuration file content and file SHA",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIExposedUpdateConfigurationRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Configuration file updated successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ConfigurationFileInfo"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
                }
              }
            }
          },
          "409": {
            "description": "Conflict",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Conflict"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
                  "$ref": "#/components/schemas/PlanAccess-Control-Allow-Origin"
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
      "APIExposedUpdateConfigurationRequest": {
        "title": "APIExposedUpdateConfigurationRequest",
        "description": "This is the `UpdateConfigurationRequest` model but without the commit attribute, which we don't want to expose\nin the API documentation, because file_sha is the only attribute that the user should provide, and it serves the\nsame purpose as commit.\nThis model is used to generate the API documentation for the update-configuration endpoint.",
        "type": "object",
        "properties": {
          "file_sha": {
            "title": "File Sha",
            "description": "The SHA-1 hash of the content prior to updating, used to prevent overwriting changes.\n\nUpdates will be rejected if the content has been modified since the last read operation.",
            "example": "1234567890abcdef1234567890abcdef12345678",
            "type": "string"
          },
          "payload": {
            "title": "Payload (content)",
            "description": "The configuration file content, more info can be found in the [Security As Code Documentation](https://docs.jit.io/docs/security-as-code-configuration).\n\nFor example `{\"folders\": [{\"exclude\": [\"/tests/*\"], \"path\": \"/\"}]}`",
            "type": "object"
          },
          "commit_message": {
            "title": "Commit Message",
            "description": "The commit message to be used when updating the configuration file.",
            "type": "string"
          }
        },
        "required": [
          "payload"
        ]
      },
      "ConfigurationFileInfo": {
        "title": "ConfigurationFileInfo",
        "type": "object",
        "properties": {
          "content": {
            "title": "Content",
            "description": "An object representing the content of the file.",
            "example": {
              "folders": [
                {
                  "exclude": [
                    "/tests/*"
                  ],
                  "path": "/"
                }
              ]
            },
            "type": "object"
          },
          "sha": {
            "title": "File SHA",
            "description": "The SHA-1 hash of the content.",
            "example": "c548d1f6410fa66f1222678eef84a26dd042fc0f",
            "type": "string"
          }
        },
        "required": [
          "content"
        ]
      },
      "Conflict": {
        "title": "ConflictErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "FILE_SHA_CONFLICT",
            "allOf": [
              {
                "title": "ErrorCode",
                "description": "An enumeration.",
                "enum": [
                  "FILE_SHA_CONFLICT",
                  "NO_GITHUB_INSTALLATION",
                  "NO_CENTRALIZED_REPO",
                  "FILE_NOT_FOUND",
                  "MALFORMED_FILE",
                  "INVALID_FILE"
                ]
              }
            ]
          },
          "message": {
            "title": "Message",
            "description": "Human readable error message.",
            "example": "The content has been updated since the last read operation. Please calculate the up-to-date SHA1 hash of the file content and provide it in the request or pass None in `file_sha` parameter to forcefully update the file content.",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "PlanAccess-Control-Allow-Origin": {
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
````