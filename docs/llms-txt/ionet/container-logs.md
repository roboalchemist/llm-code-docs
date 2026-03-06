# Source: https://io.net/docs/reference/caas/container-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Access real-time or historical logs for a specific container in a deployment.

# Container Logs

## Fetching Container Logs via API

* The logs endpoint always **produces a chunked response** - it’s a **stream**.
* Specifically, it uses **Server-Sent Events (SSE)** for streaming logs.
* **Do not** use r`esponse.json();` consume the logs line-by-line.
* Currently, the **API spec is incomplete**:
  * `offset` and `stream type` query parameters are missing.
  * Public API specs need a full review to match Swagger; other fields may be missing.

### Python Example

```python  theme={null}
import requests

# Replace with your Deployment and Log IDs
deployment_id = "Deployment ID"
log_id = "Log ID"

url = "https://api.io.solutions/enterprise/v1/io-cloud/caas/deployment/{deployment_id}/log/{log_id}"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Use stream=True to handle the response incrementally
with requests.get(url, headers=headers, stream=True) as r:
    r.raise_for_status()
    for line in r.iter_lines():
        if line:
            print(line.decode("utf-8"))
```

### Notes

* Treat all responses as **streams**, not JSON.
* Each line corresponds to a log entry (stdout/stderr), as seen in the UI.
* SSE allows for real-time log consumption for monitoring/debugging.


## OpenAPI

````yaml openapi/caas/container-logs.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/log/{container_id}
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/log/{container_id}:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get Container Log Stream
      operationId: >-
        get_container_log_stream_enterprise_v1_io_cloud_caas_deployment__deployment_id__log__container_id__get
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment Id
        - name: container_id
          in: path
          required: true
          schema:
            type: string
            title: Container Id
        - name: stream
          in: query
          required: false
          schema:
            allOf:
              - $ref: '#/components/schemas/LogStream'
            default: stdout
            title: Stream
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: io.net provided API Key
            title: X-Api-Key
          description: io.net provided API Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      deprecated: false
components:
  schemas:
    LogStream:
      type: string
      enum:
        - stdout
        - stderr
      title: LogStream
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````