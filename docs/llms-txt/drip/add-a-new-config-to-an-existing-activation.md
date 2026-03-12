# Source: https://docs.drip.re/api-reference/web3-activations-configs/add-a-new-config-to-an-existing-activation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a new config to an existing activation

> Add a new config to an existing WEB3 activation

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{activationId}/configs
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
  /api/v1/realms/{realmId}/web3/activations/{activationId}/configs:
    post:
      tags:
        - Web3-Activations-Configs
      summary: Add a new config to an existing activation
      description: Add a new config to an existing WEB3 activation
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
              required:
                - config
              properties:
                config:
                  $ref: '#/components/schemas/ActivationConfigInput'
        required: true
      responses:
        '201':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Activation'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MessageResponse'
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
      security:
        - BearerAuth: []
components:
  schemas:
    ActivationConfigInput:
      $ref: '#/components/schemas/ActivationConfigInput'
      oneOf:
        - type: object
          properties:
            configType:
              enum:
                - generator
            settings:
              $ref: '#/components/schemas/GeneratorSettingsInput'
            pointsConfig:
              type: array
              items:
                $ref: '#/components/schemas/PointsConfigInput'
              nullable: true
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - multiplier
            settings:
              $ref: '#/components/schemas/MultiplierSettingsInput'
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - passive
            settings:
              type: object
              additionalProperties: true
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - sales
            settings:
              type: object
              properties:
                targetUrl:
                  type: string
              required:
                - targetUrl
              additionalProperties: false
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - listings
            settings:
              type: object
              properties:
                targetUrl:
                  type: string
              required:
                - targetUrl
              additionalProperties: false
          required:
            - configType
            - settings
          additionalProperties: true
    Activation:
      $ref: '#/components/schemas/Activation'
      type: object
      properties:
        id:
          type: string
        activationType:
          type: string
          enum:
            - nft
            - erc1155
            - token
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
        collectionKey:
          type: string
          nullable: true
        displayName:
          type: string
          nullable: true
        configs:
          type: array
          items:
            $ref: '#/components/schemas/ActivationConfig'
        createdAt:
          type: string
          format: date-time
          readOnly: true
        updatedAt:
          type: string
          format: date-time
          readOnly: true
      additionalProperties: false
    MessageResponse:
      $ref: '#/components/schemas/MessageResponse'
      type: object
      properties:
        message:
          type: string
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
