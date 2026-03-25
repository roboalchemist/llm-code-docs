# Source: https://help.cloudsmith.io/reference/orgs_invites_list.md

# Get a list of all invites for an organization.

Get a list of all invites for an organization.

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
    "/orgs/{org}/invites/": {
      "get": {
        "operationId": "orgs_invites_list",
        "summary": "Get a list of all invites for an organization.",
        "description": "Get a list of all invites for an organization.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "A page number within the paginated result set.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "description": "Number of results to return per page.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of organization invites",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/OrganizationInvite"
                  }
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
            "description": "Organization invites not found",
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
      }
    }
  }
}
```