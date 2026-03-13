# Source: https://virustotal.readme.io/reference/rescan-a-private-file.md

# Rescan a private file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Reanalyses a private file. The same params from [/files](https://virustotal.readme.io/reference/upload-file-private-scanning) (other than the file) are accepted. Returns a [private analysis](https://virustotal.readme.io/reference/private-analyses).

```json Example
{
	"data": {
		"type": "private_analysis",
		"id": "ZmI5Y2VmNGJmZDIwZTkzNmQ5MzY0NTcwMGI2Nzc2M2Q6Tm9uZToxNjYwODI1NDE1"
	}
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-private-scanning",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/files/{sha256}/analyse": {
      "post": {
        "summary": "Rescan a private file",
        "description": "",
        "operationId": "rescan-a-private-file",
        "parameters": [
          {
            "name": "sha256",
            "in": "path",
            "description": "File's SHA256 hash",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "disable_sandbox",
            "in": "query",
            "description": "If true, then the file won't be detonated in sandbox environments. False by default.",
            "schema": {
              "type": "string",
              "default": "false"
            }
          },
          {
            "name": "enable_internet",
            "in": "query",
            "description": "If the file should have internet access when running in sandboxes. False by default.",
            "schema": {
              "type": "string",
              "default": "false"
            }
          },
          {
            "name": "intercept_tls",
            "in": "query",
            "description": "Intercept HTTPS/TLS/SSL communication. Intercept HTTPS to view encypted URLS, hostnames and HTTP headers. This is detectable by any sample that checks certificates, and makes JA3 hashes unusable.",
            "schema": {
              "type": "string",
              "default": "false"
            }
          },
          {
            "name": "command_line",
            "in": "query",
            "description": "Command line arguments to use when running the file in sandboxes.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "interaction_sandbox",
            "in": "query",
            "description": "Select the sandbox desired for interactive use.",
            "schema": {
              "type": "string",
              "default": "cape"
            }
          },
          {
            "name": "interaction_timeout",
            "in": "query",
            "description": "interaction timeout in seconds, minimum value: 60. (1 minute.) Max value: 1800: (30 minutes)",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 60
            }
          },
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