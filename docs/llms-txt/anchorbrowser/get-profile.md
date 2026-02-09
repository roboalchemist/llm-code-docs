# Source: https://docs.anchorbrowser.io/api-reference/profiles/get-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Profile

> Retrieves details of a specific profile by its name.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/profiles/{name}
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
  /v1/profiles/{name}:
    get:
      tags:
        - Profiles
      summary: Get Profile
      description: Retrieves details of a specific profile by its name.
      parameters:
        - name: name
          in: path
          required: true
          description: The name of the profile to retrieve.
          schema:
            type: string
      responses:
        '200':
          description: Profile details retrieved successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProfileResponse'
        '401':
          description: Invalid API Key.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Profile not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Unable to retrieve profile due to an unexpected error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ProfileResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ProfileResponseSchema'
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
    ProfileResponseSchema:
      type: object
      properties:
        name:
          type: string
          description: The name of the profile.
        description:
          type: string
          description: A description of the profile.
        source:
          type: string
          description: The source of the profile data.
          enum:
            - session
        session_id:
          type: string
          format: uuid
          description: The browser session ID used to create this profile, if applicable.
        status:
          type: string
          description: The current status of the profile.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the profile was created.
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````