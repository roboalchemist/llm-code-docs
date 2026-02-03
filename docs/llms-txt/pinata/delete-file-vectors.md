# Source: https://docs.pinata.cloud/api-reference/endpoint/delete-file-vectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete File Vectors

> `org:write`




## OpenAPI

````yaml delete /vectorize/files/{file_id}
openapi: 3.0.0
info:
  title: Private IPFS API
  version: 1.0.0
servers:
  - url: https://uploads.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /vectorize/files/{file_id}:
    delete:
      tags:
        - Private Files
      summary: Delete File Vectors
      description: |
        `org:write`
      parameters:
        - schema:
            type: string
            format: uuid
          required: true
          name: file_id
          in: path
      responses:
        '200':
          description: Vectorize File Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                required:
                  - success
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````