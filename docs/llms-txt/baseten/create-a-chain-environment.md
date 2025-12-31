# Source: https://docs.baseten.co/reference/management-api/environments/create-a-chain-environment.md

# Create Chain environment

> Create a chain environment. Returns the resulting environment.

## OpenAPI

````yaml post /v1/chains/{chain_id}/environments
paths:
  path: /v1/chains/{chain_id}/environments
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
        chain_id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - description: Name of the environment
                    examples:
                      - staging
                    title: Name
                    type: string
              promotion_settings:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/PromotionSettingsV1'
                      - type: 'null'
                    default: null
                    description: Promotion settings for the environment
                    examples:
                      - ramp_up_duration_seconds: 600
                        ramp_up_while_promoting: true
                        redeploy_on_promotion: true
                        rolling_deploy: false
              chainlet_settings:
                allOf:
                  - anyOf:
                      - items:
                          $ref: >-
                            #/components/schemas/ChainletEnvironmentSettingsRequestV1
                        type: array
                      - type: 'null'
                    default: null
                    description: >-
                      Mapping of chainlet name to the desired chainlet
                      environment settings
                    examples:
                      - - autoscaling_settings:
                            autoscaling_window: 800
                            concurrency_target: 4
                            max_replica: 3
                            min_replica: 2
                            scale_down_delay: 63
                            target_utilization_percentage: null
                          chainlet_name: HelloWorld
                          instance_type_id: 2x8
                        - autoscaling_settings:
                            autoscaling_window: null
                            concurrency_target: null
                            max_replica: 3
                            min_replica: 3
                            scale_down_delay: null
                            target_utilization_percentage: null
                          chainlet_name: RandInt
                          instance_type_id: A10Gx8x32
                    title: Chainlet Settings
            required: true
            title: CreateChainEnvironmentRequestV1
            description: A request to create a custom environment for a chain.
            refIdentifier: '#/components/schemas/CreateChainEnvironmentRequestV1'
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: staging
              promotion_settings:
                ramp_up_duration_seconds: 600
                ramp_up_while_promoting: true
                redeploy_on_promotion: true
                rolling_deploy: false
              chainlet_settings:
                - autoscaling_settings:
                    autoscaling_window: 800
                    concurrency_target: 4
                    max_replica: 3
                    min_replica: 2
                    scale_down_delay: 63
                    target_utilization_percentage: null
                  chainlet_name: HelloWorld
                  instance_type_id: 2x8
                - autoscaling_settings:
                    autoscaling_window: null
                    concurrency_target: null
                    max_replica: 3
                    min_replica: 3
                    scale_down_delay: null
                    target_utilization_percentage: null
                  chainlet_name: RandInt
                  instance_type_id: A10Gx8x32
    codeSamples:
      - lang: bash
        source: |-
          curl --request POST \
          --url https://api.baseten.co/v1/chains/{chain_id}/environments \
          --header "Authorization: Api-Key $BASETEN_API_KEY" \
          --data '{
            "name": "staging",
            "promotion_settings": {
              "ramp_up_duration_seconds": 600,
              "ramp_up_while_promoting": true,
              "redeploy_on_promotion": true,
              "rolling_deploy": false
            },
            "chainlet_settings": [
              {
                "autoscaling_settings": {
                  "autoscaling_window": 800,
                  "concurrency_target": 4,
                  "max_replica": 3,
                  "min_replica": 2,
                  "scale_down_delay": 63,
                  "target_utilization_percentage": null
                },
                "chainlet_name": "HelloWorld",
                "instance_type_id": "2x8"
              },
              {
                "autoscaling_settings": {
                  "autoscaling_window": null,
                  "concurrency_target": null,
                  "max_replica": 3,
                  "min_replica": 3,
                  "scale_down_delay": null,
                  "target_utilization_percentage": null
                },
                "chainlet_name": "RandInt",
                "instance_type_id": "A10Gx8x32"
              }
            ]
          }'
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/chains/{chain_id}/environments"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'name': 'staging', 'promotion_settings': {'ramp_up_duration_seconds': 600, 'ramp_up_while_promoting': True, 'redeploy_on_promotion': True, 'rolling_deploy': False}, 'chainlet_settings': [{'autoscaling_settings': {'autoscaling_window': 800, 'concurrency_target': 4, 'max_replica': 3, 'min_replica': 2, 'scale_down_delay': 63, 'target_utilization_percentage': None}, 'chainlet_name': 'HelloWorld', 'instance_type_id': '2x8'}, {'autoscaling_settings': {'autoscaling_window': None, 'concurrency_target': None, 'max_replica': 3, 'min_replica': 3, 'scale_down_delay': None, 'target_utilization_percentage': None}, 'chainlet_name': 'RandInt', 'instance_type_id': 'A10Gx8x32'}]}
          )

          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - description: Name of the environment
                    title: Name
                    type: string
              created_at:
                allOf:
                  - description: Time the environment was created in ISO 8601 format
                    format: date-time
                    title: Created At
                    type: string
              chain_id:
                allOf:
                  - description: Unique identifier of the chain
                    title: Chain Id
                    type: string
              promotion_settings:
                allOf:
                  - $ref: '#/components/schemas/PromotionSettingsV1'
                    description: Promotion settings for the environment
              chainlet_settings:
                allOf:
                  - description: Environment settings for the chainlets
                    items:
                      $ref: '#/components/schemas/ChainletEnvironmentSettingsV1'
                    title: Chainlet Settings
                    type: array
              current_deployment:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ChainDeploymentV1'
                      - type: 'null'
                    description: Current chain deployment of the environment
            title: ChainEnvironmentV1
            description: Environment for oracles.
            refIdentifier: '#/components/schemas/ChainEnvironmentV1'
            requiredProperties:
              - name
              - created_at
              - chain_id
              - promotion_settings
              - chainlet_settings
              - current_deployment
        examples:
          example:
            value:
              name: <string>
              created_at: '2023-11-07T05:31:56Z'
              chain_id: <string>
              promotion_settings:
                redeploy_on_promotion: true
                rolling_deploy: true
                ramp_up_while_promoting: true
                ramp_up_duration_seconds: 600
              chainlet_settings:
                - chainlet_name: <string>
                  autoscaling_settings:
                    min_replica: 123
                    max_replica: 123
                    autoscaling_window: 123
                    scale_down_delay: 123
                    concurrency_target: 123
                    target_utilization_percentage: 123
                  instance_type:
                    id: <string>
                    name: <string>
                    memory_limit_mib: 123
                    millicpu_limit: 123
                    gpu_count: 123
                    gpu_type: <string>
                    gpu_memory_limit_mib: 123
              current_deployment:
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
        description: Environment for oracles.
  deprecated: false
  type: path
