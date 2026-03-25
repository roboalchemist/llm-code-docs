# Source: https://virustotal.readme.io/reference/files-scan.md

# Upload a file

Upload and analyse a file
> 📘 File size
If the file to be uploaded is bigger than 32MB, please use the [/files/upload_url](ref:files-upload-url) endpoint instead which admits files up to 650MB.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "version": "v3",
    "title": "VirusTotal API v3 file upload forms"
  },
  "x-readme": {
    "proxy-enabled": false,
    "explorer-enabled": true
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "paths": {
    "/files": {
      "post": {
        "summary": "Upload a file",
        "description": "Upload and analyse a file\n> 📘 File size\nIf the file to be uploaded is bigger than 32MB, please use the [/files/upload_url](https://virustotal.readme.io/reference/files-upload-url) endpoint instead which admits files up to 650MB.",
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
                "properties": {
                  "file": {
                    "type": "string",
                    "format": "binary"
                  },
                  "password": {
                    "type": "string",
                    "description": "Optional, password to decompress and scan a file contained in a protected ZIP file."
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
            "description": "The analysis ID. Use [/analyses/<analysis_ID>](https://virustotal.readme.io/reference/analysis) API call to check the analysis status.",
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