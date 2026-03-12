# Source: https://help.cloudsmith.io/reference/files_create.md

# Request URL(s) to upload new package file upload(s) to.

Request URL(s) to upload new package file upload(s) to.

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
    "/files/{owner}/{repo}/": {
      "post": {
        "operationId": "files_create",
        "summary": "Request URL(s) to upload new package file upload(s) to.",
        "description": "Request URL(s) to upload new package file upload(s) to.",
        "requestBody": {
          "$ref": "#/components/requestBodies/PackageFileUploadRequest"
        },
        "responses": {
          "202": {
            "description": "The upload request was accepted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageFileUpload"
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
      },
      "PackageFileUpload": {
        "type": "object",
        "properties": {
          "identifier": {
            "title": "Identifier",
            "description": "The identifier for the file to use when creating packages",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "minLength": 1
          },
          "upload_fields": {
            "title": "Upload fields",
            "description": "The dictionary of fields that must be sent with POST uploads",
            "type": "object",
            "readOnly": true,
            "nullable": true
          },
          "upload_headers": {
            "title": "Upload headers",
            "description": "The dictionary of headers that must be sent with uploads",
            "type": "object",
            "readOnly": true,
            "nullable": true
          },
          "upload_querystring": {
            "title": "Upload querystring",
            "description": "The querystring to use for the next-step POST or PUT upload",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "upload_url": {
            "title": "Upload url",
            "description": "The URL to use for the next-step POST or PUT upload",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "minLength": 1
          }
        }
      }
    }
  }
}
```