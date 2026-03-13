# Source: https://virustotal.readme.io/reference/domains-rescan.md

# Request an domain (re)scan

Reanalyse a domain already in VirusTotal

This endpoint can be used to analyse domains or reanalyse them to refresh their verdicts, whois information, SSL certs, etc. This endpoint sends the domain to be (re)scanned and returns an analysis ID that can be used to retrieve the verdicts from the available vendors using the [Analyses](https://virustotal.readme.io/reference/analysis-api) endpoint.

```json Example response
{
    "data": {
        "type": "analysis",
        "id": "d-f4e5279ebbcf9d485e33f3c67007b73e9f12d54bbca875545819a2307a194752-1715608490",
        "links": {
            "self": "https://www.virustotal.com/api/v3/analyses/d-f4e5279ebbcf9d485e33f3c67007b73e9f12d54bbca875545819a2307a194752-1715608490"
        }
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
    "/domains/{id}/analyse": {
      "post": {
        "summary": "Request an domain rescan (re-analyze)",
        "description": "Reanalyse a domain already in VirusTotal",
        "operationId": "domains-rescan",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Domain",
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