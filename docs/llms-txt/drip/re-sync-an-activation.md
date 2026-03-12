# Source: https://docs.drip.re/api-reference/web3-activations/re-sync-an-activation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Re-sync an activation

> Re-sync a WEB3 activation for a realm, which will re-sync all the NFT data and ownership

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/web3/activations/{activationId}/sync
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
  /api/v1/realms/{realmId}/web3/activations/{activationId}/sync:
    post:
      tags:
        - Web3-Activations
      summary: Re-sync an activation
      description: >-
        Re-sync a WEB3 activation for a realm, which will re-sync all the NFT
        data and ownership
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
                  syncedCount:
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
      security:
        - BearerAuth: []
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
