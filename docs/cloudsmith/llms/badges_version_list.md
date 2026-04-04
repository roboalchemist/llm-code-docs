# Source: https://help.cloudsmith.io/reference/badges_version_list.md

# Get latest package version for a package or package group.

Get latest package version for a package or package group.

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
    "/badges/version/{owner}/{repo}/{package_format}/{package_name}/{package_version}/{package_identifiers}/": {
      "get": {
        "operationId": "badges_version_list",
        "summary": "Get latest package version for a package or package group.",
        "description": "Get latest package version for a package or package group.",
        "parameters": [
          {
            "name": "badge_token",
            "in": "query",
            "description": "Badge token to authenticate for private packages",
            "required": false,
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "cacheSeconds",
            "in": "query",
            "description": "Override the shields.io badge cacheSeconds value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "300"
            }
          },
          {
            "name": "color",
            "in": "query",
            "description": "Override the shields.io badge color value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "12577E"
            }
          },
          {
            "name": "label",
            "in": "query",
            "description": "Override the shields.io badge label value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "cloudsmith"
            }
          },
          {
            "name": "labelColor",
            "in": "query",
            "description": "Override the shields.io badge labelColor value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "021F2F"
            }
          },
          {
            "name": "logoColor",
            "in": "query",
            "description": "Override the shields.io badge logoColor value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "45B6EE"
            }
          },
          {
            "name": "logoWidth",
            "in": "query",
            "description": "Override the shields.io badge logoWidth value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "10"
            }
          },
          {
            "name": "render",
            "in": "query",
            "description": "If true, badge will be rendered",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "shields",
            "in": "query",
            "description": "If true, a shields response will be generated",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "show_latest",
            "in": "query",
            "description": "If true, for latest version badges a '(latest)' suffix is added",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "style",
            "in": "query",
            "description": "Override the shields.io badge style value.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "flat-square"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageVersionBadge"
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
          "badges"
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
          "name": "package_format",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "package_name",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "package_version",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "package_identifiers",
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
      "PackageVersionBadge": {
        "type": "object",
        "properties": {}
      }
    }
  }
}
```