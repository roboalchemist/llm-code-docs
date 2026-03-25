# Source: https://docs.drip.re/api-reference/credentials/delete-a-non-verified-credential-linked-or-unlinked-only-if-no-balances-exist.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a non-verified credential (linked or unlinked, only if no balances exist)

> Delete a non-verified credential (linked or unlinked, only if no balances exist)

## OpenAPI

````yaml https://api.drip.re/docs/json delete /api/v1/realms/{realmId}/credentials/
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
  /api/v1/realms/{realmId}/credentials/:
    delete:
      tags:
        - Credentials
      summary: >-
        Delete a non-verified credential (linked or unlinked, only if no
        balances exist)
      description: >-
        Delete a non-verified credential (linked or unlinked, only if no
        balances exist)
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
          description: Credential value
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
        '204':
          description: Credential successfully deleted
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
