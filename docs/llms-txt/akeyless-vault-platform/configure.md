# Source: https://docs.akeyless.io/reference/configure.md

# /configure

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
    "/configure": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "configure",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/configure"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/configureResponse"
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
      "configureResponse": {
        "description": "configureResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/configureOutput"
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
      "configure": {
        "type": "object",
        "title": "configure is a command that creates a new Akeyless profile.",
        "properties": {
          "access-id": {
            "description": "Access ID",
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access-key": {
            "description": "Access Key",
            "type": "string",
            "x-go-name": "AccessKey"
          },
          "access-type": {
            "description": "Access Type (access_key/password/azure_ad/saml/oidc/aws_iam/gcp/k8s/cert)",
            "type": "string",
            "default": "access_key",
            "x-go-name": "AccessType"
          },
          "account-id": {
            "description": "Account id (relevant only for access-type=password where the email address is associated with more than one account)",
            "type": "string",
            "x-go-name": "AccountId"
          },
          "admin-email": {
            "description": "Email (relevant only for access-type=password)",
            "type": "string",
            "x-go-name": "AdminEmail"
          },
          "admin-password": {
            "description": "Password (relevant only for access-type=password)",
            "type": "string",
            "x-go-name": "AdminPass"
          },
          "azure-ad-object-id": {
            "description": "Azure Active Directory ObjectId (relevant only for access-type=azure_ad)",
            "type": "string",
            "x-go-name": "AzureAdObjectIDV2"
          },
          "azure-cloud": {
            "description": "Azure cloud environment to use. Values: AzureCloud (default), AzureUSGovernment, AzureChinaCloud.",
            "type": "string",
            "default": "AzureCloud",
            "x-go-name": "AzureCloud"
          },
          "cert-data": {
            "description": "Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type=cert in Curl Context)",
            "type": "string",
            "x-go-name": "CertData"
          },
          "cert-issuer-name": {
            "description": "Certificate Issuer Name",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "cert-username": {
            "description": "The username to sign in the SSH certificate (use a comma-separated list for more than one username)",
            "type": "string",
            "x-go-name": "CertUsername"
          },
          "default-location-prefix": {
            "description": "Default path prefix for name of items, targets and auth methods",
            "type": "string",
            "x-go-name": "Prefix"
          },
          "disable-pafxfast": {
            "description": "Disable the FAST negotiation in the Kerberos authentication method",
            "type": "string",
            "x-go-name": "DisablePAFXFAST"
          },
          "gateway-spn": {
            "description": "The service principal name of the gateway as registered in LDAP (i.e., HTTP/gateway)",
            "type": "string",
            "x-go-name": "GatewaySPN"
          },
          "gcp-audience": {
            "description": "GCP JWT audience",
            "type": "string",
            "default": "akeyless.io",
            "x-go-name": "GCPAudience"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "k8s-auth-config-name": {
            "description": "The K8S Auth config name (relevant only for access-type=k8s)",
            "type": "string",
            "x-go-name": "K8SAuthConfigName"
          },
          "kerberos-token": {
            "description": "KerberosToken represents a Kerberos token generated for the gateway SPN (Service Principal Name).",
            "type": "string",
            "x-go-name": "KerberosToken"
          },
          "kerberos-username": {
            "description": "TThe username for the entry within the keytab to authenticate via Kerberos",
            "type": "string",
            "x-go-name": "KerberosUsername"
          },
          "key-data": {
            "description": "Private key data encoded in base64. Used if file was not provided.(relevant only for access-type=cert in Curl Context)",
            "type": "string",
            "x-go-name": "KeyData"
          },
          "keytab-data": {
            "description": "Base64-encoded content of a valid keytab file, containing the service account's entry.",
            "type": "string",
            "x-go-name": "KeytabData"
          },
          "krb5-conf-data": {
            "description": "Base64-encoded content of a valid krb5.conf file, specifying the settings and parameters required for Kerberos authentication.",
            "type": "string",
            "x-go-name": "Krb5ConfData"
          },
          "legacy-signing-alg-name": {
            "description": "Set this option to output legacy ('ssh-rsa-cert-v01@openssh.com') signing algorithm name in the certificate.",
            "type": "boolean",
            "x-go-name": "LegacySigningAlg"
          },
          "oci-auth-type": {
            "description": "The type of the OCI configuration to use [instance/apikey/resource] (relevant only for access-type=oci)",
            "type": "string",
            "default": "apikey",
            "x-go-name": "OCIAuthType"
          },
          "oci-group-ocid": {
            "description": "A list of Oracle Cloud IDs groups (relevant only for access-type=oci)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "OCIGroupOCIDs"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "configureOutput": {
        "type": "object",
        "properties": {
          "profile": {
            "type": "string",
            "x-go-name": "Profile"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```