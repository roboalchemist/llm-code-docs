# Source: https://docs.baseten.co/reference/management-api/models/deletes-a-model-by-id.md

# Delete models

## OpenAPI

````yaml delete /v1/models/{model_id}
paths:
  path: /v1/models/{model_id}
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
        model_id:
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
          --url https://api.baseten.co/v1/models/{model_id} \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/models/{model_id}"

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
              id:
                allOf:
                  - description: Unique identifier of the model
                    title: Id
                    type: string
              deleted:
                allOf:
                  - description: Whether the model was deleted
                    title: Deleted
                    type: boolean
            title: ModelTombstoneV1
            description: A model tombstone.
            refIdentifier: '#/components/schemas/ModelTombstoneV1'
            requiredProperties:
              - id
              - deleted
        examples:
          example:
            value:
              id: <string>
              deleted: true
        description: A model tombstone.
  deprecated: false
  type: path
components:
  schemas: {}

````