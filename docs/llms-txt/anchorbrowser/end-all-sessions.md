# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/end-all-sessions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# End All Sessions

> Terminates all active browser sessions associated with the provided API key.



## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/sessions/all
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
  /v1/sessions/all:
    delete:
      tags:
        - Browser Sessions
      summary: End All Sessions
      description: >-
        Terminates all active browser sessions associated with the provided API
        key.
      responses:
        '200':
          description: Successfully terminated all active browser sessions.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
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
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````