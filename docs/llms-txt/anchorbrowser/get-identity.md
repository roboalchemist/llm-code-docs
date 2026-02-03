# Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/get-identity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Identity

> Retrieves details of a specific identity by its ID.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/identities/{identityId}
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
    get:
      tags:
        - Identities (Early Availability)
      summary: Get Identity
      description: >
        Retrieves details of a specific identity by its ID.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: identityId
          in: path
          required: true
          description: The ID of the identity to retrieve
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Identity details retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetIdentityResponse'
        '404':
          description: Identity not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to get identity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    GetIdentityResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the identity
        name:
          type: string
          description: Name of the identity
        source:
          type: string
          description: Source URL for the identity
        status:
          type: string
          enum:
            - pending
            - validated
            - failed
          description: Status of the identity
        metadata:
          type: object
          additionalProperties: true
          description: Metadata associated with the identity
        created_at:
          type: string
          format: date-time
          description: Timestamp when the identity was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the identity was last updated
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