# Source: https://docs.baseten.co/reference/management-api/environments/update-an-environments-settings.md

# Update model environment

> Updates an environment's settings and returns the updated environment.

## OpenAPI

````yaml patch /v1/models/{model_id}/environments/{env_name}
paths:
  path: /v1/models/{model_id}/environments/{env_name}
  method: patch
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
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
                        rolling_deploy: null
            required: true
            title: UpdateEnvironmentRequestV1
            description: A request to update an environment.
            refIdentifier: '#/components/schemas/UpdateEnvironmentRequestV1'
            additionalProperties: false
        examples:
          example:
            value:
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
                rolling_deploy: null
    codeSamples:
      - lang: bash
        source: >-
          curl --request PATCH \

          --url
          https://api.baseten.co/v1/models/{model_id}/environments/{env_name} \

          --header "Authorization: Api-Key $BASETEN_API_KEY" \

          --data '{
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
              "rolling_deploy": null
            }
          }'
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/models/{model_id}/environments/{env_name}"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "PATCH",
              url,
              headers=headers,
              json={'autoscaling_settings': {'autoscaling_window': 800, 'concurrency_target': 3, 'max_replica': 2, 'min_replica': 1, 'scale_down_delay': 60, 'target_utilization_percentage': None}, 'promotion_settings': {'ramp_up_duration_seconds': 600, 'ramp_up_while_promoting': True, 'redeploy_on_promotion': True, 'rolling_deploy': None}}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - $ref: '#/components/schemas/UpdateAutoscalingSettingsStatusV1'
                    description: Status of the request to update autoscaling settings
              message:
                allOf:
                  - description: >-
                      A message describing the status of the request to update
                      autoscaling settings
                    title: Message
                    type: string
            title: UpdateAutoscalingSettingsResponseV1
            description: The response to a request to update autoscaling settings.
            refIdentifier: '#/components/schemas/UpdateAutoscalingSettingsResponseV1'
            requiredProperties:
              - status
              - message
        examples:
          example:
            value:
              status: ACCEPTED
              message: <string>
        description: The response to a request to update autoscaling settings.
  deprecated: false
  type: path
components:
  schemas:
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
    UpdateAutoscalingSettingsStatusV1:
      description: The status of a request to update autoscaling settings.
      enum:
        - ACCEPTED
        - QUEUED
        - UNCHANGED
      title: UpdateAutoscalingSettingsStatusV1
      type: string
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