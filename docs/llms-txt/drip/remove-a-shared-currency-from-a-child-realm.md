# Source: https://docs.drip.re/api-reference/shared-currency/remove-a-shared-currency-from-a-child-realm.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove a shared currency from a child realm

> Remove a shared currency from a child realm

## OpenAPI

````yaml https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/currencies/{currencyId}/remove
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
  /api/v1/realms/{realmId}/currencies/{currencyId}/remove:
    delete:
      tags:
        - Shared Currency
      summary: Remove a shared currency from a child realm
      description: Remove a shared currency from a child realm
      parameters:
        - schema:
            type: string
          in: path
          name: realmId
          required: true
        - schema:
            type: string
          in: path
          name: currencyId
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: string
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
