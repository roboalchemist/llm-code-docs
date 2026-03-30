# Source: https://docs.jit.io/reference/artifacts-1.md

# Return all artifacts

Returns artifacts that can be downloaded.

Jit supports the following artifact types: 'SBOM', 'WIZ_ISSUES', 'ZAP_SCANNED_URLS_web' and 'ZAP_SCANNED_URLS_api'.

Some artifacts can only be downloaded by Premium users. To download, upgrade to the Premium users pricing plan.

**Requires the following permission:**
`jit.artifacts.read`

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Jit Public APIs",
    "description": "Jit Public APIs.\n\nThe API requires that you log in first and obtain a JWT authentication bearer token:\n\nJIT Platform generates CLIENT_ID and SECRET under `Settings -> Users & Permissions -> API Tokens`\n\n For more information, refer to [Users and Permissions](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
    "version": "1",
    "termsOfService": "https://www.jit.io/legal/terms"
  },
  "servers": [
    {
      "url": "https://api.jit.io",
      "description": "Jit API domain"
    }
  ],
  "externalDocs": {
    "url": "https://docs.jit.io/docs",
    "description": "Jit docs"
  },
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "tags": [
    {
      "name": "Artifacts",
      "description": "Explore artifacts with the ability to download them.",
      "externalDocs": {
        "url": "https://docs.jit.io/docs",
        "description": "Learn more on JIT"
      }
    }
  ],
  "paths": {
    "/artifacts/": {
      "get": {
        "summary": "Return all artifacts",
        "description": "Returns artifacts that can be downloaded.\n\nJit supports the following artifact types: 'SBOM', 'WIZ_ISSUES', 'ZAP_SCANNED_URLS_web' and 'ZAP_SCANNED_URLS_api'.\n\nSome artifacts can only be downloaded by Premium users. To download, upgrade to the Premium users pricing plan.\n\n**Requires the following permission:**\n`jit.artifacts.read`",
        "operationId": "artifacts",
        "parameters": [
          {
            "name": "artifact_type",
            "in": "query",
            "description": "Filter artifacts based on their associated artifact Type.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/artifact_type"
            }
          },
          {
            "name": "asset_type",
            "in": "query",
            "description": "Filter artifacts based on their associated asset Type.\n\n**Important**: This parameter should be used together with `artifact_type`. It is not compatible with `asset_id`.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/asset_type"
            }
          },
          {
            "name": "asset_id",
            "in": "query",
            "description": "Use the unique asset Identifier for precise filtering.\n\n**Important**: Incompatible with concurrent use of `asset_type`.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/asset_id"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "The maximum number of results to be returned per page.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/limit"
            }
          },
          {
            "name": "after",
            "in": "query",
            "description": "Cursor for next request to get the results page. Null means no more results.",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/after"
            }
          }
        ],
        "tags": [
          "Artifacts"
        ],
        "responses": {
          "200": {
            "description": "Paginated list of artifacts returned successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedArtifactsResponse"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "400": {
            "description": "Bad request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BadRequest"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UnauthorizedAuthorizerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ForbiddenError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalServerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
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
      "BadRequest": {
        "title": "ValidationErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INVALID_INPUT",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable message containing fields that failed validation.",
            "example": "sample_field1: ensure this value is greater than or equal to 5\ninner_object -> sample_field2: field required",
            "type": "string"
          },
          "invalid_parameters": {
            "title": "Input parameters to errors map",
            "description": "Dictionary mapping input parameter for their corresponding error messages for programmatic use.\n\n**Important**: This dictionary should match your input. Parameters with invalid inputs display their respective messages.",
            "nullable": true,
            "example": {
              "sample_field1": "ensure this value is greater than or equal to 5",
              "inner_object": {
                "sample_field2": "field required"
              }
            },
            "type": "object"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "ForbiddenError": {
        "title": "ForbiddenErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "FORBIDDEN",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Request is missing the required permissions.",
            "type": "string"
          },
          "missing_permissions": {
            "title": "Missing permissions",
            "description": "List of missing permissions.",
            "nullable": true,
            "example": [
              "jit.category.write",
              "jit.category.read"
            ],
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "InternalServerError": {
        "title": "InternalErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INTERNAL_SERVER_ERROR",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Some error message indicating the issue that occurred",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "PaginatedArtifactsResponse": {
        "title": "PaginatedArtifactsResponse",
        "type": "object",
        "properties": {
          "metadata": {
            "title": "Metadata",
            "description": "Required fields to paginate over the response",
            "example": {
              "limit": 5,
              "count": 1,
              "after": "CURSOR"
            },
            "allOf": [
              {
                "title": "PaginatedResponseMetadata",
                "type": "object",
                "properties": {
                  "limit": {
                    "title": "Results limit",
                    "description": "Maximum number of requested results.",
                    "example": 5,
                    "type": "integer"
                  },
                  "count": {
                    "title": "Number of results",
                    "description": "Number of results in the data field.",
                    "example": 3,
                    "type": "integer"
                  },
                  "after": {
                    "title": "Cursor",
                    "description": "Cursor for next request to get the results page. Null means no more results.",
                    "example": "CURSOR",
                    "type": "string"
                  }
                },
                "required": [
                  "limit",
                  "count"
                ]
              }
            ]
          },
          "data": {
            "title": "Data",
            "description": "List of JSONs holding the requested data.",
            "type": "array",
            "items": {
              "title": "ArtifactMetadataResponse",
              "type": "object",
              "properties": {
                "artifact_type": {
                  "title": "Artifact Type",
                  "description": "The artifact's Type",
                  "example": "SBOM",
                  "readOnly": true,
                  "enum": [
                    "SBOM",
                    "WIZ_ISSUES",
                    "ZAP_SCANNED_URLS_web",
                    "ZAP_SCANNED_URLS_api"
                  ],
                  "type": "string"
                },
                "asset_type": {
                  "title": "Asset type",
                  "description": "The asset's Type.",
                  "example": "repo",
                  "enum": [
                    "repo",
                    "org",
                    "aws_account",
                    "gcp_account",
                    "azure_account",
                    "web",
                    "api",
                    "image"
                  ],
                  "type": "string"
                },
                "asset_id": {
                  "title": "Asset ID",
                  "description": "The artifact’s unique Identifier.",
                  "example": "c7a1c231-f2d1-4352-9ca0-fa2da8bf623c",
                  "type": "string"
                },
                "version": {
                  "title": "Version",
                  "description": "The artifact's version.",
                  "default": "1",
                  "example": "1",
                  "readOnly": true,
                  "type": "string"
                },
                "created_at": {
                  "title": "Creation Date",
                  "description": "Date and time the artifact was created.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                  "example": "2023-10-17 19:09:40.236710",
                  "readOnly": true,
                  "type": "string"
                },
                "created_by": {
                  "title": "Created By",
                  "description": "The entity creating the artifact, which is always `Jit`.",
                  "default": "Jit",
                  "example": "Jit",
                  "readOnly": true,
                  "type": "string"
                },
                "extra_data": {
                  "title": "Additional Metadata",
                  "description": "Additional metadata that may contain key-value pairs that help identify the artifact.",
                  "example": {
                    "asset_name": "my-awesome-repo"
                  },
                  "readOnly": true,
                  "type": "object",
                  "additionalProperties": {
                    "type": "string"
                  }
                },
                "artifact_id": {
                  "title": "Artifact ID",
                  "description": "The artifact’s unique Identifier.",
                  "example": "01HJ6QRS7YD0N57658PPWR17CG",
                  "readOnly": true,
                  "type": "string"
                },
                "updated_at": {
                  "title": "Modified Date",
                  "description": "Date and time the artifact was modified.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.",
                  "example": "2023-10-17 19:09:40.236710",
                  "readOnly": true,
                  "type": "string"
                },
                "entitled": {
                  "title": "Is entitled to download the artifact",
                  "description": "This artifact can only be downloaded by Premium users. To download, upgrade to the Premium users pricing plan.",
                  "default": true,
                  "example": true,
                  "readOnly": true,
                  "type": "boolean"
                }
              },
              "required": [
                "artifact_type",
                "asset_type",
                "asset_id",
                "created_at",
                "artifact_id",
                "updated_at"
              ]
            }
          }
        },
        "required": [
          "metadata",
          "data"
        ]
      },
      "UnauthorizedAuthorizerError": {
        "title": "UnauthorizedAuthorizerErrorResponse",
        "type": "object",
        "properties": {
          "Message": {
            "title": "Error message",
            "description": "Human readable error message.\n\n**Important**: This schema does not contain `error` field.",
            "example": "Unauthorized",
            "type": "string"
          }
        },
        "required": [
          "Message"
        ]
      },
      "artifact_type": {
        "enum": [
          "SBOM",
          "WIZ_ISSUES",
          "ZAP_SCANNED_URLS_web",
          "ZAP_SCANNED_URLS_api"
        ],
        "example": "SBOM",
        "title": "Artifact Type",
        "type": "string"
      },
      "asset_type": {
        "enum": [
          "repo",
          "org",
          "aws_account",
          "gcp_account",
          "azure_account",
          "web",
          "api",
          "image"
        ],
        "example": "repo",
        "title": "Asset Type",
        "type": "string"
      },
      "asset_id": {
        "example": "c7a1c231-f2d1-4352-9ca0-fa2da8bf623c",
        "title": "Asset ID",
        "type": "string"
      },
      "limit": {
        "default": 100,
        "example": 4,
        "title": "Results limit",
        "type": "integer"
      },
      "after": {
        "example": "CURSOR",
        "title": "Cursor",
        "type": "string"
      },
      "Access-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Credentials": {
        "type": "boolean",
        "default": true
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 103,
      "1": 96,
      "2": 119,
      "3": 178,
      "4": 114,
      "5": 109,
      "6": 158,
      "7": 128,
      "8": 238,
      "9": 252,
      "10": 241,
      "11": 194
    }
  }
}
```