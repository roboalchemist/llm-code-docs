# Source: https://docs.fireworks.ai/api-reference/get-model-download-endpoint.md

# Get Model Download Endpoint

## OpenAPI

````yaml get /v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint
paths:
  path: /v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint
  method: get
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
      query:
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
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
                    title: Signed URLs for for downloading model files
            refIdentifier: '#/components/schemas/gatewayGetModelDownloadEndpointResponse'
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