# Source: https://docs.baseten.co/reference/management-api/api-keys/delete-an-api-key.md

# Delete an API key

> Deletes an API key by prefix and returns info about the API key.

## OpenAPI

````yaml delete /v1/api_keys/{api_key_prefix}
paths:
  path: /v1/api_keys/{api_key_prefix}
  method: delete
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
      path:
        api_key_prefix:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: bash
        source: |
          curl --request DELETE \
          --url https://api.baseten.co/v1/api_keys/{api_key_prefix} \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/api_keys/{api_key_prefix}"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "DELETE",
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
              prefix:
                allOf:
                  - description: Unique prefix of the API key
                    title: Prefix
                    type: string
            title: APIKeyTombstoneV1
            description: An API key tombstone.
            refIdentifier: '#/components/schemas/APIKeyTombstoneV1'
            requiredProperties:
              - prefix
        examples:
          example:
            value:
              prefix: <string>
        description: An API key tombstone.
  deprecated: false
  type: path
components:
  schemas: {}

````