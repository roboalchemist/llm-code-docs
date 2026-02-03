# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/rest-reference/endpoint/regions-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Regions

> Retrieve a list of all available regions for deploying agents and storing secrets.



## OpenAPI

````yaml GET /regions
openapi: 3.0.0
info:
  title: Pipecat Cloud - List Regions
  version: 1.0.0
  description: List available regions via Pipecat Cloud API
servers:
  - url: https://api.pipecat.daily.co/v1
    description: API server
security: []
paths:
  /regions:
    get:
      summary: List available regions
      description: >-
        Retrieve a list of all regions available for deploying agents and
        storing secrets. This endpoint can be accessed using either Clerk
        authentication or a Private API key.
      operationId: listRegions
      responses:
        '200':
          description: List of available regions
          content:
            application/json:
              schema:
                type: object
                properties:
                  regions:
                    type: array
                    items:
                      $ref: '#/components/schemas/Region'
              example:
                regions:
                  - code: us-west
                    display_name: US West (Oregon)
                  - code: us-east
                    display_name: US East (Virginia)
                  - code: eu-central
                    display_name: Europe (Frankfurt)
                  - code: ap-south
                    display_name: Asia Pacific (Mumbai)
        '401':
          description: Unauthorized - Invalid or missing authentication
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Unauthorized
                code: UNAUTHORIZED
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Internal server error
                code: INTERNAL_SERVER_ERROR
      security:
        - PrivateKeyAuth: []
components:
  schemas:
    Region:
      type: object
      properties:
        code:
          type: string
          description: Region code identifier (e.g., 'us-west', 'eu-central')
          example: us-west
        display_name:
          type: string
          description: Human-readable region name
          example: US West (Oregon)
      required:
        - code
        - display_name
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Error code
  securitySchemes:
    PrivateKeyAuth:
      type: http
      scheme: bearer
      description: >-
        Authentication using a Pipecat Cloud Private API token.


        Generate a Private API key from your Dashboard (Settings > API Keys >
        Private > Create key) and include it as a Bearer token in the
        Authorization header.

````