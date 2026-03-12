# Source: https://docs.drip.re/api-reference/currencies/unarchive-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Unarchive Currency

> Unarchive a currency

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies/{currencyId}/unarchive
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
  /api/v1/realms/{realmId}/currencies/{currencyId}/unarchive:
    post:
      tags:
        - Currencies
      summary: Unarchive Currency
      description: Unarchive a currency
      parameters:
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: realmId
          required: true
        - schema:
            type: string
          in: path
          name: currencyId
          required: true
      responses:
        '204':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessWithNoContentResponse'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - BearerAuth: []
components:
  schemas:
    SuccessWithNoContentResponse:
      $ref: '#/components/schemas/SuccessWithNoContentResponse'
      type: object
      properties: {}
    ErrorResponse:
      $ref: '#/components/schemas/ErrorResponse'
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
        message:
          type: string
          description: Error message
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
