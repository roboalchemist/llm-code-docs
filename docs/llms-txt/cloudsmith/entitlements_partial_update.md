# Source: https://help.cloudsmith.io/reference/entitlements_partial_update.md

# Update a specific entitlement in a repository.

Update a specific entitlement in a repository.

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
    "/entitlements/{owner}/{repo}/{identifier}/": {
      "patch": {
        "operationId": "entitlements_partial_update",
        "summary": "Update a specific entitlement in a repository.",
        "description": "Update a specific entitlement in a repository.",
        "parameters": [
          {
            "name": "show_tokens",
            "in": "query",
            "description": "Show entitlement token strings in results",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RepositoryTokenRequestPatch"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Updated the specified entitlement",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryToken"
                }
              }
            }
          },
          "400": {
            "description": "The entitlement cannot be edited.",
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
          "entitlements"
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
      "Eula": {
        "type": "object",
        "properties": {
          "identifier": {
            "title": "Identifier",
            "description": "A unique identifier that you can use for your own EULA tracking purposes. This might be a date, or a semantic version, etc. The only requirement is that it is unique across multiple EULAs.",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "maxLength": 16,
            "nullable": true
          },
          "number": {
            "title": "Number",
            "description": "A sequential identifier that increments by one for each new commit in a repository.",
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0,
            "nullable": true
          }
        },
        "nullable": true
      },
      "RepositoryToken": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "access_private_broadcasts": {
            "title": "Access private broadcasts",
            "description": "If enabled, this token can be used for private broadcasts",
            "type": "boolean"
          },
          "clients": {
            "title": "Clients",
            "type": "integer",
            "readOnly": true
          },
          "created_at": {
            "title": "Created at",
            "description": "The datetime the token was updated at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "title": "Created by",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "created_by_url": {
            "title": "Created by url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "default": {
            "title": "Default",
            "description": "If selected this is the default token for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "disable_url": {
            "title": "Disable url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "downloads": {
            "title": "Downloads",
            "type": "integer",
            "readOnly": true
          },
          "enable_url": {
            "title": "Enable url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "eula_accepted": {
            "$ref": "#/components/schemas/Eula"
          },
          "eula_accepted_at": {
            "title": "Eula accepted at",
            "description": "The datetime the EULA was accepted at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "eula_accepted_from": {
            "title": "Eula accepted from",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "eula_required": {
            "title": "Eula required",
            "description": "If checked, a EULA acceptance is required for this token.",
            "type": "boolean"
          },
          "has_limits": {
            "title": "Has limits",
            "type": "boolean",
            "readOnly": true
          },
          "identifier": {
            "title": "Identifier",
            "description": "Deprecated (23-05-15): Please use 'slug_perm' instead. Previously: A monotonically increasing number that identified an entitlement within a repository.",
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "is_active": {
            "title": "Token Active",
            "description": "If enabled, the token will allow downloads based on configured restrictions (if any).",
            "type": "boolean"
          },
          "is_limited": {
            "title": "Is limited",
            "type": "boolean",
            "readOnly": true
          },
          "limit_bandwidth": {
            "title": "Limit bandwidth",
            "description": "The maximum download bandwidth allowed for the token. Values are expressed as the selected unit of bandwidth. Please note that since downloads are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point. ",
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "nullable": true
          },
          "limit_bandwidth_unit": {
            "title": "Limit bandwidth unit",
            "type": "string",
            "enum": [
              "Byte",
              "Kilobyte",
              "Megabyte",
              "Gigabyte",
              "Terabyte",
              "Petabyte",
              "Exabyte",
              "Zettabyte",
              "Yottabyte"
            ],
            "default": "Byte",
            "nullable": true
          },
          "limit_date_range_from": {
            "title": "Limit date range from",
            "description": "The starting date/time the token is allowed to be used from.",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "limit_date_range_to": {
            "title": "Limit date range to",
            "description": "The ending date/time the token is allowed to be used until.",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "limit_num_clients": {
            "title": "Limit num clients",
            "description": "The maximum number of unique clients allowed for the token. Please note that since clients are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point.",
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "nullable": true
          },
          "limit_num_downloads": {
            "title": "Limit num downloads",
            "description": "The maximum number of downloads allowed for the token. Please note that since downloads are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point.",
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "nullable": true
          },
          "limit_package_query": {
            "title": "Limit package query",
            "description": "The package-based search query to apply to restrict downloads to. This uses the same syntax as the standard search used for repositories, and also supports boolean logic operators such as OR/AND/NOT and parentheses for grouping. This will still allow access to non-package files, such as metadata.",
            "type": "string",
            "maxLength": 1024,
            "nullable": true
          },
          "limit_path_query": {
            "title": "Limit path query",
            "description": "THIS WILL SOON BE DEPRECATED, please use limit_package_query instead. The path-based search query to apply to restrict downloads to. This supports boolean logic operators such as OR/AND/NOT and parentheses for grouping. The path evaluated does not include the domain name, the namespace, the entitlement code used, the package format, etc. and it always starts with a forward slash.",
            "type": "string",
            "maxLength": 1024,
            "nullable": true
          },
          "metadata": {
            "title": "Metadata",
            "type": "object",
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
            "minLength": 1
          },
          "refresh_url": {
            "title": "Refresh url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "reset_url": {
            "title": "Reset url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "scheduled_reset_at": {
            "title": "Scheduled reset at",
            "description": "The time at which the scheduled reset period has elapsed and the token limits were automatically reset to zero.",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "scheduled_reset_period": {
            "title": "Scheduled reset period",
            "type": "string",
            "enum": [
              "Never Reset",
              "Daily",
              "Weekly",
              "Fortnightly",
              "Monthly",
              "Bi-Monthly",
              "Quarterly",
              "Every 6 months",
              "Annual"
            ],
            "default": "Never Reset",
            "nullable": true
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "token": {
            "title": "Token",
            "type": "string",
            "minLength": 1
          },
          "updated_at": {
            "title": "Updated at",
            "description": "The datetime the token was updated at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "updated_by": {
            "title": "Updated by",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "updated_by_url": {
            "title": "Updated by url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "usage": {
            "title": "Usage",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "user": {
            "title": "User",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "user_url": {
            "title": "User url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "RepositoryTokenRequestPatch": {
        "type": "object",
        "properties": {
          "access_private_broadcasts": {
            "title": "Access private broadcasts",
            "description": "If enabled, this token can be used for private broadcasts",
            "type": "boolean"
          },
          "eula_required": {
            "title": "Eula required",
            "description": "If checked, a EULA acceptance is required for this token.",
            "type": "boolean"
          },
          "is_active": {
            "title": "Token Active",
            "description": "If enabled, the token will allow downloads based on configured restrictions (if any).",
            "type": "boolean"
          },
          "limit_bandwidth": {
            "title": "Limit bandwidth",
            "description": "The maximum download bandwidth allowed for the token. Values are expressed as the selected unit of bandwidth. Please note that since downloads are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point. ",
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "nullable": true
          },
          "limit_bandwidth_unit": {
            "title": "Limit bandwidth unit",
            "type": "string",
            "enum": [
              "Byte",
              "Kilobyte",
              "Megabyte",
              "Gigabyte",
              "Terabyte",
              "Petabyte",
              "Exabyte",
              "Zettabyte",
              "Yottabyte"
            ],
            "default": "Byte",
            "nullable": true
          },
          "limit_date_range_from": {
            "title": "Limit date range from",
            "description": "The starting date/time the token is allowed to be used from.",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "limit_date_range_to": {
            "title": "Limit date range to",
            "description": "The ending date/time the token is allowed to be used until.",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "limit_num_clients": {
            "title": "Limit num clients",
            "description": "The maximum number of unique clients allowed for the token. Please note that since clients are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point.",
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "nullable": true
          },
          "limit_num_downloads": {
            "title": "Limit num downloads",
            "description": "The maximum number of downloads allowed for the token. Please note that since downloads are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point.",
            "type": "integer",
            "maximum": 9223372036854776000,
            "minimum": -9223372036854776000,
            "nullable": true
          },
          "limit_package_query": {
            "title": "Limit package query",
            "description": "The package-based search query to apply to restrict downloads to. This uses the same syntax as the standard search used for repositories, and also supports boolean logic operators such as OR/AND/NOT and parentheses for grouping. This will still allow access to non-package files, such as metadata.",
            "type": "string",
            "maxLength": 1024,
            "nullable": true
          },
          "limit_path_query": {
            "title": "Limit path query",
            "description": "THIS WILL SOON BE DEPRECATED, please use limit_package_query instead. The path-based search query to apply to restrict downloads to. This supports boolean logic operators such as OR/AND/NOT and parentheses for grouping. The path evaluated does not include the domain name, the namespace, the entitlement code used, the package format, etc. and it always starts with a forward slash.",
            "type": "string",
            "maxLength": 1024,
            "nullable": true
          },
          "metadata": {
            "title": "Metadata",
            "type": "object",
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
            "minLength": 1
          },
          "scheduled_reset_at": {
            "title": "Scheduled reset at",
            "description": "The time at which the scheduled reset period has elapsed and the token limits were automatically reset to zero.",
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "scheduled_reset_period": {
            "title": "Scheduled reset period",
            "type": "string",
            "enum": [
              "Never Reset",
              "Daily",
              "Weekly",
              "Fortnightly",
              "Monthly",
              "Bi-Monthly",
              "Quarterly",
              "Every 6 months",
              "Annual"
            ],
            "default": "Never Reset",
            "nullable": true
          },
          "token": {
            "title": "Token",
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```