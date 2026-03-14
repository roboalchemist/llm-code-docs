# Source: https://help.cloudsmith.io/reference/vulnerabilities_repo_list.md

# Lists scan results for a specific repository.

Lists scan results for a specific repository.

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
    "/vulnerabilities/{owner}/{repo}/": {
      "get": {
        "operationId": "vulnerabilities_repo_list",
        "summary": "Lists scan results for a specific repository.",
        "description": "Lists scan results for a specific repository.",
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
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/VulnerabilityScanResultsList"
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
          "vulnerabilities"
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
      "PackageVulnerability": {
        "required": [
          "identifier"
        ],
        "type": "object",
        "properties": {
          "identifier": {
            "title": "Identifier",
            "type": "string",
            "minLength": 1
          },
          "name": {
            "title": "Name",
            "description": "The name of this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "url": {
            "title": "Url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "version": {
            "title": "Version",
            "description": "The raw version for this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "VulnerabilityScanResultsList": {
        "required": [
          "identifier",
          "package",
          "scan_id"
        ],
        "type": "object",
        "properties": {
          "created_at": {
            "title": "Created at",
            "description": "The time this scan result was stored.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "has_vulnerabilities": {
            "title": "Has vulnerabilities",
            "description": "Do the results contain any known vulnerabilities?",
            "type": "boolean",
            "readOnly": true
          },
          "identifier": {
            "title": "Identifier",
            "type": "string",
            "minLength": 1
          },
          "max_severity": {
            "title": "Max severity",
            "type": "string",
            "enum": [
              "Unknown",
              "Low",
              "Medium",
              "High",
              "Critical"
            ],
            "default": "Unknown"
          },
          "num_vulnerabilities": {
            "title": "Num vulnerabilities",
            "type": "integer",
            "default": 0
          },
          "package": {
            "$ref": "#/components/schemas/PackageVulnerability"
          },
          "scan_id": {
            "title": "Scan id",
            "description": "Deprecated (23-05-15): Please use 'identifier' instead. Previously: A monotonically increasing number that identified a scan within a repository.",
            "type": "integer",
            "nullable": true
          }
        }
      }
    }
  }
}
```