# Source: https://docs.wandb.ai/api-reference/health/health-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Check



## OpenAPI

````yaml /training/api-reference/openapi.json get /v1/health
openapi: 3.1.0
info:
  title: W&B Training
  version: 1.0.0
servers: []
security: []
paths:
  /v1/health:
    get:
      tags:
        - health
      summary: Health Check
      operationId: health_check_v1_health_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````