# Source: https://docs.drip.re/api-reference/credentials-balances/transfer-points-from-one-credential-to-another-by-their-identifiers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer points from one credential to another by their identifiers

> Transfer points from one credential to another by their identifiers

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/transfer
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
  /api/v1/realms/{realmId}/credentials/transfer:
    patch:
      tags:
        - Credentials-Balances
      summary: Transfer points from one credential to another by their identifiers
      description: Transfer points from one credential to another by their identifiers
      parameters:
        - schema:
            type: string
            enum:
              - twitter-id
              - discord-id
              - wallet
              - email
              - custom
          in: query
          name: fromType
          required: true
          description: Sender credential type
        - schema:
            type: string
          in: query
          name: fromValue
          required: true
          description: Sender credential value
        - schema:
            type: string
          in: query
          name: fromSource
          required: false
          description: Required for custom fromType
        - schema:
            type: string
            enum:
              - twitter-id
              - discord-id
              - wallet
              - email
              - custom
          in: query
          name: toType
          required: true
          description: Recipient credential type
        - schema:
            type: string
          in: query
          name: toValue
          required: true
          description: Recipient credential value
        - schema:
            type: string
          in: query
          name: toSource
          required: false
          description: Required for custom toType
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
                - amount
              properties:
                realmPointId:
                  type: string
                  description: >-
                    Realm point (currency) ID. If not provided, uses the realm's
                    default currency.
                amount:
                  type: integer
                  minimum: 1
                  description: Amount to transfer
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  fromCredentialId:
                    type: string
                  toCredentialId:
                    type: string
                  amount:
                    type: integer
                  realmPointId:
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
