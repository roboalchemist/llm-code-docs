# Source: https://docs.fireworks.ai/api-reference/update-secret.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# null



## OpenAPI

````yaml patch /v1/accounts/{account_id}/secrets/{secret_id}
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
  /v1/accounts/{account_id}/secrets/{secret_id}:
    patch:
      tags:
        - Gateway
      operationId: Gateway_UpdateSecret
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: secret_id
          in: path
          required: true
          description: The Secret Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                keyName:
                  type: string
                  title: >-
                    name of the key. In this case, it can be
                    WOLFRAM_ALPHA_API_KEY
                value:
                  type: string
                  example: sk-1234567890abcdef
                  description: >-
                    The secret value. This field is INPUT_ONLY and will not be
                    returned in GET or LIST responses

                    for security reasons. The value is only accepted when
                    creating or updating secrets.
              required:
                - keyName
                - secret
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewaySecret'
components:
  schemas:
    gatewaySecret:
      type: object
      properties:
        name:
          type: string
          title: |-
            name follows the convention
            accounts/account-id/secrets/unkey-key-id
        keyName:
          type: string
          title: name of the key. In this case, it can be WOLFRAM_ALPHA_API_KEY
        value:
          type: string
          example: sk-1234567890abcdef
          description: >-
            The secret value. This field is INPUT_ONLY and will not be returned
            in GET or LIST responses

            for security reasons. The value is only accepted when creating or
            updating secrets.
      required:
        - name
        - keyName
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````