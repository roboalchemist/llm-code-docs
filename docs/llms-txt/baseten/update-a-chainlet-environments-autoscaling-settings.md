# Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/update-a-chainlet-environments-autoscaling-settings.md

# Update chainlet environment's autoscaling settings

> Updates a chainlet environment's autoscaling settings and returns the updated chainlet environment settings.

## OpenAPI

````yaml patch /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
paths:
  path: >-
    /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
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
        chain_id:
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
              updates:
                allOf:
                  - description: >-
                      Mapping of chainlet name to the desired chainlet
                      autoscaling settings. If the chainlet name doesn't exist,
                      an error is returned.
                    examples:
                      - - autoscaling_settings:
                            autoscaling_window: 800
                            concurrency_target: 4
                            max_replica: 3
                            min_replica: 2
                            scale_down_delay: 63
                            target_utilization_percentage: null
                          chainlet_name: HelloWorld
                      - - autoscaling_settings:
                            autoscaling_window: null
                            concurrency_target: null
                            max_replica: null
                            min_replica: 0
                            scale_down_delay: null
                            target_utilization_percentage: null
                          chainlet_name: HelloWorld
                        - autoscaling_settings:
                            autoscaling_window: null
                            concurrency_target: null
                            max_replica: null
                            min_replica: 0
                            scale_down_delay: null
                            target_utilization_percentage: null
                          chainlet_name: RandInt
                    items:
                      $ref: >-
                        #/components/schemas/ChainletEnvironmentAutoscalingSettingsUpdateV1
                    title: Updates
                    type: array
            required: true
            title: UpdateChainletEnvironmentAutoscalingSettingsRequestV1
            description: >-
              A request to update the autoscaling settings for a multiple
              chainlets in an environment.

              If a chainlet name doesn't exist, an error is returned.
            refIdentifier: >-
              #/components/schemas/UpdateChainletEnvironmentAutoscalingSettingsRequestV1
            requiredProperties:
              - updates
        examples:
          example:
            value:
              updates:
                - autoscaling_settings:
                    autoscaling_window: 800
                    concurrency_target: 4
                    max_replica: 3
                    min_replica: 2
                    scale_down_delay: 63
                    target_utilization_percentage: null
                  chainlet_name: HelloWorld
    codeSamples:
      - lang: bash
        source: >-
          curl --request PATCH \

          --url
          https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
          \

          --header "Authorization: Api-Key $BASETEN_API_KEY" \

          --data '{
            "updates": [
              {
                "autoscaling_settings": {
                  "autoscaling_window": 800,
                  "concurrency_target": 4,
                  "max_replica": 3,
                  "min_replica": 2,
                  "scale_down_delay": 63,
                  "target_utilization_percentage": null
                },
                "chainlet_name": "HelloWorld"
              }
            ]
          }'
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "PATCH",
              url,
              headers=headers,
              json={'updates': [{'autoscaling_settings': {'autoscaling_window': 800, 'concurrency_target': 4, 'max_replica': 3, 'min_replica': 2, 'scale_down_delay': 63, 'target_utilization_percentage': None}, 'chainlet_name': 'HelloWorld'}]}
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
    ChainletEnvironmentAutoscalingSettingsUpdateV1:
      description: The request to update the autoscaling settings for a chainlet.
      properties:
        chainlet_name:
          description: Name of the chainlet
          examples:
            - HelloWorld
          title: Chainlet Name
          type: string
        autoscaling_settings:
          $ref: '#/components/schemas/UpdateAutoscalingSettingsV1'
          description: Autoscaling settings for the chainlet
          examples:
            - autoscaling_window: 800
              concurrency_target: 3
              max_replica: 2
              min_replica: 1
              scale_down_delay: 60
              target_utilization_percentage: null
      required:
        - chainlet_name
        - autoscaling_settings
      title: ChainletEnvironmentAutoscalingSettingsUpdateV1
      type: object

````