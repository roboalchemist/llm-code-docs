# Source: https://docs.fireworks.ai/api-reference/create-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create API Key



## OpenAPI

````yaml post /v1/accounts/{account_id}/users/{user_id}/apiKeys
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
  /v1/accounts/{account_id}/users/{user_id}/apiKeys:
    post:
      tags:
        - Gateway
      summary: Create API Key
      operationId: Gateway_CreateApiKey
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
              $ref: '#/components/schemas/GatewayCreateApiKeyBody'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayApiKey'
components:
  schemas:
    GatewayCreateApiKeyBody:
      type: object
      properties:
        apiKey:
          $ref: '#/components/schemas/gatewayApiKey'
          description: The API key to be created.
      required:
        - apiKey
    gatewayApiKey:
      type: object
      properties:
        keyId:
          type: string
          description: >-
            Unique identifier (Key ID) for the API key, used primarily for
            deletion.
          readOnly: true
        displayName:
          type: string
          description: >-
            Display name for the API key, defaults to "default" if not
            specified.
        key:
          type: string
          description: >-
            The actual API key value, only available upon creation and not
            stored thereafter.
          readOnly: true
        createTime:
          type: string
          format: date-time
          description: Timestamp indicating when the API key was created.
          readOnly: true
        secure:
          type: boolean
          description: >-
            Indicates whether the plaintext value of the API key is unknown to
            Fireworks.

            If true, Fireworks does not know this API key's plaintext value. If
            false, Fireworks does

            know the plaintext value.
          readOnly: true
        email:
          type: string
          description: Email of the user who owns this API key.
          readOnly: true
        prefix:
          type: string
          title: The first few characters of the API key to visually identify it
          readOnly: true
        expireTime:
          type: string
          format: date-time
          description: >-
            Timestamp indicating when the API key will expire. If not set, the
            key never expires.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````