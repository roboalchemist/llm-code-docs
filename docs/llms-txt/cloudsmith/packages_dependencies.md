# Source: https://help.cloudsmith.io/reference/packages_dependencies.md

# Get the list of dependencies for a package. Transitive dependencies are included where supported.

Get the list of dependencies for a package. Transitive dependencies are included where supported.

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
    "/packages/{owner}/{repo}/{identifier}/dependencies/": {
      "get": {
        "operationId": "packages_dependencies",
        "summary": "Get the list of dependencies for a package. Transitive dependencies are included where supported.",
        "description": "Get the list of dependencies for a package. Transitive dependencies are included where supported.",
        "responses": {
          "200": {
            "description": "Retrieved stored dependencies for specified package.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageDependencies"
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
      "PackageDependency": {
        "type": "object",
        "properties": {
          "dep_type": {
            "title": "Dep type",
            "type": "string",
            "enum": [
              "Depends",
              "Pre-Depends",
              "Recommends",
              "Suggests",
              "Enhances",
              "Replaces",
              "Breaks",
              "Built-Using",
              "Build-Depends",
              "Build-Depends-Indep",
              "Build-Conflicts",
              "Build-Conflicts-Indep",
              "Conflicts",
              "Provides",
              "Obsoletes",
              "Requires",
              "Runtime",
              "Development",
              "Compile",
              "Provided",
              "Test",
              "System",
              "Import",
              "Excluded",
              "Build-Requires",
              "Python-Requires"
            ],
            "readOnly": true,
            "default": "Depends"
          },
          "name": {
            "title": "Name",
            "type": "string",
            "readOnly": true,
            "maxLength": 255,
            "minLength": 1
          },
          "operator": {
            "title": "Operator",
            "type": "string",
            "enum": [
              "=",
              "!=",
              "<",
              "<<",
              "<=",
              ">",
              ">>",
              ">=",
              "~=",
              "~>",
              "matches"
            ],
            "readOnly": true,
            "default": "=",
            "nullable": true
          },
          "version": {
            "title": "Version",
            "type": "string",
            "readOnly": true,
            "maxLength": 128,
            "minLength": 1,
            "nullable": true
          }
        }
      },
      "PackageDependencies": {
        "required": [
          "dependencies"
        ],
        "type": "object",
        "properties": {
          "dependencies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PackageDependency"
            }
          }
        }
      }
    }
  }
}
```