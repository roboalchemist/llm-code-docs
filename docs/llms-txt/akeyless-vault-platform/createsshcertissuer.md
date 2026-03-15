# Source: https://docs.akeyless.io/reference/createsshcertissuer.md

# /create-ssh-cert-issuer

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
    "/create-ssh-cert-issuer": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createSSHCertIssuer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createSSHCertIssuer"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createSSHCertIssuerResponse"
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
      "createSSHCertIssuerResponse": {
        "description": "createSSHCertIssuerResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createSSHCertIssuerOutput"
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
      "createSSHCertIssuer": {
        "type": "object",
        "title": "createSSHCertIssuer is a command that creates a new SSH certificate issuer.",
        "required": [
          "signer-key-name",
          "allowed-users",
          "ttl",
          "name"
        ],
        "properties": {
          "ProviderType": {
            "$ref": "#/components/schemas/HostProviderType"
          },
          "allowed-users": {
            "description": "Users allowed to fetch the certificate, e.g root,ubuntu",
            "type": "string",
            "default": "-",
            "x-go-name": "AllowedUsers"
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
          "extensions": {
            "description": "Signed certificates with extensions, e.g permit-port-forwarding=\\\"\\\"",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Extensions"
          },
          "external-username": {
            "description": "Externally provided username [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "FixedUserOnly"
          },
          "fixed-user-claim-keyname": {
            "description": "For externally provided users, denotes the key-name of IdP claim to extract the username from (relevant only for external-username=true)",
            "type": "string",
            "x-go-name": "FixedUserClaimKeyname"
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
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "name": {
            "description": "SSH certificate issuer name",
            "type": "string",
            "x-go-name": "IssuerName"
          },
          "principals": {
            "description": "Signed certificates with principal, e.g example_role1,example_role2",
            "type": "string",
            "x-go-name": "Principals"
          },
          "secure-access-api": {
            "description": "Secure Access SSH control API endpoint. E.g. https://my.sra-server:9900",
            "type": "string",
            "x-go-name": "SecureAccessAPI"
          },
          "secure-access-bastion-api": {
            "description": "Deprecated. use secure-access-api",
            "type": "string",
            "x-go-name": "SecureAccessBastionAPI"
          },
          "secure-access-bastion-ssh": {
            "description": "Deprecated. use secure-access-ssh",
            "type": "string",
            "x-go-name": "SecureAccessBastionSSH"
          },
          "secure-access-enable": {
            "description": "Enable/Disable secure remote access [true/false]",
            "type": "string",
            "x-go-name": "SecureAccessEnabled"
          },
          "secure-access-enforce-hosts-restriction": {
            "description": "Enable this flag to enforce connections only to the hosts listed in --secure-access-host",
            "type": "boolean",
            "x-go-name": "EnforceHostsRestriction"
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
          "secure-access-ssh": {
            "description": "Bastion's SSH server. E.g. my.sra-server:22",
            "type": "string",
            "x-go-name": "SecureAccessSSH"
          },
          "secure-access-ssh-creds-user": {
            "description": "SSH username to connect to target server, must be in 'Allowed Users' list",
            "type": "string",
            "x-go-name": "SecureAccessSSHUser"
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
          "signer-key-name": {
            "description": "A key to sign the certificate with",
            "type": "string",
            "x-go-name": "SignerKeyName"
          },
          "tag": {
            "description": "List of the tags attached to this key",
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
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "The requested Time To Live for the certificate, in seconds",
            "type": "integer",
            "format": "int64",
            "x-go-name": "TTL"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "createSSHCertIssuerOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```