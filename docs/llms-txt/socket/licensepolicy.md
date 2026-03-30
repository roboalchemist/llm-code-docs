# Source: https://docs.socket.dev/reference/licensepolicy.md

# License Policy (Beta)

Compare the license data found for a list of packages (given as PURL strings) with the contents of a configurable license policy,
    returning information about license data which does not comply with the license allow list.

    ## Example request body:

    ```json
    {
      "components": [
        {
          "purl": "pkg:npm/lodash@4.17.21"
        },
        {
          "purl": "pkg:npm/lodash@4.14.1"
        }
      ],
      "allow": [
        "permissive",
        "pkg:npm/lodash?file_name=foo/test/*&version_glob=4.17.*"
      ],
      "warn": [
        "copyleft",
        "pkg:npm/lodash?file_name=foo/prod/*&version_glob=4.14.*"
      ],
      "options": ["toplevelOnly"]
    }
    ```


    ## Return value

    For each requested PURL, an array is returned. Each array contains a list of license policy violations
    detected for the requested PURL.

    Violations are accompanied by a string identifying the offending license data as `spdxAtomOrExtraData`,
    a message describing why the license data is believed to be incompatible with the license policy, and a list
    of locations (by filepath or other provenance information) where the offending license data may be found.

    ```json
    Array<
      Array<{
        filepathOrProvenance: Array<string>,
        level: "warning" | "violation",
        purl: string,
        spdxAtomOrExtraData: string,
        violationExplanation: string
      }>
    >
    ```

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

This endpoint consumes 100 units of your quota.

This endpoint requires the following org token scopes:
      - packages:list
- license-policy:read

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
      "LicenseAllowListRequest": {
        "type": "object",
        "description": "",
        "default": null
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
    "/license-policy": {
      "post": {
        "tags": [
          "license-policy"
        ],
        "summary": "License Policy (Beta)",
        "operationId": "licensePolicy",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LicenseAllowListRequest"
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "packages:list",
              "license-policy:read"
            ]
          },
          {
            "basicAuth": [
              "packages:list",
              "license-policy:read"
            ]
          }
        ],
        "description": "Compare the license data found for a list of packages (given as PURL strings) with the contents of a configurable license policy,\n    returning information about license data which does not comply with the license allow list.\n\n    ## Example request body:\n\n    ```json\n    {\n      \"components\": [\n        {\n          \"purl\": \"pkg:npm/lodash@4.17.21\"\n        },\n        {\n          \"purl\": \"pkg:npm/lodash@4.14.1\"\n        }\n      ],\n      \"allow\": [\n        \"permissive\",\n        \"pkg:npm/lodash?file_name=foo/test/*&version_glob=4.17.*\"\n      ],\n      \"warn\": [\n        \"copyleft\",\n        \"pkg:npm/lodash?file_name=foo/prod/*&version_glob=4.14.*\"\n      ],\n      \"options\": [\"toplevelOnly\"]\n    }\n    ```\n\n\n    ## Return value\n\n    For each requested PURL, an array is returned. Each array contains a list of license policy violations\n    detected for the requested PURL.\n\n    Violations are accompanied by a string identifying the offending license data as `spdxAtomOrExtraData`,\n    a message describing why the license data is believed to be incompatible with the license policy, and a list\n    of locations (by filepath or other provenance information) where the offending license data may be found.\n\n    ```json\n    Array<\n      Array<{\n        filepathOrProvenance: Array<string>,\n        level: \"warning\" | \"violation\",\n        purl: string,\n        spdxAtomOrExtraData: string,\n        violationExplanation: string\n      }>\n    >\n    ```\n\n    ## License policy schema\n\n```json\n{\n  allow?: Array<string>\n  warn?: Array<string>\n  options?: Array<string>\n}\n```\n\nElements of the `allow` and `warn` arrays strings representing items which should be allowed, or which should trigger a warning; license data found in package which not present in either array will produce a license violation (effectively a \"hard\" error). For example, to allow Apache-2.0 and MIT to the allow list, simply add the strings \"Apache-2.0\" and \"MIT\" to the `allow` array. Strings appearing in these arrays are generally \"what you see is what you get\", with two important exceptions: strings which are recognized as license classes and strings which are recognized as PURLs are handled differently to allow for more flexible license policy creation.\n\n## License Classes\n\nStrings which are license classes will expand to a list of licenses known to be in that particular license class. Recognized license classes are:\n  'permissive',\n  'permissive (model)',\n  'permissive (gold)',\n  'permissive (silver)',\n  'permissive (bronze)',\n  'permissive (lead)',\n  'copyleft',\n  'maximal copyleft',\n  'network copyleft',\n  'strong copyleft',\n  'weak copyleft',\n  'contributor license agreement',\n  'public domain',\n  'proprietary free',\n  'source available',\n  'proprietary',\n  'commercial',\n  'patent'\n\nUsers can learn more about [copyleft tiers](https://blueoakcouncil.org/copyleft) and [permissive tiers](https://blueoakcouncil.org/list) by reading the linked resources.\n\n\n## PURLs\n\nUsers may also modify their license policy's allow and warn lists by using [package URLs](https://github.com/package-url/purl-spec) (aka PURLs), which support glob patterns to allow a range of versions, files and directories, etc.\n\npurl qualifiers which support globs are `filename`, `version_glob`, `artifact_id` and `license_provenance` (primarily used for allowing data from registry metadata).\n\n### Examples:\nAllow all license data found in a specific version of a package 4.14.1: `pkg:npm/lodash@4.14.1`\nAllow all license data found in a version range of a package: `pkg:npm/lodash?version_glob=15.*`\nAllow all license data in the test directory of a given package for certain version ranges: `pkg:npm/lodash@15.*.*?file_name=lodash/test/*`\nAllow all license data taken from the package registry for a package and version range: `pkg:npm/lodash?version_glob=*&license_provenance=registry_metadata`\n\n## Available options\n\n`toplevelOnly`: only apply the license policy to \"top level\" license data in a package, which includes registry metadata, LICENSE files, and manifest files which are closest to the root of the package.\n\n`applyToUnidentified`: Apply license policy to found but unidentified license data. If enabled, the license policy will be applied to license data which could not be affirmatively identified as a known license (this will effectively merge the license policy violation and unidentified license alerts). If disabled, license policy alerts will only be shown for license data which is positively identified as something not allowed or set to warn by the license policy.\n\nThis endpoint consumes 100 units of your quota.\n\nThis endpoint requires the following org token scopes:\n      - packages:list\n- license-policy:read",
        "responses": {
          "200": {
            "content": {
              "application/x-ndjson": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "description": "",
                    "properties": {
                      "filepathOrProvenance": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "description": ""
                      },
                      "level": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "purl": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "spdxAtomOrExtraData": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "violationExplanation": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      }
                    },
                    "required": [
                      "filepathOrProvenance",
                      "level",
                      "purl",
                      "spdxAtomOrExtraData",
                      "violationExplanation"
                    ]
                  },
                  "description": ""
                }
              }
            },
            "description": "Data about license policy violations, if any exist"
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