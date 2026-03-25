# Source: https://docs.akeyless.io/reference/updateaccountsettings.md

# /update-account-settings

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
    "/update-account-settings": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateAccountSettings",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateAccountSettings"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateAccountSettingsResponse"
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
      "updateAccountSettingsResponse": {
        "description": "updateAccountSettingsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateAccountSettingsOutput"
            }
          }
        }
      }
    },
    "schemas": {
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
      "VersionSettingsObjectType": {
        "description": "VersionSettingsObjectType defines object types for account version settings",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "updateAccountSettings": {
        "type": "object",
        "title": "updateAccountSettings is a command that updates an existing account settings.",
        "properties": {
          "address": {
            "description": "Address",
            "type": "string",
            "x-go-name": "Address"
          },
          "allowed-client-type": {
            "description": "A default list of client types that are allowed to authenticate [cli,ui,gateway-admin,sdk,mobile,extension].",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedClientTypes"
          },
          "allowed-email-domains": {
            "description": "Limits email sharing to the specified domains. Relevant only when item sharing is enabled. By default, all domains are allowed.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedEmailDomainsInput"
          },
          "bound-ips": {
            "description": "A default list of comma-separated CIDR block that are allowed to authenticate.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CIDRWhitelist"
          },
          "city": {
            "description": "City",
            "type": "string",
            "x-go-name": "City"
          },
          "company-name": {
            "description": "Company name",
            "type": "string",
            "x-go-name": "CompanyName"
          },
          "country": {
            "description": "Country",
            "type": "string",
            "x-go-name": "Country"
          },
          "default-certificate-expiration-notification-days": {
            "description": "How many days before the expiration of the certificate would you like to be notified. To specify multiple events, use argument multiple times: --default-certificate-expiration-notification-days 1 --default-certificate-expiration-notification-days 5",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "default-key-name": {
            "description": "Set the account default key based on the DFC key name.\nUse \"set-original-akeyless-default-key\" to revert to using the original default key of the account.",
            "type": "string",
            "x-go-name": "DefaultKeyName"
          },
          "default-share-link-ttl-minutes": {
            "description": "Set the default ttl in minutes for sharing item number between 60 and 43200",
            "type": "string",
            "x-go-name": "DefaultShareLinkTTLMinutes"
          },
          "default-versioning": {
            "description": "If set to true, new versions is enabled by default",
            "type": "string",
            "x-go-name": "CreateVersionByDefault"
          },
          "dp-enable-classic-key-protection": {
            "description": "Set to update protection with classic keys state [true/false]",
            "type": "string",
            "x-go-name": "EnableClassicKeyProtection"
          },
          "dynamic-secret-max-ttl": {
            "description": "Set the maximum ttl for dynamic secrets",
            "type": "integer",
            "format": "int64",
            "x-go-name": "DynamicSecretMaxTtl"
          },
          "dynamic-secret-max-ttl-enable": {
            "description": "Set a maximum ttl for dynamic secrets [true/false]",
            "type": "string",
            "x-go-name": "DynamicMaxTtlEnable"
          },
          "enable-ai-insights": {
            "description": "Enable AI insights [true/false]",
            "type": "string",
            "x-go-name": "EnableAiInsights"
          },
          "enable-default-certificate-expiration-event": {
            "description": "How many days before the expiration of the certificate would you like to be notified. [true/false]",
            "type": "string",
            "x-go-name": "ExpirationEventsInDaysEnable"
          },
          "enable-item-sharing": {
            "description": "Enable sharing items [true/false]",
            "type": "string",
            "x-go-name": "EnableShareLink"
          },
          "enable-password-expiration": {
            "description": "Enable password expiration policy [true/false]",
            "type": "string",
            "x-go-name": "EnablePasswordExpiration"
          },
          "force-new-versions": {
            "description": "If set to true, new version will be created on update",
            "type": "string",
            "x-go-name": "ForceNewVersions"
          },
          "gw-bound-ips": {
            "description": "A default list of comma-separated CIDR block that acts as a trusted Gateway entity.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GWCIDRWhitelist"
          },
          "hide-personal-folder": {
            "description": "Hide personal folder, if set - users will not be able to use personal folder [true/false]",
            "type": "string",
            "x-go-name": "HidePersonalFolder"
          },
          "hide-static-password": {
            "description": "Hide static secret's password type [true/false]",
            "type": "string",
            "x-go-name": "HideStaticPassword"
          },
          "invalid-characters": {
            "description": "Characters that cannot be used for items/targets/roles/auths/event_forwarder names.\nEmpty string will enforce nothing.",
            "type": "string",
            "default": "notReceivedInvalidCharacter",
            "x-go-name": "InvalidCharacters"
          },
          "item-type": {
            "$ref": "#/components/schemas/VersionSettingsObjectType"
          },
          "items-deletion-protection": {
            "description": "Set or unset the default behaviour of items deletion protection [true/false]",
            "type": "string",
            "x-go-name": "ItemsDeletionProtection"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "jwt-ttl-default": {
            "description": "Default ttl",
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtlDefault"
          },
          "jwt-ttl-max": {
            "description": "Maximum ttl",
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtlMax"
          },
          "jwt-ttl-min": {
            "description": "Minimum ttl",
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtlMin"
          },
          "lock-allowed-client-type": {
            "description": "Lock allowed-client-type setting in the account [true/false].",
            "type": "string",
            "x-go-name": "AllowedClientTypeLock"
          },
          "lock-bound-ips": {
            "description": "Lock bound-ips setting globally in the account.",
            "type": "string",
            "x-go-name": "CIDRWhitelistLock"
          },
          "lock-default-key": {
            "description": "Lock the account's default protection key, if set - users will not be able to use a different protection key,\nrelevant only if default-key-name is configured [true/false]",
            "type": "string",
            "x-go-name": "LockDefaultKey"
          },
          "lock-gw-bound-ips": {
            "description": "Lock gw-bound-ips setting in the account.",
            "type": "string",
            "x-go-name": "GWCIDRWhitelistLock"
          },
          "max-rotation-interval": {
            "description": "Set the maximum rotation interval for rotated secrets auto rotation settings",
            "type": "integer",
            "format": "int32",
            "x-go-name": "MaxRotationInterval"
          },
          "max-rotation-interval-enable": {
            "description": "Set a maximum rotation interval for rotated secrets auto rotation settings [true/false]",
            "type": "string",
            "x-go-name": "MaxRotationIntervalEnable"
          },
          "max-versions": {
            "description": "Max versions",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "password-expiration-days": {
            "description": "Specifies the number of days that a password is valid before it must be changed. A default value of 90 days is used.",
            "type": "string",
            "x-go-name": "PasswordExpirationDays"
          },
          "password-expiration-notification-days": {
            "description": "Specifies the number of days before a user receives notification that their password will expire. A default value of 14 days is used.",
            "type": "string",
            "x-go-name": "PasswordExpirationNotificationDays"
          },
          "password-length": {
            "description": "Password length between 5 - to 50 characters",
            "type": "integer",
            "format": "int64",
            "x-go-name": "PasswordLength"
          },
          "phone": {
            "description": "Phone number",
            "type": "string",
            "x-go-name": "Phone"
          },
          "postal-code": {
            "description": "Postal code",
            "type": "string",
            "x-go-name": "PostalCode"
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
          },
          "usage-event-enable": {
            "description": "Enable event for objects that have not been used or changed [true/false]",
            "type": "string",
            "x-go-name": "UsageEventEnable"
          },
          "usage-event-interval": {
            "description": "Interval by days for unused objects. Default and minimum interval is 90 days",
            "type": "integer",
            "format": "int64",
            "x-go-name": "UsageEventInterval"
          },
          "usage-event-object-type": {
            "description": "Usage event is supported for auth method or secrets-and-keys [auth/item]",
            "type": "string",
            "x-go-name": "UsageEventObjectType"
          },
          "use-capital-letters": {
            "description": "Password must contain capital letters [true/false]",
            "type": "string",
            "x-go-name": "UseCapitalLettersV2"
          },
          "use-lower-letters": {
            "description": "Password must contain lower case letters [true/false]",
            "type": "string",
            "x-go-name": "UseLowerLetters"
          },
          "use-numbers": {
            "description": "Password must contain numbers [true/false]",
            "type": "string",
            "x-go-name": "UseNumbers"
          },
          "use-special-characters": {
            "description": "Password must contain special characters [true/false]",
            "type": "string",
            "x-go-name": "UseSpecialCharacters"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateAccountSettingsOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```