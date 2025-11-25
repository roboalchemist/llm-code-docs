# Source: https://docs.pinata.cloud/api-reference/endpoint/upload-a-file.md

# Upload a File

> `org:files:write`


## OpenAPI

````yaml post /files
paths:
  path: /files
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
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              network:
                allOf:
                  - type: string
                    enum:
                      - public
                      - private
                    description: >-
                      Determine if the file should be uploaded to either the
                      public or private IPFS network. If not designated it will
                      default to private.
                    default: private
              file:
                allOf:
                  - type: string
                    format: binary
                    description: File object you want to upload
              name:
                allOf:
                  - type: string
                    description: Add a custom name for the file
              group_id:
                allOf:
                  - type: string
                    description: ID of the group you would like to upload
              keyvalues:
                allOf:
                  - type: object
                    description: Add additional key value metadata to files upon upload
                    additionalProperties:
                      type: string
              car:
                allOf:
                  - type: boolean
                    description: >-
                      Upload a file as a raw CAR file (only supported for public
                      network)
            requiredProperties:
              - file
              - network
        examples:
          example:
            value:
              network: private
              name: <string>
              group_id: <string>
              keyvalues: {}
              car: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                      name:
                        type: string
                      cid:
                        type: string
                      created_at:
                        type: string
                      size:
                        type: number
                      number_of_files:
                        type: number
                      mime_type:
                        type: string
                      user_id:
                        type: string
                      group_id:
                        type: string
                      is_duplicate:
                        type: boolean
        examples:
          example:
            value:
              data:
                id: <string>
                name: <string>
                cid: <string>
                created_at: <string>
                size: 123
                number_of_files: 123
                mime_type: <string>
                user_id: <string>
                group_id: <string>
                is_duplicate: true
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````