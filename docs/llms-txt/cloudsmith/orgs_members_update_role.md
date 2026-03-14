# Source: https://help.cloudsmith.io/reference/orgs_members_update_role.md

# Update a member's role in the organization.

Update a member's role in the organization.

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
    "/orgs/{org}/members/{member}/update-role/": {
      "patch": {
        "operationId": "orgs_members_update_role",
        "summary": "Update a member's role in the organization.",
        "description": "Update a member's role in the organization.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationMembershipRoleUpdateRequestPatch"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationMembershipRoleUpdate"
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
          "name": "member",
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
      "OrganizationMembershipRoleUpdateRequestPatch": {
        "type": "object",
        "properties": {
          "role": {
            "title": "Role",
            "type": "string",
            "enum": [
              "Owner",
              "Manager",
              "Member",
              "Collaborator"
            ],
            "default": "Owner"
          }
        }
      },
      "OrganizationMembershipRoleUpdate": {
        "type": "object",
        "properties": {
          "email": {
            "title": "Email",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "has_two_factor": {
            "title": "Has two factor",
            "type": "boolean",
            "readOnly": true
          },
          "joined_at": {
            "title": "Joined at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "last_login_at": {
            "title": "Last login at",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_login_method": {
            "title": "Last login method",
            "type": "string",
            "enum": [
              "Unknown",
              "Password",
              "Social",
              "SAML",
              "OIDC"
            ],
            "readOnly": true,
            "default": "Unknown"
          },
          "role": {
            "title": "Role",
            "type": "string",
            "enum": [
              "Owner",
              "Manager",
              "Member",
              "Collaborator"
            ],
            "default": "Owner"
          },
          "user": {
            "title": "User",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "user_id": {
            "title": "User id",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "user_name": {
            "title": "User name",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "user_url": {
            "title": "User url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "visibility": {
            "title": "Visibility",
            "type": "string",
            "enum": [
              "Public",
              "Private"
            ],
            "readOnly": true,
            "default": "Public"
          }
        }
      }
    }
  }
}
```