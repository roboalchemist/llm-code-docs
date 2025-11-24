# Source: https://docs.fireworks.ai/api-reference/upload-dataset-files.md

# Upload Dataset Files

> Provides a streamlined way to upload a dataset file in a single API request. This path can handle file sizes up to 150Mb. For larger file sizes use [Get Dataset Upload Endpoint](get-dataset-upload-endpoint).


## OpenAPI

````yaml post /v1/accounts/{account_id}/datasets/{dataset_id}:upload
paths:
  path: /v1/accounts/{account_id}/datasets/{dataset_id}:upload
  method: post
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The account id
        dataset_id:
          schema:
            - type: string
              required: true
              description: The dataset id
      query: {}
      header: {}
      cookie: {}
    body:
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              file:
                allOf:
                  - type: string
                    format: binary
            required: true
        examples:
          example:
            value: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The dataset id.
              object:
                allOf:
                  - type: string
                    description: The object type, which is always file.
              bytes:
                allOf:
                  - type: integer
                    format: int64
                    description: The size of the file, in bytes.
              created_at:
                allOf:
                  - type: integer
                    format: int64
                    description: >-
                      The Unix timestamp (in seconds) for when the file was
                      created.
              filename:
                allOf:
                  - type: string
                    description: The name of the file.
              purpose:
                allOf:
                  - type: string
                    description: The intended purpose of the file.
            refIdentifier: '#/components/schemas/FileUploadResponse'
        examples:
          example:
            value:
              id: <string>
              object: <string>
              bytes: 123
              created_at: 123
              filename: <string>
              purpose: <string>
        description: A successful response.
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Bad Request
        examples: {}
        description: Bad Request
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Not Found
        examples: {}
        description: Not Found
    '500':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Internal Server Error
        examples: {}
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````