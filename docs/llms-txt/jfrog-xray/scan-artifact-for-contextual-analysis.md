# Source: https://docs.jfrog.com/security/reference/scan-artifact-for-contextual-analysis.md

# Scan Artifact for Contextual Analysis

Triggers a contextual analysis (applicability) scan. This endpoint supports two modes of operation:

**Artifact mode** - scan a specific artifact by providing `repo` and `path` (and optionally `componentId`). The artifact must already be scanned by Xray SCA.

**Aggregate mode** - scan all artifacts in a build or release bundle by providing the corresponding key pair instead:
- For builds: `build_name` + `build_number`
- For Release Bundles V1: `release_bundle_name` + `release_bundle_version`
- For Release Bundles V2: `release_bundle_v2_name` + `release_bundle_v2_version`

The two modes are mutually exclusive. If `repo`, `path`, or `componentId` is provided, the request is treated as artifact mode and aggregate keys are ignored. If none of those are set, the request is treated as aggregate mode.

Optionally, `project` can be provided to scope the request to a specific project.

Requires the MANAGE_DATA permission. Since Xray 3.73.


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v1/artifact/contextualAnalysis/scan": {
      "post": {
        "operationId": "scan-artifact-for-contextual-analysis",
        "summary": "Scan Artifact for Contextual Analysis",
        "description": "Triggers a contextual analysis (applicability) scan. This endpoint supports two modes of operation:\n\n**Artifact mode** - scan a specific artifact by providing `repo` and `path` (and optionally `componentId`). The artifact must already be scanned by Xray SCA.\n\n**Aggregate mode** - scan all artifacts in a build or release bundle by providing the corresponding key pair instead:\n- For builds: `build_name` + `build_number`\n- For Release Bundles V1: `release_bundle_name` + `release_bundle_version`\n- For Release Bundles V2: `release_bundle_v2_name` + `release_bundle_v2_version`\n\nThe two modes are mutually exclusive. If `repo`, `path`, or `componentId` is provided, the request is treated as artifact mode and aggregate keys are ignored. If none of those are set, the request is treated as aggregate mode.\n\nOptionally, `project` can be provided to scope the request to a specific project.\n\nRequires the MANAGE_DATA permission. Since Xray 3.73.\n",
        "tags": [
          "Contextual Analysis V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "repo": {
                    "type": "string",
                    "description": "Artifact mode: repository name containing the artifact."
                  },
                  "path": {
                    "type": "string",
                    "description": "Artifact mode: path to the artifact in the repository."
                  },
                  "componentId": {
                    "type": "string",
                    "description": "Artifact mode: component identifier (e.g. gav://log4j:log4j:1.2.17)."
                  },
                  "project": {
                    "type": "string",
                    "description": "Project key to scope the request (optional, both modes)."
                  },
                  "build_name": {
                    "type": "string",
                    "description": "Aggregate mode: build name."
                  },
                  "build_number": {
                    "type": "string",
                    "description": "Aggregate mode: build number."
                  },
                  "release_bundle_name": {
                    "type": "string",
                    "description": "Aggregate mode: Release Bundle V1 name."
                  },
                  "release_bundle_version": {
                    "type": "string",
                    "description": "Aggregate mode: Release Bundle V1 version."
                  },
                  "release_bundle_v2_name": {
                    "type": "string",
                    "description": "Aggregate mode: Release Bundle V2 name."
                  },
                  "release_bundle_v2_version": {
                    "type": "string",
                    "description": "Aggregate mode: Release Bundle V2 version."
                  }
                }
              },
              "examples": {
                "artifactMode": {
                  "summary": "Scan a specific artifact",
                  "value": {
                    "repo": "my-docker-local",
                    "path": "my-image/latest/manifest.json"
                  }
                },
                "buildMode": {
                  "summary": "Scan all artifacts in a build",
                  "value": {
                    "build_name": "my-build",
                    "build_number": "42",
                    "project": "my-project"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Scan triggered successfully or already in progress.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string",
                      "description": "Status message."
                    }
                  }
                },
                "example": {
                  "info": "Scan triggered successfully"
                }
              }
            }
          },
          "400": {
            "description": "Bad request - invalid or missing parameters.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Permission denied - requires MANAGE_DATA permission.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "Internal server error.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    }
  },
  "tags": [
    {
      "name": "Contextual Analysis V1",
      "description": "APIs from Contextual Analysis V1"
    }
  ]
}
```