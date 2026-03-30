# Source: https://virustotal.readme.io/reference/upload-file-private-scanning.md

# Upload a file

Privately upload and analyse a file.
> 📘 File size
If the file to be uploaded is bigger than 32MB, please use the [/private/files/upload_url](ref:private-files-upload-url) endpoint instead which admits files up to 650MB.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "version": "v3.0",
    "title": "New category"
  },
  "x-readme": {
    "proxy-enabled": false,
    "explorer-enabled": true
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
    }
  ],
  "paths": {
    "/files": {
      "post": {
        "summary": "Upload a file",
        "description": "Privately upload and analyse a file.\n> 📘 File size\nIf the file to be uploaded is bigger than 32MB, please use the [/private/files/upload_url](https://virustotal.readme.io/reference/private-files-upload-url) endpoint instead which admits files up to 650MB.",
        "parameters": [
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key",
            "required": true,
            "example": "<your API key>"
          }
        ],
        "requestBody": {
          "required": true,
          "description": "File to scan",
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "required": [
                  "file"
                ],
                "properties": {
                  "file": {
                    "type": "string",
                    "format": "binary"
                  },
                  "disable_sandbox": {
                    "description": "If true, then the file won't be detonated in sandbox environments. False by default.",
                    "type": "string",
                    "default": false
                  },
                  "enable_internet": {
                    "description": "If the file should have internet access when running in sandboxes. False by default.",
                    "type": "string",
                    "default": false
                  },
                  "intercept_tls": {
                    "description": "Intercept HTTPS/TLS/SSL communication. Intercept HTTPS to view encypted URLS, hostnames and HTTP headers.  This is detectable by any sample that checks certificates, and makes JA3 hashes unusable.",
                    "type": "string",
                    "default": false
                  },
                  "command_line": {
                    "type": "string",
                    "description": "Command line arguments to use when running the file in sandboxes."
                  },
                  "password": {
                    "type": "string",
                    "description": "Optional, password to decompress and scan a file contained in a protected ZIP file."
                  },
                  "retention_period_days": {
                    "type": "integer",
                    "description": "Optional, number of days the report and file are kept in VT (between 1 and 28). If not set it defaults to the group's retention policy preference (1 day by default)."
                  },
                  "storage_region": {
                    "type": "string",
                    "description": "Optional, storage region where the file will be stored. By default uses the group's private_scanning.storage_region preference. Allowed values are US, EU."
                  },
                  "interaction_sandbox": {
                    "type": "string",
                    "description": "Select the sandbox desired for interactive use."
                  },
                  "interaction_timeout": {
                    "type": "integer",
                    "description": "Interaction timeout in seconds, minimum value: 60. (1 minute.) Max value: 1800: (30 minutes)"
                  },
                  "locale": {
                    "default": "EN_US",
                    "description": "Preferred sandbox locale. On windows this selection will change the language and keyboard settings of the analysis machine.",
                    "type": "string",
                    "enum": [
                      "EN_US",
                      "AR_SA",
                      "DE_DE",
                      "ES_ES",
                      "PT_BR"
                    ]
                  }
                }
              },
              "encoding": {
                "file": {
                  "contentType": "application/octet-stream"
                }
              },
              "example": "/path/to/file"
            }
          }
        },
        "responses": {
          "200": {
            "description": "The analysis ID. Use [/private/analyses/<analysis_ID>](https://virustotal.readme.io/reference/list-private-analyses) API call to check the analysis status.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "description": "object type",
                          "example": "analysis"
                        },
                        "id": {
                          "type": "string",
                          "description": "analysis ID.",
                          "example": "OTFiMDcwMjVjZDIzZTI0NGU4ZDlmMjI2NjkzZDczNGE6MTY1MzY1NDM3Nw=="
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "If password was provided and the file isn't a ZIP, it contains more than one file, the password is incorrect, or the file is corrupt."
          }
        }
      }
    }
  }
}
```