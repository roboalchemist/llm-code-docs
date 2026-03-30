# Source: https://docs.akeyless.io/reference/createauthmethodawsiam.md

# /create-auth-method-aws-iam

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
    "/create-auth-method-aws-iam": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createAuthMethodAWSIAM",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createAuthMethodAWSIAM"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createAuthMethodAWSIAMResponse"
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
      "createAuthMethodAWSIAMResponse": {
        "description": "createAuthMethodAWSIAMResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createAuthMethodAWSIAMOutput"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
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
      "createAuthMethodAWSIAM": {
        "description": "createAuthMethodAWSIAM is a command that creates a new Auth Method that will\nbe able to authenticate using AWS IAM credentials. [Deprecated: Use auth-method-create-aws-iam command]",
        "type": "object",
        "required": [
          "name",
          "bound-aws-account-id"
        ],
        "properties": {
          "access-expires": {
            "description": "Access expiration date in Unix timestamp (select 0 for access without\nexpiry date)",
            "type": "integer",
            "format": "int64",
            "default": 0,
            "x-go-name": "AccessExpires"
          },
          "allowed-client-type": {
            "description": "limit the auth method usage for specific client types [cli,ui,gateway-admin,sdk,mobile,extension]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedClientTypes"
          },
          "audit-logs-claims": {
            "description": "Subclaims to include in audit logs, e.g \"--audit-logs-claims email --audit-logs-claims username\"",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AuditLogsClaims"
          },
          "bound-arn": {
            "description": "A list of full arns that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundArn"
          },
          "bound-aws-account-id": {
            "description": "A list of AWS account-IDs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundAccountID"
          },
          "bound-ips": {
            "description": "A CIDR whitelist with the IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CIDRWhitelist"
          },
          "bound-resource-id": {
            "description": "A list of full resource ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceID"
          },
          "bound-role-id": {
            "description": "A list of full role ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundRoleID"
          },
          "bound-role-name": {
            "description": "A list of full role-name that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundRoleName"
          },
          "bound-user-id": {
            "description": "A list of full user ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundUserID"
          },
          "bound-user-name": {
            "description": "A list of full user-name that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundUserName"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Auth Method description",
            "type": "string",
            "x-go-name": "Description"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the auth method would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "force-sub-claims": {
            "description": "if true: enforce role-association must include sub claims",
            "type": "boolean",
            "x-go-name": "ForceSubClaims"
          },
          "gw-bound-ips": {
            "description": "A CIDR whitelist with the GW IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GWCIDRWhitelist"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "jwt-ttl": {
            "description": "Jwt TTL",
            "type": "integer",
            "format": "int64",
            "default": 0,
            "x-go-name": "JwtTtl"
          },
          "name": {
            "description": "Auth Method name",
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "product-type": {
            "description": "Choose the relevant product type for the auth method [sm, sra, pm, dp, ca]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ProductTypes"
          },
          "sts-url": {
            "description": "sts URL",
            "type": "string",
            "default": "https://sts.amazonaws.com",
            "x-go-name": "STSEndpoint"
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
          "unique-identifier": {
            "description": "A unique identifier (ID) value which is a \"sub claim\" name that contains details uniquely identifying that resource. This \"sub claim\" is used to distinguish between different identities.",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "createAuthMethodAWSIAMOutput": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```