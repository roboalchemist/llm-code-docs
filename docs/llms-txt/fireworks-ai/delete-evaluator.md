# Source: https://docs.fireworks.ai/api-reference/delete-evaluator.md

# Delete Evaluator

> Deletes an evaluator and its associated versions and build artifacts.



## OpenAPI

````yaml delete /v1/accounts/{account_id}/evaluators/{evaluator_id}
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
  /v1/accounts/{account_id}/evaluators/{evaluator_id}:
    delete:
      tags:
        - Gateway
      summary: Delete Evaluator
      description: Deletes an evaluator and its associated versions and build artifacts.
      operationId: Gateway_DeleteEvaluator
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: evaluator_id
          in: path
          required: true
          description: The Evaluator Id
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt