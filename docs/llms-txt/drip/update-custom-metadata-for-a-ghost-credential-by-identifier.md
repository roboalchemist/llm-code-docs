# Source: https://docs.drip.re/api-reference/credentials/update-custom-metadata-for-a-ghost-credential-by-identifier.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Update custom metadata for a ghost credential by identifier

> Update custom metadata for a ghost credential by identifier

## OpenAPI

````yaml https://api.drip.re/docs/json patch /api/v1/realms/{realmId}/credentials/metadata
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
  /api/v1/realms/{realmId}/credentials/metadata:
    patch:
      tags:
        - Credentials
      summary: Update custom metadata for a ghost credential by identifier
      description: Update custom metadata for a ghost credential by identifier
      parameters:
        - schema:
            type: string
            enum:
              - twitter-id
              - discord-id
              - wallet
              - email
              - custom
          in: query
          name: type
          required: true
          description: Type of credential identifier
        - schema:
            type: string
          in: query
          name: value
          required: true
          description: >-
            Credential value (email address, wallet address, discord ID, twitter
            ID, or custom ID)
        - schema:
            type: string
          in: query
          name: source
          required: false
          description: >-
            Required for custom type. The source/provider name (e.g.,
            'shopify-customer-id', 'internal-user-id')
        - schema:
            type: string
          in: path
          name: realmId
          required: true
          description: Realm ID
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - metadata
              properties:
                metadata:
                  type: object
                  description: Custom metadata object to store for this credential
        required: true
      responses:
        '204':
          description: Default Response
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
