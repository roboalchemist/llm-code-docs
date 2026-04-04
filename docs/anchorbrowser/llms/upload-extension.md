# Source: https://docs.anchorbrowser.io/api-reference/extensions/upload-extension.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Extension

> Upload a new browser extension as a ZIP file. The extension will be validated and stored for use in browser sessions.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/extensions
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
    post:
      tags:
        - Extensions
      summary: Upload Extension
      description: >-
        Upload a new browser extension as a ZIP file. The extension will be
        validated and stored for use in browser sessions.
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - name
                - file
              properties:
                name:
                  type: string
                  description: User-friendly name for the extension (1-255 characters)
                file:
                  type: string
                  format: binary
                  description: ZIP file containing the browser extension
      responses:
        '200':
          description: Extension uploaded successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/ExtensionResponseSchema'
        '400':
          description: Invalid request or extension validation failed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Unable to upload extension
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