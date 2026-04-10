# Source: https://docs.drip.re/api-reference/realm-members-balances/transfer-member-balance-of-a-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Member Balance Of A Currency

> Transfer points from one DRIP user to another in a realm by their drip ids and currency id

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/{dripId}/transfer
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
  /api/v1/realms/{realmId}/members/{dripId}/transfer:
    patch:
      tags:
        - Realm-Members-Balances
      summary: Transfer Member Balance Of A Currency
      description: >-
        Transfer points from one DRIP user to another in a realm by their drip
        ids and currency id
      parameters:
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: realmId
          required: true
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: dripId
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                amount:
                  type: integer
                  minimum: 1
                  description: Amount to transfer
                recipientId:
                  type: string
                  description: ID of the recipient
                currencyId:
                  type: string
                  description: ID of the realm point type
              required:
                - amount
                - recipientId
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  senderId:
                    type: string
                  recipientId:
                    type: string
                  balance:
                    type: integer
                  currencyId:
                    type: string
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
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
