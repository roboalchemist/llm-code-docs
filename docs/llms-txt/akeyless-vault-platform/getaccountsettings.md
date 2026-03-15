# Source: https://docs.akeyless.io/reference/getaccountsettings.md

# /get-account-settings

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
    "/get-account-settings": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getAccountSettings",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getAccountSettings"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getAccountSettingsResponse"
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
      "getAccountSettingsResponse": {
        "description": "getAccountSettingsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetAccountSettingsCommandOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AccessRulesType": {
        "type": "string",
        "title": "Access rules type.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AccountGeneralSettings": {
        "description": "AccountGeneralSettings describes general settings for an account",
        "type": "object",
        "properties": {
          "account_default_key_item_id": {
            "description": "AccountDefaultKeyItemID is the item ID of the DFC key item configured as the default protection key",
            "type": "integer",
            "format": "int64",
            "x-go-name": "AccountDefaultKeyItemID"
          },
          "account_default_key_name": {
            "description": "AccountDefaultKeyName is the name of the DFC key item configured as the default key\nThis is here simply for the response to include the item name in addition to the display ID so the\nclient can properly show this to the user.\nIt will not be saved to the DB, only the AccountDefaultKeyItemID will.",
            "type": "string",
            "x-go-name": "AccountDefaultKeyName"
          },
          "ai_insights": {
            "$ref": "#/components/schemas/AiInsightsSetting"
          },
          "allow_auto_fill": {
            "type": "boolean",
            "x-go-name": "AllowAutoFill"
          },
          "allowed_client_types": {
            "$ref": "#/components/schemas/AllowedClientType"
          },
          "allowed_clients_ips": {
            "$ref": "#/components/schemas/AllowedIpSettings"
          },
          "allowed_gateways_ips": {
            "$ref": "#/components/schemas/AllowedIpSettings"
          },
          "auth_usage_event": {
            "$ref": "#/components/schemas/UsageEventSetting"
          },
          "certificate_expiration_events": {
            "$ref": "#/components/schemas/CertificateExpirationEventsSettings"
          },
          "data_protection_section": {
            "$ref": "#/components/schemas/DataProtectionSection"
          },
          "default_auth_method": {
            "$ref": "#/components/schemas/DefaultAuthMethodSettings"
          },
          "default_home_page": {
            "$ref": "#/components/schemas/DefaultHomePage"
          },
          "dynamic_secret_max_ttl": {
            "$ref": "#/components/schemas/DynamicSecretMaxTtl"
          },
          "enable_request_for_access": {
            "type": "boolean",
            "x-go-name": "EnableRequestForAccess"
          },
          "hide_personal_folder": {
            "type": "boolean",
            "x-go-name": "HidePersonalFolder"
          },
          "hide_static_password": {
            "type": "boolean",
            "x-go-name": "HideStaticPassword"
          },
          "invalid_characters": {
            "description": "InvalidCharacters is the invalid characters for items/targets/roles/auths/notifier_forwarder naming convention",
            "type": "string",
            "x-go-name": "InvalidCharacters"
          },
          "item_usage_event": {
            "$ref": "#/components/schemas/UsageEventSetting"
          },
          "lock_default_key": {
            "description": "LockDefaultKey determines whether the configured default key can be updated by end-users on a per-request basis\ntrue - all requests use the configured default key\nfalse - every request can determine its protection key (default)\nnil - change nothing (every request can determine its protection key (default))\nThis parameter is only relevant if AccountDefaultKeyItemID is not empty",
            "type": "boolean",
            "x-go-name": "LockDefaultKey"
          },
          "password_expiration_info": {
            "$ref": "#/components/schemas/PasswordExpirationInfo"
          },
          "password_policy": {
            "$ref": "#/components/schemas/PasswordPolicyInfo"
          },
          "password_score": {
            "$ref": "#/components/schemas/PasswordScoreSetting"
          },
          "protect_items_by_default": {
            "type": "boolean",
            "x-go-name": "ProtectItemsByDefault"
          },
          "rotation_secret_max_interval": {
            "$ref": "#/components/schemas/RotationSecretMaxInterval"
          },
          "sharing_policy": {
            "$ref": "#/components/schemas/SharingPolicyInfo"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AccountObjectVersionSettingsOutput": {
        "type": "object",
        "properties": {
          "default-versioning": {
            "type": "boolean",
            "x-go-name": "CreateNewVersionByDefault"
          },
          "force_new_versions": {
            "type": "boolean",
            "x-go-name": "ForceNewVersion"
          },
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ObjectVersionSettingsOutput"
            },
            "x-go-name": "ObjectSettings"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "AiInsightsSetting": {
        "type": "object",
        "properties": {
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AllowedClientType": {
        "type": "object",
        "properties": {
          "client_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ClientTypes"
          },
          "lock": {
            "type": "boolean",
            "x-go-name": "Lock"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "AllowedIpSettings": {
        "type": "object",
        "properties": {
          "cidr_whitelist": {
            "type": "string",
            "x-go-name": "CIDRWhitelist"
          },
          "lock": {
            "type": "boolean",
            "x-go-name": "Lock"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateExpirationEvent": {
        "type": "object",
        "properties": {
          "seconds_before": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "SecondsBefore"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateExpirationEventsSettings": {
        "type": "object",
        "properties": {
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          },
          "expirations_list": {
            "description": "ExpirationEventsList is the default expiration events for the account",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CertificateExpirationEvent"
            },
            "x-go-name": "ExpirationEventsList"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CustomerFullAddress": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "x-go-name": "City"
          },
          "country": {
            "type": "string",
            "x-go-name": "Country"
          },
          "postal_code": {
            "type": "string",
            "x-go-name": "PostalCode"
          },
          "street": {
            "type": "string",
            "x-go-name": "Street"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DataProtectionSection": {
        "description": "We need the fields to be pointers as we\nuse the same struct for partial updates as well",
        "type": "object",
        "properties": {
          "enable_classic_key_protection": {
            "type": "boolean",
            "x-go-name": "EnableClassicKeyProtection"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DefaultAuthMethodSettings": {
        "type": "object",
        "properties": {
          "default_access_id": {
            "type": "string",
            "x-go-name": "DefaultAccessID"
          },
          "default_auth_method_type": {
            "$ref": "#/components/schemas/AccessRulesType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DefaultHomePage": {
        "type": "object",
        "properties": {
          "route": {
            "type": "string",
            "x-go-name": "Route"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "DynamicSecretMaxTtl": {
        "type": "object",
        "properties": {
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          },
          "max_ttl_by_minutes": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MaxTtlByMinutes"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GetAccountSettingsCommandOutput": {
        "type": "object",
        "title": "GetAccountSettingsCommandOutput defines cli output of get-account-settings command.",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AccountID"
          },
          "address": {
            "$ref": "#/components/schemas/CustomerFullAddress"
          },
          "company_name": {
            "type": "string",
            "x-go-name": "CompanyName"
          },
          "email": {
            "type": "string",
            "x-go-name": "CustomerEmail"
          },
          "general_settings": {
            "$ref": "#/components/schemas/AccountGeneralSettings"
          },
          "object_version_settings": {
            "$ref": "#/components/schemas/AccountObjectVersionSettingsOutput"
          },
          "phone": {
            "type": "string",
            "x-go-name": "CustomerPhone"
          },
          "secret_management": {
            "$ref": "#/components/schemas/SmInfo"
          },
          "secure_remote_access": {
            "$ref": "#/components/schemas/SraInfo"
          },
          "system_access_creds_settings": {
            "$ref": "#/components/schemas/SystemAccessCredsSettings"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
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
      "ObjectVersionSettingsOutput": {
        "type": "object",
        "properties": {
          "item-type": {
            "$ref": "#/components/schemas/VersionSettingsObjectType"
          },
          "max-versions": {
            "type": "string",
            "x-go-name": "MaxVersions"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "PasswordExpirationInfo": {
        "type": "object",
        "properties": {
          "days_before_expire": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DaysBeforeExpire"
          },
          "days_before_notification": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DaysBeforeNotification"
          },
          "days_until_expire": {
            "description": "r/o calculated parameter",
            "type": "integer",
            "format": "int64",
            "x-go-name": "DaysUntilExpiration"
          },
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordPolicyInfo": {
        "type": "object",
        "properties": {
          "password_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "PasswordLength"
          },
          "use_capital_letters": {
            "type": "boolean",
            "x-go-name": "UseCapitalLetters"
          },
          "use_lower_letters": {
            "type": "boolean",
            "x-go-name": "UseLowerLetters"
          },
          "use_numbers": {
            "type": "boolean",
            "x-go-name": "UseNumbers"
          },
          "use_special_characters": {
            "type": "boolean",
            "x-go-name": "UseSpecialCharacters"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreSetting": {
        "type": "object",
        "properties": {
          "enabled": {
            "type": "boolean",
            "x-go-name": "Enable"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RotationSecretMaxInterval": {
        "type": "object",
        "properties": {
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          },
          "max_interval_by_days": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "MaxIntervalByDays"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SLA": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SharingPolicyInfo": {
        "type": "object",
        "properties": {
          "allowed_email_domains": {
            "description": "AllowedEmailDomains limits email sharing to these domains. By default all domains are allowed.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedEmailDomains"
          },
          "default_share_link_ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DefaultShareLinkTTL"
          },
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SmInfo": {
        "type": "object",
        "properties": {
          "sla": {
            "$ref": "#/components/schemas/SLA"
          },
          "tier": {
            "$ref": "#/components/schemas/Tier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "SraInfo": {
        "type": "object",
        "properties": {
          "sla": {
            "$ref": "#/components/schemas/SLA"
          },
          "tier": {
            "$ref": "#/components/schemas/Tier"
          },
          "user_type": {
            "type": "string",
            "x-go-name": "UserType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "SystemAccessCredsSettings": {
        "description": "SystemAccessCredsSettings describes system access credential settings for account by minutes",
        "type": "object",
        "properties": {
          "jwt_ttl_default": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtlDefault"
          },
          "jwt_ttl_maximum": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtlMaximum"
          },
          "jwt_ttl_minimum": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "JwtTtlMinimum"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Tier": {
        "description": "Tier represents a level of extensibility the account will have, defined by various limits for different\nresources of Akeyless\ne.g - A StarterTier may have a limit of 3 Client resources and 50 Secret resources",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "UsageEventSetting": {
        "type": "object",
        "properties": {
          "enable": {
            "type": "boolean",
            "x-go-name": "Enable"
          },
          "enable_time": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "EnableTime"
          },
          "interval_by_days": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "IntervalByDays"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "VersionSettingsObjectType": {
        "description": "VersionSettingsObjectType defines object types for account version settings",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "getAccountSettings": {
        "type": "object",
        "title": "getAccountSettings is a command that returns account settings.",
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