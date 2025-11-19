# Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings.md

# Any model deployment by ID

> Updates a deployment's autoscaling settings and returns the update status.

## OpenAPI

````yaml patch /v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings
paths:
  path: /v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings
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
        deployment_id:
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
              min_replica:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Minimum number of replicas
                    examples:
                      - 0
                    title: Min Replica
              max_replica:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Maximum number of replicas
                    examples:
                      - 7
                    title: Max Replica
              autoscaling_window:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Timeframe of traffic considered for autoscaling decisions
                    examples:
                      - 600
                    title: Autoscaling Window
              scale_down_delay:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Waiting period before scaling down any active replica
                    examples:
                      - 120
                    title: Scale Down Delay
              concurrency_target:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Number of requests per replica before scaling up
                    examples:
                      - 2
                    title: Concurrency Target
              target_utilization_percentage:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    default: null
                    description: Target utilization percentage for scaling up/down.
                    examples:
                      - 70
                    title: Target Utilization Percentage
            required: true
            title: UpdateAutoscalingSettingsV1
            description: >-
              A request to update autoscaling settings for a deployment. All
              fields are optional, and we only update ones passed in.
            refIdentifier: '#/components/schemas/UpdateAutoscalingSettingsV1'
            additionalProperties: false
        examples:
          example:
            value:
              min_replica: 0
              max_replica: 7
              autoscaling_window: 600
              scale_down_delay: 120
              concurrency_target: 2
              target_utilization_percentage: 70
    codeSamples:
      - lang: bash
        source: >-
          curl --request PATCH \

          --url
          https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY" \

          --data '{
            "min_replica": 0,
            "max_replica": 7,
            "autoscaling_window": 600,
            "scale_down_delay": 120,
            "concurrency_target": 2,
            "target_utilization_percentage": 70
          }'
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "PATCH",
              url,
              headers=headers,
              json={'min_replica': 0, 'max_replica': 7, 'autoscaling_window': 600, 'scale_down_delay': 120, 'concurrency_target': 2, 'target_utilization_percentage': 70}
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
    UpdateAutoscalingSettingsStatusV1:
      description: The status of a request to update autoscaling settings.
      enum:
        - ACCEPTED
        - QUEUED
        - UNCHANGED
      title: UpdateAutoscalingSettingsStatusV1
      type: string

````