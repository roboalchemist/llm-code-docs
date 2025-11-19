# Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-chain-deployment-by-id.md

# Delete chain deployment

## OpenAPI

````yaml delete /v1/chains/{chain_id}/deployments/{chain_deployment_id}
paths:
  path: /v1/chains/{chain_id}/deployments/{chain_deployment_id}
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
        chain_id:
          schema:
            - type: string
              required: true
        chain_deployment_id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: bash
        source: >
          curl --request DELETE \

          --url
          https://api.baseten.co/v1/chains/{chain_id}/deployments/{chain_deployment_id}
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/chains/{chain_id}/deployments/{chain_deployment_id}"


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
                  - description: Unique identifier of the chain deployment
                    title: Id
                    type: string
              deleted:
                allOf:
                  - description: Whether the chain deployment was deleted
                    title: Deleted
                    type: boolean
              chain_id:
                allOf:
                  - description: Unique identifier of the chain
                    title: Chain Id
                    type: string
            title: ChainDeploymentTombstoneV1
            description: A chain deployment tombstone.
            refIdentifier: '#/components/schemas/ChainDeploymentTombstoneV1'
            requiredProperties:
              - id
              - deleted
              - chain_id
        examples:
          example:
            value:
              id: <string>
              deleted: true
              chain_id: <string>
        description: A chain deployment tombstone.
  deprecated: false
  type: path
components:
  schemas: {}

````