# Source: https://docs.fireworks.ai/api-reference/delete-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete API Key



## OpenAPI

````yaml post /v1/accounts/{account_id}/users/{user_id}/apiKeys:delete
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
  /v1/accounts/{account_id}/users/{user_id}/apiKeys:delete:
    post:
      tags:
        - Gateway
      summary: Delete API Key
      operationId: Gateway_DeleteApiKey
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: user_id
          in: path
          required: true
          description: The User Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayDeleteApiKeyBody'
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
    GatewayDeleteApiKeyBody:
      type: object
      properties:
        keyId:
          type: string
          description: The key ID for the API key.
      required:
        - keyId
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````