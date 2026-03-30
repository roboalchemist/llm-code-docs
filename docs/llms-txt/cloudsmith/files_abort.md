# Source: https://help.cloudsmith.io/reference/files_abort.md

# Abort a multipart file upload.

Abort a multipart file upload.

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
    "/files/{owner}/{repo}/{identifier}/abort/": {
      "post": {
        "operationId": "files_abort",
        "summary": "Abort a multipart file upload.",
        "description": "Abort a multipart file upload.",
        "requestBody": {
          "$ref": "#/components/requestBodies/PackageFileUploadRequest"
        },
        "responses": {
          "204": {
            "description": "The multipart upload was aborted successfully."
          },
          "400": {
            "description": "The multipart upload could not be aborted.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "Namespace (owner), repository or upload file not found",
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
          "files"
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
        },
        {
          "name": "identifier",
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
      "PackageFileUploadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/PackageFileUploadRequest"
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
      "PackageFileUploadRequest": {
        "required": [
          "filename"
        ],
        "type": "object",
        "properties": {
          "filename": {
            "title": "Filename",
            "description": "Filename for the package file upload.",
            "type": "string",
            "minLength": 1
          },
          "md5_checksum": {
            "title": "Md5 checksum",
            "description": "MD5 checksum for a POST-based package file upload.",
            "type": "string",
            "maxLength": 32,
            "minLength": 32
          },
          "method": {
            "title": "Method",
            "description": "The method to use for package file upload.",
            "type": "string",
            "enum": [
              "put_parts",
              "put",
              "post",
              "presigned",
              "unsigned_put"
            ],
            "default": "post"
          },
          "sha256_checksum": {
            "title": "Sha256 checksum",
            "description": "SHA256 checksum for a PUT-based package file upload.",
            "type": "string",
            "maxLength": 64,
            "minLength": 64
          }
        }
      }
    }
  }
}
```