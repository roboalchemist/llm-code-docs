# Source: https://docs.fireworks.ai/api-reference/get-model-upload-endpoint.md

# Get Model Upload Endpoint

## OpenAPI

````yaml post /v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint
paths:
  path: /v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint
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
        model_id:
          schema:
            - type: string
              required: true
              description: The Model Id
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
              enableResumableUpload:
                allOf:
                  - type: boolean
                    description: If true, enable resumable upload instead of PUT.
              readMask:
                allOf:
                  - type: string
                    description: >-
                      The fields to be returned in the response. If empty or
                      "*", all fields will be returned.
            required: true
            refIdentifier: '#/components/schemas/GatewayGetModelUploadEndpointBody'
            requiredProperties:
              - filenameToSize
        examples:
          example:
            value:
              filenameToSize: {}
              enableResumableUpload: true
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
                    title: Signed URLs for uploading model files
              filenameToUnsignedUris:
                allOf:
                  - type: object
                    additionalProperties:
                      type: string
                    description: >-
                      Unsigned URIs (e.g. s3://bucket/key, gs://bucket/key) for
                      uploading model files.

                      Returned when the caller has permission to upload to the
                      URIs.
            refIdentifier: '#/components/schemas/gatewayGetModelUploadEndpointResponse'
        examples:
          example:
            value:
              filenameToSignedUrls: {}
              filenameToUnsignedUris: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````