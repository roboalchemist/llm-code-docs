# Source: https://help.cloudsmith.io/reference/orgs_deny-policy_create.md

# Create a package deny policy.

Create a package deny policy.

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
    "/orgs/{org}/deny-policy/": {
      "post": {
        "operationId": "orgs_deny-policy_create",
        "summary": "Create a package deny policy.",
        "description": "Create a package deny policy.",
        "requestBody": {
          "$ref": "#/components/requestBodies/PackageDenyPolicyRequest"
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageDenyPolicy"
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
    "requestBodies": {
      "PackageDenyPolicyRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/PackageDenyPolicyRequest"
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
      "PackageDenyPolicy": {
        "required": [
          "package_query_string"
        ],
        "type": "object",
        "properties": {
          "action": {
            "title": "Action",
            "type": "string",
            "enum": [
              "Block downloads"
            ],
            "readOnly": true,
            "default": "Block downloads"
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
            "nullable": true
          },
          "enabled": {
            "title": "Enabled",
            "description": "Whether this rule is enabled or disabled.",
            "type": "boolean"
          },
          "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 100,
            "nullable": true
          },
          "package_query_string": {
            "title": "Package query string",
            "description": "Packages that match this query will trigger this deny rule.",
            "type": "string",
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
          "status": {
            "title": "Status",
            "type": "string",
            "enum": [
              "Pending",
              "In Progress",
              "Complete",
              "Cancelled",
              "Errored"
            ],
            "readOnly": true,
            "default": "In Progress"
          },
          "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        }
      },
      "PackageDenyPolicyRequest": {
        "required": [
          "package_query_string"
        ],
        "type": "object",
        "properties": {
          "description": {
            "title": "Description",
            "type": "string",
            "maxLength": 250,
            "nullable": true
          },
          "enabled": {
            "title": "Enabled",
            "description": "Whether this rule is enabled or disabled.",
            "type": "boolean"
          },
          "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 100,
            "nullable": true
          },
          "package_query_string": {
            "title": "Package query string",
            "description": "Packages that match this query will trigger this deny rule.",
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```