# Source: https://virustotal.readme.io/reference/widgethtmltoken.md

# Retrieve the widget's HTML content

This endpoint returns the actual HTML content of the widget report for a given observable. It is a URL that will have been previously returned by a call to the [/widget/url](https://virustotal.readme.io/reference/widgeturl) endpoint. It does not require authentication but it is only **valid for three days**. This endpoint will be typically called from your application's front-end/client-side, as a result of embedding it in an iframe.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/74f60de-widget.png",
        "widget.png",
        500,
        866,
        "#3b4560"
      ],
      "caption": "Example HTML response visualized in a browser."
    }
  ]
}
[/block]

You might find the [VT Augment client library](https://github.com/VirusTotal/vt-augment) helpful when building the flow to display the widget in your own product. Its usage is not mandatory, a couple of lines of JavaScript will also do the job.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-augment",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/ui/"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/widget/html/{token}": {
      "get": {
        "summary": "Retrieve the widget's HTML content",
        "description": "",
        "operationId": "widgethtmltoken",
        "parameters": [
          {
            "name": "token",
            "in": "path",
            "description": "This token is provided by the previous endpoint: /widget/url",
            "schema": {
              "type": "string"
            },
            "required": true
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