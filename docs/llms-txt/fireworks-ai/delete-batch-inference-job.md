# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-batch-inference-job.md

# Source: https://docs.fireworks.ai/api-reference/delete-batch-inference-job.md

# Delete Batch Inference Job

## OpenAPI

````yaml delete /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}
paths:
  path: /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}
  method: delete
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
        batch_inference_job_id:
          schema:
            - type: string
              required: true
              description: The Batch Inference Job Id
      query: {}
      header: {}
      cookie: {}
    body: {}
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