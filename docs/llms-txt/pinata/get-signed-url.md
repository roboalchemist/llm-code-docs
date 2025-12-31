# Source: https://docs.pinata.cloud/api-reference/endpoint/get-signed-url.md

# Create Download Link

> `org:files:write`


## OpenAPI

````yaml pinata-api-v3.yaml post /files/private/download_link
paths:
  path: /files/private/download_link
  method: post
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - type: string
                    description: >-
                      The full URL of your file in the format of
                      `https://{yourgatewaydomain}.mypinata.cloud/files/{cid}`
              date:
                allOf:
                  - type: number
                    description: >-
                      The unix timestamp that the URL is signed, ie time of
                      request
              expires:
                allOf:
                  - type: number
                    description: >-
                      How long the URL is valid for in sconds after signing
                      based on the date parameter
              method:
                allOf:
                  - type: string
                    description: The URL method, ie `GET`
            example:
              url: >-
                https://example.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm
              expires: 500000
              date: 1724875300
              method: GET
        examples:
          example:
            value:
              url: >-
                https://example.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm
              expires: 500000
              date: 1724875300
              method: GET
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: string
                    description: The signed URL
        examples:
          example:
            value:
              data: >-
                https://blush-fast-impala-660.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm?X-Algorithm=PINATA1&X-Date=1724875300&X-Expires=500000&X-Method=GET&X-Signature=example-signature
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````