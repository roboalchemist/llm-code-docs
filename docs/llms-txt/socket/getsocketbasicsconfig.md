# Source: https://docs.socket.dev/reference/getsocketbasicsconfig.md

# Get Socket Basics configuration, including toggles for the various tools it supports.

Socket Basics is a CI/CD security scanning suite that runs on your source code, designed to complement Socket SCA and provide full coverage.

- **SAST** - Find issues and risks with your code via static analysis using best in class Open Source tools
- **Secret Scanning** - Detected potentially leaked secrets and credentials within your code
- **Container Security** - Docker image and Dockerfile vulnerability scanning

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- socket-basics:read

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
      "name": "org-settings"
    }
  ],
  "components": {
    "responses": {
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
    "/orgs/{org_slug}/settings/socket-basics": {
      "get": {
        "tags": [
          "org-settings"
        ],
        "summary": "Get Socket Basics configuration, including toggles for the various tools it supports.",
        "operationId": "getSocketBasicsConfig",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "socket-basics:read"
            ]
          },
          {
            "basicAuth": [
              "socket-basics:read"
            ]
          }
        ],
        "description": "Socket Basics is a CI/CD security scanning suite that runs on your source code, designed to complement Socket SCA and provide full coverage.\n\n- **SAST** - Find issues and risks with your code via static analysis using best in class Open Source tools\n- **Secret Scanning** - Detected potentially leaked secrets and credentials within your code\n- **Container Security** - Docker image and Dockerfile vulnerability scanning\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- socket-basics:read",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "consoleTabularEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable tabular console output"
                    },
                    "consoleJsonEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable JSON console output"
                    },
                    "verbose": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable verbose logging"
                    },
                    "allLanguagesEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable all language SAST scanning"
                    },
                    "pythonSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Python SAST scanning"
                    },
                    "javascriptSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run JavaScript SAST scanning"
                    },
                    "goSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Go SAST scanning"
                    },
                    "golangSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Golang SAST scanning"
                    },
                    "javaSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Java SAST scanning"
                    },
                    "phpSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run PHP SAST scanning"
                    },
                    "rubySastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Ruby SAST scanning"
                    },
                    "csharpSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run C# SAST scanning"
                    },
                    "dotnetSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run .NET SAST scanning"
                    },
                    "cSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run C SAST scanning"
                    },
                    "cppSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run C++ SAST scanning"
                    },
                    "kotlinSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Kotlin SAST scanning"
                    },
                    "scalaSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Scala SAST scanning"
                    },
                    "swiftSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Swift SAST scanning"
                    },
                    "rustSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Rust SAST scanning"
                    },
                    "elixirSastEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Run Elixir SAST scanning"
                    },
                    "allRulesEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable all SAST rules"
                    },
                    "pythonEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Python SAST rules",
                      "default": ""
                    },
                    "pythonDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Python SAST rules",
                      "default": ""
                    },
                    "javascriptEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled JavaScript SAST rules",
                      "default": ""
                    },
                    "javascriptDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled JavaScript SAST rules",
                      "default": ""
                    },
                    "goEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Go SAST rules",
                      "default": ""
                    },
                    "goDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Go SAST rules",
                      "default": ""
                    },
                    "javaEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Java SAST rules",
                      "default": ""
                    },
                    "javaDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Java SAST rules",
                      "default": ""
                    },
                    "kotlinEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Kotlin SAST rules",
                      "default": ""
                    },
                    "kotlinDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Kotlin SAST rules",
                      "default": ""
                    },
                    "scalaEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Scala SAST rules",
                      "default": ""
                    },
                    "scalaDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Scala SAST rules",
                      "default": ""
                    },
                    "phpEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled PHP SAST rules",
                      "default": ""
                    },
                    "phpDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled PHP SAST rules",
                      "default": ""
                    },
                    "rubyEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Ruby SAST rules",
                      "default": ""
                    },
                    "rubyDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Ruby SAST rules",
                      "default": ""
                    },
                    "csharpEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled C# SAST rules",
                      "default": ""
                    },
                    "csharpDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled C# SAST rules",
                      "default": ""
                    },
                    "dotnetEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled .NET SAST rules",
                      "default": ""
                    },
                    "dotnetDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled .NET SAST rules",
                      "default": ""
                    },
                    "cEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled C SAST rules",
                      "default": ""
                    },
                    "cDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled C SAST rules",
                      "default": ""
                    },
                    "cppEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled C++ SAST rules",
                      "default": ""
                    },
                    "cppDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled C++ SAST rules",
                      "default": ""
                    },
                    "swiftEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Swift SAST rules",
                      "default": ""
                    },
                    "swiftDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Swift SAST rules",
                      "default": ""
                    },
                    "rustEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Rust SAST rules",
                      "default": ""
                    },
                    "rustDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Rust SAST rules",
                      "default": ""
                    },
                    "elixirEnabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of enabled Elixir SAST rules",
                      "default": ""
                    },
                    "elixirDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Elixir SAST rules",
                      "default": ""
                    },
                    "openGrepNotificationMethod": {
                      "type": "string",
                      "description": "Notification method for OpenGrep",
                      "default": ""
                    },
                    "socketTier1Enabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable Socket Tier 1 reachability analysis"
                    },
                    "socketAdditionalParams": {
                      "type": "string",
                      "description": "Additional parameters for Socket SCA",
                      "default": ""
                    },
                    "secretScanningEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable secret scanning"
                    },
                    "trufflehogExcludeDir": {
                      "type": "string",
                      "description": "Directories to exclude from Trufflehog scanning",
                      "default": ""
                    },
                    "trufflehogShowUnverified": {
                      "type": "boolean",
                      "default": false,
                      "description": "Show unverified secrets in Trufflehog results"
                    },
                    "trufflehogNotificationMethod": {
                      "type": "string",
                      "description": "Notification method for Trufflehog",
                      "default": ""
                    },
                    "containerImagesToScan": {
                      "type": "string",
                      "description": "Comma-separated list of container images to scan",
                      "default": ""
                    },
                    "dockerfiles": {
                      "type": "string",
                      "description": "Comma-separated list of Dockerfiles to scan",
                      "default": ""
                    },
                    "trivyImageEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable Trivy image scanning"
                    },
                    "trivyDockerfileEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable Trivy Dockerfile scanning"
                    },
                    "trivyNotificationMethod": {
                      "type": "string",
                      "description": "Notification method for Trivy",
                      "default": ""
                    },
                    "trivyDisabledRules": {
                      "type": "string",
                      "description": "Comma-separated list of disabled Trivy rules",
                      "default": ""
                    },
                    "trivyImageScanningDisabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Disable Trivy image scanning"
                    },
                    "slackWebhookUrl": {
                      "type": "string",
                      "description": "Slack webhook URL for notifications",
                      "default": ""
                    },
                    "webhookUrl": {
                      "type": "string",
                      "description": "Generic webhook URL for notifications",
                      "default": ""
                    },
                    "msSentinelWorkspaceId": {
                      "type": "string",
                      "description": "Microsoft Sentinel workspace ID",
                      "default": ""
                    },
                    "msSentinelKey": {
                      "type": "string",
                      "description": "Microsoft Sentinel key",
                      "default": ""
                    },
                    "sumologicEndpoint": {
                      "type": "string",
                      "description": "Sumo Logic endpoint URL",
                      "default": ""
                    },
                    "jiraUrl": {
                      "type": "string",
                      "description": "Jira server URL",
                      "default": ""
                    },
                    "jiraProject": {
                      "type": "string",
                      "description": "Jira project key",
                      "default": ""
                    },
                    "jiraEmail": {
                      "type": "string",
                      "description": "Jira user email",
                      "default": ""
                    },
                    "jiraApiToken": {
                      "type": "string",
                      "description": "Jira API token",
                      "default": ""
                    },
                    "githubToken": {
                      "type": "string",
                      "description": "GitHub API token",
                      "default": ""
                    },
                    "githubApiUrl": {
                      "type": "string",
                      "description": "GitHub API URL",
                      "default": ""
                    },
                    "msteamsWebhookUrl": {
                      "type": "string",
                      "description": "Microsoft Teams webhook URL",
                      "default": ""
                    },
                    "s3Enabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable S3 upload for scan results"
                    },
                    "s3Bucket": {
                      "type": "string",
                      "description": "S3 bucket name",
                      "default": ""
                    },
                    "s3AccessKey": {
                      "type": "string",
                      "description": "S3 access key",
                      "default": ""
                    },
                    "s3SecretKey": {
                      "type": "string",
                      "description": "S3 secret key",
                      "default": ""
                    },
                    "s3Endpoint": {
                      "type": "string",
                      "description": "S3 endpoint URL",
                      "default": ""
                    },
                    "s3Region": {
                      "type": "string",
                      "description": "S3 region",
                      "default": ""
                    },
                    "externalCveScanningEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable external CVE scanning"
                    },
                    "socketScanningEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable Socket dependency scanning (legacy)"
                    },
                    "socketScaEnabled": {
                      "type": "boolean",
                      "default": false,
                      "description": "Enable Socket SCA scanning (legacy)"
                    },
                    "additionalParameters": {
                      "type": "string",
                      "description": "Additional configuration parameters (legacy)",
                      "default": ""
                    }
                  },
                  "description": ""
                }
              }
            },
            "description": "Socket Basics settings"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
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