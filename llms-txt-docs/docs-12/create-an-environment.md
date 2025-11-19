# Source: https://docs.baseten.co/reference/management-api/environments/create-an-environment.md

# Create environment

> Creates an environment for the specified model and returns the environment.

## OpenAPI

````yaml post /v1/models/{model_id}/environments
paths:
  path: /v1/models/{model_id}/environments
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
              autoscaling_settings:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/UpdateAutoscalingSettingsV1'
                      - type: 'null'
                    default: null
                    description: Autoscaling settings for the environment
                    examples:
                      - autoscaling_window: 800
                        concurrency_target: 3
                        max_replica: 2
                        min_replica: 1
                        scale_down_delay: 60
                        target_utilization_percentage: null
              promotion_settings:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/UpdatePromotionSettingsV1'
                      - type: 'null'
                    default: null
                    description: Promotion settings for the environment
                    examples:
                      - ramp_up_duration_seconds: 600
                        ramp_up_while_promoting: true
                        redeploy_on_promotion: true
                        rolling_deploy: true
            required: true
            title: CreateEnvironmentRequestV1
            description: A request to create an environment.
            refIdentifier: '#/components/schemas/CreateEnvironmentRequestV1'
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: staging
              autoscaling_settings:
                autoscaling_window: 800
                concurrency_target: 3
                max_replica: 2
                min_replica: 1
                scale_down_delay: 60
                target_utilization_percentage: null
              promotion_settings:
                ramp_up_duration_seconds: 600
                ramp_up_while_promoting: true
                redeploy_on_promotion: true
                rolling_deploy: true
    codeSamples:
      - lang: bash
        source: |-
          curl --request POST \
          --url https://api.baseten.co/v1/models/{model_id}/environments \
          --header "Authorization: Api-Key $BASETEN_API_KEY" \
          --data '{
            "name": "staging",
            "autoscaling_settings": {
              "autoscaling_window": 800,
              "concurrency_target": 3,
              "max_replica": 2,
              "min_replica": 1,
              "scale_down_delay": 60,
              "target_utilization_percentage": null
            },
            "promotion_settings": {
              "ramp_up_duration_seconds": 600,
              "ramp_up_while_promoting": true,
              "redeploy_on_promotion": true,
              "rolling_deploy": true
            }
          }'
      - lang: python
        source: |-
          import requests
          import os
          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")
          url = "https://api.baseten.co/v1/models/{model_id}/environments"

          headers = {"Authorization": f"Api-Key {API_KEY}"}

          response = requests.request(
              "POST",
              url,
              headers=headers,
              json={'name': 'staging', 'autoscaling_settings': {'autoscaling_window': 800, 'concurrency_target': 3, 'max_replica': 2, 'min_replica': 1, 'scale_down_delay': 60, 'target_utilization_percentage': None}, 'promotion_settings': {'ramp_up_duration_seconds': 600, 'ramp_up_while_promoting': True, 'redeploy_on_promotion': True, 'rolling_deploy': True}}
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
              model_id:
                allOf:
                  - description: Unique identifier of the model
                    title: Model Id
                    type: string
              current_deployment:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DeploymentV1'
                      - type: 'null'
                    description: Current deployment of the environment
              autoscaling_settings:
                allOf:
                  - $ref: '#/components/schemas/AutoscalingSettingsV1'
                    description: Autoscaling settings for the environment
              promotion_settings:
                allOf:
                  - $ref: '#/components/schemas/PromotionSettingsV1'
                    description: Promotion settings for the environment
              instance_type:
                allOf:
                  - $ref: '#/components/schemas/InstanceTypeV1'
                    description: Instance type for the environment
            title: EnvironmentV1
            description: Environment for oracles.
            refIdentifier: '#/components/schemas/EnvironmentV1'
            requiredProperties:
              - name
              - created_at
              - model_id
              - current_deployment
              - autoscaling_settings
              - promotion_settings
              - instance_type
        examples:
          example:
            value:
              name: <string>
              created_at: '2023-11-07T05:31:56Z'
              model_id: <string>
              current_deployment:
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
              autoscaling_settings:
                min_replica: 123
                max_replica: 123
                autoscaling_window: 123
                scale_down_delay: 123
                concurrency_target: 123
                target_utilization_percentage: 123
              promotion_settings:
                redeploy_on_promotion: true
                rolling_deploy: true
                ramp_up_while_promoting: true
                ramp_up_duration_seconds: 600
              instance_type:
                id: <string>
                name: <string>
                memory_limit_mib: 123
                millicpu_limit: 123
                gpu_count: 123
                gpu_type: <string>
                gpu_memory_limit_mib: 123
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
    DeploymentV1:
      description: A deployment of a model.
      properties:
        id:
          description: Unique identifier of the deployment
          title: Id
          type: string
        created_at:
          description: Time the deployment was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the deployment
          title: Name
          type: string
        model_id:
          description: Unique identifier of the model
          title: Model Id
          type: string
        is_production:
          description: Whether the deployment is the production deployment of the model
          title: Is Production
          type: boolean
        is_development:
          description: Whether the deployment is the development deployment of the model
          title: Is Development
          type: boolean
        status:
          $ref: '#/components/schemas/DeploymentStatusV1'
          description: Status of the deployment
        active_replica_count:
          description: Number of active replicas
          title: Active Replica Count
          type: integer
        autoscaling_settings:
          anyOf:
            - $ref: '#/components/schemas/AutoscalingSettingsV1'
            - type: 'null'
          description: >-
            Autoscaling settings for the deployment. If null, the model has not
            finished deploying
        instance_type_name:
          anyOf:
            - type: string
            - type: 'null'
          description: Name of the instance type the model deployment is running on
          title: Instance Type Name
        environment:
          anyOf:
            - type: string
            - type: 'null'
          description: The environment associated with the deployment
          title: Environment
      required:
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
      title: DeploymentV1
      type: object
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
    UpdatePromotionSettingsV1:
      description: Promotion settings for model promotion
      properties:
        redeploy_on_promotion:
          anyOf:
            - type: boolean
            - type: 'null'
          default: null
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
          default: null
          description: Whether the environment should rely on rolling deploy orchestration.
          examples:
            - true
          title: Rolling Deploy
        ramp_up_while_promoting:
          anyOf:
            - type: boolean
            - type: 'null'
          default: null
          description: Whether to ramp up traffic while promoting
          examples:
            - true
          title: Ramp Up While Promoting
        ramp_up_duration_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: Duration of the ramp up in seconds
          examples:
            - 600
          title: Ramp Up Duration Seconds
      title: UpdatePromotionSettingsV1
      type: object

````