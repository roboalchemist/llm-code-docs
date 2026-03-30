# Source: https://virustotal.readme.io/reference/get-private-file-behaviour-id.md

# Get a behaviour report from a private file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Fetches a [Private File Behaviour](https://virustotal.readme.io/reference/private-file-behaviours) object by ID. It expects the sandbox ID returned by the [GET /private/files/{id}/behaviours](https://virustotal.readme.io/reference/get-all-behaviour-reports-from-a-private-file) endpoint.

```json Example response
{
    "data": {
        "attributes": {
            "behash": "3f4a02b305dde56c7c606849289bb194",
            "calls_highlighted": [
                "GetTickCount"
            ],
            "files_opened": [
                "C:\\Windows\\system32\\ws2_32.dll",
                "C:\\Windows\\system32\\UxTheme.dll",
                "C:\\Windows\\system32\\ole32.dll",
                "C:\\Users\\<USER>\\Downloads\\putty.hlp",
                "C:\\Users\\<USER>\\Downloads\\putty.cnt",
                "C:\\Users\\<USER>\\Downloads\\putty.chm",
                "C:\\Windows\\system32\\user32.dll",
                "C:\\Windows\\system32\\advapi32.dll",
                "C:\\Windows\\system32\\ntmarta.dll",
                "C:\\Windows\\WinSxS\\x86_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.18837_none_41e855142bd5705d",
                "C:\\Windows\\Fonts\\staticcache.dat"
            ],
            "has_html_report": true,
            "has_pcap": true,
            "modules_loaded": [
                "UxTheme.dll",
                "IMM32.dll",
                "SspiCli.dll",
                "ADVAPI32.dll"
            ],
            "processes_tree": [
                {
                    "name": "9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91.exe",
                    "process_id": "2340"
                }
            ],
            "registry_keys_opened": [
                "HKCU\\Software\\SimonTatham\\PuTTY\\Sessions",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink\\SystemLink",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\Disable",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\DataStore_V1.0\\DataFilePath",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback",
                "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\LanguagePack\\SurrogateFallback\\MS Shell Dlg"
            ],
            "sandbox_name": "VirusTotal Jujubox",
            "tags": [
                "DIRECT_CPU_CLOCK_ACCESS",
                "RUNTIME_MODULES"
            ],
            "text_highlighted": [
                "PuTTY Configuration",
                "&Open",
                "Cate&gory:",
                "C:\\Windows\\system32\\cmd.exe"
            ]
        },
        "id": "9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91_VirusTotal Jujubox-1658933614",
        "links": {
            "self": "https://www.virustotal.com/api/v3/private/file_behaviours/9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91_VirusTotal Jujubox-1658933614"
        },
        "type": "private_file_behaviour"
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
    "/file_behaviours/{sandbox_id}": {
      "get": {
        "summary": "Get a behaviour report from a private file",
        "description": "",
        "operationId": "get-private-file-behaviour-id",
        "parameters": [
          {
            "name": "sandbox_id",
            "in": "path",
            "description": "Sandbox report ID.",
            "schema": {
              "type": "string"
            },
            "required": true
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