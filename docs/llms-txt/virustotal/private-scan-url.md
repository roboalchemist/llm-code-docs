# Source: https://virustotal.readme.io/reference/private-scan-url.md

# Private Scan URL

This returns an [Analysis](https://virustotal.readme.io/reference/analyses-object) ID. The analysis can be retrieved by using the [Analysis](https://virustotal.readme.io/reference/get-a-private-url-analysis-report) endpoint.

### Analysis observations:

To get a more comprehensive analysis and gather different kinds of information beyond what a typical sandbox provides, you should use `chrome_headless_linux` as an additional or specific type of sandbox environment.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-scan-url-form",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/private/urls": {
      "post": {
        "summary": "Private Scan URL",
        "description": "",
        "operationId": "private-scan-url",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "required": [
                  "url"
                ],
                "properties": {
                  "url": {
                    "type": "string",
                    "description": "URL to scan"
                  },
                  "user_agent": {
                    "type": "string",
                    "description": "User agent string."
                  },
                  "sandboxes": {
                    "type": "string",
                    "description": "Comma separated eg: `chrome_headless_linux,cape_win,zenbox_windows` possible values `chrome_headless_linux`, `cape_win` and `zenbox_windows`."
                  },
                  "retention_period_days": {
                    "type": "integer",
                    "description": "Optional, number of days the report and URL are kept in VT (between 1 and 28). If not set it defaults to the group's retention policy preference (1 day by default).",
                    "format": "int32"
                  },
                  "storage_region": {
                    "type": "string",
                    "description": "Optional, storage region where the URL will be stored. By default uses the group's private_scanning.storage_region preference. Allowed values are US, CA, EU, GB.",
                    "enum": [
                      "US",
                      "CA",
                      "EU",
                      "GB"
                    ]
                  },
                  "interaction_sandbox": {
                    "type": "string",
                    "description": "Select the sandbox desired for interactive use, possible values `cape_win`.",
                    "default": "cape_win"
                  },
                  "interaction_timeout": {
                    "type": "integer",
                    "description": "Interaction timeout in seconds, minimum value: 60. (1 minute.) Max value: 1800: (30 minutes)",
                    "default": 60,
                    "format": "int32"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```