# Source: https://docs.akeyless.io/reference/updateitem.md

# /update-item

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
    "/update-item": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateItem",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateItem"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateItemResponse"
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
      "updateItemResponse": {
        "description": "updateItemResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateItemOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "CertificateFormat": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "updateItem": {
        "type": "object",
        "title": "updateItem is a command that updates item.",
        "required": [
          "name"
        ],
        "properties": {
          "ProviderType": {
            "$ref": "#/components/schemas/HostProviderType"
          },
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "add-tag": {
            "description": "List of the new tags that will be attached to this item",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AddTags"
          },
          "cert-file-data": {
            "description": "PEM Certificate in a Base64 format. Used for updating RSA keys' certificates.",
            "type": "string",
            "x-go-name": "CertFileData"
          },
          "certificate-format": {
            "$ref": "#/components/schemas/CertificateFormat"
          },
          "change-event": {
            "description": "Trigger an event when a secret value changed [true/false] (Relevant only for Static Secret)",
            "type": "string",
            "x-go-name": "NotifyOnChangeEvent"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "default": "default_metadata",
            "x-go-name": "Description"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the certificate would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "gcp-sm-regions": {
            "description": "GCP Secret Manager regions to query for regional secrets (comma-separated, e.g., us-east1,us-west1). Max 12 regions.\nUSC with GCP targets only.",
            "type": "string",
            "x-go-name": "GcpSmRegions"
          },
          "host-provider": {
            "description": "Host provider type [explicit/target], Default Host provider is explicit, Relevant only for Secure Remote Access of ssh cert issuer, ldap rotated secret and ldap dynamic secret",
            "type": "string",
            "x-go-name": "HostProviderType"
          },
          "item-custom-fields": {
            "description": "Additional custom fields to associate with the item",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "ItemCustomFields"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "name": {
            "description": "Current item name",
            "type": "string",
            "x-go-name": "ItemName"
          },
          "new-metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "default": "default_metadata",
            "x-go-name": "NewMetadata"
          },
          "new-name": {
            "description": "New item name",
            "type": "string",
            "x-go-name": "NewName"
          },
          "rm-tag": {
            "description": "List of the existent tags that will be removed from this item",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RemoveTags"
          },
          "rotate-after-disconnect": {
            "description": "Rotate the value of the secret after SRA session ends [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "RotateAfterDisconnect"
          },
          "secure-access-add-host": {
            "description": "List of the new hosts that will be attached to SRA servers host",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SecureAccessAddHost"
          },
          "secure-access-allow-external-user": {
            "description": "Allow providing external user for a domain users [true/false]",
            "type": "string",
            "x-go-name": "SecureAccessAllowProvidingExternalUser"
          },
          "secure-access-allow-port-forwading": {
            "description": "Enable Port forwarding while using CLI access (relevant only for EKS/GKE/K8s Dynamic-Secret)",
            "type": "boolean",
            "x-go-name": "SecureAccessK8SAllowPortForwading"
          },
          "secure-access-api": {
            "description": "Bastion's SSH control API endpoint. E.g. https://my.sra-server:9900 (relevant only for ssh cert issuer)",
            "type": "string",
            "x-go-name": "SecureAccessAPI"
          },
          "secure-access-aws-account-id": {
            "description": "The AWS account id (relevant only for aws)",
            "type": "string",
            "x-go-name": "SecureAccessAccountId"
          },
          "secure-access-aws-native-cli": {
            "description": "The AWS native cli (relevant only for aws)",
            "type": "boolean",
            "x-go-name": "SecureAccessAwsNativeCli"
          },
          "secure-access-aws-region": {
            "description": "The AWS region (relevant only for aws)",
            "type": "string",
            "x-go-name": "SecureAccessAwsRegion"
          },
          "secure-access-bastion-api": {
            "description": "Deprecated. use secure-access-api",
            "type": "string",
            "x-go-name": "SecureAccessBastionAPI"
          },
          "secure-access-bastion-issuer": {
            "description": "Deprecated. use secure-access-certificate-issuer",
            "type": "string",
            "x-go-name": "SecureAccessBastionIssuer"
          },
          "secure-access-bastion-ssh": {
            "description": "Deprecated. use secure-access-ssh",
            "type": "string",
            "x-go-name": "SecureAccessBastionSSH"
          },
          "secure-access-certificate-issuer": {
            "description": "Path to the SSH Certificate Issuer for your Akeyless Secure Access",
            "type": "string",
            "x-go-name": "SecureAccessCertIssuer"
          },
          "secure-access-cluster-endpoint": {
            "description": "The K8s cluster endpoint URL (relevant only for EKS/GKE/K8s Dynamic-Secret)",
            "type": "string",
            "x-go-name": "SecureAccessEndpoint"
          },
          "secure-access-dashboard-url": {
            "description": "The K8s dashboard url (relevant only for k8s)",
            "type": "string",
            "x-go-name": "SecureAccessDashboardURL"
          },
          "secure-access-db-name": {
            "description": "The DB name (relevant only for DB Dynamic-Secret)",
            "type": "string",
            "x-go-name": "SecureAccessDBName"
          },
          "secure-access-db-schema": {
            "description": "The DB schema (relevant only for DB Dynamic-Secret)",
            "type": "string",
            "x-go-name": "SecureAccessSchema"
          },
          "secure-access-enable": {
            "description": "Enable/Disable secure remote access [true/false]",
            "type": "string",
            "x-go-name": "SecureAccessEnabled"
          },
          "secure-access-gateway": {
            "type": "string",
            "x-go-name": "SecureAccessGwUrl"
          },
          "secure-access-host": {
            "description": "Target servers for connections (In case of Linked Target association, host(s) will inherit Linked Target hosts - Relevant only for Dynamic Secrets/producers)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SecureAccessHost"
          },
          "secure-access-rd-gateway-server": {
            "description": "RD Gateway server (relevant only for rdp)",
            "type": "string",
            "x-go-name": "SecureAccessRDGatewayServer"
          },
          "secure-access-rdp-domain": {
            "description": "Required when the Dynamic Secret is used for a domain user (relevant only for RDP Dynamic-Secret)",
            "type": "string",
            "x-go-name": "SecureAccessDomain"
          },
          "secure-access-rdp-user": {
            "description": "Override the RDP Domain username",
            "type": "string",
            "x-go-name": "SecureAccessOverrideUser"
          },
          "secure-access-rm-host": {
            "description": "List of the existent hosts that will be removed from SRA servers host",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SecureAccessRemoveHost"
          },
          "secure-access-ssh": {
            "description": "Bastion's SSH server. E.g. my.sra-server:22 (relevant only for ssh cert issuer)",
            "type": "string",
            "x-go-name": "SecureAccessSSH"
          },
          "secure-access-ssh-creds": {
            "description": "Secret values contains SSH Credentials, either Private Key or Password [password/private-key] (relevant only for Static-Secret or Rotated-secret)",
            "type": "string",
            "x-go-name": "SecureAccessSSHCategory"
          },
          "secure-access-ssh-creds-user": {
            "description": "SSH username to connect to target server, must be in 'Allowed Users' list (relevant only for ssh cert issuer)",
            "type": "string",
            "x-go-name": "SecureAccessSSHUser"
          },
          "secure-access-url": {
            "description": "Destination URL to inject secrets",
            "type": "string",
            "x-go-name": "SecureAccessURL"
          },
          "secure-access-use-internal-bastion": {
            "description": "Deprecated. Use secure-access-use-internal-ssh-access",
            "type": "boolean",
            "x-go-name": "SecureAccessUseInternalBastion"
          },
          "secure-access-use-internal-ssh-access": {
            "description": "Use internal SSH Access",
            "type": "boolean",
            "x-go-name": "SecureAccessUseInternalSSHAccess"
          },
          "secure-access-web-browsing": {
            "description": "Secure browser via Akeyless's Secure Remote Access (SRA)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessIsolated"
          },
          "secure-access-web-proxy": {
            "description": "Web-Proxy via Akeyless's Secure Remote Access (SRA)",
            "type": "boolean",
            "default": false,
            "x-go-name": "SecureAccessWebProxy"
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
      "updateItemOutput": {
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