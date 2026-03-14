# Source: https://virustotal.readme.io/reference/monitorpartner-hashes-comments.md

# Create a comment over a hash

Create a comment and if necessary confirm detection over a hash

This endpoint allows you to create a comment over certain hash, this comment may be visible to other partners (for example if they also detect the hash) and to monitor users who have a file with this hash.
A MonitorHashComment also have a *detection* attribute that could be set to 'confirmed' to ignore this particular hash from that moment on. Once the hash comment is marked as confirmed any new monitor analysis for this file that your engine will detect will not be shown anymore when requesting latests analyses. This behaviour can be reverted deleting the comment or updating it with detection attribute set to None.
Ignored hashes with detections still can be retrieved using [/hashes](https://virustotal.readme.io/reference/monitorpartner-hashes) endpoint with a filter "tag:ignored"

```python
import requests

sha256 = '<hash-sha256>'
engine = '<your-engine-id>'

url = "https://www.virustotal.com/api/v3/monitor_partner/hashes/%s/comments" % sha256
data = {'data': [{'attributes': {
          'comment': '[TEXT]',
          'detection': 'confirmed',
          'engine': engine,
          'sha256': sha256},
        'type': 'monitor_hash_comment'}]}

response = requests.request("POST", url, data=json.dumps(data))
print(response.text)
```

```json
{
  'data': [
    {
      'type': 'monitor_hash_comment',
      'id': '{id}',
      'attributes': {
        'comment': '{text}',
        'detection': 'confirmed',
        'engine': '{engine name}',
        'sha256': '{sha256}'
      }
    }
  ]
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
    "/monitor_partner/hashes/{sha256}/comments": {
      "post": {
        "summary": "Create a comment over a hash",
        "description": "Create a comment and if necessary confirm detection over a hash",
        "operationId": "monitorpartner-hashes-comments",
        "parameters": [
          {
            "name": "sha256",
            "in": "path",
            "description": "Hash sha256",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A json object with a MonitorHashComment",
                    "default": "{\"data\": [{\"attributes\": {\"comment\": \"[TEXT]\", \"detection\": \"confirmed\", \"engine\": \"[ENGINE-ID]\", \"sha256\": \"[HASH-SHA256]\"}, \"type\": \"monitor_hash_comment\"}]}",
                    "format": "json"
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