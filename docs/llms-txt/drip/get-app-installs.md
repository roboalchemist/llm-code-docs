# Source: https://docs.drip.re/api-reference/apps/get-app-installs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get App Installs

> Get paginated list of realms that have installed this app

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/apps/{appId}/installs
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
  /api/v1/realms/{realmId}/apps/{appId}/installs:
    get:
      tags:
        - Apps
      summary: Get App Installs
      description: Get paginated list of realms that have installed this app
      parameters:
        - schema:
            type: integer
            minimum: 1
            default: 1
          in: query
          name: page
          required: false
          description: Page number
        - schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: limit
          required: false
          description: Number of items per page
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: Search term for realm name or description
        - schema:
            type: string
            enum:
              - createdAt
              - updatedAt
              - realmName
              - memberCount
            default: createdAt
          in: query
          name: sortBy
          required: false
          description: Field to sort by
        - schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
          in: query
          name: sortOrder
          required: false
          description: Sort order
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: realmId
          required: true
          description: Realm ID
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: appId
          required: true
          description: App ID
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
                        id:
                          type: string
                        realmId:
                          type: string
                        appId:
                          type: string
                        approvedScopes:
                          type: array
                          items:
                            type: string
                        platformType:
                          type: string
                          nullable: true
                        platformId:
                          type: string
                          nullable: true
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                        realm:
                          type: object
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            description:
                              type: string
                              nullable: true
                            imageUrl:
                              type: string
                              nullable: true
                            ownerId:
                              type: string
                            owner:
                              type: object
                              properties:
                                id:
                                  type: string
                                displayName:
                                  type: string
                                  nullable: true
                                username:
                                  type: string
                                  nullable: true
                                imageUrl:
                                  type: string
                                  nullable: true
                            createdAt:
                              type: string
                              format: date-time
                            memberCount:
                              type: integer
                  meta:
                    type: object
                    properties:
                      total:
                        type: integer
                      page:
                        type: integer
                      limit:
                        type: integer
                      totalPages:
                        type: integer
                      hasNextPage:
                        type: boolean
                      hasPreviousPage:
                        type: boolean
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API Key
      description: API Key

````

Built with [Mintlify](https://mintlify.com).
