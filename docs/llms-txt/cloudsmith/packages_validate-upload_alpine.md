# Source: https://help.cloudsmith.io/reference/packages_validate-upload_alpine.md

# Validate parameters for create Alpine package

Validate parameters for create Alpine package

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
    "/packages/{owner}/{repo}/validate-upload/alpine/": {
      "post": {
        "operationId": "packages_validate-upload_alpine",
        "summary": "Validate parameters for create Alpine package",
        "description": "Validate parameters for create Alpine package",
        "requestBody": {
          "$ref": "#/components/requestBodies/AlpinePackageUploadRequest"
        },
        "responses": {
          "204": {
            "description": "Validation was successful, parameters are OK."
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
            "description": "Namespace (owner) or repository not found",
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
          "packages"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "repo",
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
      "AlpinePackageUploadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AlpinePackageUploadRequest"
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
      "AlpinePackageUploadRequest": {
        "required": [
          "distribution",
          "package_file"
        ],
        "type": "object",
        "properties": {
          "distribution": {
            "title": "Distribution",
            "description": "The distribution to store the package for.",
            "type": "string",
            "minLength": 1
          },
          "package_file": {
            "title": "Package file",
            "description": "The primary file for the package.",
            "type": "string",
            "minLength": 1
          },
          "republish": {
            "title": "Republish",
            "description": "If true, the uploaded package will overwrite any others with the same attributes (e.g. same version); otherwise, it will be flagged as a duplicate.",
            "type": "boolean"
          },
          "tags": {
            "title": "Tags",
            "description": "A comma-separated values list of tags to add to the package.",
            "type": "string",
            "maxLength": 1024,
            "minLength": 1,
            "nullable": true
          }
        }
      }
    }
  }
}
```