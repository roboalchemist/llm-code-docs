# Source: https://docs.infera.org/api-reference/endpoint/get-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Job



## OpenAPI

````yaml get /worker/get_job
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /worker/get_job:
    get:
      summary: Get Job
      operationId: get_job_worker_get_job_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}

````