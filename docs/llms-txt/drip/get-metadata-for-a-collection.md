# Source: https://docs.drip.re/api-reference/web3-data-collections/get-metadata-for-a-collection.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get metadata for a collection

> Get metadata for a collection by its contract address

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/web3-data/collections/{contractAddress}
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
  /api/v1/web3-data/collections/{contractAddress}:
    get:
      tags:
        - Web3-Data-Collections
      summary: Get metadata for a collection
      description: Get metadata for a collection by its contract address
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
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/NFTCollection'
      security:
        - BearerAuth: []
components:
  schemas:
    NFTCollection:
      $ref: '#/components/schemas/NFTCollection'
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        description:
          type: string
        image:
          type: string
        bannerImage:
          type:
            - 'null'
            - string
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
        totalSupply:
          type: number
        floorPrice:
          type:
            - 'null'
            - number
        volume:
          type:
            - 'null'
            - number
            - object
        marketCap:
          type:
            - 'null'
            - number
        nfts:
          type: array
          items:
            $ref: '#/components/schemas/NFTData'
      additionalProperties: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
