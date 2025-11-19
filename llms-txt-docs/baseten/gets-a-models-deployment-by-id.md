# Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-deployment-by-id.md

# Any model deployment by ID

> Gets a model's deployment by ID and returns the deployment.

## OpenAPI

````yaml get /v1/models/{model_id}/deployments/{deployment_id}
paths:
  path: /v1/models/{model_id}/deployments/{deployment_id}
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
          curl --request GET \

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
                  - description: Unique identifier of the deployment
                    title: Id
                    type: string
              created_at:
                allOf:
                  - description: Time the deployment was created in ISO 8601 format
                    format: date-time
                    title: Created At
                    type: string
              name:
                allOf:
                  - description: Name of the deployment
                    title: Name
                    type: string
              model_id:
                allOf:
                  - description: Unique identifier of the model
                    title: Model Id
                    type: string
              is_production:
                allOf:
                  - description: >-
                      Whether the deployment is the production deployment of the
                      model
                    title: Is Production
                    type: boolean
              is_development:
                allOf:
                  - description: >-
                      Whether the deployment is the development deployment of
                      the model
                    title: Is Development
                    type: boolean
              status:
                allOf:
                  - $ref: '#/components/schemas/DeploymentStatusV1'
                    description: Status of the deployment
              active_replica_count:
                allOf:
                  - description: Number of active replicas
                    title: Active Replica Count
                    type: integer
              autoscaling_settings:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AutoscalingSettingsV1'
                      - type: 'null'
                    description: >-
                      Autoscaling settings for the deployment. If null, the
                      model has not finished deploying
              instance_type_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: >-
                      Name of the instance type the model deployment is running
                      on
                    title: Instance Type Name
              environment:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: The environment associated with the deployment
                    title: Environment
            title: DeploymentV1
            description: A deployment of a model.
            refIdentifier: '#/components/schemas/DeploymentV1'
            requiredProperties:
              - id
              - created_at
              - name
              - model_id
              - is_production
              - is_development
              - status
              - active_replica_count
              - autoscaling_settings
              - instance_type_name
              - environment
        examples:
          example:
            value:
              id: <string>
              created_at: '2023-11-07T05:31:56Z'
              name: <string>
              model_id: <string>
              is_production: true
              is_development: true
              status: BUILDING
              active_replica_count: 123
              autoscaling_settings:
                min_replica: 123
                max_replica: 123
                autoscaling_window: 123
                scale_down_delay: 123
                concurrency_target: 123
                target_utilization_percentage: 123
              instance_type_name: <string>
              environment: <string>
        description: A deployment of a model.
  deprecated: false
  type: path
components:
  schemas:
    AutoscalingSettingsV1:
      description: Autoscaling settings for a deployment.
      properties:
        min_replica:
          description: Minimum number of replicas
          title: Min Replica
          type: integer
        max_replica:
          description: Maximum number of replicas
          title: Max Replica
          type: integer
        autoscaling_window:
          anyOf:
            - type: integer
            - type: 'null'
          description: Timeframe of traffic considered for autoscaling decisions
          title: Autoscaling Window
        scale_down_delay:
          anyOf:
            - type: integer
            - type: 'null'
          description: Waiting period before scaling down any active replica
          title: Scale Down Delay
        concurrency_target:
          description: Number of requests per replica before scaling up
          title: Concurrency Target
          type: integer
        target_utilization_percentage:
          anyOf:
            - type: integer
            - type: 'null'
          description: Target utilization percentage for scaling up/down.
          title: Target Utilization Percentage
      required:
        - min_replica
        - max_replica
        - autoscaling_window
        - scale_down_delay
        - concurrency_target
        - target_utilization_percentage
      title: AutoscalingSettingsV1
      type: object
    DeploymentStatusV1:
      description: The status of a deployment.
      enum:
        - BUILDING
        - DEPLOYING
        - DEPLOY_FAILED
        - LOADING_MODEL
        - ACTIVE
        - UNHEALTHY
        - BUILD_FAILED
        - BUILD_STOPPED
        - DEACTIVATING
        - INACTIVE
        - FAILED
        - UPDATING
        - SCALED_TO_ZERO
        - WAKING_UP
      title: DeploymentStatusV1
      type: string

````