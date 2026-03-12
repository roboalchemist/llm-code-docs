# Source: https://docs.drip.re/api-reference/realm-members/list-realm-members.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# List Realm Members

> List members of a realm with optional pagination, search, and sorting.

## OpenAPI

````yaml https://api.drip.re/docs/json get /api/v1/realms/{realmId}/members/
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
  /api/v1/realms/{realmId}/members/:
    get:
      tags:
        - Realm-Members
      summary: List Realm Members
      description: List members of a realm with optional pagination, search, and sorting.
      parameters:
        - schema:
            type: string
          in: query
          name: page
          required: false
          description: Page number (1-based)
        - schema:
            type: string
          in: query
          name: limit
          required: false
          description: Number of items per page
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: Search term for username, displayName, or email
        - schema:
            type: string
            enum:
              - username
              - displayName
              - firstVisit
              - lastVisit
              - updatedAt
              - lastActive
              - createdAt
              - joinedAt
              - name
              - user
              - status
          in: query
          name: sortBy
          required: false
          description: Field to sort by
        - schema:
            type: string
            enum:
              - asc
              - desc
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
                      $ref: '#/components/schemas/RealmMember'
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
    RealmMember:
      $ref: '#/components/schemas/RealmMember'
      type: object
      required:
        - id
        - joinedAt
      additionalProperties: false
      properties:
        id:
          type: string
          description: The unique identifier for the user's account.
          format: objectId
        realmMemberId:
          type: string
          description: The unique identifier for this realm membership.
          format: objectId
        dynamicId:
          type: string
          description: A unique dynamic identifier for the user.
        username:
          type: string
          description: The username of the user.
        displayName:
          type: string
          description: The display name of the user.
        imageUrl:
          type: string
          description: The URL of the user's profile image.
        email:
          type: string
          description: The email address of the user.
        about:
          type: string
          description: A short bio for the user.
        alias:
          type: string
          description: An alias for the user.
        firstVisit:
          type: string
          format: date-time
          description: The date and time of the user's first visit to the platform.
        lastVisit:
          type: string
          format: date-time
          description: The date and time of the user's last visit to the platform.
        lastActive:
          type: string
          format: date-time
          description: The date and time of the user's last active visit to the platform.
        joinedAt:
          type: string
          format: date-time
          description: The date and time when the user joined this realm.
        hasRealmActivity:
          type: boolean
          description: Whether the user has any activity in this realm (is a member).
        referralId:
          type: string
          description: A unique identifier for the user's referral.
          format: objectId
        credentials:
          type: array
          description: Credentials associated with the user.
          items:
            type: object
            properties:
              format:
                type: string
              publicIdentifier:
                type: string
              oauthProvider:
                type: string
              oauthAccountId:
                type: string
              oauthAccountPhotos:
                type: array
                items:
                  type: string
                description: Profile photos from OAuth providers
              oauthUsername:
                type: string
                description: Username from OAuth providers
              walletName:
                type: string
                description: Name of the wallet (e.g., metamask, abstract)
              chain:
                type: string
                description: Blockchain chain identifier (e.g., eip155)
        balances:
          type: array
          items:
            type: object
            properties:
              balance:
                type: integer
                description: The balance amount for this point type.
              currencyId:
                type: string
                description: The unique identifier for the realm point.
                format: objectId
              currencyName:
                type: string
                description: The name of the realm point.
              currencyEmoji:
                type: string
                description: The emoji associated with the realm point.
            required:
              - balance
          description: List of point balances for the user in this realm.
        teamMembership:
          type: object
          properties:
            id:
              type: string
              description: The unique identifier for the team membership.
              format: objectId
            role:
              type: string
              description: The role of the user in the team.
            scopes:
              type: array
              items:
                type: string
              description: The scopes (permissions) assigned to this team member.
          description: The user's team membership information for this realm, if any.
        notes:
          type:
            - 'null'
            - string
          description: Admin notes for this member (only visible to team members).
        metadata:
          type:
            - 'null'
            - object
          description: Custom metadata for this member.
          additionalProperties: true
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
