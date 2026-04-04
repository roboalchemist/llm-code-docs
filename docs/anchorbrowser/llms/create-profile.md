# Source: https://docs.anchorbrowser.io/api-reference/profiles/create-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Profile

> Creates a new profile from a browser session. A Profile stores cookies, local storage, and cache.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/profiles
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
  /v1/profiles:
    post:
      tags:
        - Profiles
      summary: Create Profile
      description: >-
        Creates a new profile from a browser session. A Profile stores cookies,
        local storage, and cache.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProfileRequestSchema'
      responses:
        '200':
          description: Profile created successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '400':
          description: Invalid request or input.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Session not found or unreachable.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '409':
          description: Profile name already exists.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '501':
          description: Feature not implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ProfileRequestSchema:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: The name of the profile.
        description:
          type: string
          description: A description of the profile.
        source:
          type: string
          description: >-
            The source of the profile data. currently only `session` is
            supported.
          enum:
            - session
        session_id:
          type: string
          format: uuid
          description: >-
            The browser session ID is required if the source is set to
            `session`. The browser session must be running, and the profile will
            be stored once the browser session terminates.
        dedicated_sticky_ip:
          type: boolean
          description: >-
            Whether to use a dedicated sticky IP for this profile. Defaults to
            false.
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