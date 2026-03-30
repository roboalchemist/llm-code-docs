# Source: https://help.cloudsmith.io/reference/packages_validate-upload_conan.md

# Validate parameters for create Conan package

Validate parameters for create Conan package

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
    "/packages/{owner}/{repo}/validate-upload/conan/": {
      "post": {
        "operationId": "packages_validate-upload_conan",
        "summary": "Validate parameters for create Conan package",
        "description": "Validate parameters for create Conan package",
        "requestBody": {
          "$ref": "#/components/requestBodies/ConanPackageUploadRequest"
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
      "ConanPackageUploadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ConanPackageUploadRequest"
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
      "ConanPackageUploadRequest": {
        "required": [
          "info_file",
          "manifest_file",
          "metadata_file",
          "package_file"
        ],
        "type": "object",
        "properties": {
          "conan_channel": {
            "title": "Conan channel",
            "description": "Conan channel.",
            "type": "string",
            "maxLength": 128,
            "minLength": 1,
            "nullable": true
          },
          "conan_prefix": {
            "title": "Conan prefix",
            "description": "Conan prefix (User).",
            "type": "string",
            "maxLength": 128,
            "minLength": 1,
            "nullable": true
          },
          "info_file": {
            "title": "Info file",
            "description": "The info file is an python file containing the package metadata.",
            "type": "string",
            "minLength": 1
          },
          "manifest_file": {
            "title": "Manifest file",
            "description": "The info file is an python file containing the package metadata.",
            "type": "string",
            "minLength": 1
          },
          "metadata_file": {
            "title": "Metadata file",
            "description": "The conan file is an python file containing the package metadata.",
            "type": "string",
            "minLength": 1
          },
          "name": {
            "title": "Name",
            "description": "The name of this package.",
            "type": "string",
            "maxLength": 200,
            "nullable": true
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
          },
          "version": {
            "title": "Version",
            "description": "The raw version for this package.",
            "type": "string",
            "maxLength": 255,
            "nullable": true
          }
        }
      }
    }
  }
}
```