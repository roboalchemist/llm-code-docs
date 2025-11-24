# Source: https://docs.fireworks.ai/api-reference-dlde/cancel-batch-job.md

# Cancel Batch Job

> Cancels an existing batch job if it is queued, pending, or running.

## OpenAPI

````yaml post /v1/accounts/{account_id}/batchJobs/{batch_job_id}:cancel
paths:
  path: /v1/accounts/{account_id}/batchJobs/{batch_job_id}:cancel
  method: post
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
        batch_job_id:
          schema:
            - type: string
              required: true
              description: The Batch Job Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties: {}
            required: true
            refIdentifier: '#/components/schemas/GatewayCancelBatchJobBody'
        examples:
          example:
            value: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````