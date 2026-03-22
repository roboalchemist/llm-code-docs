# Source: https://docs.wandb.ai/weave/reference/service-api/service/server-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Info



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /server_info
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /server_info:
    get:
      tags:
        - Service
      summary: Server Info
      operationId: server_info_server_info_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServerInfoRes'
components:
  schemas:
    ServerInfoRes:
      properties:
        min_required_weave_python_version:
          type: string
          title: Min Required Weave Python Version
        trace_server_version:
          type: string
          title: Trace Server Version
      type: object
      required:
        - min_required_weave_python_version
        - trace_server_version
      title: ServerInfoRes

````