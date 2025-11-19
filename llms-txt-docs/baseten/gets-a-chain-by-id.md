# Source: https://docs.baseten.co/reference/management-api/chains/gets-a-chain-by-id.md

# By ID

## OpenAPI

````yaml get /v1/chains/{chain_id}
paths:
  path: /v1/chains/{chain_id}
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
      path:
        chain_id:
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
          curl --request GET \
          --url https://api.baseten.co/v1/chains/{chain_id} \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/chains/{chain_id}"

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
              id:
                allOf:
                  - description: Unique identifier of the chain
                    title: Id
                    type: string
              created_at:
                allOf:
                  - description: Time the chain was created in ISO 8601 format
                    format: date-time
                    title: Created At
                    type: string
              name:
                allOf:
                  - description: Name of the chain
                    title: Name
                    type: string
              deployments_count:
                allOf:
                  - description: Number of deployments of the chain
                    title: Deployments Count
                    type: integer
            title: ChainV1
            description: A chain.
            refIdentifier: '#/components/schemas/ChainV1'
            requiredProperties:
              - id
              - created_at
              - name
              - deployments_count
        examples:
          example:
            value:
              id: <string>
              created_at: '2023-11-07T05:31:56Z'
              name: <string>
              deployments_count: 123
        description: A chain.
  deprecated: false
  type: path
components:
  schemas: {}

````