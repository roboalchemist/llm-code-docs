# Source: https://docs.fireworks.ai/api-reference/cancel-reinforcement-fine-tuning-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel Reinforcement Fine-tuning Job



## OpenAPI

````yaml post /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel
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
  /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel:
    post:
      tags:
        - Gateway
      summary: Cancel Reinforcement Fine-tuning Job
      operationId: Gateway_CancelReinforcementFineTuningJob
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: reinforcement_fine_tuning_job_id
          in: path
          required: true
          description: The Reinforcement Fine-tuning Job Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayCancelReinforcementFineTuningJobBody'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                type: object
                properties: {}
components:
  schemas:
    GatewayCancelReinforcementFineTuningJobBody:
      type: object
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````