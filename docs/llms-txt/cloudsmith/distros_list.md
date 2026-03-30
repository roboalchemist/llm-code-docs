# Source: https://help.cloudsmith.io/reference/distros_list.md

# Get a list of all supported distributions.

Get a list of all supported distributions.

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
    "/distros/": {
      "get": {
        "operationId": "distros_list",
        "summary": "Get a list of all supported distributions.",
        "description": "Get a list of all supported distributions.",
        "responses": {
          "200": {
            "description": "Available package formats retrieved",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/DistributionFull"
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
          "distros"
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
      "DistributionVersion": {
        "description": "A list of the versions for this distribution",
        "type": "object",
        "properties": {
          "name": {
            "title": "Name",
            "description": "The textual name for this version.",
            "type": "string",
            "maxLength": 64
          },
          "slug": {
            "title": "Slug",
            "description": "The slug identifier for this version",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          }
        }
      },
      "DistributionFull": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "format": {
            "title": "Format",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "format_url": {
            "title": "Format url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
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
          },
          "versions": {
            "description": "A list of the versions for this distribution",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DistributionVersion"
            },
            "readOnly": true
          }
        }
      }
    }
  }
}
```