# Source: https://docs.socket.dev/reference/getscorebynpmpackage.md

# Get score by package

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/batchpackagefetch) instead.

Get all the scores and metrics by category that are used to evaluate the package version.

- depscore: The average of all score factors. (0-1)
- supplyChainRisk: Score factors relating to supply chain security (0-1)
- downloadCount: The number of downloads for the package. Higher downloads contribute to a higher score.
- supplyChainRiskIssueLow/Mid/High/Critical: The number of supply chain risk issues of varying severity. Lower numbers contribute to a higher score.
- dependencyCount: The number of production dependencies. Lower count contributes to a higher score.
- devDependencyCount: The number of development dependencies. Lower count contributes to a higher score.
- transitiveDependencyCount: The number of transitive dependencies. Lower count contributes to a higher score.
- totalDependencyCount: The total number of dependencies (production + development + transitive). Lower count contributes to a higher score.
- quality: Score factors relating to code quality (0-1)
- qualityIssueLow/Mid/High/Critical: The number of code quality issues of varying severity. Lower numbers contribute to a higher score.
- linesOfCode: The number of lines of code in the package. Lower count contributes to a higher score.
- readmeLength: The length of the package's README file. Longer READMEs contribute to a higher score.
- maintenance: Score factors relating to package maintenance (0-1)
- maintainerCount: The number of maintainers for the package. More maintainers contribute to a higher score.
- versionsLastWeek/Month/TwoMonths/Year: The number of versions released in different time periods. More recent releases contribute to a higher score.
- versionCount: The total number of versions released. Higher count contributes to a higher score.
- maintenanceIssueLow/Mid/High/Critical: The number of maintenance issues of varying severity. Lower numbers contribute to a higher score.
- vulnerability: Score factors relating to package vulnerabilities (0-1)
- vulnerabilityIssueLow/Mid/High/Critical: The number of vulnerability issues of varying severity. Lower numbers contribute to a higher score.
- dependencyVulnerabilityCount: The number of vulnerabilities in the package's dependencies. Lower count contributes to a higher score.
- vulnerabilityCount: The number of vulnerabilities in the package itself. Lower count contributes to a higher score.
- license: Score factors relating to package licensing (0-1)
- licenseIssueLow/Mid/High/Critical: The number of license issues of varying severity. Lower numbers contribute to a higher score.
- licenseQuality: A score indicating the quality/permissiveness of the package's license. Higher quality contributes to a higher score.
- miscellaneous: Miscellaneous metadata about the package version.
- versionAuthorName/Email: The name and email of the version author.
- fileCount: The number of files in the package.
- byteCount: The total size in bytes of the package.
- typeModule: Whether the package declares a "type": "module" field.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- No Scopes Required, but authentication is required

# OpenAPI definition

```json
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
      }
    },
    "schemas": {
      "SocketPackageScore": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "supplyChainRisk": {
            "$ref": "#/components/schemas/SocketMetricSchema"
          },
          "quality": {
            "$ref": "#/components/schemas/SocketMetricSchema"
          },
          "maintenance": {
            "$ref": "#/components/schemas/SocketMetricSchema"
          },
          "vulnerability": {
            "$ref": "#/components/schemas/SocketMetricSchema"
          },
          "license": {
            "$ref": "#/components/schemas/SocketMetricSchema"
          },
          "miscellaneous": {
            "$ref": "#/components/schemas/SocketMetricSchema"
          },
          "depscore": {
            "type": "number",
            "description": "",
            "default": 0
          }
        },
        "required": [
          "depscore",
          "license",
          "maintenance",
          "miscellaneous",
          "quality",
          "supplyChainRisk",
          "vulnerability"
        ]
      },
      "SocketMetricSchema": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "score": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "components": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/SocketMetricComponent"
            },
            "properties": {},
            "description": ""
          },
          "limit": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "limitingMetric": {
            "type": "string",
            "description": "",
            "default": ""
          }
        },
        "required": [
          "components",
          "score"
        ]
      },
      "SocketMetricComponent": {
        "type": "object",
        "additionalProperties": false,
        "description": "",
        "properties": {
          "score": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "maxScore": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "limit": {
            "type": "number",
            "description": "",
            "default": 0
          },
          "value": {
            "type": "object",
            "description": "",
            "default": null
          }
        },
        "required": [
          "limit",
          "maxScore",
          "score",
          "value"
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
    "/npm/{package}/{version}/score": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "Get score by package",
        "deprecated": true,
        "operationId": "getScoreByNPMPackage",
        "parameters": [
          {
            "name": "package",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "version",
            "in": "path",
            "required": true,
            "description": "",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": []
          },
          {
            "basicAuth": []
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/batchpackagefetch) instead.\n\nGet all the scores and metrics by category that are used to evaluate the package version.\n\n- depscore: The average of all score factors. (0-1)\n- supplyChainRisk: Score factors relating to supply chain security (0-1)\n- downloadCount: The number of downloads for the package. Higher downloads contribute to a higher score.\n- supplyChainRiskIssueLow/Mid/High/Critical: The number of supply chain risk issues of varying severity. Lower numbers contribute to a higher score.\n- dependencyCount: The number of production dependencies. Lower count contributes to a higher score.\n- devDependencyCount: The number of development dependencies. Lower count contributes to a higher score.\n- transitiveDependencyCount: The number of transitive dependencies. Lower count contributes to a higher score.\n- totalDependencyCount: The total number of dependencies (production + development + transitive). Lower count contributes to a higher score.\n- quality: Score factors relating to code quality (0-1)\n- qualityIssueLow/Mid/High/Critical: The number of code quality issues of varying severity. Lower numbers contribute to a higher score.\n- linesOfCode: The number of lines of code in the package. Lower count contributes to a higher score.\n- readmeLength: The length of the package's README file. Longer READMEs contribute to a higher score.\n- maintenance: Score factors relating to package maintenance (0-1)\n- maintainerCount: The number of maintainers for the package. More maintainers contribute to a higher score.\n- versionsLastWeek/Month/TwoMonths/Year: The number of versions released in different time periods. More recent releases contribute to a higher score.\n- versionCount: The total number of versions released. Higher count contributes to a higher score.\n- maintenanceIssueLow/Mid/High/Critical: The number of maintenance issues of varying severity. Lower numbers contribute to a higher score.\n- vulnerability: Score factors relating to package vulnerabilities (0-1)\n- vulnerabilityIssueLow/Mid/High/Critical: The number of vulnerability issues of varying severity. Lower numbers contribute to a higher score.\n- dependencyVulnerabilityCount: The number of vulnerabilities in the package's dependencies. Lower count contributes to a higher score.\n- vulnerabilityCount: The number of vulnerabilities in the package itself. Lower count contributes to a higher score.\n- license: Score factors relating to package licensing (0-1)\n- licenseIssueLow/Mid/High/Critical: The number of license issues of varying severity. Lower numbers contribute to a higher score.\n- licenseQuality: A score indicating the quality/permissiveness of the package's license. Higher quality contributes to a higher score.\n- miscellaneous: Miscellaneous metadata about the package version.\n- versionAuthorName/Email: The name and email of the version author.\n- fileCount: The number of files in the package.\n- byteCount: The total size in bytes of the package.\n- typeModule: Whether the package declares a \"type\": \"module\" field.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- No Scopes Required, but authentication is required",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SocketPackageScore"
                }
              }
            },
            "description": "Socket package scores"
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
```