# Source: https://docs.baseten.co/reference/management-api/chains/gets-all-chains.md

# All chains

## OpenAPI

````yaml get /v1/chains
paths:
  path: /v1/chains
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
          --url https://api.baseten.co/v1/chains \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/chains"

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
              chains:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ChainV1'
                    title: Chains
                    type: array
            title: ChainsV1
            description: A list of chains.
            refIdentifier: '#/components/schemas/ChainsV1'
            requiredProperties:
              - chains
        examples:
          example:
            value:
              chains:
                - id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  name: <string>
                  deployments_count: 123
        description: A list of chains.
  deprecated: false
  type: path
components:
  schemas:
    ChainV1:
      description: A chain.
      properties:
        id:
          description: Unique identifier of the chain
          title: Id
          type: string
        created_at:
          description: Time the chain was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the chain
          title: Name
          type: string
        deployments_count:
          description: Number of deployments of the chain
          title: Deployments Count
          type: integer
      required:
        - id
        - created_at
        - name
        - deployments_count
      title: ChainV1
      type: object

````