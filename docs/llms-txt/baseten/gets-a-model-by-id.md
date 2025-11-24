# Source: https://docs.baseten.co/reference/management-api/models/gets-a-model-by-id.md

# By ID

## OpenAPI

````yaml get /v1/models/{model_id}
paths:
  path: /v1/models/{model_id}
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
          curl --request GET \
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
                  - description: Unique identifier of the model
                    title: Id
                    type: string
              created_at:
                allOf:
                  - description: Time the model was created in ISO 8601 format
                    format: date-time
                    title: Created At
                    type: string
              name:
                allOf:
                  - description: Name of the model
                    title: Name
                    type: string
              deployments_count:
                allOf:
                  - description: Number of deployments of the model
                    title: Deployments Count
                    type: integer
              production_deployment_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: >-
                      Unique identifier of the production deployment of the
                      model
                    title: Production Deployment Id
              development_deployment_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: >-
                      Unique identifier of the development deployment of the
                      model
                    title: Development Deployment Id
              instance_type_name:
                allOf:
                  - description: >-
                      Name of the instance type for the production deployment of
                      the model
                    title: Instance Type Name
                    type: string
            title: ModelV1
            description: A model.
            refIdentifier: '#/components/schemas/ModelV1'
            requiredProperties:
              - id
              - created_at
              - name
              - deployments_count
              - production_deployment_id
              - development_deployment_id
              - instance_type_name
        examples:
          example:
            value:
              id: <string>
              created_at: '2023-11-07T05:31:56Z'
              name: <string>
              deployments_count: 123
              production_deployment_id: <string>
              development_deployment_id: <string>
              instance_type_name: <string>
        description: A model.
  deprecated: false
  type: path
components:
  schemas: {}

````