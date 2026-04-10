# Source: https://docs.drip.re/api-reference/shared-currency/share-a-currency-with-another-realm.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Share a currency with another realm

> Share a currency with another realm

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies/{currencyId}/share
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
  /api/v1/realms/{realmId}/currencies/{currencyId}/share:
    post:
      tags:
        - Shared Currency
      summary: Share a currency with another realm
      description: Share a currency with another realm
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                childRealmId:
                  type: string
                permissions:
                  type: array
                  items:
                    type: string
              required:
                - childRealmId
                - permissions
        required: true
      responses:
        '201':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
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
                      status:
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
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
