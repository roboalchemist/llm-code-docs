# Source: https://docs.fireworks.ai/api-reference/validate-evaluator-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate Evaluator Upload

> Triggers server-side validation of the uploaded source code (**step 5** in
the [Create Evaluator](/api-reference/create-evaluator) workflow). The server
extracts and processes the archive, then builds the evaluator environment.
Poll [Get Evaluator](/api-reference/get-evaluator) to monitor progress.



## OpenAPI

````yaml post /v1/accounts/{account_id}/evaluators/{evaluator_id}:validateUpload
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
  /v1/accounts/{account_id}/evaluators/{evaluator_id}:validateUpload:
    post:
      tags:
        - Gateway
      summary: Validate Evaluator Upload
      description: >-
        Triggers server-side validation of the uploaded source code (**step 5**
        in

        the [Create Evaluator](/api-reference/create-evaluator) workflow). The
        server

        extracts and processes the archive, then builds the evaluator
        environment.

        Poll [Get Evaluator](/api-reference/get-evaluator) to monitor progress.
      operationId: Gateway_ValidateEvaluatorUpload
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayValidateEvaluatorUploadBody'
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
    GatewayValidateEvaluatorUploadBody:
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