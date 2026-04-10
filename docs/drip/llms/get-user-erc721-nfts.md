# Source: https://docs.drip.re/api-reference/web3-activations-members/get-user-erc721-nfts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user ERC721 NFTs

> Get user ERC721 NFTs with pagination by a specific member of a specific activation

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/members/{dripId}/nfts
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
  /api/v1/realms/{realmId}/web3/members/{dripId}/nfts:
    get:
      tags:
        - Web3-Activations-Members
      summary: Get user ERC721 NFTs
      description: >-
        Get user ERC721 NFTs with pagination by a specific member of a specific
        activation
      parameters:
        - schema:
            type: number
          in: query
          name: limit
          required: false
        - schema:
            type: string
          in: query
          name: cursor
          required: false
        - schema:
            type: string
          in: query
          name: activationId
          required: false
        - schema:
            type: boolean
          in: query
          name: includeBalances
          required: false
        - schema:
            type: boolean
          in: query
          name: includeAttributes
          required: false
        - schema:
            type: string
          in: path
          name: realmId
          required: true
        - schema:
            type: string
          in: path
          name: dripId
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
                      $ref: '#/components/schemas/ActivationNFTData'
                  meta:
                    type: object
                    properties:
                      totalCount:
                        type: number
                      hasNextPage:
                        type: boolean
                      nextCursor:
                        type: string
                    additionalProperties: true
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
