# Source: https://docs.drip.re/api-reference/realm-members-balances/update-member-balance-of-a-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Member Balance Of A Currency

> Update the balance of a DRIP user in a realm by their drip id and currency id

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/{dripId}/balance
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
  /api/v1/realms/{realmId}/members/{dripId}/balance:
    patch:
      tags:
        - Realm-Members-Balances
      summary: Update Member Balance Of A Currency
      description: >-
        Update the balance of a DRIP user in a realm by their drip id and
        currency id
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
                currencyId:
                  type: string
                initiatorId:
                  type: string
              required:
                - amount
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
                  dripId:
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
