# Source: https://docs.drip.re/api-reference/shared-currency/list-all-child-realms-that-use-a-parents-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# List all child realms that use a parent's currency

> List all child realms that use a parent's currency

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/currencies/{currencyId}/shares
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
  /api/v1/realms/{realmId}/currencies/{currencyId}/shares:
    get:
      tags:
        - Shared Currency
      summary: List all child realms that use a parent's currency
      description: List all child realms that use a parent's currency
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
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        childRealmId:
                          type: string
                        createdAt:
                          type: string
                          format: date-time
                        permissions:
                          type: array
                          items:
                            type: string
                        status:
                          type: string
                        childRealm:
                          type: object
                          properties:
                            id:
                              type: string
                            name:
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
