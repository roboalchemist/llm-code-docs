# Source: https://docs.drip.re/api-reference/web3-activations-members/claim-web3-balance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Claim Web3 Balance

> Claim Web3 Balance of a specific member of a specific activation

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/members/{dripId}/claim
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
  /api/v1/realms/{realmId}/web3/members/{dripId}/claim:
    post:
      tags:
        - Web3-Activations-Members
      summary: Claim Web3 Balance
      description: Claim Web3 Balance of a specific member of a specific activation
      parameters:
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                claimType:
                  type: string
                  enum:
                    - all
                    - nft
                    - tokens
                    - erc1155
                activationId:
                  type: string
                nftIds:
                  type: array
                  items:
                    type: string
              required:
                - claimType
        required: true
      responses:
        '204':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessWithNoContentResponse'
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
      security:
        - BearerAuth: []
components:
  schemas:
    SuccessWithNoContentResponse:
      $ref: '#/components/schemas/SuccessWithNoContentResponse'
      type: object
      properties: {}
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
