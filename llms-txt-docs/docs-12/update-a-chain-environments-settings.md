# Source: https://docs.baseten.co/reference/management-api/environments/update-a-chain-environments-settings.md

# Update Chain environment

> Update a chain environment's settings and returns the chain environment.

## OpenAPI

````yaml patch /v1/chains/{chain_id}/environments/{env_name}
paths:
  path: /v1/chains/{chain_id}/environments/{env_name}
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
                        redeploy_on_promotion: false
                        rolling_deploy: false
            required: true
            title: UpdateChainEnvironmentRequestV1
            description: A request to update a chain environment.
            refIdentifier: '#/components/schemas/UpdateChainEnvironmentRequestV1'
        examples:
          example:
            value:
              promotion_settings:
                ramp_up_duration_seconds: 600
                ramp_up_while_promoting: true
                redeploy_on_promotion: false
                rolling_deploy: false
    codeSamples:
      - lang: bash
        source: >-
          curl --request PATCH \

          --url
          https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name} \

          --header "Authorization: Api-Key $BASETEN_API_KEY" \

          --data '{
            "promotion_settings": {
              "ramp_up_duration_seconds": 600,
              "ramp_up_while_promoting": true,
              "redeploy_on_promotion": false,
              "rolling_deploy": false
            }
          }'
      - lang: python
        source: >-
          import requests

          import os

          API_KEY = os.environ.get("BASETEN_API_KEY", "<YOUR_API_KEY>")

          url =
          "https://api.baseten.co/v1/chains/{chain_id}/environments/{env_name}"


          headers = {"Authorization": f"Api-Key {API_KEY}"}


          response = requests.request(
              "PATCH",
              url,
              headers=headers,
              json={'promotion_settings': {'ramp_up_duration_seconds': 600, 'ramp_up_while_promoting': True, 'redeploy_on_promotion': False, 'rolling_deploy': False}}
          )


          print(response.text)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              ok:
                allOf:
                  - description: Whether the update was successful
                    title: Ok
                    type: boolean
            title: UpdateChainEnvironmentResponseV1
            description: A response to update a chain environment.
            refIdentifier: '#/components/schemas/UpdateChainEnvironmentResponseV1'
            requiredProperties:
              - ok
        examples:
          example:
            value:
              ok: true
        description: A response to update a chain environment.
  deprecated: false
  type: path
components:
  schemas:
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