# Source: https://docs.wandb.ai/api-reference/health/system-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# System Check

> Check health of all system components.

Returns:
    JSON with status of:
    - api: Always true (if endpoint is reachable)
    - database: Whether DB connection works
    - cpu_queue: Success, duration, and any errors
    - gpu_queue: Success, duration, and any errors

Returns HTTP 503 if any checks fail.



## OpenAPI

````yaml /training/api-reference/openapi.json get /v1/system-check
openapi: 3.1.0
info:
  title: W&B Training
  version: 1.0.0
servers: []
security: []
paths:
  /v1/system-check:
    get:
      tags:
        - health
      summary: System Check
      description: |-
        Check health of all system components.

        Returns:
            JSON with status of:
            - api: Always true (if endpoint is reachable)
            - database: Whether DB connection works
            - cpu_queue: Success, duration, and any errors
            - gpu_queue: Success, duration, and any errors

        Returns HTTP 503 if any checks fail.
      operationId: system_check_v1_system_check_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````