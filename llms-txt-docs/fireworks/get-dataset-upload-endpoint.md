# Source: https://docs.fireworks.ai/api-reference/get-dataset-upload-endpoint.md

# Get Dataset Upload Endpoint

## OpenAPI

````yaml post /v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint
paths:
  path: /v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint
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
              description: The Account Id
        dataset_id:
          schema:
            - type: string
              required: true
              description: The Dataset Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              filenameToSize:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                      format: int64
                    description: A mapping from the file name to its size in bytes.
              readMask:
                allOf:
                  - type: string
                    description: >-
                      The fields to be returned in the response. If empty or
                      "*", all fields will be returned.
            required: true
            refIdentifier: '#/components/schemas/GatewayGetDatasetUploadEndpointBody'
            requiredProperties:
              - filenameToSize
        examples:
          example:
            value:
              filenameToSize: {}
              readMask: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              filenameToSignedUrls:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    title: Signed URLs for uploading dataset files
            refIdentifier: '#/components/schemas/gatewayGetDatasetUploadEndpointResponse'
        examples:
          example:
            value:
              filenameToSignedUrls: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````