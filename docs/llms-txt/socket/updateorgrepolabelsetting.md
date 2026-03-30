# Source: https://docs.socket.dev/reference/updateorgrepolabelsetting.md

# Update repository label setting (beta)

Update the setting (e.g. security/license policy) for a repository label.


Note that repository label settings currently only support `issueRules`
and `issueRulesPolicyDefault`. A policy is considered "active" for
a given repository label if the `issueRulesPolicyDefault` is set,
and inactive when not set. `issueRules` can be used to further
refine the alert triage strategy.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- repo-label:update

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
      "name": "repo-labels"
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
    "/orgs/{org_slug}/repos/labels/{label_id}/label-setting": {
      "put": {
        "tags": [
          "repo-labels"
        ],
        "summary": "Update repository label setting (beta)",
        "operationId": "updateOrgRepoLabelSetting",
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
            "name": "label_id",
            "in": "path",
            "required": true,
            "description": "The ID of the label",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "issueRules": {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                      "gptSecurity": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for gptSecurity issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "gptAnomaly": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for gptAnomaly issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "gptMalware": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for gptMalware issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "filesystemAccess": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for filesystemAccess issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "networkAccess": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for networkAccess issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "shellAccess": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for shellAccess issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "debugAccess": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for debugAccess issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "chromePermission": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for chromePermission issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "chromeHostPermission": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for chromeHostPermission issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "chromeWildcardHostPermission": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for chromeWildcardHostPermission issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "chromeContentScript": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for chromeContentScript issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "criticalCVE": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for criticalCVE issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "cve": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for cve issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "mediumCVE": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for mediumCVE issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "mildCVE": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for mildCVE issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "emptyPackage": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for emptyPackage issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "trivialPackage": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for trivialPackage issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noREADME": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noREADME issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "shrinkwrap": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for shrinkwrap issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "tooManyFiles": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for tooManyFiles issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "generic": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for generic issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaArgToSink": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaArgToSink issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaEnvToSink": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaEnvToSink issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaContextToSink": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaContextToSink issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaArgToOutput": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaArgToOutput issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaArgToEnv": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaArgToEnv issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaContextToOutput": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaContextToOutput issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ghaContextToEnv": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ghaContextToEnv issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "recentlyPublished": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for recentlyPublished issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "licenseSpdxDisj": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for licenseSpdxDisj issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unsafeCopyright": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unsafeCopyright issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "licenseChange": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for licenseChange issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "nonOSILicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for nonOSILicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "deprecatedLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for deprecatedLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "missingLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for missingLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "nonSPDXLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for nonSPDXLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unclearLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unclearLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "mixedLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for mixedLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "notice": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for notice issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "modifiedLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for modifiedLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "modifiedException": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for modifiedException issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "licenseException": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for licenseException issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "deprecatedException": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for deprecatedException issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "miscLicenseIssues": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for miscLicenseIssues issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unidentifiedLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unidentifiedLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noLicenseFound": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noLicenseFound issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "explicitlyUnlicensedItem": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for explicitlyUnlicensedItem issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "copyleftLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for copyleftLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "nonpermissiveLicense": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for nonpermissiveLicense issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "ambiguousClassifier": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for ambiguousClassifier issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "invalidPackageJSON": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for invalidPackageJSON issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "httpDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for httpDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "gitDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for gitDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "gitHubDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for gitHubDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "fileDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for fileDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noTests": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noTests issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noRepository": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noRepository issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "badSemver": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for badSemver issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "badSemverDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for badSemverDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noV1": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noV1 issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noWebsite": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noWebsite issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noBugTracker": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noBugTracker issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "noAuthorData": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for noAuthorData issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "typeModuleCompatibility": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for typeModuleCompatibility issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "floatingDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for floatingDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "manifestConfusion": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for manifestConfusion issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "malware": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for malware issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "telemetry": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for telemetry issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "troll": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for troll issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "deprecated": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for deprecated issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "chronoAnomaly": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for chronoAnomaly issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "compromisedSSHKey": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for compromisedSSHKey issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "semverAnomaly": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for semverAnomaly issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "newAuthor": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for newAuthor issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unstableOwnership": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unstableOwnership issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "missingAuthor": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for missingAuthor issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unmaintained": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unmaintained issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unpublished": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unpublished issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "majorRefactor": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for majorRefactor issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "missingTarball": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for missingTarball issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "suspiciousStarActivity": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for suspiciousStarActivity issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unpopularPackage": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unpopularPackage issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillAutonomyAbuse": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillAutonomyAbuse issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillCommandInjection": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillCommandInjection issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillDataExfiltration": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillDataExfiltration issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillDiscoveryAbuse": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillDiscoveryAbuse issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillHardcodedSecrets": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillHardcodedSecrets issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillObfuscation": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillObfuscation issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillPromptInjection": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillPromptInjection issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillResourceAbuse": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillResourceAbuse issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillSupplyChain": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillSupplyChain issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillToolAbuse": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillToolAbuse issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillToolChaining": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillToolChaining issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "skillTransitiveTrust": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for skillTransitiveTrust issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "socketUpgradeAvailable": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for socketUpgradeAvailable issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "longStrings": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for longStrings issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "highEntropyStrings": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for highEntropyStrings issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "urlStrings": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for urlStrings issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "usesEval": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for usesEval issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "dynamicRequire": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for dynamicRequire issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "envVars": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for envVars issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "missingDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for missingDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unusedDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unusedDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "peerDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for peerDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "uncaughtOptionalDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for uncaughtOptionalDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "unresolvedRequire": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for unresolvedRequire issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "extraneousDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for extraneousDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "obfuscatedRequire": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for obfuscatedRequire issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "obfuscatedFile": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for obfuscatedFile issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "minifiedFile": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for minifiedFile issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "installScripts": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for installScripts issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "hasNativeCode": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for hasNativeCode issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "binScriptConfusion": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for binScriptConfusion issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "shellScriptOverride": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for shellScriptOverride issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "didYouMean": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for didYouMean issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "gptDidYouMean": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for gptDidYouMean issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "bidi": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for bidi issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "zeroWidth": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for zeroWidth issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "badEncoding": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for badEncoding issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "homoglyphs": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for homoglyphs issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "invisibleChars": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for invisibleChars issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "suspiciousString": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for suspiciousString issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "potentialVulnerability": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for potentialVulnerability issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxProposedApiUsage": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxProposedApiUsage issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxActivationWildcard": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxActivationWildcard issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxWorkspaceContainsActivation": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxWorkspaceContainsActivation issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxUntrustedWorkspaceSupported": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxUntrustedWorkspaceSupported issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxVirtualWorkspaceSupported": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxVirtualWorkspaceSupported issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxWebviewContribution": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxWebviewContribution issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxDebuggerContribution": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxDebuggerContribution issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxExtensionDependency": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxExtensionDependency issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      },
                      "vsxExtensionPack": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "action": {
                            "type": "string",
                            "enum": [
                              "defer",
                              "error",
                              "warn",
                              "monitor",
                              "ignore"
                            ],
                            "description": "The action to take for vsxExtensionPack issues."
                          }
                        },
                        "required": [
                          "action"
                        ]
                      }
                    },
                    "description": ""
                  },
                  "issueRulesPolicyDefault": {
                    "type": "string",
                    "enum": [
                      "default",
                      "low",
                      "medium",
                      "high"
                    ],
                    "description": "The default security policy for the repository label",
                    "default": "medium"
                  },
                  "licensePolicy": {
                    "$ref": "#/components/schemas/LicenseAllowListRequest"
                  }
                },
                "description": ""
              }
            }
          },
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "repo-label:update"
            ]
          },
          {
            "basicAuth": [
              "repo-label:update"
            ]
          }
        ],
        "description": "Update the setting (e.g. security/license policy) for a repository label.\n\n\nNote that repository label settings currently only support `issueRules`\nand `issueRulesPolicyDefault`. A policy is considered \"active\" for\na given repository label if the `issueRulesPolicyDefault` is set,\nand inactive when not set. `issueRules` can be used to further\nrefine the alert triage strategy.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- repo-label:update",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "status": {
                      "type": "string",
                      "description": "",
                      "default": "ok"
                    }
                  },
                  "required": [
                    "status"
                  ]
                }
              }
            },
            "description": "Success"
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