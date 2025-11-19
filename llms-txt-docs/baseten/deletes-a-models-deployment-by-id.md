# Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-models-deployment-by-id.md

# Delete model deployments

> Deletes a model's deployment by ID and returns the tombstone of the deployment.

## OpenAPI

````yaml delete /v1/models/{model_id}/deployments/{deployment_id}
paths:
  path: /v1/models/{model_id}/deployments/{deployment_id}
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
        deployment_id:
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
          https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}"


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
                  - description: Unique identifier of the deployment
                    title: Id
                    type: string
              deleted:
                allOf:
                  - description: Whether the deployment was deleted
                    title: Deleted
                    type: boolean
              model_id:
                allOf:
                  - description: Unique identifier of the model
                    title: Model Id
                    type: string
            title: DeploymentTombstoneV1
            description: A model deployment tombstone.
            refIdentifier: '#/components/schemas/DeploymentTombstoneV1'
            requiredProperties:
              - id
              - deleted
              - model_id
        examples:
          example:
            value:
              id: <string>
              deleted: true
              model_id: <string>
        description: A model deployment tombstone.
  deprecated: false
  type: path
components:
  schemas: {}

````