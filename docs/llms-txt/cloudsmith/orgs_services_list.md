# Source: https://help.cloudsmith.io/reference/orgs_services_list.md

# Get a list of all services within an organization.

Get a list of all services within an organization.

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
    "/orgs/{org}/services/": {
      "get": {
        "operationId": "orgs_services_list",
        "summary": "Get a list of all services within an organization.",
        "description": "Get a list of all services within an organization.",
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
            "name": "query",
            "in": "query",
            "description": "A search term for querying of services within an Organization.Available options are: name, role",
            "required": false,
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "A field for sorting objects in ascending or descending order. Use `-` prefix for descending order (e.g., `-created_at`). Available options: created_at, name, role.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "created_at"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of services within the org",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Service"
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
      "ServiceTeams": {
        "required": [
          "slug"
        ],
        "type": "object",
        "properties": {
          "role": {
            "title": "Role",
            "description": "The team role associated with the service",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Manager"
          },
          "slug": {
            "title": "Slug",
            "description": "The teams associated with the service",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "minLength": 1
          }
        }
      },
      "Service": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "title": "Created by",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "created_by_url": {
            "title": "Created by url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "description": {
            "title": "Description",
            "description": "The description of the service",
            "type": "string",
            "maxLength": 1024,
            "minLength": 1
          },
          "key": {
            "title": "Key",
            "description": "The API key of the service",
            "type": "string",
            "readOnly": true
          },
          "key_expires_at": {
            "title": "Key expires at",
            "description": "The time at which the API key will expire. This will only be populated if the Organization has an active API Key Policy.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The name of the service",
            "type": "string",
            "maxLength": 120,
            "minLength": 1
          },
          "role": {
            "title": "Role",
            "description": "The role of the service.",
            "type": "string",
            "enum": [
              "Manager",
              "Member"
            ],
            "default": "Member"
          },
          "slug": {
            "title": "Slug",
            "description": "The slug of the service",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "teams": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ServiceTeams"
            }
          }
        }
      }
    }
  }
}
```