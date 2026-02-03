# Source: https://docs.fireworks.ai/api-reference/delete-dpo-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# null



## OpenAPI

````yaml delete /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}
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
  /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:
    delete:
      tags:
        - Gateway
      operationId: Gateway_DeleteDpoJob
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