# Source: https://docs.drip.re/api-reference/web3-data-wallets/get-token-balances-for-a-wallet.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get token balances for a wallet

> Get token balances for a wallet by its address

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/web3-data/wallets/{walletAddress}/token-balances
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
  /api/v1/web3-data/wallets/{walletAddress}/token-balances:
    get:
      tags:
        - Web3-Data-Wallets
      summary: Get token balances for a wallet
      description: Get token balances for a wallet by its address
      parameters:
        - schema:
            type: string
            enum:
              - ethereum
              - polygon
              - arbitrum
              - optimism
              - base
              - zksync
              - starknet
              - scroll
              - polygonZkEVM
              - arbitrumNova
              - avalanche
              - gnosis
              - opbnb
              - metis
              - astar
              - linea
              - mantle
              - berachain
              - flow
              - crossfi
              - soneium
              - worldchain
              - rootstock
              - shape
              - unichain
              - apechain
              - geist
              - lens
              - abstract
              - lumia
              - ink
              - zetachain
              - blast
              - sonic
              - zora
              - settlus
              - solana
              - bsc
            default: ethereum
          in: query
          name: chain
          required: false
        - schema:
            type: string
          in: query
          name: cursor
          required: false
        - schema:
            type: number
            default: 100
          in: query
          name: limit
          required: false
        - schema:
            type: string
          in: path
          name: walletAddress
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
                        token:
                          type: object
                          properties:
                            address:
                              type: string
                            name:
                              type: string
                            symbol:
                              type: string
                            decimals:
                              type: number
                            chain:
                              type: string
                            logo:
                              type:
                                - 'null'
                                - string
                            type:
                              type: string
                          additionalProperties: true
                        balance:
                          type: string
                        balanceFormatted:
                          type: string
                        balanceUsd:
                          type:
                            - 'null'
                            - number
                      additionalProperties: true
                  meta:
                    $ref: '#/components/schemas/Meta'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  error:
                    type: string
      security:
        - BearerAuth: []
components:
  schemas:
    Meta:
      $ref: '#/components/schemas/Meta'
      type: object
      properties:
        hasNextPage:
          type: boolean
          default: false
        hasPreviousPage:
          type: boolean
          default: false
        startCursor:
          type: string
        endCursor:
          type: string
        totalCount:
          type: number
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
