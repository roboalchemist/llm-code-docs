# Source: https://docs.drip.re/api-reference/web3-data-wallets/get-erc1155-nfts-owned-by-a-wallet.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get ERC1155 NFTs owned by a wallet

> Get ERC1155 NFTs owned by a wallet by its address

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/web3-data/wallets/{walletAddress}/nfts
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
  /api/v1/web3-data/wallets/{walletAddress}/nfts:
    get:
      tags:
        - Web3-Data-Wallets
      summary: Get ERC1155 NFTs owned by a wallet
      description: Get ERC1155 NFTs owned by a wallet by its address
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
            default: 20
          in: query
          name: limit
          required: false
        - schema:
            type: array
            items:
              type: string
          in: query
          name: contractAddresses
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
                      $ref: '#/components/schemas/NFTData'
                  meta:
                    $ref: '#/components/schemas/Meta'
      security:
        - BearerAuth: []
components:
  schemas:
    NFTData:
      $ref: '#/components/schemas/NFTData'
      type: object
      properties:
        id:
          type: string
        contractAddress:
          type: string
        chain:
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
        tokenId:
          type: string
        owner:
          type: string
        name:
          type: string
        description:
          type: string
        image:
          type: string
        attributes:
          type: array
          items:
            $ref: '#/components/schemas/NFTAttribute'
      additionalProperties: false
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
