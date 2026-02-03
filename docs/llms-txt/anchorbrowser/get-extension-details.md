# Source: https://docs.anchorbrowser.io/api-reference/extensions/get-extension-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Extension Details

> Get details of a specific extension by its ID



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/extensions/{id}
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
  /v1/extensions/{id}:
    get:
      tags:
        - Extensions
      summary: Get Extension Details
      description: Get details of a specific extension by its ID
      parameters:
        - name: id
          in: path
          required: true
          description: The ID of the extension to retrieve
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Extension details retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExtensionResponseSchema'
        '404':
          description: Extension not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Unable to get extension
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
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