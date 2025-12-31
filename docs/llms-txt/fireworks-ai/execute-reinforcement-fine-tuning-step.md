# Source: https://docs.fireworks.ai/api-reference/execute-reinforcement-fine-tuning-step.md

# Execute one training step for keep-alive Reinforcement Fine-tuning Step



## OpenAPI

````yaml post /v1/accounts/{account_id}/rlorTrainerJobs/{rlor_trainer_job_id}:executeTrainStep
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.15.25
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/rlorTrainerJobs/{rlor_trainer_job_id}:executeTrainStep:
    post:
      tags:
        - Gateway
      summary: Execute one training step for keep-alive Reinforcement Fine-tuning Step
      operationId: Gateway_ExecuteRlorTrainStep
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: rlor_trainer_job_id
          in: path
          required: true
          description: The Rlor Trainer Job Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayExecuteRlorTrainStepBody'
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
    GatewayExecuteRlorTrainStepBody:
      type: object
      properties:
        dataset:
          type: string
          description: Dataset to process for this iteration.
        outputModel:
          type: string
          description: Output model to materialize when training completes.
      required:
        - dataset
        - outputModel
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt