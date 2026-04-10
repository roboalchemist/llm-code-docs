# Source: https://docs.drip.re/api-reference/credentials/create-a-wallet-credential.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a wallet credential

> Create a wallet credential - can be unlinked or linked to an account

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/credentials/wallet
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
  /api/v1/realms/{realmId}/credentials/wallet:
    post:
      tags:
        - Credentials
      summary: Create a wallet credential
      description: Create a wallet credential - can be unlinked or linked to an account
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
                - address
                - chain
              properties:
                address:
                  type: string
                  description: Wallet address
                chain:
                  type: string
                  description: Blockchain name (e.g., ethereum, polygon, solana, base)
                walletProvider:
                  type: string
                  description: Wallet provider (e.g., metamask, coinbase, phantom)
                walletName:
                  type: string
                  description: Wallet display name
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
                  address:
                    type: string
                  chain:
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
