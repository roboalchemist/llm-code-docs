# Source: https://docs.jfrog.com/artifactory/reference/getstorageitem.md

# Get Storage Item Information

Returns different types of information about an item based on query parameters.

**Query parameters are mutually exclusive** - only one operation type can be requested at a time:
- list - Get file/folder listing (flat or deep)
- stats - Get file statistics (download count, last download info)
- lastModified - Get last modified timestamp
- properties - Get item properties
- permissions - Get item permissions
- No parameters - Get folder or file info

Since: 2.2.1  
Security: Requires a privileged user (can be anonymous)


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
      "get": {
        "tags": [
          "Item Management APIs"
        ],
        "summary": "Get Storage Item Information",
        "description": "Returns different types of information about an item based on query parameters.\n\n**Query parameters are mutually exclusive** - only one operation type can be requested at a time:\n- list - Get file/folder listing (flat or deep)\n- stats - Get file statistics (download count, last download info)\n- lastModified - Get last modified timestamp\n- properties - Get item properties\n- permissions - Get item permissions\n- No parameters - Get folder or file info\n\nSince: 2.2.1  \nSecurity: Requires a privileged user (can be anonymous)\n",
        "operationId": "getStorageItem",
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
            "description": "Comma-separated list of property keys to retrieve. **Mutually exclusive with other query parameters.**",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "lastModified",
            "in": "query",
            "description": "Returns the last modified item at the given path. If the given path is a folder, the latest last modified item is searched for recursively. **Mutually exclusive with other query parameters.**",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "stats",
            "in": "query",
            "description": "Returns item statistics (download count, last download date, last downloader). **Mutually exclusive with other query parameters.**",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "permissions",
            "in": "query",
            "description": "Returns item permissions. **Mutually exclusive with other query parameters.**",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "list",
            "in": "query",
            "description": "Get a flat (the default) or deep listing of the files and folders. **Mutually exclusive with other query parameters except listing-related parameters (deep, depth, listFolders, etc.).**",
            "required": false,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "deep",
            "in": "query",
            "description": "Deep listing (0 or 1). Used with list parameter only.",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            }
          },
          {
            "name": "depth",
            "in": "query",
            "description": "Optional depth to limit the results for deep listing. Used with list parameter only.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "listFolders",
            "in": "query",
            "description": "Include folders in listing (0 or 1). Used with list parameter only.",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            }
          },
          {
            "name": "mdTimestamps",
            "in": "query",
            "description": "Include metadata timestamp values (0 or 1). Used with list parameter only.",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            }
          },
          {
            "name": "includeRootPath",
            "in": "query",
            "description": "Include folder root path (0 or 1). Used with list parameter only.",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                0,
                1
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved item information",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/FileList"
                    },
                    {
                      "$ref": "#/components/schemas/FileStatistics"
                    },
                    {
                      "$ref": "#/components/schemas/ItemLastModified"
                    },
                    {
                      "$ref": "#/components/schemas/ItemProperties"
                    },
                    {
                      "$ref": "#/components/schemas/ItemPermissions"
                    },
                    {
                      "$ref": "#/components/schemas/FolderInfo"
                    },
                    {
                      "$ref": "#/components/schemas/FileInfo"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Bad Request - Invalid query parameter combination or malformed path.",
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
            "description": "Permission Denied - The user does not have the necessary permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found - The specified item does not exist.",
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
      "ItemProperties": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      },
      "ItemPermissions": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "principals": {
            "type": "object",
            "properties": {
              "users": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "groups": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      },
      "FolderInfo": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "repo": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "createdBy": {
            "type": "string"
          },
          "lastModified": {
            "type": "string",
            "format": "date-time"
          },
          "modifiedBy": {
            "type": "string"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "children": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FolderChild"
            }
          }
        }
      },
      "FolderChild": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "folder": {
            "type": "boolean"
          }
        }
      },
      "FileInfo": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "downloadUri": {
            "type": "string"
          },
          "repo": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "remoteUrl": {
            "type": "string"
          },
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "createdBy": {
            "type": "string"
          },
          "lastModified": {
            "type": "string",
            "format": "date-time"
          },
          "modifiedBy": {
            "type": "string"
          },
          "lastUpdated": {
            "type": "string",
            "format": "date-time"
          },
          "size": {
            "type": "string",
            "description": "Size in bytes"
          },
          "mimeType": {
            "type": "string"
          },
          "checksums": {
            "$ref": "#/components/schemas/Checksums"
          },
          "originalChecksums": {
            "$ref": "#/components/schemas/Checksums"
          }
        }
      },
      "Checksums": {
        "type": "object",
        "properties": {
          "md5": {
            "type": "string"
          },
          "sha1": {
            "type": "string"
          },
          "sha256": {
            "type": "string"
          }
        }
      },
      "ItemLastModified": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "lastModified": {
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "FileStatistics": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "lastDownloaded": {
            "type": "integer",
            "format": "int64",
            "description": "Timestamp in milliseconds"
          },
          "downloadCount": {
            "type": "integer",
            "format": "int64"
          },
          "lastDownloadedBy": {
            "type": "string"
          }
        }
      },
      "FileList": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FileListItem"
            }
          }
        }
      },
      "FileListItem": {
        "type": "object",
        "properties": {
          "uri": {
            "type": "string"
          },
          "size": {
            "type": "string",
            "description": "Size in bytes, or \"-1\" for folders"
          },
          "lastModified": {
            "type": "string",
            "format": "date-time"
          },
          "folder": {
            "type": "boolean"
          },
          "sha1": {
            "type": "string"
          },
          "mdTimestamps": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "format": "date-time"
            }
          }
        }
      },
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