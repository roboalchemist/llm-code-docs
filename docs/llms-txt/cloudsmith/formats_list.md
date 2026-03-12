# Source: https://help.cloudsmith.io/reference/formats_list.md

# Get a list of all supported package formats.

Get a list of all supported package formats.

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
    "/formats/": {
      "get": {
        "operationId": "formats_list",
        "summary": "Get a list of all supported package formats.",
        "description": "Get a list of all supported package formats.",
        "responses": {
          "200": {
            "description": "Available package formats retrieved",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Format"
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
          "formats"
        ],
        "x-simplified": "fields[distributions]=slug,name"
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
      "Distribution": {
        "description": "The distributions supported by this package format",
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "slug": {
            "title": "Slug",
            "description": "The slug identifier for this distribution",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "variants": {
            "title": "Variants",
            "type": "string",
            "maxLength": 128,
            "nullable": true
          }
        },
        "nullable": true
      },
      "FormatSupportUpstream": {
        "description": "The upstream support for the package format",
        "required": [
          "auth_modes",
          "caching",
          "indexing",
          "proxying",
          "trust"
        ],
        "type": "object",
        "properties": {
          "auth_modes": {
            "description": "The authentication modes supported by the upstream format",
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "Username and Password",
                "Token",
                "Certificate and Key"
              ],
              "default": "Username and Password"
            }
          },
          "caching": {
            "title": "Caching",
            "description": "If true the upstream format supports caching",
            "type": "boolean"
          },
          "indexing": {
            "title": "Indexing",
            "description": "If true the upstream format supports indexing",
            "type": "boolean"
          },
          "indexing_behavior": {
            "title": "Indexing behavior",
            "description": "The behavior of the upstream when indexing",
            "type": "string",
            "enum": [
              "Unsupported",
              "Ahead-of-time (static) indexing",
              "Just-in-time (dynamic) indexing"
            ],
            "default": "Unsupported"
          },
          "proxying": {
            "title": "Proxying",
            "description": "If true the upstream format supports proxying",
            "type": "boolean"
          },
          "signature_verification": {
            "title": "Signature verification",
            "description": "The signature verification supported by the upstream format",
            "type": "string",
            "enum": [
              "Unsupported",
              "Repository Metadata",
              "Packages",
              "Repository Metadata and Packages"
            ],
            "default": "Unsupported"
          },
          "trust": {
            "title": "Trust",
            "description": "If true the upstream format supports configurable trust levels (trusted vs untrusted) for upstream sources.",
            "type": "boolean"
          }
        }
      },
      "FormatSupport": {
        "description": "A set of what the package format supports",
        "required": [
          "dependencies",
          "distributions",
          "file_lists",
          "filepaths",
          "metadata",
          "upstreams",
          "versioning"
        ],
        "type": "object",
        "properties": {
          "dependencies": {
            "title": "Dependencies",
            "description": "If true the package format supports dependencies",
            "type": "boolean"
          },
          "distributions": {
            "title": "Distributions",
            "description": "If true the package format supports distributions",
            "type": "boolean"
          },
          "file_lists": {
            "title": "File lists",
            "description": "If true the package format supports file lists",
            "type": "boolean"
          },
          "filepaths": {
            "title": "Filepaths",
            "description": "If true the package format supports filepaths",
            "type": "boolean"
          },
          "metadata": {
            "title": "Metadata",
            "description": "If true the package format supports metadata",
            "type": "boolean"
          },
          "upstreams": {
            "$ref": "#/components/schemas/FormatSupportUpstream"
          },
          "versioning": {
            "title": "Versioning",
            "description": "If true the package format supports versioning",
            "type": "boolean"
          }
        }
      },
      "Format": {
        "required": [
          "description",
          "extensions",
          "name",
          "premium",
          "slug",
          "supports"
        ],
        "type": "object",
        "properties": {
          "description": {
            "title": "Description",
            "description": "Description of the package format",
            "type": "string",
            "minLength": 1
          },
          "distributions": {
            "description": "The distributions supported by this package format",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Distribution"
            },
            "nullable": true
          },
          "extensions": {
            "description": "A non-exhaustive list of extensions supported",
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            }
          },
          "name": {
            "title": "Name",
            "description": "Name for the package format",
            "type": "string",
            "minLength": 1
          },
          "premium": {
            "title": "Premium",
            "description": "If true the package format is a premium-only feature",
            "type": "boolean"
          },
          "premium_plan_id": {
            "title": "Premium plan id",
            "description": "The minimum plan id required for this package format",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "premium_plan_name": {
            "title": "Premium plan name",
            "description": "The minimum plan name required for this package format",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "slug": {
            "title": "Slug",
            "description": "Slug for the package format",
            "type": "string",
            "minLength": 1
          },
          "supports": {
            "$ref": "#/components/schemas/FormatSupport"
          }
        }
      }
    }
  }
}
```