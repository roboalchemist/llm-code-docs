# Source: https://docs.drip.re/api-reference/currencies/get-currencies.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Currencies

> Get all currencies in a realm with pagination, search, filtering, and sorting

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/currencies
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
    get:
      tags:
        - Currencies
      summary: Get Currencies
      description: >-
        Get all currencies in a realm with pagination, search, filtering, and
        sorting
      parameters:
        - schema:
            type: number
            minimum: 1
            default: 1
          in: query
          name: page
          required: false
          description: Page number (1-based)
        - schema:
            type: number
            minimum: 1
            maximum: 100
            default: 10
          in: query
          name: limit
          required: false
          description: Number of items per page (max 100)
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: Search query to filter results
        - schema:
            type: string
          in: query
          name: sortBy
          required: false
          description: Field to sort by
        - schema:
            type: string
            enum:
              - asc
              - desc
            default: asc
          in: query
          name: sortOrder
          required: false
          description: Sort order (ascending or descending)
        - schema:
            type: boolean
            default: false
          in: query
          name: includeArchived
          required: false
          description: Include archived currencies in results
        - schema:
            type: string
            enum:
              - active
              - archived
          in: query
          name: status
          required: false
          description: Filter by currency status
        - schema:
            type: boolean
          in: query
          name: isDefault
          required: false
          description: Filter by default currency status
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
                allOf:
                  - $ref: '#/components/schemas/PaginatedResponse'
                  - type: object
                    properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/Currency'
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
    PaginatedResponse:
      $ref: '#/components/schemas/PaginatedResponse'
      type: object
      properties:
        data:
          type: array
          description: Array of items for current page
        meta:
          $ref: '#/components/schemas/OffsetPaginationMeta'
      required:
        - data
        - meta
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
