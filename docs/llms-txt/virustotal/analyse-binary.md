# Source: https://virustotal.readme.io/reference/analyse-binary.md

# Analyse code blocks with Code Insights

> 🚧
>
> This API endpoint is limited to 50 requests per day. Please use it with caution!

To analyze disassembled or decompiled code, use this endpoint. It requires the input code Base64-encoded and returns a Base64-encoded description of the functionality, focusing on aspects relevant to malware analysis.

```json Example request
"data": {
    "code": "<_string_> Code block in Base64",
    "code_type": "<_string_> Whether the code is `disassembled` or `decompiled`"
}
```

This endpoint can be used as well to query code blocks, chaining previous analyses with modifications or corrections made by the analyst as follows:

```json Example request
"data": {
    "code": "<_string_> Code block in Base64",
    "code_type": "<_string_> Whether the code is `disassembled` or `decompiled`"
    "history": [
        {
            "request": "<_string_> Same or related code block in Base64",
            "response": {
                "summary":"<_string_> The summary explanation provided by Code Insights in a previous analysis of the same or related code block, which is used as context for the new analysis",
                "description":"<_string_> Remarks made by the human analyst related to this previous analysis",
            },
        },
        {
            "request": "<_string_> Same or related code block in Base64",
            "response": {
                "summary": "<_string_> The summary explanation provided by Code Insights in a previous analysis of the same or related code block, which is used as context for the new analysis",
                "description": "<_string_> Remarks made by the human analyst related to this previous analysis",
            }
        }
    ]
}
```

# Examples

```python
import requests
import base64

decompiled_code = '''int create_persistence_entry(char *path_to_malware)
{
    HKEY hKey;
    DWORD result;
    result = RegOpenKeyExA(
        HKEY_CURRENT_USER,
        "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
        0,
        KEY_SET_VALUE,
        &hKey
    );

    if (result == ERROR_SUCCESS) {
        result = RegSetValueExA(
            hKey,
            "MalwareEntry",
            0,
            REG_SZ,
            (const BYTE *)path_to_malware,
            (strlen(path_to_malware) + 1) * sizeof(char)
        );
        
        RegCloseKey(hKey);
    }
    return result;
}'''
code_b64 = base64.b64encode(decompiled_code.encode('utf-8')).decode('utf-8')

url = f"https://www.virustotal.com/api/v3/codeinsights/analyse-binary"
payload =  { "data": {
        'code': code_b64,
        'code_type': 'decompiled'
    } 
  }
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
if response.status_code == 200:
  print(base64.b64decode(response.json()["data"]).decode('utf-8'))
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
    "/codeinsights/analyse-binary": {
      "post": {
        "summary": "Analyse code blocks with Code Insights",
        "description": "",
        "operationId": "analyse-binary",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API Key.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "format": "json"
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