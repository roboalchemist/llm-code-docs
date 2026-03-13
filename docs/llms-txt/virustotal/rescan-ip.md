# Source: https://virustotal.readme.io/reference/rescan-ip.md

# Request an IP address (re)scan

Reanalyse an IP address already in VirusTotal

IPs in VirusTotal can be reanalysed to refresh their verdicts, whois information, SSL certs, etc. This endpoint sends the IP to be (re)scanned and returns an analysis ID that can be used to retrieve the verdicts from the available vendors using the [Analyses](https://virustotal.readme.io/reference/analysis-api) endpoint.

```json Example response
{
    "data": {
        "type": "analysis",
        "id": "i-f41d931c01fcee6c19e73200aa87ea5d8a8de5316c5288a8df869d31efa1d0fc-1715609875",
        "links": {
            "self": "https://www.virustotal.com/api/v3/analyses/i-f41d931c01fcee6c19e73200aa87ea5d8a8de5316c5288a8df869d31efa1d0fc-1715609875"
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
    "/ip_addresses/{id}/analyse": {
      "post": {
        "summary": "Request an IP address rescan (re-analyze)",
        "description": "Reanalyse an IP address already in VirusTotal",
        "operationId": "rescan-ip",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "IP address",
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