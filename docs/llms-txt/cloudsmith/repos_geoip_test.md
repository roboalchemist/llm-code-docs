# Source: https://help.cloudsmith.io/reference/repos_geoip_test.md

# Test a list of IP addresses against the repository's current GeoIP rules.

Test a list of IP addresses against the repository's current GeoIP rules.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/repos/{owner}/{identifier}/geoip/test/": {
      "post": {
        "operationId": "repos_geoip_test",
        "summary": "Test a list of IP addresses against the repository's current GeoIP rules.",
        "description": "Test a list of IP addresses against the repository's current GeoIP rules.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RepositoryGeoIpTestAddress"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Successfuly tested addresses against the repository's GeoIP rules",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryGeoIpTestAddressResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "402": {
            "description": "Geo/IP restrictions are not available; upgrade your account!",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "Owner namespace or repository not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "repos"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "identifier",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "RepositoryGeoIpTestAddress": {
        "required": [
          "addresses"
        ],
        "type": "object",
        "properties": {
          "addresses": {
            "description": "The IP addresses to test against this repository",
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            }
          }
        }
      },
      "RepositoryGeoIpTestAddressResponseDict": {
        "required": [
          "allowed",
          "country_code",
          "ip_address",
          "reason"
        ],
        "type": "object",
        "properties": {
          "allowed": {
            "title": "Allowed",
            "description": "The result of the IP test",
            "type": "boolean"
          },
          "country_code": {
            "title": "Country code",
            "description": "The country code of the tested IP address",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "ip_address": {
            "title": "Ip address",
            "description": "The IP address that was tested",
            "type": "string",
            "minLength": 1
          },
          "reason": {
            "title": "Reason",
            "description": "The reason for the result",
            "type": "string",
            "minLength": 1
          }
        }
      },
      "RepositoryGeoIpTestAddressResponse": {
        "required": [
          "addresses"
        ],
        "type": "object",
        "properties": {
          "addresses": {
            "description": "The IP address test results ordered by allowed",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RepositoryGeoIpTestAddressResponseDict"
            }
          }
        }
      }
    }
  }
}
```