components:
  schemas:
    InstanceTypeV1:
      description: An instance type.
      properties:
        id:
          description: Identifier string for the instance type
          title: Id
          type: string
        name:
          description: Display name of the instance type
          title: Name
          type: string
        memory_limit_mib:
          description: Memory limit of the instance type in Mebibytes
          title: Memory Limit Mib
          type: integer
        millicpu_limit:
          description: CPU limit of the instance type in millicpu
          title: Millicpu Limit
          type: integer
        gpu_count:
          description: Number of GPUs on the instance type
          title: Gpu Count
          type: integer
        gpu_type:
          anyOf:
            - type: string
            - type: 'null'
          description: Type of GPU on the instance type
          title: Gpu Type
        gpu_memory_limit_mib:
          anyOf:
            - type: integer
            - type: 'null'
          description: Memory limit of the GPU on the instance type in Mebibytes
          title: Gpu Memory Limit Mib
      required:
        - id
        - name
        - memory_limit_mib
        - millicpu_limit
        - gpu_count
        - gpu_type
        - gpu_memory_limit_mib
      title: InstanceTypeV1
      type: object
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
    UpdateAutoscalingSettingsV1:
      additionalProperties: false
      description: >-
        A request to update autoscaling settings for a deployment. All fields
        are optional, and we only update ones passed in.
      properties:
        min_replica:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Minimum number of replicas
          examples:
            - 0
          title: Min Replica
        max_replica:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Maximum number of replicas
          examples:
            - 7
          title: Max Replica
        autoscaling_window:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Timeframe of traffic considered for autoscaling decisions
          examples:
            - 600
          title: Autoscaling Window
        scale_down_delay:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Waiting period before scaling down any active replica
          examples:
            - 120
          title: Scale Down Delay
        concurrency_target:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Number of requests per replica before scaling up
          examples:
            - 2
          title: Concurrency Target
        target_utilization_percentage:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Target utilization percentage for scaling up/down.
          examples:
            - 70
          title: Target Utilization Percentage
      title: UpdateAutoscalingSettingsV1
      type: object
    PromotionSettingsV1:
      description: Promotion settings for promoting chains and oracles
      properties:
        redeploy_on_promotion:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          description: >-
            Whether to deploy on all promotions. Enabling this flag allows model
            code to safely handle environment-specific logic. When a deployment
            is promoted, a new deployment will be created with a copy of the
            image.
          examples:
            - true
          title: Redeploy On Promotion
        rolling_deploy:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          description: Whether the environment should rely on rolling deploy orchestration.
          examples:
            - true
          title: Rolling Deploy
        ramp_up_while_promoting:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          description: Whether to ramp up traffic while promoting
          examples:
            - true
          title: Ramp Up While Promoting
        ramp_up_duration_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: 600
          description: Duration of the ramp up in seconds
          examples:
            - 600
          title: Ramp Up Duration Seconds
      title: PromotionSettingsV1
      type: object
    ChainDeploymentV1:
      description: A deployment of a chain.
      properties:
        id:
          description: Unique identifier of the chain deployment
          title: Id
          type: string
        created_at:
          description: Time the chain deployment was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        chain_id:
          description: Unique identifier of the chain
          title: Chain Id
          type: string
        environment:
          anyOf:
            - type: string
            - type: 'null'
          description: Environment the chain deployment is deployed in
          title: Environment
        chainlets:
          description: Chainlets in the chain deployment
          items:
            $ref: '#/components/schemas/ChainletV1'
          title: Chainlets
          type: array
        status:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: Status of the chain deployment
      required:
        - id
        - created_at
        - chain_id
        - environment
        - chainlets
        - status
      title: ChainDeploymentV1
      type: object
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
    ChainletEnvironmentSettingsRequestV1:
      description: Request to create environment settings for a chainlet.
      properties:
        chainlet_name:
          description: Name of the chainlet
          examples:
            - HelloWorld
          title: Chainlet Name
          type: string
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/UpdateAutoscalingSettingsV1'
            - type: 'null'
          default: null
          description: Autoscaling settings for the chainlet
          examples:
            - autoscaling_window: 60
              concurrency_target: 1
              max_replica: 1
              min_replica: 0
              scale_down_delay: 900
              target_utilization_percentage: 70
        instance_type_id:
          default: 1x2
          description: ID of the instance type to use for the chainlet
          examples:
            - 1x4
            - 2x8
            - A10G:2x24x96
            - H100:2x52x468
          title: Instance Type Id
          type: string
      required:
        - chainlet_name
      title: ChainletEnvironmentSettingsRequestV1
      type: object
    ChainletEnvironmentSettingsV1:
      description: Environment settings for a chainlet.
      properties:
        chainlet_name:
          description: Name of the chainlet
          title: Chainlet Name
          type: string
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/AutoscalingSettingsV1'
            - type: 'null'
          description: >-
            Autoscaling settings for the chainlet. If null, it has not finished
            deploying
        instance_type:
          $ref: '#/components/schemas/InstanceTypeV1'
          description: Instance type for the chainlet
      required:
        - chainlet_name
        - autoscaling_settings
        - instance_type
      title: ChainletEnvironmentSettingsV1
      type: object

````