# Source: https://docs.baseten.co/reference/management-api/models/gets-all-models.md

# All models

## OpenAPI

````yaml get /v1/models
paths:
  path: /v1/models
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
          --url https://api.baseten.co/v1/models \
          --header "Authorization: Api-Key $BASETEN_API_KEY"
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/models"

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
              models:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ModelV1'
                    title: Models
                    type: array
            title: ModelsV1
            description: A list of models.
            refIdentifier: '#/components/schemas/ModelsV1'
            requiredProperties:
              - models
        examples:
          example:
            value:
              models:
                - id: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  name: <string>
                  deployments_count: 123
                  production_deployment_id: <string>
                  development_deployment_id: <string>
                  instance_type_name: <string>
        description: A list of models.
  deprecated: false
  type: path
components:
  schemas:
    ModelV1:
      description: A model.
      properties:
        id:
          description: Unique identifier of the model
          title: Id
          type: string
        created_at:
          description: Time the model was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the model
          title: Name
          type: string
        deployments_count:
          description: Number of deployments of the model
          title: Deployments Count
          type: integer
        production_deployment_id:
          anyOf:
            - type: string
            - type: 'null'
          description: Unique identifier of the production deployment of the model
          title: Production Deployment Id
        development_deployment_id:
          anyOf:
            - type: string
            - type: 'null'
          description: Unique identifier of the development deployment of the model
          title: Development Deployment Id
        instance_type_name:
          description: Name of the instance type for the production deployment of the model
          title: Instance Type Name
          type: string
      required:
        - id
        - created_at
        - name
        - deployments_count
        - production_deployment_id
        - development_deployment_id
        - instance_type_name
      title: ModelV1
      type: object

````