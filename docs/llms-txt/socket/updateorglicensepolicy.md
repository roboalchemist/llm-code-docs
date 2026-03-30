# Source: https://docs.socket.dev/reference/updateorglicensepolicy.md

# Update License Policy

Set the organization's license policy

      ## License policy schema

```json
{
  allow?: Array<string>
  warn?: Array<string>
  options?: Array<string>
}
```

Elements of the `allow` and `warn` arrays strings representing items which should be allowed, or which should trigger a warning; license data found in package which not present in either array will produce a license violation (effectively a "hard" error). For example, to allow Apache-2.0 and MIT to the allow list, simply add the strings "Apache-2.0" and "MIT" to the `allow` array. Strings appearing in these arrays are generally "what you see is what you get", with two important exceptions: strings which are recognized as license classes and strings which are recognized as PURLs are handled differently to allow for more flexible license policy creation.

## License Classes

Strings which are license classes will expand to a list of licenses known to be in that particular license class. Recognized license classes are:
  'permissive',
  'permissive (model)',
  'permissive (gold)',
  'permissive (silver)',
  'permissive (bronze)',
  'permissive (lead)',
  'copyleft',
  'maximal copyleft',
  'network copyleft',
  'strong copyleft',
  'weak copyleft',
  'contributor license agreement',
  'public domain',
  'proprietary free',
  'source available',
  'proprietary',
  'commercial',
  'patent'

Users can learn more about [copyleft tiers](https://blueoakcouncil.org/copyleft) and [permissive tiers](https://blueoakcouncil.org/list) by reading the linked resources.


## PURLs

Users may also modify their license policy's allow and warn lists by using [package URLs](https://github.com/package-url/purl-spec) (aka PURLs), which support glob patterns to allow a range of versions, files and directories, etc.

purl qualifiers which support globs are `filename`, `version_glob`, `artifact_id` and `license_provenance` (primarily used for allowing data from registry metadata).

### Examples:
Allow all license data found in a specific version of a package 4.14.1: `pkg:npm/lodash@4.14.1`
Allow all license data found in a version range of a package: `pkg:npm/lodash?version_glob=15.*`
Allow all license data in the test directory of a given package for certain version ranges: `pkg:npm/lodash@15.*.*?file_name=lodash/test/*`
Allow all license data taken from the package registry for a package and version range: `pkg:npm/lodash?version_glob=*&license_provenance=registry_metadata`

## Available options

`toplevelOnly`: only apply the license policy to "top level" license data in a package, which includes registry metadata, LICENSE files, and manifest files which are closest to the root of the package.

`applyToUnidentified`: Apply license policy to found but unidentified license data. If enabled, the license policy will be applied to license data which could not be affirmatively identified as a known license (this will effectively merge the license policy violation and unidentified license alerts). If disabled, license policy alerts will only be shown for license data which is positively identified as something not allowed or set to warn by the license policy.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- license-policy:update

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
      "name": "license-policy"
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
    "/orgs/{org_slug}/settings/license-policy": {
      "post": {
        "tags": [
          "license-policy"
        ],
        "summary": "Update License Policy",
        "operationId": "updateOrgLicensePolicy",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "merge_update",
            "in": "query",
            "required": true,
            "description": "Merge the policy update with the existing policy. Default is true. If false, the existing policy will be replaced with the new policy.",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "description": "",
                "default": null
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "license-policy:update"
            ]
          },
          {
            "basicAuth": [
              "license-policy:update"
            ]
          }
        ],
        "description": "Set the organization's license policy\n\n      ## License policy schema\n\n```json\n{\n  allow?: Array<string>\n  warn?: Array<string>\n  options?: Array<string>\n}\n```\n\nElements of the `allow` and `warn` arrays strings representing items which should be allowed, or which should trigger a warning; license data found in package which not present in either array will produce a license violation (effectively a \"hard\" error). For example, to allow Apache-2.0 and MIT to the allow list, simply add the strings \"Apache-2.0\" and \"MIT\" to the `allow` array. Strings appearing in these arrays are generally \"what you see is what you get\", with two important exceptions: strings which are recognized as license classes and strings which are recognized as PURLs are handled differently to allow for more flexible license policy creation.\n\n## License Classes\n\nStrings which are license classes will expand to a list of licenses known to be in that particular license class. Recognized license classes are:\n  'permissive',\n  'permissive (model)',\n  'permissive (gold)',\n  'permissive (silver)',\n  'permissive (bronze)',\n  'permissive (lead)',\n  'copyleft',\n  'maximal copyleft',\n  'network copyleft',\n  'strong copyleft',\n  'weak copyleft',\n  'contributor license agreement',\n  'public domain',\n  'proprietary free',\n  'source available',\n  'proprietary',\n  'commercial',\n  'patent'\n\nUsers can learn more about [copyleft tiers](https://blueoakcouncil.org/copyleft) and [permissive tiers](https://blueoakcouncil.org/list) by reading the linked resources.\n\n\n## PURLs\n\nUsers may also modify their license policy's allow and warn lists by using [package URLs](https://github.com/package-url/purl-spec) (aka PURLs), which support glob patterns to allow a range of versions, files and directories, etc.\n\npurl qualifiers which support globs are `filename`, `version_glob`, `artifact_id` and `license_provenance` (primarily used for allowing data from registry metadata).\n\n### Examples:\nAllow all license data found in a specific version of a package 4.14.1: `pkg:npm/lodash@4.14.1`\nAllow all license data found in a version range of a package: `pkg:npm/lodash?version_glob=15.*`\nAllow all license data in the test directory of a given package for certain version ranges: `pkg:npm/lodash@15.*.*?file_name=lodash/test/*`\nAllow all license data taken from the package registry for a package and version range: `pkg:npm/lodash?version_glob=*&license_provenance=registry_metadata`\n\n## Available options\n\n`toplevelOnly`: only apply the license policy to \"top level\" license data in a package, which includes registry metadata, LICENSE files, and manifest files which are closest to the root of the package.\n\n`applyToUnidentified`: Apply license policy to found but unidentified license data. If enabled, the license policy will be applied to license data which could not be affirmatively identified as a known license (this will effectively merge the license policy violation and unidentified license alerts). If disabled, license policy alerts will only be shown for license data which is positively identified as something not allowed or set to warn by the license policy.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- license-policy:update",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "description": "",
                  "default": null
                }
              }
            },
            "description": "Updated repository details"
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
          }
        },
        "x-readme": {}
      }
    }
  }
}
````