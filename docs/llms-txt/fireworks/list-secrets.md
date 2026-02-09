# Source: https://docs.fireworks.ai/api-reference/list-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Secrets

> Lists all secrets for an account. Note that the `value` field is not returned in the response for security reasons. Only the `name` and `key_name` fields are included for each secret.



## OpenAPI

````yaml get /v1/accounts/{account_id}/secrets
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
  /v1/accounts/{account_id}/secrets:
    get:
      tags:
        - Gateway
      summary: List Secrets
      description: >-
        Lists all secrets for an account. Note that the `value` field is not
        returned in the response for security reasons. Only the `name` and
        `key_name` fields are included for each secret.
      operationId: Gateway_ListSecrets
      parameters:
        - name: pageSize
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: pageToken
          in: query
          required: false
          schema:
            type: string
        - name: filter
          description: Unused but required to use existing ListRequest functionality.
          in: query
          required: false
          schema:
            type: string
        - name: orderBy
          description: Unused but required to use existing ListRequest functionality.
          in: query
          required: false
          schema:
            type: string
        - name: readMask
          description: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.
          in: query
          required: false
          schema:
            type: string
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayListSecretsResponse'
components:
  schemas:
    gatewayListSecretsResponse:
      type: object
      properties:
        secrets:
          type: array
          items:
            $ref: '#/components/schemas/gatewaySecret'
            type: object
        nextPageToken:
          type: string
        totalSize:
          type: integer
          format: int32
          description: The total number of secrets.
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