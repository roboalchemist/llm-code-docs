# Source: https://docs.akeyless.io/reference/certificatediscovery.md

# /certificate-discovery

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
    "/certificate-discovery": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "CertificateDiscovery",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CertificateDiscovery"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/CertificateDiscoveryResponse"
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
      "CertificateDiscoveryResponse": {
        "description": "CertificateDiscoveryResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CertificateDiscoveryOutput"
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
      "CertificateDiscovery": {
        "description": "CertificateDiscovery is a command that discovery certificates",
        "type": "object",
        "required": [
          "hosts",
          "target-location"
        ],
        "properties": {
          "debug": {
            "description": "Debug mode",
            "type": "boolean",
            "default": false,
            "x-go-name": "Debug"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the certificate would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "hosts": {
            "description": "A comma separated list of IPs, CIDR ranges, or DNS names to discovery",
            "type": "string",
            "x-go-name": "Hosts"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "port-ranges": {
            "description": "A comma separated list of port ranges\nExamples: \"80,443\" or \"80,443,8080-8090\" or \"443\"",
            "type": "string",
            "default": "443",
            "x-go-name": "PortRanges"
          },
          "protection-key": {
            "description": "The name of the key that protects the certificate value",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "target-location": {
            "description": "The folder where the results will be saved",
            "type": "string",
            "x-go-name": "TargetFolder"
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
      "CertificateDiscoveryOutput": {
        "type": "object",
        "properties": {
          "results": {
            "$ref": "#/components/schemas/ScanResults"
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
      "ScanResults": {
        "description": "ScanResults contains detailed results from a certificate scan",
        "type": "object",
        "properties": {
          "CountExisting": {
            "type": "integer",
            "format": "int64"
          },
          "CountFailed": {
            "type": "integer",
            "format": "int64"
          },
          "CountHosts": {
            "type": "integer",
            "format": "int64"
          },
          "CountNew": {
            "type": "integer",
            "format": "int64"
          },
          "CountSubdomains": {
            "type": "integer",
            "format": "int64"
          },
          "Error": {
            "type": "string",
            "x-go-type": "error"
          },
          "FailedTargets": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TargetError"
            }
          },
          "ItemNames": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/certificate/certificate_discovery/scanner/results"
      },
      "TargetError": {
        "description": "TargetError represents a failed target scan",
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Error"
          },
          "host": {
            "type": "string",
            "x-go-name": "Host"
          },
          "port": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Port"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/certificate/certificate_discovery/scanner/results"
      }
    }
  }
}
```