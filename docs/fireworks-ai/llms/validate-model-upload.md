# Source: https://docs.fireworks.ai/api-reference/validate-model-upload.md

# Validate Model Upload

## OpenAPI

````yaml get /v1/accounts/{account_id}/models/{model_id}:validateUpload
paths:
  path: /v1/accounts/{account_id}/models/{model_id}:validateUpload
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
        skipHfConfigValidation:
          schema:
            - type: boolean
              required: false
              description: If true, skip the Hugging Face config validation.
        trustRemoteCode:
          schema:
            - type: boolean
              required: false
              description: >-
                If true, trusts remote code when validating the Hugging Face
                config.
        configOnly:
          schema:
            - type: boolean
              required: false
              description: If true, skip tokenizer and parameter name validation.
      header: {}
      cookie: {}
    body: {}
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