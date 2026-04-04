# Source: https://help.cloudsmith.io/reference/repo_retention_read.md

# Retrieve the retention rules for the repository.

Retrieve the retention rules for the repository.

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
    "/repos/{owner}/{repo}/retention/": {
      "get": {
        "operationId": "repo_retention_read",
        "summary": "Retrieve the retention rules for the repository.",
        "description": "Retrieve the retention rules for the repository.",
        "responses": {
          "200": {
            "description": "Retrieved the retention rules for the repository.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryRetentionRules"
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
            "description": "Owner namespace or repository not found",
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
          "repos"
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
      "RepositoryRetentionRules": {
        "type": "object",
        "properties": {
          "retention_count_limit": {
            "title": "Retention count limit",
            "description": "The maximum X number of packages to retain.",
            "type": "integer",
            "maximum": 10000,
            "minimum": 0
          },
          "retention_days_limit": {
            "title": "Retention days limit",
            "description": "The X number of days of packages to retain.",
            "type": "integer",
            "maximum": 180,
            "minimum": 0
          },
          "retention_enabled": {
            "title": "Retention Enabled?",
            "description": "If checked, the retention lifecycle rules will be activated for the repository. Any packages that don't match will be deleted automatically, and the rest are retained.",
            "type": "boolean"
          },
          "retention_group_by_format": {
            "title": "Retention group by format",
            "description": "If checked, retention will apply to packages by package formats rather than across all package formats.For example, when retaining by a limit of 1 and you upload PythonPkg 1.0 and RubyPkg 1.0, no packages are deleted because they are different formats.",
            "type": "boolean"
          },
          "retention_group_by_name": {
            "title": "Retention Group By Name?",
            "description": "If checked, retention will apply to groups of packages by name rather than all packages.<br>For example, when retaining by a limit of 1 and you upload PkgA 1.0, PkgB 1.0 and PkgB 1.1; only PkgB 1.0 is deleted because there are two (2) PkgBs and one (1) PkgA.",
            "type": "boolean"
          },
          "retention_group_by_package_type": {
            "title": "Retention Group By Package Type?",
            "description": "If checked, retention will apply to packages by package type (e.g. by binary, by source, etc.), rather than across all package types for one or more formats. <br>For example, when retaining by a limit of 1 and you upload DebPackage 1.0 and DebSourcePackage 1.0, no packages are deleted because they are different package types, binary and source respectively.",
            "type": "boolean"
          },
          "retention_package_query_string": {
            "title": "Retention package query string",
            "description": "A package search expression which, if provided, filters the packages to be deleted.<br>For example, a search expression of `name:foo` will result in only packages called 'foo' being deleted, or a search expression of `tag:~latest` will prevent any packages tagged 'latest' from being deleted.<br>Refer to the Cloudsmith documentation for package query syntax.",
            "type": "string",
            "nullable": true
          },
          "retention_size_limit": {
            "title": "Retention size limit",
            "description": "The maximum X total size (in bytes) of packages to retain.",
            "type": "integer",
            "maximum": 21474836480,
            "minimum": 0
          }
        }
      }
    }
  }
}
```