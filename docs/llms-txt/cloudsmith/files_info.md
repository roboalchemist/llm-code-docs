# Source: https://help.cloudsmith.io/reference/files_info.md

# Get upload information to perform a multipart file upload.

Get upload information to perform a multipart file upload.

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
    "/files/{owner}/{repo}/{identifier}/info/": {
      "get": {
        "operationId": "files_info",
        "summary": "Get upload information to perform a multipart file upload.",
        "description": "Get upload information to perform a multipart file upload.",
        "parameters": [
          {
            "name": "filename",
            "in": "query",
            "description": "The filename of the file being uploaded",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "part_number",
            "in": "query",
            "description": "The part number to be uploaded next",
            "required": false,
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Information for multipart uploaded retrieved successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageFilePartsUpload"
                }
              }
            }
          },
          "400": {
            "description": "The provided upload file was not a multipart upload.",
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
      "PackageFilePartsUpload": {
        "type": "object",
        "properties": {
          "identifier": {
            "title": "Identifier",
            "description": "The identifier for the file to use uploading parts.",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "minLength": 1
          },
          "upload_querystring": {
            "title": "Upload querystring",
            "description": "The querystring to use for the next-step PUT upload.",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "upload_url": {
            "title": "Upload url",
            "description": "The URL to use for the next-step PUT upload",
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