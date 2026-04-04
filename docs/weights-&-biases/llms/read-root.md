# Source: https://docs.wandb.ai/weave/reference/service-api/service/read-root.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Root



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /health
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /health:
    get:
      tags:
        - Service
      summary: Read Root
      operationId: read_root_health_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````