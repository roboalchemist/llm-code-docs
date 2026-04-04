# Source: https://docs.fireworks.ai/api-reference-dlde/batch-delete-batch-jobs.md

# Batch Delete Batch Jobs

## OpenAPI

````yaml post /v1/accounts/{account_id}/batchJobs:batchDelete
paths:
  path: /v1/accounts/{account_id}/batchJobs:batchDelete
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              names:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: The resource names of the batch jobs to delete.
            required: true
            refIdentifier: '#/components/schemas/GatewayBatchDeleteBatchJobsBody'
            requiredProperties:
              - names
        examples:
          example:
            value:
              names:
                - <string>
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