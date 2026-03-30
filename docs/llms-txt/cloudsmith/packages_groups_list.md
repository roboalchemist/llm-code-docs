# Source: https://help.cloudsmith.io/reference/packages_groups_list.md

# Return a list of Package Groups in a repository.

Return a list of Package Groups in a repository.

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
    "/packages/{owner}/{repo}/groups/": {
      "get": {
        "operationId": "packages_groups_list",
        "summary": "Return a list of Package Groups in a repository.",
        "description": "Return a list of Package Groups in a repository.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "A page number within the paginated result set.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "description": "Number of results to return per page.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "group_by",
            "in": "query",
            "description": "A field to group packages by. Available options: name, backend_kind.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "name"
            }
          },
          {
            "name": "hide_subcomponents",
            "in": "query",
            "description": "Whether to hide packages which are subcomponents of another package in the results",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "query",
            "in": "query",
            "description": "A search term for querying names, filenames, versions, distributions, architectures, formats, or statuses of packages.",
            "required": false,
            "schema": {
              "type": "string",
              "default": ""
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "A field for sorting objects in ascending or descending order. Use `-` prefix for descending order (e.g., `-name`). Available options: name, count, num_downloads, size, last_push, backend_kind.",
            "required": false,
            "schema": {
              "type": "string",
              "default": "name"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of package groups.",
            "content": {
              "application/json": {
                "schema": {
                  "required": [
                    "results"
                  ],
                  "type": "object",
                  "properties": {
                    "results": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PackageGroup"
                      }
                    }
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
      "PackageGroup": {
        "required": [
          "count",
          "last_push",
          "num_downloads",
          "size"
        ],
        "type": "object",
        "properties": {
          "backend_kind": {
            "title": "Backend kind",
            "type": "integer"
          },
          "count": {
            "title": "Count",
            "type": "integer",
            "nullable": true
          },
          "last_push": {
            "title": "Last push",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
            "minLength": 1
          },
          "num_downloads": {
            "title": "Num downloads",
            "type": "integer",
            "nullable": true
          },
          "size": {
            "title": "Size",
            "type": "integer",
            "nullable": true
          }
        }
      }
    }
  }
}
```