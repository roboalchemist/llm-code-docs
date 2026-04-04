# Source: https://docs.salad.com/reference/s4/sign-a-file-and-return-a-signed-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sign a file and return a signed URL

*Last Updated: October 04, 2024*


## OpenAPI

````yaml s4 post /organizations/{organization_name}/file_tokens/{filename+}
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
  /organizations/{organization_name}/file_tokens/{filename+}:
    post:
      summary: Sign a file and return a signed URL
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
          application/json:
            schema:
              type: object
              properties:
                method:
                  type: string
                  example: GET
                  description: >-
                    The HTTP method to sign the URL for. Currently only supports
                    GET
                exp:
                  type: string
                  example: '3600'
                  description: The expiration ttl of the signed URL in seconds
      responses:
        '200':
          description: Signed URL generated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  url:
                    type: string
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