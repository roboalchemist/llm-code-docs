# Source: https://docs.drip.re/api-reference/realms/get-realm.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Realm

> Get a realm by id

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}
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
  /api/v1/realms/{realmId}:
    get:
      tags:
        - Realms
      summary: Get Realm
      description: Get a realm by id
      parameters:
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
                $ref: '#/components/schemas/Realm'
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
    Realm:
      $ref: '#/components/schemas/Realm'
      nullable: true
      type: object
      required:
        - id
        - name
        - ownerId
        - description
        - subdomain
      additionalProperties: false
      properties:
        id:
          type: string
          description: The unique identifier for the Realm.
          pattern: ^[a-fA-F0-9]{24}$
        activeTokens:
          type: object
          description: Active tokens data.
        analytics:
          type: object
          description: Analytics data.
        extraPerks:
          type: object
          description: Extra perks data.
          additionalProperties: true
        level:
          type: integer
          description: The level of the Realm.
        members:
          type: array
          items:
            $ref: '#/components/schemas/RealmMember'
          description: List of Realm members.
        apiClient:
          $ref: '#/components/schemas/APIClient'
          description: Associated API client.
        name:
          type: string
          description: The name of the Realm.
        ownerId:
          type: string
          description: The owner's ID.
        description:
          type: string
          description: The description of the Realm.
        logo:
          type: string
        banner:
          type: string
        image:
          type: string
        imageBlurHash:
          type: string
        fontMain:
          type: string
        fontHeader:
          type: string
        subdomain:
          type: string
          description: The subdomain of the Realm.
        customDomain:
          type: string
          description: The custom domain of the Realm.
        premiumLevel:
          type: integer
          description: The premium level of the Realm.
        serverId:
          type: string
          description: The server ID.
        subscriptions:
          type: array
          description: List of subscriptions.
        tokenAlias:
          type: string
          description: Token alias.
        wallet:
          type: string
          description: Wallet address.
        whitelabel:
          type: object
          description: Whitelabel data.
        configuration:
          $ref: '#/components/schemas/RealmConfiguration'
          description: Dynamic site configuration
        published:
          type: boolean
        verified:
          type: boolean
        tags:
          type: array
          items:
            type: string
        socialLinks:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
              value:
                type: string
            required:
              - type
              - value
          description: Community social media links
        teamMembers:
          type: array
          items:
            $ref: '#/components/schemas/TeamMember'
          description: List of team members for the Realm.
        createdAt:
          type: string
          format: date-time
          description: The creation timestamp.
        updatedAt:
          type: string
          format: date-time
          description: The last update timestamp.
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
