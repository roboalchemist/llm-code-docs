# Source: https://docs.baseten.co/reference/management-api/api-keys/creates-an-api-key.md

# Create an API key

> Creates an API key with the provided name and type. The API key is returned in the response.

## OpenAPI

````yaml post /v1/api_keys
paths:
  path: /v1/api_keys
  method: post
  servers:
    - url: https://api.baseten.co
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: >-
                You must specify the scheme 'Api-Key' in the Authorization
                header. For example, `Authorization: Api-Key <Your_Api_Key>`
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
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    default: null
                    description: Optional name for the API key
                    examples:
                      - my-api-key
                    title: Name
              type:
                allOf:
                  - $ref: '#/components/schemas/APIKeyCategory'
                    description: Type of the API key.
                    examples:
                      - PERSONAL
                      - WORKSPACE_EXPORT_METRICS
                      - WORKSPACE_INVOKE
                      - WORKSPACE_MANAGE_ALL
              model_ids:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    default: null
                    description: >-
                      List of model IDs to scope the API key to, only present if
                      type is 'WORKSPACE_EXPORT_METRICS' or 'WORKSPACE_INVOKE'
                    examples:
                      - - aaaaaaaa
                    title: Model Ids
            required: true
            title: CreateAPIKeyRequestV1
            description: Request to create an API key.
            refIdentifier: '#/components/schemas/CreateAPIKeyRequestV1'
            requiredProperties:
              - type
        examples:
          example:
            value:
              name: my-api-key
              type: PERSONAL
              model_ids:
                - aaaaaaaa
    codeSamples:
      - lang: bash
        source: |-
          curl --request POST \
          --url https://api.baseten.co/v1/api_keys \
          --header "Authorization: Api-Key $BASETEN_API_KEY" \
          --data '{
            "name": "my-api-key",
            "type": "PERSONAL"
          }'
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/api_keys"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'name': 'my-api-key', 'type': 'PERSONAL'}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              api_key:
                allOf:
                  - description: The API key string
                    title: Api Key
                    type: string
            title: APIKeyV1
            description: Represents an API key.
            refIdentifier: '#/components/schemas/APIKeyV1'
            requiredProperties:
              - api_key
        examples:
          example:
            value:
              api_key: <string>
        description: Represents an API key.
  deprecated: false
  type: path
components:
  schemas:
    APIKeyCategory:
      description: Enum representing the category of an API key.
      enum:
        - PERSONAL
        - WORKSPACE_MANAGE_ALL
        - WORKSPACE_EXPORT_METRICS
        - WORKSPACE_INVOKE
      title: APIKeyCategory
      type: string

````