# Source: https://docs.baseten.co/reference/management-api/api-keys/lists-the-users-api-keys.md

# Get all API keys

> Lists all API keys your account has access to.

## OpenAPI

````yaml get /v1/api_keys
paths:
  path: /v1/api_keys
  method: get
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
    body: {}
    codeSamples:
      - lang: bash
        source: |
          curl --request GET \
          --url https://api.baseten.co/v1/api_keys \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/api_keys"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "GET",
              url,
              headers=headers,
              json={}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              keys:
                allOf:
                  - description: A list of API key information
                    items:
                      $ref: '#/components/schemas/APIKeyInfoV1'
                    title: Keys
                    type: array
            title: APIKeysV1
            description: A list of API keys.
            refIdentifier: '#/components/schemas/APIKeysV1'
            requiredProperties:
              - keys
        examples:
          example:
            value:
              keys:
                - prefix: <string>
                  name: my-api-key
                  type: PERSONAL
                  model_ids:
                    - aaaaaaaa
        description: A list of API keys.
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
    APIKeyInfoV1:
      description: Represents the metadata of an API key.
      properties:
        prefix:
          description: The prefix of the API key
          title: Prefix
          type: string
        name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: Optional name for the API key
          examples:
            - my-api-key
          title: Name
        type:
          $ref: '#/components/schemas/APIKeyCategory'
          description: Type of the API key.
          examples:
            - PERSONAL
            - WORKSPACE_EXPORT_METRICS
            - WORKSPACE_INVOKE
            - WORKSPACE_MANAGE_ALL
        model_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          default: null
          description: >-
            List of model IDs to scope the API key to, only present if type is
            'WORKSPACE_EXPORT_METRICS' or 'WORKSPACE_INVOKE'
          examples:
            - - aaaaaaaa
          title: Model Ids
      required:
        - prefix
        - type
      title: APIKeyInfoV1
      type: object

````