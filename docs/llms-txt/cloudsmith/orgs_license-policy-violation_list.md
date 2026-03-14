# Source: https://help.cloudsmith.io/reference/orgs_license-policy-violation_list.md

# List all current license policy violations for this Organization.

List all current license policy violations for this Organization.

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
    "/orgs/{org}/license-policy-violation/": {
      "get": {
        "operationId": "orgs_license-policy-violation_list",
        "summary": "List all current license policy violations for this Organization.",
        "description": "List all current license policy violations for this Organization.",
        "parameters": [
          {
            "name": "cursor",
            "in": "query",
            "description": "The pagination cursor value.",
            "required": false,
            "schema": {
              "type": "string"
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
                  "required": [
                    "results"
                  ],
                  "type": "object",
                  "properties": {
                    "next": {
                      "type": "string",
                      "format": "uri",
                      "nullable": true
                    },
                    "previous": {
                      "type": "string",
                      "format": "uri",
                      "nullable": true
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PackageLicensePolicyViolationLog"
                      }
                    }
                  },
                  "title": "PackageLicensePolicyViolationLogCursorPage"
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
      "PackageVulnerability": {
        "required": [
          "identifier"
        ],
        "type": "object",
        "properties": {
          "identifier": {
            "title": "Identifier",
            "type": "string",
            "minLength": 1
          },
          "name": {
            "title": "Name",
            "description": "The name of this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "url": {
            "title": "Url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "version": {
            "title": "Version",
            "description": "The raw version for this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
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
      "PackageLicensePolicyViolationLog": {
        "required": [
          "package",
          "policy",
          "reasons"
        ],
        "type": "object",
        "properties": {
          "event_at": {
            "title": "Event at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "package": {
            "$ref": "#/components/schemas/PackageVulnerability"
          },
          "policy": {
            "$ref": "#/components/schemas/NestedLicensePolicy"
          },
          "reasons": {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            }
          }
        }
      }
    }
  }
}
```