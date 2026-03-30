# Source: https://docs.akeyless.io/reference/signpkicertwithclassickey.md

# /sign-pki-cert-with-classic-key

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
    "/sign-pki-cert-with-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "signPKICertWithClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/signPKICertWithClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/signPKICertWithClassicKeyResponse"
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
      "signPKICertWithClassicKeyResponse": {
        "description": "signPKICertWithClassicKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/signPKICertOutput"
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
      "signPKICertOutput": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "signPKICertWithClassicKey": {
        "type": "object",
        "title": "signPKICertWithClassicKey is a command that signs PKI certificate by using an Classic key.",
        "required": [
          "display-id",
          "version",
          "signing-method",
          "ttl"
        ],
        "properties": {
          "common-name": {
            "description": "The common name to be included in the PKI certificate",
            "type": "string",
            "x-go-name": "CommonName"
          },
          "country": {
            "description": "A comma-separated list of the country that will be set in the issued\ncertificate",
            "type": "string",
            "x-go-name": "Country"
          },
          "display-id": {
            "description": "The name of the key to use in the sign PKI Cert process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "dns-names": {
            "description": "DNS Names to be included in the PKI certificate (in a comma-delimited list)",
            "type": "string",
            "x-go-name": "DNSNames"
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
            "description": "A comma-separated list of the locality that will be set in the issued\ncertificate",
            "type": "string",
            "x-go-name": "Locality"
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
            "description": "A comma-separated list of the postal code that will be set in the issued\ncertificate",
            "type": "string",
            "x-go-name": "PostalCode"
          },
          "province": {
            "description": "A comma-separated list of the province that will be set in the issued\ncertificate",
            "type": "string",
            "x-go-name": "Province"
          },
          "public-key-pem-data": {
            "description": "PublicKey using for signing in a PEM format.",
            "type": "string",
            "x-go-name": "PublicKeyPEMData"
          },
          "signing-method": {
            "description": "SigningMethod",
            "type": "string",
            "x-go-name": "SigningMethod"
          },
          "street-address": {
            "description": "A comma-separated list of the street address that will be set in the\nissued certificate",
            "type": "string",
            "x-go-name": "StreetAddress"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "ttl": {
            "description": "he requested Time To Live for the certificate, in seconds",
            "type": "integer",
            "format": "int64",
            "x-go-name": "TTL"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "uri-sans": {
            "description": "The URI Subject Alternative Names to be included in the PKI certificate (in a comma-delimited list)",
            "type": "string",
            "x-go-name": "URISANs"
          },
          "version": {
            "description": "classic key version",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```