# Source: https://docs.akeyless.io/reference/gatewaygetcache.md

# /gateway-get-cache

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/gateway-get-cache": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetCache",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetCache"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayGetCacheResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "gatewayGetCacheResponse": {
        "description": "gatewayGetCacheResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CacheConfigPart"
            }
          }
        }
      }
    },
    "schemas": {
      "CacheConfigPart": {
        "type": "object",
        "properties": {
          "cache_enable": {
            "type": "boolean",
            "x-go-name": "CacheEnable"
          },
          "cache_encryption_key": {
            "type": "string",
            "x-go-name": "CacheEncryptionKey"
          },
          "cache_ttl": {
            "type": "string",
            "x-go-name": "CacheTTL"
          },
          "new_proactive_cache_enable": {
            "type": "boolean",
            "x-go-name": "NewProActiveCacheEnable"
          },
          "proactive_cache_dump_interval": {
            "type": "string",
            "x-go-name": "ProActiveCacheDumpInterval"
          },
          "proactive_cache_enable": {
            "type": "boolean",
            "x-go-name": "ProActiveCacheEnable"
          },
          "proactive_cache_minimum_fetching_time": {
            "type": "string",
            "x-go-name": "ProActiveCacheMinimumFetchingTime"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "gatewayGetCache": {
        "description": "gatewayGetCache is a command that get cache settings",
        "type": "object",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```