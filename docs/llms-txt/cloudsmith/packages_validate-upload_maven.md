# Source: https://help.cloudsmith.io/reference/packages_validate-upload_maven.md

# Validate parameters for create Maven package

Validate parameters for create Maven package

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
    "/packages/{owner}/{repo}/validate-upload/maven/": {
      "post": {
        "operationId": "packages_validate-upload_maven",
        "summary": "Validate parameters for create Maven package",
        "description": "Validate parameters for create Maven package",
        "requestBody": {
          "$ref": "#/components/requestBodies/MavenPackageUploadRequest"
        },
        "responses": {
          "204": {
            "description": "Validation was successful, parameters are OK."
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
          "404": {
            "description": "Namespace (owner) or repository not found",
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
          "packages"
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
          "name": "repo",
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
    "requestBodies": {
      "MavenPackageUploadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/MavenPackageUploadRequest"
            }
          }
        }
      }
    },
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
      "MavenPackageUploadRequest": {
        "required": [
          "package_file"
        ],
        "type": "object",
        "properties": {
          "artifact_id": {
            "title": "Artifact id",
            "description": "The ID of the artifact.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "extra_files": {
            "description": "Extra files to include in the package. This can be a single file or multiple files.",
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            },
            "nullable": true
          },
          "group_id": {
            "title": "Group id",
            "description": "Artifact's group ID.",
            "type": "string",
            "maxLength": 2083,
            "nullable": true
          },
          "ivy_file": {
            "title": "Ivy file",
            "description": "The ivy file is an XML file describing the dependencies of the project.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "javadoc_file": {
            "title": "Javadoc file",
            "description": "Adds bundled Java documentation to the Maven package",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "package_file": {
            "title": "Package file",
            "description": "The primary file for the package.",
            "type": "string",
            "minLength": 1
          },
          "packaging": {
            "title": "Packaging",
            "description": "Artifact's Maven packaging type.",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "pom_file": {
            "title": "Pom file",
            "description": "The POM file is an XML file containing the Maven coordinates.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "republish": {
            "title": "Republish",
            "description": "If true, the uploaded package will overwrite any others with the same attributes (e.g. same version); otherwise, it will be flagged as a duplicate.",
            "type": "boolean"
          },
          "sbt_version": {
            "title": "Sbt version",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "scala_version": {
            "title": "Scala version",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "sources_file": {
            "title": "Sources file",
            "description": "Adds bundled Java source code to the Maven package.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "tags": {
            "title": "Tags",
            "description": "A comma-separated values list of tags to add to the package.",
            "type": "string",
            "maxLength": 1024,
            "minLength": 1,
            "nullable": true
          },
          "tests_file": {
            "title": "Tests file",
            "description": "Adds bundled Java tests to the Maven package.",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "version": {
            "title": "Version",
            "description": "The raw version for this package.",
            "type": "string",
            "maxLength": 255,
            "nullable": true
          }
        }
      }
    }
  }
}
```