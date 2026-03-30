# Source: https://docs.salad.com/reference/s4/list-all-files-that-belong-to-the-organization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all files

*Last Updated: October 04, 2024*


## OpenAPI

````yaml s4 get /organizations/{organization_name}/files
openapi: 3.0.0
info:
  title: Salad Simple Storage Service
  version: 1.1.0
servers:
  - url: https://storage-api.salad.com
security:
  - ApiKeyAuth: []
  - BearerAuth: []
paths:
  /organizations/{organization_name}/files:
    get:
      summary: List all files
      parameters:
        - name: organization_name
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: List of files retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  files:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          format: uri
                        mimeType:
                          type: string
                        size:
                          type: integer
                        uploaded:
                          type: string
                          format: date-time
      security:
        - ApiKeyAuth: []
        - BearerAuth: []
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````