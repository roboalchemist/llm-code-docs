# Source: https://virustotal.readme.io/reference/widgeturl.md

# Get a widget rendering URL

This endpoint allows you to generate an ephemeral widget URL valid for three days. Such URL is precisely the URL that you will need to embed in an iframe in order to display the VirusTotal report in your product. Once the URL has expired, it should be refreshed by calling once again this endpoint with the very same observable query parameter, otherwise a bad request error will be returned.

In addition to the widget URL for the pertinent observable, the response includes an object with the last detection ratio for the observable, i.e. how many security vendors flag the item as malicious. This detection ratio can be used as a summary next to the pertinent observable when listing it in your interface, acting as a trigger to then open the full-fledged widget when clicking on it.

[block:callout]
{
  "type": "danger",
  "title": "Detection ratio usage",
  "body": "VT Augment enriches alerts generated via your own logic, it should not power the detections themselves. This is precisely why the multi-antivirus report is not returned as a parseable API object, to limit the potential for abuse and misuse."
}
[/block]

Optionally, you can pass up to four params to control the widget's theme and match your product's style. These theme parameters must be the HTML color expressed in hexadecimal notation. You can find more information about theming [in this section](https://virustotal.readme.io/reference/theme).

```json
{
  "data": {
    "url": "https://virustotal.com/ui/widget/html/OTEzZjdhMDBlYWE1YThiMzg2MDQxYWE2NDQwMTgzYmNhNTc0ODA1ZTRiMWE2OTkzODFlZjAxYmE5MGVmMzVkM3x8ZmlsZXx8eyJiZzEiOiAiIzMxM2Q1YSIsICJiZzIiOiAiIzIyMmM0MiIsICJiZDEiOiAiIzRkNjM4NSIsICJmZzEiOiAiI2ZmZmZmZiJ9fHwxNTcxOTI1MjQzfHxjMzkyOWYzMmY5NGFmZTIxMTUzN2U2NTYwNDgzZjgyYjc4NDY1MDQ2ZmNmMGY3ZTljNjgzMmY0ZWZlMzFlMTFi",
    "detection_ratio": {"detections": 5, "total": 71}
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
    "/widget/url": {
      "get": {
        "summary": "Get a widget rendering URL",
        "description": "",
        "operationId": "widgeturl",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "description": "A file hash (md5, sha1 or sha256), URL, IP address or a Domain",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "fg1",
            "in": "query",
            "description": "Theme primary foreground color in hex notation",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "bg1",
            "in": "query",
            "description": "Theme primary background color in hex notation",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "bg2",
            "in": "query",
            "description": "Theme secondary background color in hex notation",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "bd1",
            "in": "query",
            "description": "Theme border color",
            "schema": {
              "type": "string"
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
          },
          "429": {
            "description": "429",
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
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