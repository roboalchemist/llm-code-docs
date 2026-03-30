# Source: https://docs.drip.re/api-reference/credentials-balances/update-point-balance-for-a-credential-by-its-identifier-email-wallet-discord-id-etc.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Update point balance for a credential by its identifier (email, wallet, discord ID, etc)

> Update point balance for a credential by its identifier (email, wallet, discord ID, etc)

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/balance
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
  /api/v1/realms/{realmId}/credentials/balance:
    patch:
      tags:
        - Credentials-Balances
      summary: >-
        Update point balance for a credential by its identifier (email, wallet,
        discord ID, etc)
      description: >-
        Update point balance for a credential by its identifier (email, wallet,
        discord ID, etc)
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
          name: type
          required: true
          description: Type of credential identifier
        - schema:
            type: string
          in: query
          name: value
          required: true
          description: >-
            Credential value (email address, wallet address, discord ID, twitter
            ID, or custom ID)
        - schema:
            type: string
          in: query
          name: source
          required: false
          description: >-
            Required for custom type. The source/provider name (e.g.,
            'shopify-customer-id', 'internal-user-id')
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
                    default point.
                amount:
                  type: integer
                  description: Amount to add (positive) or deduct (negative)
                initiatorId:
                  type: string
                  description: ID of the user initiating this update
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  credentialId:
                    type: string
                  identifier:
                    type: string
                  balance:
                    type: integer
                  realmPointId:
                    type: string
                  linked:
                    type: boolean
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
