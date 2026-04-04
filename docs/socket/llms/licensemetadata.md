# Source: https://docs.socket.dev/reference/licensemetadata.md

# License Metadata

For an array of license identifiers or names (short form SPDX identifiers, or long form license names),
    returns an array of metadata for the corresponding license, if the license is recognized. If the query
    parameter `includetext=true` is set, the returned metadata will also include the license text.


    ## Example request body:

    ```json
    [
      "Apache-2.0",
      "BSD Zero Clause License"
    ]
    ```


    ## Return value

    ```json
    // Response schema:
    Array<{
      licenseId: string,
      name?: string,
      deprecated?: string,
      crossref?: string
      classes: Array<string>
      text?: string
    }>

    // Example response:
    [
      {
        "licenseId": "Apache-2.0",
        "name": "Apache License 2.0",
        "deprecated": false,
        "crossref": "https://spdx.org/licenses/Apache-2.0.html",
        "classes": [
          "fsf libre",
          "osi approved",
          "permissive (silver)"
        ]
      },
      {
        "licenseId": "0BSD",
        "name": "BSD Zero Clause License",
        "deprecated": false,
        "crossref": "https://spdx.org/licenses/0BSD.html",
        "classes": [
          "osi approved",
          "permissive (bronze)"
        ]
      }
    ]
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

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:

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
    },
    {
      "name": "metadata"
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
      }
    },
    "schemas": {
      "SLicenseMetaRes": {
        "type": "object",
        "description": "",
        "default": null
      },
      "SLicenseMetaReq": {
        "type": "object",
        "description": "",
        "default": null
      }
    }
  },
  "paths": {
    "/license-metadata": {
      "post": {
        "tags": [
          "metadata",
          "license-policy"
        ],
        "summary": "License Metadata",
        "operationId": "licenseMetadata",
        "parameters": [
          {
            "name": "includetext",
            "in": "query",
            "required": false,
            "description": "If `true`, the response will include the full text of the requested licenses",
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
                "$ref": "#/components/schemas/SLicenseMetaReq"
              }
            }
          },
          "required": false
        },
        "security": [],
        "description": "For an array of license identifiers or names (short form SPDX identifiers, or long form license names),\n    returns an array of metadata for the corresponding license, if the license is recognized. If the query\n    parameter `includetext=true` is set, the returned metadata will also include the license text.\n\n\n    ## Example request body:\n\n    ```json\n    [\n      \"Apache-2.0\",\n      \"BSD Zero Clause License\"\n    ]\n    ```\n\n\n    ## Return value\n\n    ```json\n    // Response schema:\n    Array<{\n      licenseId: string,\n      name?: string,\n      deprecated?: string,\n      crossref?: string\n      classes: Array<string>\n      text?: string\n    }>\n\n    // Example response:\n    [\n      {\n        \"licenseId\": \"Apache-2.0\",\n        \"name\": \"Apache License 2.0\",\n        \"deprecated\": false,\n        \"crossref\": \"https://spdx.org/licenses/Apache-2.0.html\",\n        \"classes\": [\n          \"fsf libre\",\n          \"osi approved\",\n          \"permissive (silver)\"\n        ]\n      },\n      {\n        \"licenseId\": \"0BSD\",\n        \"name\": \"BSD Zero Clause License\",\n        \"deprecated\": false,\n        \"crossref\": \"https://spdx.org/licenses/0BSD.html\",\n        \"classes\": [\n          \"osi approved\",\n          \"permissive (bronze)\"\n        ]\n      }\n    ]\n    ```\n\n    ## License policy schema\n\n```json\n{\n  allow?: Array<string>\n  warn?: Array<string>\n  options?: Array<string>\n}\n```\n\nElements of the `allow` and `warn` arrays strings representing items which should be allowed, or which should trigger a warning; license data found in package which not present in either array will produce a license violation (effectively a \"hard\" error). For example, to allow Apache-2.0 and MIT to the allow list, simply add the strings \"Apache-2.0\" and \"MIT\" to the `allow` array. Strings appearing in these arrays are generally \"what you see is what you get\", with two important exceptions: strings which are recognized as license classes and strings which are recognized as PURLs are handled differently to allow for more flexible license policy creation.\n\n## License Classes\n\nStrings which are license classes will expand to a list of licenses known to be in that particular license class. Recognized license classes are:\n  'permissive',\n  'permissive (model)',\n  'permissive (gold)',\n  'permissive (silver)',\n  'permissive (bronze)',\n  'permissive (lead)',\n  'copyleft',\n  'maximal copyleft',\n  'network copyleft',\n  'strong copyleft',\n  'weak copyleft',\n  'contributor license agreement',\n  'public domain',\n  'proprietary free',\n  'source available',\n  'proprietary',\n  'commercial',\n  'patent'\n\nUsers can learn more about [copyleft tiers](https://blueoakcouncil.org/copyleft) and [permissive tiers](https://blueoakcouncil.org/list) by reading the linked resources.\n\n\n## PURLs\n\nUsers may also modify their license policy's allow and warn lists by using [package URLs](https://github.com/package-url/purl-spec) (aka PURLs), which support glob patterns to allow a range of versions, files and directories, etc.\n\npurl qualifiers which support globs are `filename`, `version_glob`, `artifact_id` and `license_provenance` (primarily used for allowing data from registry metadata).\n\n### Examples:\nAllow all license data found in a specific version of a package 4.14.1: `pkg:npm/lodash@4.14.1`\nAllow all license data found in a version range of a package: `pkg:npm/lodash?version_glob=15.*`\nAllow all license data in the test directory of a given package for certain version ranges: `pkg:npm/lodash@15.*.*?file_name=lodash/test/*`\nAllow all license data taken from the package registry for a package and version range: `pkg:npm/lodash?version_glob=*&license_provenance=registry_metadata`\n\n## Available options\n\n`toplevelOnly`: only apply the license policy to \"top level\" license data in a package, which includes registry metadata, LICENSE files, and manifest files which are closest to the root of the package.\n\n`applyToUnidentified`: Apply license policy to found but unidentified license data. If enabled, the license policy will be applied to license data which could not be affirmatively identified as a known license (this will effectively merge the license policy violation and unidentified license alerts). If disabled, license policy alerts will only be shown for license data which is positively identified as something not allowed or set to warn by the license policy.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SLicenseMetaRes"
                }
              }
            },
            "description": "Metadata for the requested licenses"
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
          }
        },
        "x-readme": {}
      }
    }
  }
}
````