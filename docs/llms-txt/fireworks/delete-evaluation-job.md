# Source: https://docs.fireworks.ai/api-reference/delete-evaluation-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Evaluation Job



## OpenAPI

````yaml delete /v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}
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
  /v1/accounts/{account_id}/evaluationJobs/{evaluation_job_id}:
    delete:
      tags:
        - Gateway
      summary: Delete Evaluation Job
      operationId: Gateway_DeleteEvaluationJob
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: evaluation_job_id
          in: path
          required: true
          description: The Evaluation Job Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                type: object
                properties: {}
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````