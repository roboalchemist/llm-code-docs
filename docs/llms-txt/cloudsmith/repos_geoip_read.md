# Source: https://help.cloudsmith.io/reference/repos_geoip_read.md

# List all repository geoip rules.

List all repository geoip rules.

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
    "/repos/{owner}/{identifier}/geoip": {
      "get": {
        "operationId": "repos_geoip_read",
        "summary": "List all repository geoip rules.",
        "description": "List all repository geoip rules.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryGeoIpRules"
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
      "RepositoryGeoIpCidr": {
        "required": [
          "allow",
          "deny"
        ],
        "type": "object",
        "properties": {
          "allow": {
            "description": "The allowed CIDRs for this repository",
            "type": "array",
            "items": {
              "description": "The allowed CIDRs for this repository",
              "type": "string"
            },
            "uniqueItems": true
          },
          "deny": {
            "description": "The denied CIDRs for this repository",
            "type": "array",
            "items": {
              "description": "The denied CIDRs for this repository",
              "type": "string"
            },
            "uniqueItems": true
          }
        }
      },
      "RepositoryGeoIpCountryCode": {
        "required": [
          "allow",
          "deny"
        ],
        "type": "object",
        "properties": {
          "allow": {
            "description": "The allowed country codes for this repository",
            "type": "array",
            "items": {
              "description": "The allowed country codes for this repository",
              "type": "string"
            },
            "uniqueItems": true
          },
          "deny": {
            "description": "The denied country codes for this repository",
            "type": "array",
            "items": {
              "description": "The denied country codes for this repository",
              "type": "string"
            },
            "uniqueItems": true
          }
        }
      },
      "RepositoryGeoIpRules": {
        "required": [
          "cidr",
          "country_code"
        ],
        "type": "object",
        "properties": {
          "cidr": {
            "$ref": "#/components/schemas/RepositoryGeoIpCidr"
          },
          "country_code": {
            "$ref": "#/components/schemas/RepositoryGeoIpCountryCode"
          }
        }
      }
    }
  }
}
```