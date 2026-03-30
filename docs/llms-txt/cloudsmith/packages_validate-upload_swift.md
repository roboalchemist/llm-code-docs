# Source: https://help.cloudsmith.io/reference/packages_validate-upload_swift.md

# Validate parameters for create Swift package

Validate parameters for create Swift package

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
    "/packages/{owner}/{repo}/validate-upload/swift/": {
      "post": {
        "operationId": "packages_validate-upload_swift",
        "summary": "Validate parameters for create Swift package",
        "description": "Validate parameters for create Swift package",
        "requestBody": {
          "$ref": "#/components/requestBodies/SwiftPackageUploadRequest"
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
      "SwiftPackageUploadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/SwiftPackageUploadRequest"
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
      "SwiftPackageUploadRequest": {
        "required": [
          "name",
          "package_file",
          "scope",
          "version"
        ],
        "type": "object",
        "properties": {
          "author_name": {
            "title": "Author name",
            "description": "The name of the author of the package.",
            "type": "string",
            "minLength": 1
          },
          "author_org": {
            "title": "Author org",
            "description": "The organization of the author.",
            "type": "string",
            "minLength": 1
          },
          "license_url": {
            "title": "License url",
            "description": "The license URL of this package.",
            "type": "string",
            "format": "uri",
            "maxLength": 200,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The name of this package.",
            "type": "string",
            "maxLength": 200
          },
          "package_file": {
            "title": "Package file",
            "description": "The primary file for the package.",
            "type": "string",
            "minLength": 1
          },
          "readme_url": {
            "title": "Readme url",
            "description": "The URL of the readme for the package.",
            "type": "string",
            "format": "uri",
            "minLength": 1
          },
          "repository_url": {
            "title": "Repository url",
            "description": "The URL of the SCM repository for the package.",
            "type": "string",
            "format": "uri",
            "minLength": 1
          },
          "republish": {
            "title": "Republish",
            "description": "If true, the uploaded package will overwrite any others with the same attributes (e.g. same version); otherwise, it will be flagged as a duplicate.",
            "type": "boolean"
          },
          "scope": {
            "title": "Scope",
            "description": "A scope provides a namespace for related packages within the package registry.",
            "type": "string",
            "maxLength": 39,
            "minLength": 1
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
            "maxLength": 255
          }
        }
      }
    }
  }
}
```