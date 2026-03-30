# Source: https://docs.drip.re/api-reference/currencies/create-currency.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Currency

> Create a new currency in a realm

## OpenAPI

````yaml https://api.drip.re/docs/json post /api/v1/realms/{realmId}/currencies
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
  /api/v1/realms/{realmId}/currencies:
    post:
      tags:
        - Currencies
      summary: Create Currency
      description: Create a new currency in a realm
      parameters:
        - schema:
            type: string
            pattern: ^[0-9a-fA-F]{24}$
          in: path
          name: realmId
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                emoji:
                  type: string
                  nullable: true
                customEmojiUrl:
                  type: string
                  nullable: true
                metadata:
                  type: object
                default:
                  type: boolean
              required:
                - name
        required: true
      responses:
        '201':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Currency'
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
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
    Currency:
      $ref: '#/components/schemas/Currency'
      type: object
      nullable: true
      required:
        - id
        - name
      additionalProperties: false
      properties:
        id:
          type: string
          description: The unique identifier for the currency.
          format: objectId
        realmId:
          type: string
          description: The ID of the realm these currencies belong to.
          format: objectId
        name:
          type: string
          description: The name of the currency.
        emoji:
          type: string
          description: The emoji associated with these currencies.
          nullable: true
        customEmojiUrl:
          type: string
          description: The custom emoji URL associated with these currencies.
          nullable: true
        default:
          type: boolean
          description: Whether this is the default currency for the realm.
          default: false
        metadata:
          type: object
          description: Additional metadata for the currency.
          additionalProperties: true
        scopes:
          type: array
          items:
            type: string
          description: The scopes associated with this currency.
        archived:
          type: boolean
          description: Whether this currency is archived.
          default: false
        archivedAt:
          type: string
          format: date-time
          description: The timestamp when this currency was archived.
          nullable: true
        ownership:
          type: string
          enum:
            - OWNED
            - SHARED
          description: >-
            Whether this currency is owned by the realm or shared from another
            realm.
          nullable: true
        shareStatus:
          type: string
          enum:
            - PENDING
            - ACCEPTED
            - REJECTED
          description: >-
            Status of the currency if it is shared. Defaults to 'PENDING' until
            the child realm accepts.
          nullable: true
        parentRealmId:
          type: string
          format: objectId
          description: The ID of the realm that owns this currency if shared.
          nullable: true
        parentRealmName:
          type: string
          description: The name of the parent realm that owns this currency if shared.
          nullable: true
        permissions:
          type: array
          items:
            type: string
          description: >-
            Shared currency permissions granted to the child realm (e.g.,
            ['spend', 'earn', 'view']).
          nullable: true
        createdAt:
          type: string
          format: date-time
          description: The creation timestamp of the currency.
        updatedAt:
          type: string
          format: date-time
          description: The last update timestamp of the currency.
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
