# Source: https://docs.akeyless.io/reference/updatedbtarget.md

# /update-db-target

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
    "/update-db-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateDBTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateDBTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateDBTargetResponse"
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
      "updateDBTargetResponse": {
        "description": "updateDBTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateDBTargetOutput"
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
      "TargetType": {
        "type": "string",
        "title": "TargetType ..",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "updateDBTarget": {
        "description": "updateDBTarget is a command that updates an existing target. [Deprecated: Use target-update-db command]",
        "type": "object",
        "required": [
          "name",
          "db-type",
          "connection-type"
        ],
        "properties": {
          "azure-client-id": {
            "description": "(Optional) Client id (relevant for \"cloud-service-provider\" only)",
            "type": "string",
            "x-go-name": "MssqlAzureClientID"
          },
          "azure-client-secret": {
            "description": "(Optional) Client secret (relevant for \"cloud-service-provider\" only)",
            "type": "string",
            "x-go-name": "MssqlAzureClientSecret"
          },
          "azure-tenant-id": {
            "description": "(Optional) Tenant id (relevant for \"cloud-service-provider\" only)",
            "type": "string",
            "x-go-name": "MssqlAzureTenantID"
          },
          "cloud-service-provider": {
            "description": "(Optional) Cloud service provider (currently only supports Azure)",
            "type": "string",
            "x-go-name": "CloudServiceProvider"
          },
          "cluster-mode": {
            "description": "Cluster Mode",
            "type": "boolean",
            "x-go-name": "ClusterMode"
          },
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
          },
          "connection-type": {
            "description": "Type of connection to mssql database [credentials/cloud-identity/wallet/parent-target]",
            "type": "string",
            "default": "credentials",
            "x-go-name": "ConnectionType"
          },
          "db-name": {
            "type": "string",
            "x-go-name": "DbName"
          },
          "db-server-certificates": {
            "description": "(Optional) DB server certificates",
            "type": "string",
            "x-go-name": "DBServerCertificates"
          },
          "db-server-name": {
            "description": "(Optional) Server name for certificate verification",
            "type": "string",
            "x-go-name": "DBServerName"
          },
          "db-type": {
            "$ref": "#/components/schemas/TargetType"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "host": {
            "type": "string",
            "x-go-name": "DbHostName"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
          },
          "key": {
            "description": "The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "mongodb-atlas": {
            "type": "boolean",
            "x-go-name": "MongoDBAtlas"
          },
          "mongodb-atlas-api-private-key": {
            "description": "MongoDB Atlas private key",
            "type": "string",
            "x-go-name": "MongoAPIPrivateKey"
          },
          "mongodb-atlas-api-public-key": {
            "description": "MongoDB Atlas public key",
            "type": "string",
            "x-go-name": "MongoAPIPublicKey"
          },
          "mongodb-atlas-project-id": {
            "description": "MongoDB Atlas project ID",
            "type": "string",
            "x-go-name": "MongoProjectID"
          },
          "mongodb-default-auth-db": {
            "description": "MongoDB server default authentication database",
            "type": "string",
            "x-go-name": "MongoDefaultAuthDB"
          },
          "mongodb-uri-options": {
            "description": "MongoDB server URI options",
            "type": "string",
            "x-go-name": "MongoURIOptions"
          },
          "name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "new-name": {
            "description": "New target name",
            "type": "string",
            "x-go-name": "NewTargetName"
          },
          "oracle-service-name": {
            "description": "Oracle db service name",
            "type": "string",
            "x-go-name": "OracleServiceName"
          },
          "oracle-wallet-login-type": {
            "description": "Oracle Wallet login type (password/mtls)",
            "type": "string",
            "x-go-name": "OracleWalletLoginType"
          },
          "oracle-wallet-p12-file-data": {
            "description": "Oracle wallet p12 file data in base64",
            "type": "string",
            "x-go-name": "OracleWalletP12FileData"
          },
          "oracle-wallet-sso-file-data": {
            "description": "Oracle wallet sso file data in base64",
            "type": "string",
            "x-go-name": "OracleWalletSSOFileData"
          },
          "parent-target-name": {
            "description": "Name of the parent target, relevant only when connection-type is parent-target",
            "type": "string",
            "x-go-name": "ParentTargetName"
          },
          "port": {
            "type": "string",
            "x-go-name": "DbPort"
          },
          "pwd": {
            "type": "string",
            "x-go-name": "DbPwd"
          },
          "snowflake-account": {
            "type": "string",
            "x-go-name": "SnowflakeAccount"
          },
          "snowflake-api-private-key": {
            "description": "RSA Private key (base64 encoded)",
            "type": "string",
            "x-go-name": "SnowflakeAPIPrivateKey"
          },
          "snowflake-api-private-key-password": {
            "description": "The Private key passphrase",
            "type": "string",
            "x-go-name": "SnowflakeAPIPrivateKeyPass"
          },
          "ssl": {
            "description": "Enable/Disable SSL [true/false]",
            "type": "boolean",
            "default": false,
            "x-go-name": "SSLConnection"
          },
          "ssl-certificate": {
            "description": "SSL connection certificate",
            "type": "string",
            "x-go-name": "SSLConnectionCertificate"
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
          "update-version": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "CreateNewVersion"
          },
          "user-name": {
            "type": "string",
            "x-go-name": "DbUserName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateDBTargetOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```