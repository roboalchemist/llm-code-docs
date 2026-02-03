# Source: https://docs.anchorbrowser.io/api-reference/extensions/list-extensions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Extensions

> Get all extensions for the authenticated user



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/extensions
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/extensions:
    get:
      tags:
        - Extensions
      summary: List Extensions
      description: Get all extensions for the authenticated user
      responses:
        '200':
          description: List of user extensions retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExtensionListResponse'
        '500':
          description: Unable to list extensions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ExtensionListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/ExtensionResponseSchema'
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
    ExtensionResponseSchema:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the extension
        name:
          type: string
          description: Extension name
        manifest:
          $ref: '#/components/schemas/ExtensionManifest'
        createdAt:
          type: string
          format: date-time
          description: Timestamp when the extension was created
        updatedAt:
          type: string
          format: date-time
          description: Timestamp when the extension was last updated
    ExtensionManifest:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        manifest_version:
          type: integer
        description:
          type: string
        permissions:
          type: array
          items:
            type: string
      additionalProperties: true
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````