# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/cancel-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/api-reference/cancel-reinforcement-fine-tuning-job.md

# Cancel Reinforcement Fine-tuning Job

## OpenAPI

````yaml post /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel
paths:
  path: >-
    /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel
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
        reinforcement_fine_tuning_job_id:
          schema:
            - type: string
              required: true
              description: The Reinforcement Fine-tuning Job Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties: {}
            required: true
            refIdentifier: '#/components/schemas/GatewayCancelReinforcementFineTuningJobBody'
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