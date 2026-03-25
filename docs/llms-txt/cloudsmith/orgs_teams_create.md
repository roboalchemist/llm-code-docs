# Source: https://help.cloudsmith.io/reference/orgs_teams_create.md

# Create a team for this organization.

Create a team for this organization.

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
    "/orgs/{org}/teams/": {
      "post": {
        "operationId": "orgs_teams_create",
        "summary": "Create a team for this organization.",
        "description": "Create a team for this organization.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OrganizationTeamRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Team created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationTeam"
                }
              }
            }
          },
          "400": {
            "description": "The team cannot be created.",
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
      "OrganizationTeam": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "description": {
            "title": "Description",
            "description": "A detailed description of the team.",
            "type": "string",
            "maxLength": 200,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "A descriptive name for the team.",
            "type": "string",
            "pattern": "^\\w[\\w \\-'\\.\\/()]+$",
            "maxLength": 200,
            "minLength": 1
          },
          "slug": {
            "title": "Slug",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "visibility": {
            "title": "Visibility",
            "type": "string",
            "enum": [
              "Visible",
              "Hidden"
            ],
            "default": "Visible"
          }
        }
      },
      "OrganizationTeamRequest": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "description": {
            "title": "Description",
            "description": "A detailed description of the team.",
            "type": "string",
            "maxLength": 200,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "A descriptive name for the team.",
            "type": "string",
            "pattern": "^\\w[\\w \\-'\\.\\/()]+$",
            "maxLength": 200,
            "minLength": 1
          },
          "slug": {
            "title": "Slug",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          },
          "visibility": {
            "title": "Visibility",
            "type": "string",
            "enum": [
              "Visible",
              "Hidden"
            ],
            "default": "Visible"
          }
        }
      }
    }
  }
}
```