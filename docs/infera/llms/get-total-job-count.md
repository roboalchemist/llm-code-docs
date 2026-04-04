# Source: https://docs.infera.org/api-reference/endpoint/get-total-job-count.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Total Job Count



## OpenAPI

````yaml get /total_job_count
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /total_job_count:
    get:
      summary: Get Total Job Count
      operationId: get_total_job_count_total_job_count_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
      security:
        - APIKeyHeader: []
components:
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````