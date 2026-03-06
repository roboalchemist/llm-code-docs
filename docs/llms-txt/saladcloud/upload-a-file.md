# Source: https://docs.salad.com/reference/s4/upload-a-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a file

*Last Updated: October 04, 2024*


## OpenAPI

````yaml s4 put /organizations/{organization_name}/files/{filename+}
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
    put:
      summary: Upload a file
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
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: The file to upload
                mimeType:
                  type: string
                  description: The MIME type of the file
                sign:
                  type: string
                  description: '"true" to return a signed url'
                signatureExp:
                  type: string
                  description: >-
                    The expiration ttl of the signature in seconds. Default is
                    30 days.
      responses:
        '200':
          description: File uploaded successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  url:
                    type: string
                    format: uri
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