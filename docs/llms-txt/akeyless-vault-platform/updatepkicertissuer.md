# Source: https://docs.akeyless.io/reference/updatepkicertissuer.md

# /update-pki-cert-issuer

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
    "/update-pki-cert-issuer": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "UpdatePKICertIssuer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdatePKICertIssuer"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updatePKICertIssuerResponse"
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
      "updatePKICertIssuerResponse": {
        "description": "updatePKICertIssuerResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updatePKICertIssuerOutput"
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
      "UpdatePKICertIssuer": {
        "type": "object",
        "title": "UpdatePKICertIssuer is a command that updates a new PKI certificate issuer.",
        "required": [
          "ttl",
          "name"
        ],
        "properties": {
          "add-tag": {
            "description": "List of the new tags that will be attached to this item",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AddTags"
          },
          "allow-any-name": {
            "description": "If set, clients can request certificates for any CN",
            "type": "boolean",
            "x-go-name": "AllowAnyName"
          },
          "allow-copy-ext-from-csr": {
            "description": "If set, will allow copying the extra extensions from the csr file (if given)",
            "type": "boolean",
            "x-go-name": "AllowCopyExtFromCsr"
          },
          "allow-subdomains": {
            "description": "If set, clients can request certificates for subdomains of the allowed domains",
            "type": "boolean",
            "x-go-name": "AllowSubdomains"
          },
          "allowed-domains": {
            "description": "A list of the allowed domains that clients can request to be included in\nthe certificate (in a comma-delimited list)",
            "type": "string",
            "x-go-name": "AllowedDomains"
          },
          "allowed-extra-extensions": {
            "description": "A json string containing the allowed extra extensions for the pki cert issuer",
            "type": "string",
            "x-go-name": "AllowedExtraExtensions"
          },
          "allowed-ip-sans": {
            "description": "A list of the allowed CIDRs for ips that clients can request to be included in the certificate as part of the IP Subject Alternative Names (in a comma-delimited list)",
            "type": "string",
            "x-go-name": "AllowedIPSANs"
          },
          "allowed-uri-sans": {
            "description": "A list of the allowed URIs that clients can request to be included in\nthe certificate as part of the URI Subject Alternative Names (in a\ncomma-delimited list)",
            "type": "string",
            "x-go-name": "AllowedURISANs"
          },
          "auto-renew": {
            "description": "Automatically renew certificates before expiration",
            "type": "boolean",
            "x-go-name": "AutoRenew"
          },
          "client-flag": {
            "description": "If set, certificates will be flagged for client auth use",
            "type": "boolean",
            "x-go-name": "ClientFlag"
          },
          "code-signing-flag": {
            "description": "If set, certificates will be flagged for code signing use",
            "type": "boolean",
            "x-go-name": "CodeSigningFlag"
          },
          "country": {
            "description": "A comma-separated list of countries that will be set in the issued certificate",
            "type": "string",
            "x-go-name": "Country"
          },
          "create-private-crl": {
            "description": "Set this to allow the issuer will expose a CRL endpoint in the Gateway",
            "type": "boolean",
            "x-go-name": "CreatePrivateCrl"
          },
          "create-private-ocsp": {
            "description": "Set this to enable an OCSP endpoint in the Gateway and include its URL in AIA",
            "type": "boolean",
            "x-go-name": "CreatePrivateOcsp"
          },
          "create-public-crl": {
            "description": "Set this to allow the cert issuer will expose a public CRL endpoint",
            "type": "boolean",
            "x-go-name": "CreatePublicCrl"
          },
          "create-public-ocsp": {
            "description": "Set this to enable a public OCSP endpoint and include its URL in AIA (served by UAM and includes account id)",
            "type": "boolean",
            "x-go-name": "CreatePublicOcsp"
          },
          "critical-key-usage": {
            "description": "Mark key usage as critical [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "CriticalKeyUsage"
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
          "destination-path": {
            "description": "A path in which to save generated certificates",
            "type": "string",
            "x-go-name": "DestinationPath"
          },
          "disable-wildcards": {
            "description": "If set, generation of wildcard certificates will be disabled.",
            "type": "boolean",
            "x-go-name": "DisableWildcards"
          },
          "enable-acme": {
            "description": "If set, the cert issuer will support the acme protocol",
            "type": "boolean",
            "x-go-name": "EnableAcme"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the certificate would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "gw-cluster-url": {
            "description": "The GW cluster URL to issue the certificate from. Required in Public CA mode, to allow CRLs on private CA, or to enable ACME",
            "type": "string",
            "x-go-name": "GWClusterURL"
          },
          "is-ca": {
            "description": "If set, the basic constraints extension will be added to certificate",
            "type": "boolean",
            "x-go-name": "IsCA"
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
          "key-usage": {
            "description": "key-usage",
            "type": "string",
            "default": "DigitalSignature,KeyAgreement,KeyEncipherment",
            "x-go-name": "KeyUsage"
          },
          "locality": {
            "description": "A comma-separated list of localities that will be set in the issued certificate",
            "type": "string",
            "x-go-name": "Locality"
          },
          "max-path-len": {
            "description": "The maximum path length for the generated certificate. -1, means unlimited",
            "type": "integer",
            "format": "int64",
            "default": -1,
            "x-go-name": "MaxPathLen"
          },
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "name": {
            "description": "PKI certificate issuer name",
            "type": "string",
            "x-go-name": "IssuerName"
          },
          "new-name": {
            "description": "New item name",
            "type": "string",
            "x-go-name": "NewName"
          },
          "not-enforce-hostnames": {
            "description": "If set, any names are allowed for CN and SANs in the certificate and not\nonly a valid host name",
            "type": "boolean",
            "x-go-name": "NotEnforceHostnames"
          },
          "not-require-cn": {
            "description": "If set, clients can request certificates without a CN",
            "type": "boolean",
            "x-go-name": "NotRequireCN"
          },
          "ocsp-ttl": {
            "description": "OCSP NextUpdate window for OCSP responses (min 10m). Supports s,m,h,d suffix.",
            "type": "string",
            "x-go-name": "OcspNextUpdate"
          },
          "organizational-units": {
            "description": "A comma-separated list of organizational units (OU) that will be set in\nthe issued certificate",
            "type": "string",
            "x-go-name": "OrganizationalUnits"
          },
          "organizations": {
            "description": "A comma-separated list of organizations (O) that will be set in the\nissued certificate",
            "type": "string",
            "x-go-name": "Organizations"
          },
          "postal-code": {
            "description": "A comma-separated list of postal codes that will be set in the issued certificate",
            "type": "string",
            "x-go-name": "PostalCode"
          },
          "protect-certificates": {
            "description": "Whether to protect generated certificates from deletion",
            "type": "boolean",
            "x-go-name": "ProtectGeneratedCertificates"
          },
          "province": {
            "description": "A comma-separated list of provinces that will be set in the issued certificate",
            "type": "string",
            "x-go-name": "Province"
          },
          "rm-tag": {
            "description": "List of the existent tags that will be removed from this item",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RemoveTags"
          },
          "scheduled-renew": {
            "description": "Number of days before expiration to renew certificates",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ScheduledRenew"
          },
          "server-flag": {
            "description": "If set, certificates will be flagged for server auth use",
            "type": "boolean",
            "x-go-name": "ServerFlag"
          },
          "signer-key-name": {
            "description": "A key to sign the certificate with, required in Private CA mode",
            "type": "string",
            "x-go-name": "SignerKeyName"
          },
          "street-address": {
            "description": "A comma-separated list of street addresses that will be set in the issued certificate",
            "type": "string",
            "x-go-name": "StreetAddress"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "The maximum requested Time To Live for issued certificates, in seconds. In case of Public CA, this is based on the CA target's supported maximum TTLs",
            "type": "string",
            "x-go-name": "MaxTTL"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updatePKICertIssuerOutput": {
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