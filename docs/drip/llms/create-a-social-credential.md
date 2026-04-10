# Source: https://docs.drip.re/api-reference/credentials/create-a-social-credential.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a social credential

> Create a social credential (Twitter, Discord, etc.) - can be unlinked or linked to an account

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/credentials/social
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
  /api/v1/realms/{realmId}/credentials/social:
    post:
      tags:
        - Credentials
      summary: Create a social credential
      description: >-
        Create a social credential (Twitter, Discord, etc.) - can be unlinked or
        linked to an account
      parameters:
        - schema:
            type: string
          in: path
          name: realmId
          required: true
          description: Realm ID
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - provider
                - providerId
              properties:
                provider:
                  type: string
                  description: >-
                    Social provider name (e.g., twitter, discord, telegram,
                    github, google, facebook, or any custom provider)
                providerId:
                  type: string
                  description: User ID from the social provider
                username:
                  type: string
                  description: Username on the social platform
                accountId:
                  type: string
                  description: >-
                    Optional: Link this credential to an existing account
                    immediately
                metadata:
                  type: object
                  description: Additional metadata
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
                  format:
                    type: string
                  publicIdentifier:
                    type: string
                  oauthProvider:
                    type: string
                  oauthAccountId:
                    type: string
                  isVerified:
                    type: boolean
                  accountId:
                    type: string
                  createdAt:
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
