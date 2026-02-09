# Source: https://docs.infera.org/api-reference/endpoint/ping-worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Ping Worker



## OpenAPI

````yaml get /worker/ping
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /worker/ping:
    get:
      summary: Ping Worker
      operationId: ping_worker_worker_ping_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````