# Source: https://docs.drip.re/api-reference/realm-members/get-realm-member-leaderboard.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Realm Member Leaderboard

> Get the leaderboard of a realm by their currency id

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/members/leaderboard
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
  /api/v1/realms/{realmId}/members/leaderboard:
    get:
      tags:
        - Realm-Members
      summary: Get Realm Member Leaderboard
      description: Get the leaderboard of a realm by their currency id
      parameters:
        - schema:
            type: string
          in: query
          name: currencyId
          required: false
        - schema:
            type: string
          in: query
          name: take
          required: false
        - schema:
            type: string
          in: query
          name: after
          required: false
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: realmId
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
                      type: object
                      properties:
                        accountId:
                          type: string
                        username:
                          type: string
                        displayName:
                          type: string
                        imageUrl:
                          type: string
                        balance:
                          type: integer
                        rank:
                          type: integer
                  meta:
                    $ref: '#/components/schemas/Meta'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenResponse'
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
