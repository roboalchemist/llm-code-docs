# Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/delete-identity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Identity

> Deletes an existing identity.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/identities/{identityId}
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
  /v1/identities/{identityId}:
    delete:
      tags:
        - Identities (Early Availability)
      summary: Delete Identity
      description: >
        Deletes an existing identity.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: identityId
          in: path
          required: true
          description: The ID of the identity to delete
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Identity deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteIdentityResponse'
        '404':
          description: Identity not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to delete identity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    DeleteIdentityResponse:
      type: object
      properties:
        message:
          type: string
          description: Deletion result message
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