# Source: https://docs.salad.com/reference/s4/download-a-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download a file

*Last Updated: October 04, 2024*


## OpenAPI

````yaml s4 get /organizations/{organization_name}/files/{filename+}
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
  /organizations/{organization_name}/files/{filename+}:
    get:
      summary: Download a file
      parameters:
        - name: organization_name
          in: path
          required: true
          schema:
            type: string
        - name: filename+
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: File retrieved successfully
          content:
            '*/*':
              schema:
                type: string
                format: binary
        '404':
          description: File not found
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