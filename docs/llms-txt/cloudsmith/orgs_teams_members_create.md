# Source: https://help.cloudsmith.io/reference/orgs_teams_members_create.md

# Add users to a team.

Add users to a team.

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
    "/orgs/{org}/teams/{team}/members": {
      "post": {
        "operationId": "orgs_teams_members_create",
        "summary": "Add users to a team.",
        "description": "Add users to a team.",
        "requestBody": {
          "$ref": "#/components/requestBodies/OrganizationTeamMembers"
        },
        "responses": {
          "201": {
            "description": "The users were added to the team.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationTeamMembers"
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
          "404": {
            "description": "Team not found.",
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
          "orgs"
        ]
      },
      "parameters": [
        {
          "name": "org",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "team",
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
    "requestBodies": {
      "OrganizationTeamMembers": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/OrganizationTeamMembers"
            }
          }
        }
      }
    },
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
      "OrganizationTeamServiceMember": {
        "description": "The team members",
        "required": [
          "role",
          "user"
        ],
        "type": "object",
        "properties": {
          "role": {
            "title": "Role",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ]
          },
          "user": {
            "title": "User",
            "type": "string",
            "minLength": 1
          },
          "user_kind": {
            "title": "User kind",
            "type": "string",
            "enum": [
              "User",
              "Service"
            ],
            "default": "User"
          }
        }
      },
      "OrganizationTeamMembers": {
        "required": [
          "members"
        ],
        "type": "object",
        "properties": {
          "members": {
            "description": "The team members",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OrganizationTeamServiceMember"
            }
          }
        }
      }
    }
  }
}
```