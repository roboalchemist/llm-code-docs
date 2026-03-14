# Source: https://help.cloudsmith.io/reference/orgs_teams_list.md

# Get the details of all teams within an organization.

Get the details of all teams within an organization.

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
      "get": {
        "operationId": "orgs_teams_list",
        "summary": "Get the details of all teams within an organization.",
        "description": "Get the details of all teams within an organization.",
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
            "name": "for_user",
            "in": "query",
            "description": "Filter for teams that you are a member of.",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "query",
            "in": "query",
            "description": "A search term for querying of teams within an Organization.Available options are: name, slug, user, userslug",
            "required": false,
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "A field for sorting objects in ascending or descending order. Use `-` prefix for descending order (e.g., `-name`). Available options: name, members.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "name"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of teams within the org",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/OrganizationTeam"
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
            "description": "Org namespace not found",
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
      }
    }
  }
}
```