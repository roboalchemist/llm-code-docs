# Source: https://docs.wandb.ai/weave/reference/service-api/service/read-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Version



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /version
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /version:
    get:
      tags:
        - Service
      summary: Read Version
      operationId: read_version_version_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````