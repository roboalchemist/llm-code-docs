# Source: https://docs.anchorbrowser.io/api-reference/profiles/list-profiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Profiles

> Fetches all stored profiles.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/profiles
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
    get:
      tags:
        - Profiles
      summary: List Profiles
      description: Fetches all stored profiles.
      responses:
        '200':
          description: List of user profiles retrieved successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProfileListResponse'
        '500':
          description: Unable to list user profiles due to an unexpected error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ProfileListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            count:
              type: integer
              description: Total number of profiles
            items:
              type: array
              items:
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