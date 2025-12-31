# Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-deployment-associated-with-an-environment.md

# Activate environment deployment

> Activates an inactive deployment associated with an environment and returns the activation status.

## OpenAPI

````yaml post /v1/models/{model_id}/environments/{env_name}/activate
paths:
  path: /v1/models/{model_id}/environments/{env_name}/activate
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
      path:
        model_id:
          schema:
            - type: string
              required: true
        env_name:
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
          curl --request POST \

          --url
          https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/activate
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}/activate"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "POST",
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
              success:
                allOf:
                  - default: true
                    description: Whether the deployment was successfully activated
                    title: Success
                    type: boolean
            title: ActivateResponseV1
            description: The response to a request to activate a deployment.
            refIdentifier: '#/components/schemas/ActivateResponseV1'
        examples:
          example:
            value:
              success: true
        description: The response to a request to activate a deployment.
  deprecated: false
  type: path
components:
  schemas: {}

````