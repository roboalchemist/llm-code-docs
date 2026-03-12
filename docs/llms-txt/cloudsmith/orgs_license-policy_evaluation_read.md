# Source: https://help.cloudsmith.io/reference/orgs_license-policy_evaluation_read.md

# Retrieve an evaluation request for this policy.

Retrieve an evaluation request for this policy.

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
    "/orgs/{org}/license-policy/{policy_slug_perm}/evaluation/{slug_perm}/": {
      "get": {
        "operationId": "orgs_license-policy_evaluation_read",
        "summary": "Retrieve an evaluation request for this policy.",
        "description": "Retrieve an evaluation request for this policy.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageLicensePolicyEvaluationRequest"
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
          "name": "policy_slug_perm",
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
      "NestedLicensePolicy": {
        "required": [
          "spdx_identifiers"
        ],
        "type": "object",
        "properties": {
          "allow_unknown_licenses": {
            "title": "Allow unknown licenses",
            "type": "boolean",
            "readOnly": true
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
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "on_violation_quarantine": {
            "title": "On violation quarantine",
            "type": "boolean",
            "readOnly": true
          },
          "package_query_string": {
            "title": "Package query string",
            "type": "string",
            "readOnly": true,
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
          },
          "url": {
            "title": "Url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          }
        }
      },
      "PackageLicensePolicyEvaluationRequest": {
        "type": "object",
        "properties": {
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "evaluation_count": {
            "title": "Evaluation count",
            "type": "integer",
            "readOnly": true
          },
          "policy": {
            "$ref": "#/components/schemas/NestedLicensePolicy"
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
            "default": "Pending"
          },
          "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "violation_count": {
            "title": "Violation count",
            "type": "integer",
            "readOnly": true
          }
        }
      }
    }
  }
}
```