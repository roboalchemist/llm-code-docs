# Source: https://help.cloudsmith.io/reference/orgs_invites_partial_update.md

# Update a specific organization invite.

Update a specific organization invite.

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
    "/orgs/{org}/invites/{slug_perm}/": {
      "patch": {
        "operationId": "orgs_invites_partial_update",
        "summary": "Update a specific organization invite.",
        "description": "Update a specific organization invite.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationInviteUpdateRequestPatch"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Invite updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationInvite"
                }
              }
            }
          },
          "400": {
            "description": "The invite cannot be updated.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "Invite not found.",
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
          "name": "slug_perm",
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
      "OrganizationTeamInvite": {
        "required": [
          "team"
        ],
        "type": "object",
        "properties": {
          "role": {
            "title": "Role",
            "description": "The role to be assigned to the invited user in the team.",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Member"
          },
          "team": {
            "title": "Team",
            "description": "The team identifier (slug).",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          }
        }
      },
      "OrganizationInvite": {
        "type": "object",
        "properties": {
          "email": {
            "title": "Email",
            "description": "The email of the user to be invited.",
            "type": "string",
            "format": "email",
            "minLength": 1
          },
          "expires_at": {
            "title": "Expires at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "inviter": {
            "title": "Inviter",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "inviter_url": {
            "title": "Inviter url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "org": {
            "title": "Org",
            "type": "string",
            "readOnly": true
          },
          "role": {
            "title": "Role",
            "description": "The role to be assigned to the invited user.",
            "type": "string",
            "enum": [
              "Owner",
              "Manager",
              "Member",
              "Collaborator"
            ],
            "default": "Member"
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "teams": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/OrganizationTeamInvite"
            }
          },
          "user": {
            "title": "User",
            "description": "The slug of the user to be invited.",
            "type": "string",
            "minLength": 1
          },
          "user_url": {
            "title": "User url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "OrganizationInviteUpdateRequestPatch": {
        "type": "object",
        "properties": {
          "role": {
            "title": "Role",
            "description": "The role to be assigned to the invited user.",
            "type": "string",
            "enum": [
              "Owner",
              "Manager",
              "Member",
              "Collaborator"
            ],
            "default": "Member"
          }
        }
      }
    }
  }
}
```