# Source: https://docs.anchorbrowser.io/api-reference/profiles/delete-profile.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Profile

> Deletes an existing profile by its name.



## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/profiles/{name}
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
    delete:
      tags:
        - Profiles
      summary: Delete Profile
      description: Deletes an existing profile by its name.
      parameters:
        - name: name
          in: path
          required: true
          description: The name of the profile to delete.
          schema:
            type: string
      responses:
        '200':
          description: Profile deleted successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Profile not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Unable to delete the profile due to an unexpected error.
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