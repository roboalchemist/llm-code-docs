# Source: https://docs.drip.re/api-reference/credentials-balances/batch-update-point-balances-for-multiple-credentials-by-their-identifiers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch update point balances for multiple credentials by their identifiers

> Batch update point balances for multiple credentials by their identifiers

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/transaction
openapi: 3.1.0
info:
  title: Drip Rewards API
  description: The official API documentation for the Drip Rewards Ecosystem
  version: 1.0.0
servers:
  - url: https://api.drip.re/
    description: DRIP API
security:
  - BearerAuth: []
tags: []
externalDocs:
  url: https://swagger.io
  description: Find more info here
paths:
  /api/v1/realms/{realmId}/credentials/transaction:
    patch:
      tags:
        - Credentials-Balances
      summary: >-
        Batch update point balances for multiple credentials by their
        identifiers
      description: >-
        Batch update point balances for multiple credentials by their
        identifiers
      parameters:
        - schema:
            type: string
          in: path
          name: realmId
          required: true
          description: Realm ID
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - updates
              properties:
                updates:
                  type: array
                  items:
                    type: object
                    required:
                      - type
                      - value
                      - amount
                    properties:
                      type:
                        type: string
                        enum:
                          - twitter-id
                          - discord-id
                          - wallet
                          - email
                          - custom
                      value:
                        type: string
                      source:
                        type: string
                        description: Required for custom type
                      realmPointId:
                        type: string
                      amount:
                        type: integer
                initiatorId:
                  type: string
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        type:
                          type: string
                        value:
                          type: string
                        credentialId:
                          type: string
                        balance:
                          type: integer
                        realmPointId:
                          type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        type:
                          type: string
                        value:
                          type: string
                        error:
                          type: string
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
