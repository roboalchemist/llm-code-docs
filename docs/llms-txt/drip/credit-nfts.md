# Source: https://docs.drip.re/api-reference/web3-activations/credit-nfts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Credit NFTs

> Credit NFTs of a specific activation by a specific currency

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{activationId}/credit
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
  /api/v1/realms/{realmId}/web3/activations/{activationId}/credit:
    post:
      tags:
        - Web3-Activations
      summary: Credit NFTs
      description: Credit NFTs of a specific activation by a specific currency
      parameters:
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                nftIds:
                  type: array
                  items:
                    type: string
                  default: []
                amount:
                  type: number
                currencyId:
                  type: string
                selectionMode:
                  type: string
                  enum:
                    - specific
                    - exclude
                    - all
                  default: all
                  description: >-
                    How to apply the nftIds: 'specific' = only listed, 'exclude'
                    = all except listed, 'all' = all NFTs
              required:
                - amount
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  creditedCount:
                    type: number
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
