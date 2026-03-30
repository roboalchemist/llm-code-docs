# Source: https://docs.drip.re/api-reference/credentials/find-non-verified-credential-by-type-and-value-twitter-id-uses-oauthaccountid-wallet-uses-address-email-uses-email.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Find non-verified credential by type and value (twitter-id uses oauthAccountId, wallet uses address, email uses email)

> Find non-verified credential by type and value (twitter-id uses oauthAccountId, wallet uses address, email uses email)

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/credentials/find
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
  /api/v1/realms/{realmId}/credentials/find:
    get:
      tags:
        - Credentials
      summary: >-
        Find non-verified credential by type and value (twitter-id uses
        oauthAccountId, wallet uses address, email uses email)
      description: >-
        Find non-verified credential by type and value (twitter-id uses
        oauthAccountId, wallet uses address, email uses email)
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
            Credential value (twitter ID, discord ID, wallet address, email, or
            custom ID)
        - schema:
            type: string
          in: query
          name: source
          required: false
          description: Required for custom type
        - schema:
            type: string
          in: path
          name: realmId
          required: true
          description: Realm ID
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
                  format:
                    type: string
                  publicIdentifier:
                    type: string
                  balances:
                    type: array
                    items:
                      type: object
                      properties:
                        balance:
                          type: number
                        currencyId:
                          type: string
                        currencyName:
                          type: string
                        currencyEmoji:
                          type:
                            - 'null'
                            - string
                  metadata:
                    type:
                      - 'null'
                      - object
                    description: Custom metadata for this credential
                    additionalProperties: true
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
