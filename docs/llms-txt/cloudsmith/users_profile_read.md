# Source: https://help.cloudsmith.io/reference/users_profile_read.md

# Provide a brief for the specified user (if any).

Provide a brief for the specified user (if any).

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
    "/users/profile/{slug}/": {
      "get": {
        "operationId": "users_profile_read",
        "summary": "Provide a brief for the specified user (if any).",
        "description": "Provide a brief for the specified user (if any).",
        "responses": {
          "200": {
            "description": "Retrieved details for the specified user (or current user, if none was specified)",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserProfile"
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
          "users"
        ]
      },
      "parameters": [
        {
          "name": "slug",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
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
      "UserProfile": {
        "required": [
          "first_name",
          "last_name"
        ],
        "type": "object",
        "properties": {
          "company": {
            "title": "Company",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "first_name": {
            "title": "First name",
            "type": "string",
            "maxLength": 120,
            "minLength": 1
          },
          "job_title": {
            "title": "Job title",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "joined_at": {
            "title": "Joined at",
            "type": "string",
            "format": "date-time"
          },
          "last_name": {
            "title": "Last name",
            "type": "string",
            "maxLength": 120,
            "minLength": 1
          },
          "name": {
            "title": "Name",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "slug": {
            "title": "Slug",
            "type": "string",
            "readOnly": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "readOnly": true
          },
          "tagline": {
            "title": "Tagline",
            "description": "Your tagline is a sentence about you. Make it funny. Make it professional. Either way, it's public and it represents who you are.",
            "type": "string",
            "maxLength": 1024,
            "nullable": true
          },
          "url": {
            "title": "Url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          }
        }
      }
    }
  }
}
```