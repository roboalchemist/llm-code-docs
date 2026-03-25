# Source: https://docs.akeyless.io/reference/auth.md

# /auth

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
    "/auth": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "auth",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Auth"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/authResponse"
          },
          "401": {
            "$ref": "#/components/responses/errorResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        },
        "x-generate-protobuf": "true"
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
      "authResponse": {
        "description": "authResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AuthOutput"
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
      "Auth": {
        "type": "object",
        "properties": {
          "access-id": {
            "description": "Access ID",
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access-key": {
            "description": "Access key (relevant only for access-type=access_key)",
            "type": "string",
            "x-go-name": "AccessKey"
          },
          "access-type": {
            "description": "Access Type\n(access_key/password/saml/ldap/k8s/azure_ad/oidc/aws_iam/universal_identity/jwt/gcp/cert/oci/kerberos)",
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
          "azure-cloud": {
            "description": "Azure cloud environment to use. Values: AzureCloud (default), AzureUSGovernment, AzureChinaCloud.",
            "type": "string",
            "default": "AzureCloud",
            "x-go-name": "AzureCloud"
          },
          "cert-challenge": {
            "description": "Certificate challenge encoded in base64. (relevant only for access-type=cert)",
            "type": "string",
            "x-go-name": "CertChallengeB64"
          },
          "cert-data": {
            "description": "Certificate data encoded in base64. Used if file was not provided. (relevant only for access-type=cert)",
            "type": "string",
            "x-go-name": "CertData"
          },
          "cloud-id": {
            "description": "The cloud identity (relevant only for access-type=azure_ad,aws_iam,gcp)",
            "type": "string",
            "x-go-name": "CloudIdentity"
          },
          "debug": {
            "type": "boolean",
            "x-go-name": "Debug"
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
          "gateway-url": {
            "description": "Gateway URL relevant only for access-type=k8s/oauth2/saml/oidc",
            "type": "string",
            "x-go-name": "GatewayURL"
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
          "jwt": {
            "description": "The Json Web Token (relevant only for access-type=jwt/oidc)",
            "type": "string",
            "x-go-name": "JWT"
          },
          "k8s-auth-config-name": {
            "description": "The K8S Auth config name (relevant only for access-type=k8s)",
            "type": "string",
            "x-go-name": "K8SAuthConfigName"
          },
          "k8s-service-account-token": {
            "description": "The K8S service account token. (relevant only for access-type=k8s)",
            "type": "string",
            "x-go-name": "K8SServiceAccountToken"
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
            "description": "Private key data encoded in base64. Used if file was not provided.(relevant only for access-type=cert)",
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
          "ldap-password": {
            "description": "LDAP password (relevant only for access-type=ldap)",
            "type": "string",
            "x-go-name": "LDAPPasswordV2"
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
          },
          "otp": {
            "type": "string",
            "x-go-name": "Otp"
          },
          "signed-cert-challenge": {
            "description": "Signed certificate challenge encoded in base64. (relevant only for access-type=cert)",
            "type": "string",
            "x-go-name": "SignedCertChallengeB64"
          },
          "uid-token": {
            "description": "The universal_identity token (relevant only for\naccess-type=universal_identity)",
            "type": "string",
            "x-go-name": "UIDTokenV2"
          },
          "use-remote-browser": {
            "description": "Returns a link to complete the authentication remotely (relevant only for access-type=saml/oidc)",
            "type": "boolean",
            "x-go-name": "UseRemoteBrowser"
          },
          "username": {
            "description": "LDAP username (relevant only for access-type=ldap)",
            "type": "string",
            "x-go-name": "LDAPUsernameV2"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "AuthOutput": {
        "type": "object",
        "properties": {
          "complete_auth_link": {
            "type": "string",
            "x-go-name": "Link"
          },
          "creds": {
            "$ref": "#/components/schemas/SystemAccessCredentialsReplyObj"
          },
          "expiration": {
            "type": "string",
            "x-go-name": "ExpirationTime"
          },
          "token": {
            "type": "string",
            "x-go-name": "Token"
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
      "MFAType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SystemAccessCredentialsReplyObj": {
        "type": "object",
        "title": "Combination of three temporary credentials signed by Auth for accessing Auth, UAM and KFMs instances.",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "auth_creds": {
            "description": "Temporary credentials for accessing Auth",
            "type": "string",
            "x-go-name": "AuthAccessCredentials"
          },
          "expiry": {
            "description": "Credentials expiration date",
            "type": "integer",
            "format": "int64",
            "x-go-name": "Expiry"
          },
          "kfm_creds": {
            "description": "Temporary credentials for accessing the KFMs instances",
            "type": "string",
            "x-go-name": "KFMsAccessCredentials"
          },
          "need_mfa_app_first_config": {
            "description": "If the user didn't complete to configure the MFA app",
            "type": "boolean",
            "x-go-name": "NeedMfaAppFirstConfig"
          },
          "required_mfa": {
            "$ref": "#/components/schemas/MFAType"
          },
          "token": {
            "description": "Credentials tmp token",
            "type": "string",
            "x-go-name": "Token"
          },
          "uam_creds": {
            "description": "Temporary credentials for accessing the UAM service",
            "type": "string",
            "x-go-name": "UAMAccessCredentials"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/auth"
      }
    }
  }
}
```