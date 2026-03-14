# Source: https://help.cloudsmith.io/reference/orgs_license-policy_read.md

# Get a package license policy.

Get a package license policy.

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
    "/orgs/{org}/license-policy/{slug_perm}/": {
      "get": {
        "operationId": "orgs_license-policy_read",
        "summary": "Get a package license policy.",
        "description": "Get a package license policy.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OrganizationPackageLicensePolicy"
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
      "OrganizationPackageLicensePolicy": {
        "required": [
          "name",
          "spdx_identifiers"
        ],
        "type": "object",
        "properties": {
          "allow_unknown_licenses": {
            "title": "Allow unknown licenses",
            "type": "boolean"
          },
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "description": {
            "title": "Description",
            "type": "string",
            "maxLength": 250,
            "minLength": 1,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 100,
            "minLength": 1
          },
          "on_violation_quarantine": {
            "title": "On violation quarantine",
            "type": "boolean"
          },
          "package_query_string": {
            "title": "Package query string",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "spdx_identifiers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "uniqueItems": true
          },
          "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        }
      }
    }
  }
}
```