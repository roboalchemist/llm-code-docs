# Source: https://docs.akeyless.io/reference/createrotatedsecret.md

# /create-rotated-secret

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
    "/create-rotated-secret": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createRotatedSecret",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createRotatedSecret"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createRotatedSecretResponse"
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
      "createRotatedSecretResponse": {
        "description": "createRotatedSecretResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateRotatedSecretOutput"
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
      "CreateRotatedSecretOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "HostProviderType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "createRotatedSecret": {
        "description": "createRotatedSecret is a command that creates a rotated secret [Deprecated: Use rotated-secret-create commands]",
        "type": "object",
        "required": [
          "name",
          "target-name",
          "rotator-type"
        ],
        "properties": {
          "ProviderType": {
            "$ref": "#/components/schemas/HostProviderType"
          },
          "api-id": {
            "description": "API ID to rotate (relevant only for rotator-type=api-key)",
            "type": "string",
            "x-go-name": "ApiId"
          },
          "api-key": {
            "description": "API key to rotate (relevant only for rotator-type=api-key)",
            "type": "string",
            "x-go-name": "ApiKey"
          },
          "application-id": {
            "description": "ApplicationId (used in azure)",
            "type": "string",
            "x-go-name": "ApplicationId"
          },
          "authentication-credentials": {
            "description": "The credentials to connect with use-user-creds/use-target-creds",
            "type": "string",
            "default": "use-user-creds",
            "x-go-name": "RotatorCredsType"
          },
          "auto-rotate": {
            "description": "Whether to automatically rotate every --rotation-interval days, or\ndisable existing automatic rotation [true/false]",
            "type": "string",
            "x-go-name": "AutoRotate"
          },
          "aws-region": {
            "description": "Aws Region (relevant only for aws)",
            "type": "string",
            "default": "us-east-2",
            "x-go-name": "AwsRegion"
          },
          "custom-payload": {
            "description": "Secret payload to be sent with rotation request (relevant only for rotator-type=custom)",
            "type": "string",
            "x-go-name": "Payload"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "gcp-key": {
            "description": "Base64-encoded service account private key text",
            "type": "string",
            "x-go-name": "ServiceAccountKey"
          },
          "gcp-service-account-email": {
            "description": "The email of the gcp service account to rotate",
            "type": "string",
            "x-go-name": "GcpServiceAccountEmail"
          },
          "gcp-service-account-key-id": {
            "description": "The key id of the gcp service account to rotate",
            "type": "string",
            "x-go-name": "GcpServiceAccountKeyId"
          },
          "grace-rotation": {
            "description": "Create a new access key without deleting the old key from AWS for backup (relevant only for AWS) [true/false]",
            "type": "string",
            "x-go-name": "GraceRotation"
          },
          "host-provider": {
            "description": "Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret",
            "type": "string",
            "x-go-name": "HostProviderType"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key": {
            "description": "The name of a key that used to encrypt the secret value (if empty, the\naccount default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "name": {
            "description": "Secret name",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "password-length": {
            "description": "The length of the password to be generated",
            "type": "string",
            "x-go-name": "PasswordLengthInput"
          },
          "rotate-after-disconnect": {
            "description": "Rotate the value of the secret after SRA session ends [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "RotateAfterDisconnect"
          },
          "rotated-password": {
            "description": "rotated-username password (relevant only for rotator-type=password)",
            "type": "string",
            "x-go-name": "RotatedPassword"
          },
          "rotated-username": {
            "description": "username to be rotated, if selected use-self-creds at rotator-creds-type, this username will try to rotate it's own password, if use-target-creds is selected, target credentials will be use to rotate the rotated-password (relevant only for rotator-type=password)",
            "type": "string",
            "x-go-name": "RotatedUser"
          },
          "rotation-hour": {
            "description": "The Hour of the rotation in UTC. Default rotation-hour is 14:00",
            "type": "integer",
            "format": "int32",
            "x-go-name": "RotationHour"
          },
          "rotation-interval": {
            "description": "The number of days to wait between every automatic key rotation (1-365)",
            "type": "string",
            "x-go-name": "RotationInterval"
          },
          "rotator-creds-type": {
            "type": "string",
            "x-go-name": "RotatorCredsTypeBC"
          },
          "rotator-custom-cmd": {
            "description": "Custom rotation command (relevant only for ssh target)",
            "type": "string",
            "x-go-name": "RotatorCustomCmd"
          },
          "rotator-type": {
            "description": "Rotator Type",
            "type": "string",
            "x-go-name": "RotatorType"
          },
          "same-password": {
            "description": "Rotate same password for each host from the Linked Target (relevant only for Linked Target)",
            "type": "string",
            "x-go-name": "SamePassword"
          },
          "secure-access-allow-external-user": {
            "description": "Allow providing external user for a domain users (relevant only for rdp)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessAllowProvidingExternalUser"
          },
          "secure-access-aws-account-id": {
            "description": "The AWS account id (relevant only for aws)",
            "type": "string",
            "x-go-name": "SecureAccessAccountId"
          },
          "secure-access-aws-native-cli": {
            "description": "The AWS native cli",
            "type": "boolean",
            "x-go-name": "SecureAccessAwsNativeCli"
          },
          "secure-access-bastion-issuer": {
            "description": "Deprecated. use secure-access-certificate-issuer",
            "type": "string",
            "x-go-name": "SecureAccessBastionIssuer"
          },
          "secure-access-certificate-issuer": {
            "description": "Path to the SSH Certificate Issuer for your Akeyless Secure Access",
            "type": "string",
            "x-go-name": "SecureAccessCertIssuer"
          },
          "secure-access-db-name": {
            "description": "The DB name (relevant only for DB Dynamic-Secret)",
            "type": "string",
            "x-go-name": "SecureAccessDBName"
          },
          "secure-access-db-schema": {
            "description": "The db schema (relevant only for mssql or postgresql)",
            "type": "string",
            "x-go-name": "SecureAccessSchema"
          },
          "secure-access-disable-concurrent-connections": {
            "description": "Enable this flag to prevent simultaneous use of the same secret",
            "type": "boolean",
            "x-go-name": "BlockConcurrentConnections"
          },
          "secure-access-enable": {
            "description": "Enable/Disable secure remote access [true/false]",
            "type": "string",
            "x-go-name": "SecureAccessEnabled"
          },
          "secure-access-host": {
            "description": "Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SecureAccessHost"
          },
          "secure-access-rdp-domain": {
            "description": "Required when the Dynamic Secret is used for a domain user (relevant only for RDP Dynamic-Secret)",
            "type": "string",
            "x-go-name": "SecureAccessDomain"
          },
          "secure-access-rdp-user": {
            "description": "Override the RDP Domain username (relevant only for rdp)",
            "type": "string",
            "x-go-name": "SecureAccessOverrideUser"
          },
          "secure-access-url": {
            "description": "Destination URL to inject secrets",
            "type": "string",
            "x-go-name": "SecureAccessURL"
          },
          "secure-access-web": {
            "description": "Enable Web Secure Remote Access",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessWebCategory"
          },
          "secure-access-web-browsing": {
            "description": "Secure browser viaAkeyless's Secure Remote Access (SRA) (relevant only for aws or azure)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessIsolated"
          },
          "secure-access-web-proxy": {
            "description": "Web-Proxy via Akeyless's Secure Remote Access (SRA) (relevant only for aws or azure)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessWebProxy"
          },
          "ssh-password": {
            "description": "Deprecated: use RotatedPassword",
            "type": "string",
            "x-go-name": "SshPassword"
          },
          "ssh-username": {
            "description": "Deprecated: use RotatedUser",
            "type": "string",
            "x-go-name": "SshUser"
          },
          "storage-account-key-name": {
            "description": "The name of the storage account key to rotate [key1/key2/kerb1/kerb2] (relevat to azure-storage-account)",
            "type": "string",
            "x-go-name": "StorageKeyName"
          },
          "tags": {
            "description": "Add tags attached to this object",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "target": {
            "description": "A list of linked targets to be associated, Relevant only for Secure Remote Access for ssh cert issuer, ldap rotated secret and ldap dynamic secret, To specify multiple targets use argument multiple times",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "TargetNames"
          },
          "target-name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
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
            "description": "LDAP User Attribute, Default value \"cn\"",
            "type": "string",
            "default": "cn",
            "x-go-name": "UserAttribute"
          },
          "user-dn": {
            "description": "LDAP User Base DN",
            "type": "string",
            "x-go-name": "UserDn"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```