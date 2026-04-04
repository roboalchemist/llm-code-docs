# Source: https://docs.galileo.ai/api-reference/health/healthcheck.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Healthcheck



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json get /v1/healthcheck
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/healthcheck:
    get:
      tags:
        - health
      summary: Healthcheck
      operationId: healthcheck_v1_healthcheck_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HealthcheckResponse'
components:
  schemas:
    HealthcheckResponse:
      properties:
        api_version:
          type: string
          title: Api Version
        message:
          type: string
          title: Message
        version:
          type: string
          title: Version
      type: object
      required:
        - api_version
        - message
        - version
      title: HealthcheckResponse

````