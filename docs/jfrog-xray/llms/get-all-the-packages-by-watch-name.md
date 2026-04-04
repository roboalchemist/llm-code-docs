# Source: https://docs.jfrog.com/security/reference/get-all-the-packages-by-watch-name.md

# Get Component List Per Watch

Returns package details for all packages in repositories watched by the specified watch. Requires Reports Manager permission.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v2/component/data/{name}": {
      "get": {
        "operationId": "get-all-the-packages-by-watch-name",
        "summary": "Get Component List Per Watch",
        "description": "Returns package details for all packages in repositories watched by the specified watch. Requires Reports Manager permission.",
        "tags": [
          "Components V2"
        ],
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "The watch name to retrieve component data for."
          },
          {
            "name": "limit",
            "in": "query",
            "required": false,
            "description": "Maximum number of results to return (default 1000).",
            "schema": {
              "type": "integer",
              "default": 1000
            }
          },
          {
            "name": "offset",
            "in": "query",
            "required": false,
            "description": "Number of results to skip for pagination (default 0).",
            "schema": {
              "type": "integer",
              "default": 0
            }
          },
          {
            "name": "from",
            "in": "query",
            "required": false,
            "description": "Start date-time for filtering components (ISO 8601 format).",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "to",
            "in": "query",
            "required": false,
            "description": "End date-time for filtering components (ISO 8601 format).",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Streamed JSON array of package details.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "description": "Array of package detail objects for components in watched repositories.",
                  "items": {
                    "type": "object",
                    "properties": {
                      "name": {
                        "type": "string",
                        "description": "Package name."
                      },
                      "version": {
                        "type": "string",
                        "description": "Package version."
                      },
                      "type": {
                        "type": "string",
                        "description": "Package type (e.g., npm, maven)."
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request parameters or watch does not include repository resources.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "Watch not found.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    }
  },
  "tags": [
    {
      "name": "Components V2",
      "description": "APIs from Components V2"
    }
  ]
}
```