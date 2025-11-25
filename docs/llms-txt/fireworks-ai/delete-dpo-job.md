# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-dpo-job.md

# Source: https://docs.fireworks.ai/api-reference/delete-dpo-job.md

# null

## OpenAPI

````yaml delete /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}
paths:
  path: /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}
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
        dpo_job_id:
          schema:
            - type: string
              required: true
              description: The Dpo Job Id
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