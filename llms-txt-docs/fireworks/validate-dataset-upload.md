# Source: https://docs.fireworks.ai/api-reference/validate-dataset-upload.md

# Validate Dataset Upload

## OpenAPI

````yaml post /v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload
paths:
  path: /v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload
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
            properties: {}
            required: true
            refIdentifier: '#/components/schemas/GatewayValidateDatasetUploadBody'
        examples:
          example:
            value: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````