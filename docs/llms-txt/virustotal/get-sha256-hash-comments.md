# Source: https://virustotal.readme.io/reference/get-sha256-hash-comments.md

# Get comments on a sha256 hash

This endpoint allows you to retrieve partner comments over a certain sha256 hash.

```python
import requests

session = requests.Session()
session.headers = {'X-Apikey': '<api-key>'}

url = "https://www.virustotal.com/api/v3/monitor_partner/comments/<comment-id>/"
response = session.get(url)
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
    "/monitor_partner/comments/{id}": {
      "get": {
        "summary": "Get comments on a sha256 hash",
        "description": "",
        "operationId": "get-sha256-hash-comments",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Comment ID",
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