# Source: https://help.cloudsmith.io/reference/orgs_members_list.md

# Get the details for all organization members.

Get the details for all organization members.

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
    "/orgs/{org}/members/": {
      "get": {
        "operationId": "orgs_members_list",
        "summary": "Get the details for all organization members.",
        "description": "Get the details for all organization members.",
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
          },
          {
            "name": "is_active",
            "in": "query",
            "description": "Filter for active/inactive users.",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "query",
            "in": "query",
            "description": "A search term for querying of members within an Organization.Available options are: email, org, user, userslug, inactive, user_name, role",
            "required": false,
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "A field for sorting objects in ascending or descending order. Use `-` prefix for descending order (e.g., `-user_name`). Available options: user_name, role.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "user_name"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of organization's members",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/OrganizationMembership"
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
      "OrganizationMembership": {
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
          "is_active": {
            "title": "Is active",
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
            "readOnly": true,
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