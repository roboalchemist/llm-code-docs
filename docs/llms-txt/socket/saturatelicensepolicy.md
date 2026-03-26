# Source: https://docs.socket.dev/reference/saturatelicensepolicy.md

# Saturate License Policy (Legacy)

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/updateorglicensepolicy) instead.

Get the "saturated" version of a license policy's allow list, filling in the entire set of allowed
license data. For example, the saturated form of a license allow list which only specifies that
licenses in the tier "maximal copyleft" are allowed is shown below (note the expanded `allowedStrings` property):

```json
{
  "allowedApprovalSources": [],
  "allowedFamilies": [],
  "allowedTiers": [
    "maximal copyleft"
  ],
  "allowedStrings": [
    "Parity-6.0.0",
    "QPL-1.0-INRIA-2004",
    "QPL-1.0",
    "RPL-1.1",
    "RPL-1.5"
  ],
  "allowedPURLs": [],
  "focusAlertsHere": false
}
```

This may be helpful for users who want to compose more complex sets of allowed license data via
the "allowedStrings" property, or for users who want to know more about the contents of a particular
license group (family, tier, or approval source).

## Allow List Schema

```json
```

where

PermissiveTier ::= "model permissive" | "gold" | "silver" | "bronze" | "lead"
CopyleftTier ::= "maximal copyleft" | "network copyleft" | "strong copyleft" | "weak copyleft"

## Return Value

The returned value has the same shape as a license allow list:

```json
{
  allowedApprovalSources?: Array<"fsf" | "osi">,
  allowedFamilies?: Array<"copyleft" | "permissive">,
  allowedTiers?: Array<PermissiveTier | CopyleftTier>,
  allowedStrings?: Array<string>
  allowedPURLs?: Array<string>
  focusAlertsHere?: boolean
}
```

where

PermissiveTier ::= "model permissive" | "gold" | "silver" | "bronze" | "lead"
CopyleftTier ::= "maximal copyleft" | "network copyleft" | "strong copyleft" | "weak copyleft"

