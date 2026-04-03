# Source: https://docs.jfrog.com/artifactory/reference/zapcache.md

# Zap Cache

Zapping cache invalidates all cached metadata artifacts downloaded from central registries like pypi.org, repo1.maven.org, registry.npmjs.org and stored in remote repo cache to speed up remote repo actions. The zapping action does not invalidate immutable artifacts (like software binaries).

After Zapping, whenever an invalidated metadata artifact is needed, Artifactory refreshes it from the central registry first. If unavailable, it falls back to the stale version.

Zapping the cache may slow down for clients who download packages requiring stale metadata updates.

Zapping cache solves:
- Resolving Cache Issues: If there are problems with the cached packages artifacts, such as corruption or inconsistencies with the central repository, zapping the cache fixes these issues.

Since: 7.49.3

Security: Requires a privileged user, Manage or Delete permissions on the Remote Repository.


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
      "name": "System Operations",
      "description": "System-level operations"
    }
  ],
  "paths": {
    "/zap/{repoPath}": {
      "post": {
        "tags": [
          "System Operations"
        ],
        "summary": "Zap Cache",
        "description": "Zapping cache invalidates all cached metadata artifacts downloaded from central registries like pypi.org, repo1.maven.org, registry.npmjs.org and stored in remote repo cache to speed up remote repo actions. The zapping action does not invalidate immutable artifacts (like software binaries).\n\nAfter Zapping, whenever an invalidated metadata artifact is needed, Artifactory refreshes it from the central registry first. If unavailable, it falls back to the stale version.\n\nZapping the cache may slow down for clients who download packages requiring stale metadata updates.\n\nZapping cache solves:\n- Resolving Cache Issues: If there are problems with the cached packages artifacts, such as corruption or inconsistencies with the central repository, zapping the cache fixes these issues.\n\nSince: 7.49.3\n\nSecurity: Requires a privileged user, Manage or Delete permissions on the Remote Repository.\n",
        "operationId": "zapCache",
        "parameters": [
          {
            "name": "repoPath",
            "in": "path",
            "description": "Repository path",
            "required": true,
            "schema": {
              "type": "string",
              "minLength": 1
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Cache zapped successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "Message": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - The repoPath does not resolve to a valid remote repository or cache.",
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
            "description": "Permission Denied - The user does not have Manage or Delete permissions on the Remote Repository.",
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