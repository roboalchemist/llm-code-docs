# Source: https://docs.anchorbrowser.io/api-reference/extensions/delete-extension.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Extension

> Delete an extension and remove it from storage



## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/extensions/{id}
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
    delete:
      tags:
        - Extensions
      summary: Delete Extension
      description: Delete an extension and remove it from storage
      parameters:
        - name: id
          in: path
          required: true
          description: The ID of the extension to delete
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Extension deleted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Extension not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Unable to delete extension
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            status:
              type: string
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
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````