# Source: https://help.cloudsmith.io/reference/user_self.md

# Provide a brief for the current user (if any).

Provide a brief for the current user (if any).

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/user/self/": {
      "get": {
        "operationId": "user_self",
        "summary": "Provide a brief for the current user (if any).",
        "description": "Provide a brief for the current user (if any).",
        "responses": {
          "200": {
            "description": "Retrieved brief for the current user",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserBrief"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "user"
        ]
      },
      "parameters": []
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "UserBrief": {
        "type": "object",
        "properties": {
          "authenticated": {
            "title": "Authenticated",
            "description": "If true then you're logged in as a user.",
            "type": "boolean",
            "readOnly": true
          },
          "email": {
            "title": "Email address",
            "description": "Your email address that we use to contact you. This is only visible to you.",
            "type": "string",
            "format": "email",
            "maxLength": 254,
            "minLength": 1,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The full name of the user (if any).",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "profile_url": {
            "title": "Profile url",
            "description": "The URL for the full profile of the user.",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "readOnly": true
          },
          "slug": {
            "title": "Slug",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      }
    }
  }
}
```