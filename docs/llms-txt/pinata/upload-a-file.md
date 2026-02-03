# Source: https://docs.pinata.cloud/api-reference/endpoint/upload-a-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a File

> `org:files:write`


<Note>
  The V3 Upload endpoint currently does not support folder uploads. Please use the legacy [pinFileToIPFS endpoint](/api-reference/endpoint/ipfs/pin-file-to-ipfs)
</Note>


## OpenAPI

````yaml post /files
openapi: 3.0.0
info:
  title: Private IPFS API
  version: 1.0.0
servers:
  - url: https://uploads.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files:
    post:
      tags:
        - default
      summary: Upload a File
      description: |
        `org:files:write`
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - file
                - network
              properties:
                network:
                  type: string
                  enum:
                    - public
                    - private
                  description: >-
                    Determine if the file should be uploaded to either the
                    public or private IPFS network. If not designated it will
                    default to private.
                  default: private
                file:
                  type: string
                  format: binary
                  description: File object you want to upload
                name:
                  type: string
                  description: Add a custom name for the file
                group_id:
                  type: string
                  description: ID of the group you would like to upload
                keyvalues:
                  type: object
                  description: Add additional key value metadata to files upon upload
                  additionalProperties:
                    type: string
                car:
                  type: boolean
                  description: >-
                    Upload a file as a raw CAR file (only supported for public
                    network)
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
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
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````