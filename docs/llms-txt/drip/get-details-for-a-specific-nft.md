# Source: https://docs.drip.re/api-reference/web3-data-collections/get-details-for-a-specific-nft.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get details for a specific NFT

> Get details for a specific NFT by its contract address and token id

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}/nfts/{tokenId}
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
  /api/v1/web3-data/collections/{contractAddress}/nfts/{tokenId}:
    get:
      tags:
        - Web3-Data-Collections
      summary: Get details for a specific NFT
      description: Get details for a specific NFT by its contract address and token id
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
          name: cache
          required: false
        - schema:
            type: string
          in: path
          name: contractAddress
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
                    $ref: '#/components/schemas/NFTData'
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
