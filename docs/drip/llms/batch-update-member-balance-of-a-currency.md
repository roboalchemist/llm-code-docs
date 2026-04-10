# Source: https://docs.drip.re/api-reference/realm-members-balances/batch-update-member-balance-of-a-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch Update Member Balance Of A Currency

> Batch update the balances of multiple DRIP users in a realm by their drip ids and currency id. All updates are applied in a single transaction, so if any update fails, the entire batch will fail.

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/members/transaction
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
  /api/v1/realms/{realmId}/members/transaction:
    patch:
      tags:
        - Realm-Members-Balances
      summary: Batch Update Member Balance Of A Currency
      description: >-
        Batch update the balances of multiple DRIP users in a realm by their
        drip ids and currency id. All updates are applied in a single
        transaction, so if any update fails, the entire batch will fail.
      parameters:
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: realmId
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                updates:
                  type: array
                  items:
                    type: object
                    properties:
                      dripId:
                        type: string
                      amount:
                        type: integer
                      currencyId:
                        type: string
                    required:
                      - dripId
                      - amount
                initiatorId:
                  type: string
              required:
                - updates
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
                  updates:
                    type: array
                    items:
                      type: object
                      properties:
                        dripId:
                          type: string
                        balance:
                          type: integer
                        currencyId:
                          type: string
                        newBalance:
                          type: integer
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
