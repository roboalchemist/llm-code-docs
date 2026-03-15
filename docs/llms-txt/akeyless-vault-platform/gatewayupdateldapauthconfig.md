# Source: https://docs.akeyless.io/reference/gatewayupdateldapauthconfig.md

# /gateway-update-ldap-auth-config

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
    "/gateway-update-ldap-auth-config": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "GatewayUpdateLdapAuthConfig",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GatewayUpdateLdapAuthConfig"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/GatewayUpdateLdapAuthConfigResponse"
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
      "GatewayUpdateLdapAuthConfigResponse": {
        "description": "GatewayUpdateLdapAuthConfigResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GatewayUpdateLdapAuthConfigOutput"
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
      "GatewayUpdateLdapAuthConfig": {
        "description": "gatewayUpdateLdapAuth is a command that updates ldap auth config",
        "type": "object",
        "properties": {
          "access-id": {
            "description": "The access ID of the Ldap auth method",
            "type": "string",
            "x-go-name": "AuthMethodAccessId"
          },
          "bind-dn": {
            "description": "Bind DN",
            "type": "string",
            "x-go-name": "BindDn"
          },
          "bind-dn-password": {
            "description": "Bind DN Password",
            "type": "string",
            "x-go-name": "BindDnPassword"
          },
          "group-attr": {
            "description": "Group Attr",
            "type": "string",
            "x-go-name": "GroupAttr"
          },
          "group-dn": {
            "description": "Group Dn",
            "type": "string",
            "x-go-name": "GroupDn"
          },
          "group-filter": {
            "description": "Group Filter",
            "type": "string",
            "x-go-name": "GroupFilter"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "ldap-ca-cert": {
            "description": "LDAP CA Certificate (base64 encoded)",
            "type": "string",
            "x-go-name": "LdapCACert"
          },
          "ldap-enable": {
            "description": "Enable Ldap [true/false]",
            "type": "string",
            "x-go-name": "LdapEnable"
          },
          "ldap-url": {
            "description": "LDAP Server URL, e.g. ldap://planetexpress.com:389",
            "type": "string",
            "x-go-name": "LdapUrlAddress"
          },
          "signing-key-data": {
            "description": "The private key (base64 encoded), associated with the public key defined in the Ldap auth",
            "type": "string",
            "x-go-name": "AuthMethodSigningKey"
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
          "user-attribute": {
            "description": "User Attribute",
            "type": "string",
            "x-go-name": "UserAttribute"
          },
          "user-dn": {
            "description": "User DN",
            "type": "string",
            "x-go-name": "UserDn"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "GatewayUpdateLdapAuthConfigOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
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
      }
    }
  }
}
```