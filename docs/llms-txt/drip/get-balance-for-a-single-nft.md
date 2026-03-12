# Source: https://docs.drip.re/api-reference/web3-activations/get-balance-for-a-single-nft.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get balance for a single NFT

> Get balance for a single NFT of a specific activation

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/activations/{activationId}/nfts/{tokenId}/balance
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
  /api/v1/realms/{realmId}/web3/activations/{activationId}/nfts/{tokenId}/balance:
    get:
      tags:
        - Web3-Activations
      summary: Get balance for a single NFT
      description: Get balance for a single NFT of a specific activation
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
            type: boolean
            default: false
          in: query
          name: includeNft
          required: false
        - schema:
            type: string
          in: path
          name: realmId
          required: true
        - schema:
            type: string
          in: path
          name: activationId
          required: true
        - schema:
            type: string
          in: path
          name: tokenId
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
                    allOf:
                      - $ref: '#/components/schemas/ActivationNFTData'
                      - type: object
                        properties:
                          balances:
                            type: array
                            items:
                              $ref: '#/components/schemas/ActivationNFTBalancesData'
                        required:
                          - balances
                        additionalProperties: false
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenResponse'
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundResponse'
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    ActivationNFTData:
      $ref: '#/components/schemas/ActivationNFTData'
      type: object
      allOf:
        - $ref: '#/components/schemas/NFTData'
      properties:
        balances:
          type: array
          items:
            $ref: '#/components/schemas/ActivationNFTBalancesData'
      additionalProperties: false
    ActivationNFTBalancesData:
      $ref: '#/components/schemas/ActivationNFTBalancesData'
      type: object
      properties:
        realmPointId:
          type: string
        balance:
          type: number
        lastCredited:
          type: string
          format: date-time
        lastCreditedBy:
          type: number
        pointMetadata:
          type:
            - object
            - 'null'
      additionalProperties: false
    ForbiddenResponse:
      $ref: '#/components/schemas/ForbiddenResponse'
      description: Forbidden response, user is not authorized to access the resource
      type: object
      required:
        - error
        - message
      properties:
        error:
          type: string
          enum:
            - Forbidden
          description: Error type
        message:
          type: string
          description: Error message
    NotFoundResponse:
      $ref: '#/components/schemas/NotFoundResponse'
      type: object
      description: Not found response, resource not found
      required:
        - error
        - message
      properties:
        error:
          type: string
          enum:
            - Not Found
          description: Error type
        message:
          type: string
          description: Error message
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
