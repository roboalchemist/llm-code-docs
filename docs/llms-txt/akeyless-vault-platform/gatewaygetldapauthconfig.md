# Source: https://docs.akeyless.io/reference/gatewaygetldapauthconfig.md

# /gateway-get-ldap-auth-config

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
    "/gateway-get-ldap-auth-config": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetLdapAuthConfig",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetLdapAuthConfig"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayGetLdapAuthConfigResponse"
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
      "gatewayGetLdapAuthConfigResponse": {
        "description": "gatewayGetLdapAuthConfigResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayGetLdapAuthConfigOutput"
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
      "gatewayGetLdapAuthConfig": {
        "description": "gatewayGetLdapAuth is a command that gets ldap auth config",
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
      },
      "gatewayGetLdapAuthConfigOutput": {
        "type": "object",
        "properties": {
          "ldap_access_id": {
            "type": "string",
            "x-go-name": "LdapAccessId"
          },
          "ldap_anonymous_search": {
            "type": "boolean",
            "x-go-name": "LdapAnonymousSearch"
          },
          "ldap_bind_dn": {
            "type": "string",
            "x-go-name": "LdapBindDn"
          },
          "ldap_bind_password": {
            "type": "string",
            "x-go-name": "LdapBindPassword"
          },
          "ldap_cert": {
            "type": "string",
            "x-go-name": "LdapCertificate"
          },
          "ldap_enable": {
            "type": "boolean",
            "x-go-name": "LdapEnable"
          },
          "ldap_group_attr": {
            "type": "string",
            "x-go-name": "LdapGroupAttr"
          },
          "ldap_group_dn": {
            "type": "string",
            "x-go-name": "LdapGroupDn"
          },
          "ldap_group_filter": {
            "type": "string",
            "x-go-name": "LdapGroupFilter"
          },
          "ldap_private_key": {
            "type": "string",
            "x-go-name": "LdapPrivateKey"
          },
          "ldap_token_expiration": {
            "type": "string",
            "x-go-name": "LdapTokenExpiration"
          },
          "ldap_url": {
            "type": "string",
            "x-go-name": "LdapUrlAddress"
          },
          "ldap_user_attr": {
            "type": "string",
            "x-go-name": "LdapUserAttr"
          },
          "ldap_user_dn": {
            "type": "string",
            "x-go-name": "LdapUserDn"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```