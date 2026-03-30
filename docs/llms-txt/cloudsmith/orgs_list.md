# Source: https://help.cloudsmith.io/reference/orgs_list.md

# Get a list of all the organizations you are associated with.

Get a list of all the organizations you are associated with.

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
    "/orgs/": {
      "get": {
        "operationId": "orgs_list",
        "summary": "Get a list of all the organizations you are associated with.",
        "description": "Get a list of all the organizations you are associated with.",
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
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Organization"
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
      "parameters": []
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
      "Organization": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "country": {
            "title": "Country",
            "type": "string",
            "readOnly": true,
            "maxLength": 32,
            "minLength": 1,
            "nullable": true
          },
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "location": {
            "title": "Location",
            "description": "The city/town/area your organization is based in.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
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
            "description": "A short public descriptive for your organization.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      }
    }
  }
}
```