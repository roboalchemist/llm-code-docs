# Source: https://docs.drip.re/api-reference/apps/search-app-authorized-realms.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Search App Authorized Realms

> Search for realms that an app is authorized to access. Can only be used by the app itself.

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/apps/{appId}/authorized-realms/search
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
  /api/v1/apps/{appId}/authorized-realms/search:
    get:
      tags:
        - Apps
      summary: Search App Authorized Realms
      description: >-
        Search for realms that an app is authorized to access. Can only be used
        by the app itself.
      parameters:
        - schema:
            type: string
            enum:
              - realmId
              - platformId
          in: query
          name: type
          required: true
        - schema:
            type: string
          in: query
          name: values
          required: true
          description: Comma-separated list of values to search for
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: take
          required: false
        - schema:
            type: string
          in: query
          name: from
          required: false
          description: Cursor to start from
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: appId
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
                      $ref: '#/components/schemas/AppAuthorizedRealm'
                  meta:
                    $ref: '#/components/schemas/Meta'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
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
    AppAuthorizedRealm:
      $ref: '#/components/schemas/AppAuthorizedRealm'
      type: object
      nullable: true
      required:
        - id
        - realmId
        - platformType
        - platformId
        - createdAt
        - updatedAt
      additionalProperties: false
      properties:
        id:
          type: string
        realmId:
          type: string
        platformType:
          type: string
        platformId:
          type: string
        approvedScopes:
          type: array
          items:
            type: string
        createdAt:
          type: string
        updatedAt:
          type: string
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
