# Source: https://docs.jfrog.com/security/reference/get-artifact-dependency-graph.md

# Get Artifact Dependency Graph

Retrieves the complete dependency graph for a specified artifact. Returns the artifact metadata and a recursive tree of all its component dependencies, including package type and component IDs.

Requires a user with Read permission.


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
    "/api/v1/dependencyGraph/artifact": {
      "post": {
        "operationId": "get-artifact-dependency-graph",
        "summary": "Get Artifact Dependency Graph",
        "description": "Retrieves the complete dependency graph for a specified artifact. Returns the artifact metadata and a recursive tree of all its component dependencies, including package type and component IDs.\n\nRequires a user with Read permission.\n",
        "tags": [
          "Artifacts V1"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ArtifactsArtifactDependencyGraphRequest"
              },
              "example": {
                "path": "default/libs-release-local/org/acme/app/1.0/app-1.0.jar"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ArtifactsArtifactDependencyGraphResponse"
                }
              }
            }
          },
          "400": {
            "description": "Artifact '<PATH&>' doesn't exist or isn't indexed in Xray",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "401": {
            "description": "Bad credentials",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
          },
          "415": {
            "description": "Failed to parse request",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
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
    },
    "schemas": {
      "ArtifactsArtifactDependencyGraphRequest": {
        "type": "object",
        "required": [
          "path"
        ],
        "description": "Artifact locator for dependency graph (see JFrog documentation). Path is the artifact path (/artifactory-name/repo-name/path); default artifactory name is often 'Artifactory'.",
        "properties": {
          "path": {
            "type": "string",
            "description": "Full path of the artifact, e.g. /default/my-repo/myArtifact/3.14",
            "example": "/Artifactory/pnnl/goss/goss-core-client/0.1.7/goss-core-client-0.1.7-sources.jar"
          }
        }
      },
      "ArtifactsDependencyGraphNode": {
        "type": "object",
        "description": "Recursive dependency node (nested components arrays in responses).",
        "properties": {
          "component_name": {
            "type": "string"
          },
          "component_id": {
            "type": "string"
          },
          "package_type": {
            "type": "string"
          },
          "version": {
            "type": "string"
          },
          "created": {
            "type": "string"
          },
          "modified": {
            "type": "string"
          },
          "components": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ArtifactsDependencyGraphNode"
            }
          }
        }
      },
      "ArtifactsArtifactDependencyGraphResponse": {
        "type": "object",
        "properties": {
          "artifact": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "path": {
                "type": "string"
              },
              "pkg_type": {
                "type": "string"
              },
              "sha256": {
                "type": "string"
              },
              "sha1": {
                "type": "string"
              },
              "component_id": {
                "type": "string"
              }
            }
          },
          "components": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ArtifactsDependencyGraphNode"
            }
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "Artifacts V1",
      "description": "APIs from Artifacts V1"
    }
  ]
}
```