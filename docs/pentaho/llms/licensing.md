# Source: https://docs.pentaho.com/pdc-api-docs/pdc-api-ref-v2/licensing.md

# Source: https://docs.pentaho.com/pdc-api-docs/v1/pdc-api-ref-v1/licensing.md

# Licensing

## Licenses

> Check what licensed features are in use

```json
{"openapi":"3.0.3","info":{"title":"PDC Public API (v1)","version":"v1"},"servers":[{"url":"/"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer","description":"Insert the JWT token here","bearerFormat":"JWT"}}},"paths":{"/api/public/v1/licensing/licenses":{"get":{"summary":"Licenses","tags":["Licensing"],"description":"Check what licensed features are in use","responses":{"200":{"description":"Default Response","content":{"application/json":{"schema":{"type":"object","properties":{"status":{"type":"boolean","description":"Indicates if the request was successful"},"errMessage":{"type":"string","description":"Error message if the request failed"},"features":{"type":"array","items":{"type":"object","properties":{"featureName":{"type":"string","description":"Name of the licensed feature"},"version":{"type":"string","description":"Version of the licensed feature"},"count":{"type":"number","description":"Number of licenses used for the feature"}}}}}}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"description":"Bad Request","type":"object","properties":{"status":{"type":"number"},"message":{"oneOf":[{"type":"string"},{"type":"array"},{"type":"object","additionalProperties":true}]}}}}}},"401":{"description":"Unauthorized - The request requires a valid Bearer token.\n\n    \tTo access this endpoint:\n\n        1. Make a POST request to /api/public/v1/auth with valid credentials to obtain the access token.\n        2. Click the \"Authorize\" button in the Swagger UI and enter the token.\n        3. All protected endpoints require the Authorization header: \"Authorization: 'Bearer your-access-token'\"\n    ","content":{"application/json":{"schema":{"description":"Unauthorized - The request requires a valid Bearer token.\n\n    \tTo access this endpoint:\n\n        1. Make a POST request to /api/public/v1/auth with valid credentials to obtain the access token.\n        2. Click the \"Authorize\" button in the Swagger UI and enter the token.\n        3. All protected endpoints require the Authorization header: \"Authorization: 'Bearer your-access-token'\"\n    ","type":"object","properties":{"status":{"type":"number"},"message":{"type":"string"}}}}}},"500":{"description":"Internal Server Error","content":{"application/json":{"schema":{"description":"Internal Server Error","type":"object","properties":{"status":{"type":"number"},"message":{"type":"string"}}}}}},"503":{"description":"Service Unavailable — Connection Refused","content":{"application/json":{"schema":{"description":"Service Unavailable — Connection Refused","type":"object","properties":{"status":{"type":"number"},"message":{"type":"string"}}}}}}}}}}}
```

## Upload Offline License File

> Upload Offline License file with device ID

```json
{"openapi":"3.0.3","info":{"title":"PDC Public API (v1)","version":"v1"},"servers":[{"url":"/"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer","description":"Insert the JWT token here","bearerFormat":"JWT"}}},"paths":{"/api/public/v1/licensing/uploadLicense":{"post":{"summary":"Upload Offline License File","tags":["Licensing"],"description":"Upload Offline License file with device ID","requestBody":{"content":{"multipart/form-data":{"schema":{"type":"object","properties":{"deviceId":{"type":"string"},"fileData":{"type":"string","format":"binary"}},"required":["fileData"]}}}},"responses":{"200":{"description":"Default Response","content":{"application/json":{"schema":{"type":"object","properties":{"success":{"type":"boolean"},"message":{"type":"string"},"deviceId":{"type":"string"},"fileName":{"type":"string"},"fileSize":{"type":"number"},"featuresCount":{"type":"number"}}}}}}}}}}}
```
