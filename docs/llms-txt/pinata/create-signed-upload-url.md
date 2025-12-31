# Source: https://docs.pinata.cloud/api-reference/endpoint/create-signed-upload-url.md

# Create Signed Upload URL

> `org:files:write`


## OpenAPI

````yaml pinata-api-v3-uploads.yaml post /files/sign
paths:
  path: /files/sign
  method: post
  servers:
    - url: https://uploads.pinata.cloud/v3
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
              max_file_size:
                allOf:
                  - type: number
                    description: Restrict the max size of a file upload in `bytes`
              allow_mime_types:
                allOf:
                  - type: array
                    description: >-
                      Array of allowed mime types for a file upload, includes
                      wildcards `"image/*"`
                    items:
                      type: string
              group_id:
                allOf:
                  - type: string
                    description: ID of the group that the file will be uploaded to
              keyvalues:
                allOf:
                  - type: object
                    description: Add additional key value metadata to files upon upload
                    additionalProperties:
                      type: string
              filename:
                allOf:
                  - type: string
                    description: Name of the file that will be uploaded
            requiredProperties:
              - date
              - expires
        examples:
          example:
            value:
              date: 123
              expires: 123
              max_file_size: 123
              allow_mime_types:
                - <string>
              group_id: <string>
              keyvalues: {}
              filename: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: string
        examples:
          example:
            value:
              data: <string>
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````