# Source: https://docs.mystic.ai/reference/get_logged_in_user_v4_users_me_get.md

# Get Logged In User

Retrieve the currently logged in user.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/users/me": {
      "get": {
        "tags": [
          "Users"
        ],
        "summary": "Get Logged In User",
        "description": "Retrieve the currently logged in user.",
        "operationId": "get_logged_in_user_v4_users_me_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserGet"
                }
              }
            }
          }
        },
        "security": [
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "UserGet": {
        "properties": {
          "firstname": {
            "type": "string",
            "title": "Firstname"
          },
          "lastname": {
            "type": "string",
            "title": "Lastname"
          },
          "company": {
            "type": "string",
            "title": "Company"
          },
          "job_title": {
            "type": "string",
            "title": "Job Title"
          },
          "avatar_colour": {
            "type": "string",
            "title": "Avatar Colour"
          },
          "show_tutorial": {
            "type": "boolean",
            "title": "Show Tutorial"
          },
          "email": {
            "type": "string",
            "title": "Email"
          },
          "username": {
            "type": "string",
            "title": "Username"
          },
          "id": {
            "type": "string",
            "title": "Id"
          },
          "has_password": {
            "type": "boolean",
            "title": "Has Password"
          },
          "roles": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Roles"
          },
          "teams": {
            "items": {
              "$ref": "#/components/schemas/UserTeam"
            },
            "type": "array",
            "title": "Teams"
          },
          "selected_team": {
            "type": "string",
            "title": "Selected Team"
          }
        },
        "type": "object",
        "required": [
          "email",
          "username",
          "id",
          "has_password"
        ],
        "title": "UserGet",
        "description": "Base model for schemas."
      },
      "UserTeam": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "role": {
            "type": "string",
            "title": "Role"
          }
        },
        "type": "object",
        "required": [
          "id",
          "name",
          "role"
        ],
        "title": "UserTeam",
        "description": "Simple schema for returning info about teams a user is in, plus their\nrole in that team."
      }
    },
    "securitySchemes": {
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```