# Source: https://docs.drip.re/api-reference/web3-activations-configs/get-all-configs-for-a-given-activation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all configs for a given activation

> Get all configs for a given WEB3 activation

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/web3/activations/{activationId}/configs
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
    get:
      tags:
        - Web3-Activations-Configs
      summary: Get all configs for a given activation
      description: Get all configs for a given WEB3 activation
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
                      $ref: '#/components/schemas/ActivationConfig'
                  meta:
                    $ref: '#/components/schemas/Meta'
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
    ActivationConfig:
      $ref: '#/components/schemas/ActivationConfig'
      oneOf:
        - type: object
          properties:
            configType:
              enum:
                - generator
            id:
              type: string
            settings:
              $ref: '#/components/schemas/GeneratorSettings'
            pointsConfig:
              type: array
              items:
                $ref: '#/components/schemas/PointsConfig'
              nullable: true
            createdAt:
              type: string
              format: date-time
            updatedAt:
              type: string
              format: date-time
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - multiplier
            id:
              type: string
            settings:
              $ref: '#/components/schemas/MultiplierSettings'
            pointsConfig:
              type: array
              items:
                $ref: '#/components/schemas/PointsConfig'
              nullable: true
            createdAt:
              type: string
              format: date-time
            updatedAt:
              type: string
              format: date-time
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - passive
            id:
              type: string
            settings:
              type: object
              additionalProperties: true
            pointsConfig:
              type: array
              items:
                $ref: '#/components/schemas/PointsConfig'
              nullable: true
            createdAt:
              type: string
              format: date-time
            updatedAt:
              type: string
              format: date-time
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - sales
            id:
              type: string
            settings:
              type: object
              properties:
                targetUrl:
                  type: string
                webhookId:
                  type: string
                  nullable: true
              additionalProperties: true
            createdAt:
              type: string
              format: date-time
            updatedAt:
              type: string
              format: date-time
          required:
            - configType
            - settings
          additionalProperties: true
        - type: object
          properties:
            configType:
              enum:
                - listings
            id:
              type: string
            settings:
              type: object
              properties:
                targetUrl:
                  type: string
                webhookId:
                  type: string
                  nullable: true
              additionalProperties: true
            createdAt:
              type: string
              format: date-time
            updatedAt:
              type: string
              format: date-time
          required:
            - configType
            - settings
          additionalProperties: true
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
