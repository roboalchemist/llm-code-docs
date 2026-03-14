# Source: https://virustotal.readme.io/reference/file-all-behaviours-summary.md

# Get a summary of all behavior reports for a file

This endpoint returns a summary with behavioural information about the file. The summary consists in merging together the reports produced by the multiple sandboxes we have integrated in VirusTotal.

This API call returns all fields contained in the [File behaviour](https://virustotal.readme.io/reference/file-behaviour-summary) object, except the ones that make sense only for individual sandboxes:

* `analysis_date`
* `behash`
* `has_html_report`
* `has_pcap`
* `last_modification_date`
* `sandbox_name`

```json
{
    "data": {
        "calls_highlighted": [
            "GetTickCount"
        ],
        "files_opened": [
            "C:\\WINDOWS\\system32\\winime32.dll",
            "C:\\WINDOWS\\system32\\ws2_32.dll",
            "C:\\WINDOWS\\system32\\ws2help.dll",
            "C:\\WINDOWS\\system32\\psapi.dll",
            "C:\\WINDOWS\\system32\\imm32.dll",
            "C:\\WINDOWS\\system32\\lpk.dll",
            "C:\\WINDOWS\\system32\\usp10.dll",
            "C:\\WINDOWS\\WinSxS\\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\\comctl32.dll",
            "C:\\WINDOWS\\system32\\winmm.dll",
            "C:\\WINDOWS\\system32\\winspool.drv",
            "C:\\WINDOWS\\WindowsShell.Manifest",
            "C:\\WINDOWS\\system32\\shell32.dll",
            "C:\\WINDOWS\\system32\\MSCTF.dll"
        ],
        "modules_loaded": [
            "comctl32.dll",
            "C:\\WINDOWS\\system32\\ws2_32.dll",
            "C:\\WINDOWS\\system32\\MSCTF.dll",
            "version.dll",
            "C:\\WINDOWS\\system32\\msctfime.ime",
            "C:\\WINDOWS\\system32\\ole32.dll",
            "USER32.dll",
            "IMM32.dll",
            "C:\\WINDOWS\\system32\\user32.dll"
        ],
        "mutexes_created": [
            "CTF.LBES.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.Compart.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.Asm.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.Layouts.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.TMD.MutexDefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "CTF.TimListCache.FMPDefaultS-1-5-21-1482476501-1645522239-1417001333-500MUTEX.DefaultS-1-5-21-1482476501-1645522239-1417001333-500",
            "MSCTF.Shared.MUTEX.EBH"
        ],
        "mutexes_opened": [
            "ShimCacheMutex"
        ],
        "processes_terminated": [
            "C:\\Documents and Settings\\Administrator\\Local Settings\\Temp\\EB93A6\\996E.exe"
        ],
        "processes_tree": [
            {
                "name": "****.exe",
                "process_id": "1036"
            },
            {
                "name": "9f9e74241d59eccfe7040bfdcbbceacb374eda397cc53a4197b59e4f6f380a91.exe",
                "process_id": "2340"
            }
        ],
        "registry_keys_opened": [
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\996E.exe",
            "\\Registry\\MACHINE\\System\\CurrentControlSet\\Control\\SafeBoot\\Option",
            "\\Registry\\Machine\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers\\TransparentEnabled",
            "\\REGISTRY\\USER\\S-1-5-21-1482476501-1645522239-1417001333-500\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\COMCTL32.dll",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\SHELL32.dll",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\comdlg32.dll",
            "\\Registry\\Machine\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\WINMM.dll",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave1",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave2",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave3",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave4",
            "\\REGISTRY\\MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\wave5"
        ],
        "tags": [
            "DIRECT_CPU_CLOCK_ACCESS",
            "RUNTIME_MODULES"
        ],
        "text_highlighted": [
            "&Open",
            "&Cancel",
            "&About",
            "Cate&gory:",
            "Host &Name (or IP address)",
            "&Port",
            "22",
            "Connection type:",
            "Ra&w",
            "&Telnet",
            "Rlog&in"
        ]
    }
}

```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
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
    "/files/{id}/behaviour_summary": {
      "get": {
        "summary": "Get a summary of all behavior reports for a file",
        "description": "",
        "operationId": "file-all-behaviours-summary",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
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
        "deprecated": false,
        "security": []
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