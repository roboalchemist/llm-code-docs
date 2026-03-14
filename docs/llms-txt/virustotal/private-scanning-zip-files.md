# Source: https://virustotal.readme.io/reference/private-scanning-zip-files.md

# Create a password-protected ZIP with VirusTotal private files

Creates a ZIP file containing the files specified in the request. Optionally you can provide a password for protecting the ZIP file. The request's body must have the following structure:

```json Example request
{
  "data": {
    "password": "mysecretpassword", 
    "hashes":[
      "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
      "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "ed1707bf39a62b0efd40e76f55409ee99db0289dc5027d0a5e5337b4e7a61ccc"]
  }
}
```

The response from this endpoint is the object corresponding to the newly created ZIP file. Notice however that your ZIP file won't be ready to be downloaded right away, you must wait for the backend to create the ZIP file for you, that's why the returned object has a `status` and `progress` attribute, which indicates the current status and current progress for the ZIP creation process.

```json Example response
{
  "data": {
    "type": "zip_file",
    "id": "4939392292",
    "attributes": {
      "status": "starting",
      "progress": 0,
      "files_ok": 0,
      "files_error": 0
    }  
  }
}
```

The [GET /private/zip\_files/{id}](https://virustotal.readme.io/reference/private-scanning-get-zip-file) endpoint should be used for retrieving the latest status of the ZIP file until it's `finished`.

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
    "/zip_files": {
      "post": {
        "summary": "Create a password-protected ZIP with VirusTotal private files",
        "description": "",
        "operationId": "private-scanning-zip-files",
        "parameters": [
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
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A list of hashes (SHA-256, SHA-1, or MD5) for the files included in the ZIP",
                    "default": "{\"password\": \"<password>\", \"hashes\":[\"<hash1>\", \"<hash2>\"]}",
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