readers can learn more about [copyleft tiers](https://blueoakcouncil.org/copyleft) and [permissive tiers](https://blueoakcouncil.org/list) by reading the linked resources.

### Example request bodies:
```json
{
  "allowedApprovalSources": ["fsf"],
  "allowedPURLs": [],
  "allowedFamilies": ["copyleft"],
  "allowedTiers": ["model permissive"],
  "allowedStrings": ["License :: OSI Approved :: BSD License"],
  "focusAlertsHere": false
}
```

This endpoint consumes 100 units of your quota.

This endpoint requires the following org token scopes:
- packages:list

# OpenAPI definition

````json
{
  "openapi": "3.0.0",
  "info": {
    "description": "Specification of the Socket API endpoints",
    "title": "API Endpoints",
    "version": "0"
  },
  "servers": [
    {
      "url": "https://api.socket.dev/v0"
    }
  ],
  "tags": [
    {
      "name": "deprecated"
    }
  ],
  "components": {
    "responses": {
      "SocketBadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Bad request"
      },
      "SocketUnauthorized": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Unauthorized"
      },
      "SocketForbidden": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Insufficient max_quota for API method"
      },
      "SocketNotFoundResponse": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Resource not found"
      },
      "SocketTooManyRequestsResponse": {
        "description": "Insufficient quota for API route",
        "headers": {
          "Retry-After": {
            "description": "Retry contacting the endpoint *at least* after seconds.\nSee https://tools.ietf.org/html/rfc7231#section-7.1.3",
            "schema": {
              "format": "int32",
              "type": "integer"
            }
          }
        },
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        }
      },
      "SocketInternalServerError": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Internal server error"
      }
    },
    "schemas": {
      "LicensePolicy": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "allow": {
            "$ref": "#/components/schemas/LicenseAllowListElabbed"
          },
          "warn": {
            "$ref": "#/components/schemas/LicenseAllowListElabbed"
          },
          "monitor": {
            "$ref": "#/components/schemas/LicenseAllowListElabbed"
          }
        },
        "required": [
          "allow",
          "monitor",
          "warn"
        ]
      },
      "LicenseAllowList": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "strings": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          }
        },
        "required": [
          "strings"
        ]
      },
      "LicenseAllowListElabbed": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "strings": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          },
          "classes": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          },
          "packageURLs": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          },
          "disjs": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "",
              "default": ""
            },
            "description": ""
          }
        },
        "required": [
          "classes",
          "disjs",
          "packageURLs",
          "strings"
        ]
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "description": "Organization Tokens can be passed as a Bearer token"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Organization Tokens can be passed as the user field in basic auth"
      }
    }
  },
  "paths": {
    "/saturate-license-policy": {
      "post": {
        "tags": [
          "deprecated"
        ],
        "summary": "Saturate License Policy (Legacy)",
        "deprecated": true,
        "operationId": "saturateLicensePolicy",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": false,
                "description": "",
                "properties": {
                  "allow": {
                    "$ref": "#/components/schemas/LicenseAllowList"
                  },
                  "warn": {
                    "$ref": "#/components/schemas/LicenseAllowList"
                  },
                  "monitor": {
                    "$ref": "#/components/schemas/LicenseAllowList"
                  },
                  "allowedApprovalSources": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "description": "",
                    "nullable": true
                  },
                  "allowedFamilies": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "description": "",
                    "nullable": true
                  },
                  "allowedTiers": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "description": "",
                    "nullable": true
                  },
                  "allowedStrings": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "description": "",
                    "nullable": true
                  },
                  "allowedPURLs": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "description": "",
                    "nullable": true
                  },
                  "focusAlertsHere": {
                    "type": "boolean",
                    "default": false,
                    "description": "",
                    "nullable": true
                  }
                },
                "required": [
                  "allow",
                  "allowedApprovalSources",
                  "allowedFamilies",
                  "allowedPURLs",
                  "allowedStrings",
                  "allowedTiers",
                  "focusAlertsHere",
                  "monitor",
                  "warn"
                ]
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "packages:list"
            ]
          },
          {
            "basicAuth": [
              "packages:list"
            ]
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/updateorglicensepolicy) instead.\n\nGet the \"saturated\" version of a license policy's allow list, filling in the entire set of allowed\nlicense data. For example, the saturated form of a license allow list which only specifies that\nlicenses in the tier \"maximal copyleft\" are allowed is shown below (note the expanded `allowedStrings` property):\n\n```json\n{\n  \"allowedApprovalSources\": [],\n  \"allowedFamilies\": [],\n  \"allowedTiers\": [\n    \"maximal copyleft\"\n  ],\n  \"allowedStrings\": [\n    \"Parity-6.0.0\",\n    \"QPL-1.0-INRIA-2004\",\n    \"QPL-1.0\",\n    \"RPL-1.1\",\n    \"RPL-1.5\"\n  ],\n  \"allowedPURLs\": [],\n  \"focusAlertsHere\": false\n}\n```\n\nThis may be helpful for users who want to compose more complex sets of allowed license data via\nthe \"allowedStrings\" property, or for users who want to know more about the contents of a particular\nlicense group (family, tier, or approval source).\n\n## Allow List Schema\n\n```json\n```\n\nwhere\n\nPermissiveTier ::= \"model permissive\" | \"gold\" | \"silver\" | \"bronze\" | \"lead\"\nCopyleftTier ::= \"maximal copyleft\" | \"network copyleft\" | \"strong copyleft\" | \"weak copyleft\"\n\n## Return Value\n\nThe returned value has the same shape as a license allow list:\n\n```json\n{\n  allowedApprovalSources?: Array<\"fsf\" | \"osi\">,\n  allowedFamilies?: Array<\"copyleft\" | \"permissive\">,\n  allowedTiers?: Array<PermissiveTier | CopyleftTier>,\n  allowedStrings?: Array<string>\n  allowedPURLs?: Array<string>\n  focusAlertsHere?: boolean\n}\n```\n\nwhere\n\nPermissiveTier ::= \"model permissive\" | \"gold\" | \"silver\" | \"bronze\" | \"lead\"\nCopyleftTier ::= \"maximal copyleft\" | \"network copyleft\" | \"strong copyleft\" | \"weak copyleft\"\n\nreaders can learn more about [copyleft tiers](https://blueoakcouncil.org/copyleft) and [permissive tiers](https://blueoakcouncil.org/list) by reading the linked resources.\n\n### Example request bodies:\n```json\n{\n  \"allowedApprovalSources\": [\"fsf\"],\n  \"allowedPURLs\": [],\n  \"allowedFamilies\": [\"copyleft\"],\n  \"allowedTiers\": [\"model permissive\"],\n  \"allowedStrings\": [\"License :: OSI Approved :: BSD License\"],\n  \"focusAlertsHere\": false\n}\n```\n\nThis endpoint consumes 100 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- packages:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/LicensePolicy"
                }
              }
            },
            "description": "Saturated License Allow List"
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
          },
          "404": {
            "$ref": "#/components/responses/SocketNotFoundResponse"
          },
          "429": {
            "$ref": "#/components/responses/SocketTooManyRequestsResponse"
          },
          "500": {
            "$ref": "#/components/responses/SocketInternalServerError"
          }
        },
        "x-readme": {}
      }
    }
  }
}
````