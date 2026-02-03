# Source: https://docs.pinata.cloud/api-reference/endpoint/create-signed-upload-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Signed Upload URL

> `org:files:write`




## OpenAPI

````yaml pinata-api-v3-uploads.yaml post /files/sign
openapi: 3.0.0
info:
  title: Private IPFS API
  version: 1.0.0
servers:
  - url: https://uploads.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/sign:
    post:
      tags:
        - default
      summary: Create Signed Upload URL
      description: |
        `org:files:write`
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - date
                - expires
              properties:
                date:
                  type: number
                  description: >-
                    The unix timestamp that the URL is signed, ie time of
                    request
                expires:
                  type: number
                  description: >-
                    How long the URL is valid for in sconds after signing based
                    on the date parameter
                max_file_size:
                  type: number
                  description: Restrict the max size of a file upload in `bytes`
                allow_mime_types:
                  type: array
                  description: >-
                    Array of allowed mime types for a file upload, includes
                    wildcards `"image/*"`
                  items:
                    type: string
                group_id:
                  type: string
                  description: ID of the group that the file will be uploaded to
                keyvalues:
                  type: object
                  description: Add additional key value metadata to files upon upload
                  additionalProperties:
                    type: string
                filename:
                  type: string
                  description: Name of the file that will be uploaded
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: string
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````