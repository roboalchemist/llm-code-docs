# Source: https://docs.pinata.cloud/api-reference/endpoint/get-signed-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Download Link

> `org:files:write`




## OpenAPI

````yaml pinata-api-v3.yaml post /files/private/download_link
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/private/download_link:
    post:
      tags:
        - Private Files
      summary: Create Download Link
      description: |
        `org:files:write`
      operationId: createDownloadLink
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: >-
                    The full URL of your file in the format of
                    `https://{yourgatewaydomain}.mypinata.cloud/files/{cid}`
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
                method:
                  type: string
                  description: The URL method, ie `GET`
              example:
                url: >-
                  https://example.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm
                expires: 500000
                date: 1724875300
                method: GET
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Wed, 28 Aug 2024 20:01:46 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '291'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 0c7a656fdb5c98f6a89cd9cd70147c6d
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: string
                    description: The signed URL
              example:
                data: >-
                  https://blush-fast-impala-660.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm?X-Algorithm=PINATA1&X-Date=1724875300&X-Expires=500000&X-Method=GET&X-Signature=example-signature
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````