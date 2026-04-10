# Source: https://docs.drip.re/api-reference/shared-currency/get-all-the-pending-requests-for-a-realm-not-by-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all the pending requests for a realm (not by currency)

> Get all the pending requests for a realm (not by currency)

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/shares/pending
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
  /api/v1/realms/{realmId}/shares/pending:
    get:
      tags:
        - Shared Currency
      summary: Get all the pending requests for a realm (not by currency)
      description: Get all the pending requests for a realm (not by currency)
      parameters:
        - schema:
            type: string
          in: path
          name: realmId
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
                        parentRealmId:
                          type: string
                        childRealmId:
                          type: string
                        realmPointId:
                          type: string
                        permissions:
                          type: array
                          items:
                            type: string
                        createdAt:
                          type: string
                          format: date-time
                        status:
                          type: string
                        parentRealm:
                          type: object
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                        realmPoint:
                          type: object
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            emoji:
                              type: string
                            customEmojiUrl:
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
