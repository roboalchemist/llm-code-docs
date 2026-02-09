# Source: https://docs.fireworks.ai/api-reference/get-dpo-job-metrics-file-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# null



## OpenAPI

````yaml get /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint:
    get:
      tags:
        - Gateway
      operationId: Gateway_GetDpoJobMetricsFileEndpoint
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: dpo_job_id
          in: path
          required: true
          description: The Dpo Job Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayGetDpoJobMetricsFileResponse'
components:
  schemas:
    gatewayGetDpoJobMetricsFileResponse:
      type: object
      properties:
        signedUrl:
          type: string
          title: The signed URL for the metrics file
      title: |-
        when the JobMetrics file has been created for the DPO job
        and the file exists, we will populate this field
        empty otherwise
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````