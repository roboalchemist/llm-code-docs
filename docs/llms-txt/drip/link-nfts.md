# Source: https://docs.drip.re/api-reference/web3-activations-members/link-nfts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Link NFTs

> Link NFTs of a specific member of a specific activation to another activation

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/members/{dripId}/nfts/link
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
  /api/v1/realms/{realmId}/web3/members/{dripId}/nfts/link:
    post:
      tags:
        - Web3-Activations-Members
      summary: Link NFTs
      description: >-
        Link NFTs of a specific member of a specific activation to another
        activation
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
                activationIds:
                  type: array
                  items:
                    type: string
                  description: >-
                    Optional array of generator activation IDs. If not provided,
                    all activations will be linked.
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
