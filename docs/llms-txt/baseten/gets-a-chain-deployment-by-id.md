# Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-chain-deployment-by-id.md

# Any chain deployment by ID

## OpenAPI

````yaml get /v1/chains/{chain_id}/deployments/{chain_deployment_id}
paths:
  path: /v1/chains/{chain_id}/deployments/{chain_deployment_id}
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
          curl --request GET \

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
                  - description: Unique identifier of the chain deployment
                    title: Id
                    type: string
              created_at:
                allOf:
                  - description: Time the chain deployment was created in ISO 8601 format
                    format: date-time
                    title: Created At
                    type: string
              chain_id:
                allOf:
                  - description: Unique identifier of the chain
                    title: Chain Id
                    type: string
              environment:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    description: Environment the chain deployment is deployed in
                    title: Environment
              chainlets:
                allOf:
                  - description: Chainlets in the chain deployment
                    items:
                      $ref: '#/components/schemas/ChainletV1'
                    title: Chainlets
                    type: array
              status:
                allOf:
                  - $ref: '#/components/schemas/DeploymentStatusV1'
                    description: Status of the chain deployment
            title: ChainDeploymentV1
            description: A deployment of a chain.
            refIdentifier: '#/components/schemas/ChainDeploymentV1'
            requiredProperties:
              - id
              - created_at
              - chain_id
              - environment
              - chainlets
              - status
        examples:
          example:
            value:
              id: <string>
              created_at: '2023-11-07T05:31:56Z'
              chain_id: <string>
              environment: <string>
              chainlets:
                - id: <string>
                  name: <string>
                  autoscaling_settings:
                    min_replica: 123
                    max_replica: 123
                    autoscaling_window: 123
                    scale_down_delay: 123
                    concurrency_target: 123
                    target_utilization_percentage: 123
                  instance_type_name: <string>
                  active_replica_count: 123
                  status: BUILDING
              status: BUILDING
        description: A deployment of a chain.
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
    ChainletV1:
      description: A chainlet in a chain deployment.
      properties:
        id:
          description: Unique identifier of the chainlet
          title: Id
          type: string
        name:
          description: Name of the chainlet
          title: Name
          type: string
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/AutoscalingSettingsV1'
            - type: 'null'
          description: >-
            Autoscaling settings for the chainlet. If null, it has not finished
            deploying
        instance_type_name:
          description: Name of the instance type the chainlet is deployed on
          title: Instance Type Name
          type: string
        active_replica_count:
          description: Number of active replicas
          title: Active Replica Count
          type: integer
        status:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: Status of the chainlet
      required:
        - id
        - name
        - autoscaling_settings
        - instance_type_name
        - active_replica_count
        - status
      title: ChainletV1
      type: object

````