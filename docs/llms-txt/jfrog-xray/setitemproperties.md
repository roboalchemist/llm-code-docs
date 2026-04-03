# Source: https://docs.jfrog.com/artifactory/reference/setitemproperties.md

# Set Item Properties

Attach properties to an existing item (file, folder, repository, or Release Bundle v2).

To supply special characters (comma (,), backslash(\), pipe(|), equals(=)) as a key/value you must add an encoded backslash (%5C) before them. For example: ..?properties=a=1%5C=1 will attach key a with 1=1 as value.

Requires Artifactory Pro, supported by local and local-cached repositories only.

Since: 2.3.0  
Security: Requires a privileged user (can be anonymous)

Tip: Starting with Artifactory 7.104.x, it is possible to define an upper limit on the number of artifacts on which property updates can be performed at one time. For example, if you revise a folder property and the folder contains more items than the limit defined in this system parameter, the operation will fail. This feature is useful for preventing heavy loads on the database. The limit is defined using the system parameter, artifactory.max.artifacts.set.properties.recursive. By default, this feature is off. There is no default value when turned on.


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "JFrog Artifactory Artifacts & Storage API",
    "description": "REST API for managing artifacts, storage, and related operations in JFrog Artifactory",
    "version": "1.0.0",
    "contact": {
      "name": "JFrog Support"
    }
  },
  "servers": [
    {
      "url": "https://{jfrog_url}/artifactory/api",
      "description": "JFrog Platform",
      "variables": {
        "jfrog_url": {
          "default": "myserver.jfrog.io",
          "description": "Your JFrog Platform hostname (e.g., mycompany.jfrog.io)"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Item Management APIs",
      "description": "Item management operations including properties, deployment, and deletion"
    }
  ],
  "paths": {
    "/storage/{repoKey}/{itemPath}": {
      "put": {
        "tags": [
          "Item Management APIs"
        ],
        "summary": "Set Item Properties",
        "operationId": "setItemProperties",
        "description": "Attach properties to an existing item (file, folder, repository, or Release Bundle v2).\n\nTo supply special characters (comma (,), backslash(\\), pipe(|), equals(=)) as a key/value you must add an encoded backslash (%5C) before them. For example: ..?properties=a=1%5C=1 will attach key a with 1=1 as value.\n\nRequires Artifactory Pro, supported by local and local-cached repositories only.\n\nSince: 2.3.0  \nSecurity: Requires a privileged user (can be anonymous)\n\nTip: Starting with Artifactory 7.104.x, it is possible to define an upper limit on the number of artifacts on which property updates can be performed at one time. For example, if you revise a folder property and the folder contains more items than the limit defined in this system parameter, the operation will fail. This feature is useful for preventing heavy loads on the database. The limit is defined using the system parameter, artifactory.max.artifacts.set.properties.recursive. By default, this feature is off. There is no default value when turned on.\n",
        "parameters": [
          {
            "name": "repoKey",
            "in": "path",
            "description": "Repository key",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "itemPath",
            "in": "path",
            "description": "Item path within the repository",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          },
          {
            "name": "properties",
            "in": "query",
            "description": "Properties to set in format: properties=key1=value1[,value2][|key2=value3]. Multiple properties can be separated by semicolon (;) or pipe (|).",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "recursive",
            "in": "query",
            "description": "Apply properties recursively to all items in folder (0 or 1). For folders, , property attachment is recursive by default.",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ],
              "default": 1
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Properties set successfully (no content)"
          },
          "400": {
            "description": "Bad Request - The properties parameter is missing or malformed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Bad Credentials - Authentication failed. A valid token is required.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Permission Denied - The user does not have annotate permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - The specified item or repository does not exist.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "errors": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "status": {
                  "type": "integer",
                  "description": "HTTP status code"
                },
                "message": {
                  "type": "string",
                  "description": "Error message"
                }
              }
            }
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "JWT token authentication"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication"
      }
    }
  },
  "security": [
    {
      "bearerAuth": []
    },
    {
      "basicAuth": []
    }
  ]
}
```