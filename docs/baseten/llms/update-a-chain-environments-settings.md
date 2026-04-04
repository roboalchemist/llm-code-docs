# Source: https://docs.baseten.co/reference/management-api/environments/update-a-chain-environments-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Chain environment

> Update a chain environment's settings and returns the chain environment.



## OpenAPI

````yaml patch /v1/chains/{chain_id}/environments/{env_name}
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/chains/{chain_id}/environments/{env_name}:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/env_name'
    patch:
      summary: Update a chain environment's settings
      description: Update a chain environment's settings and returns the chain environment.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateChainEnvironmentRequestV1'
        required: true
      responses:
        '200':
          description: A response to update a chain environment.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateChainEnvironmentResponseV1'
components:
  parameters:
    chain_id:
      schema:
        type: string
      name: chain_id
      in: path
      required: true
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    UpdateChainEnvironmentRequestV1:
      description: A request to update a chain environment.
      properties:
        promotion_settings:
          anyOf:
            - $ref: '#/components/schemas/UpdatePromotionSettingsV1'
            - type: 'null'
          default: null
          description: Promotion settings for the environment
          examples:
            - ramp_up_duration_seconds: 600
              ramp_up_while_promoting: true
              redeploy_on_promotion: null
              rolling_deploy: null
              rolling_deploy_config: null
      title: UpdateChainEnvironmentRequestV1
      type: object
    UpdateChainEnvironmentResponseV1:
      description: A response to update a chain environment.
      properties:
        ok:
          description: Whether the update was successful
          title: Ok
          type: boolean
      required:
        - ok
      title: UpdateChainEnvironmentResponseV1
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
        rolling_deploy_config:
          anyOf:
            - $ref: '#/components/schemas/UpdateRollingDeployConfigV1'
            - type: 'null'
          default: null
          description: Rolling deploy configuration for promotions
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
    UpdateRollingDeployConfigV1:
      description: Rolling deploy config for promoting chains and oracles
      properties:
        rolling_deploy_strategy:
          anyOf:
            - $ref: '#/components/schemas/RollingDeployStrategyV1'
            - type: 'null'
          default: null
          description: The rolling deploy strategy to use for promotions.
          examples:
            - REPLICA
        max_surge_percent:
          anyOf:
            - type: integer
            - type: 'null'
          default: 20
          description: The maximum surge percentage for rolling deploys.
          examples:
            - 20
          title: Max Surge Percent
        max_unavailable_percent:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: The maximum unavailable percentage for rolling deploys.
          examples:
            - 20
          title: Max Unavailable Percent
        stabilization_time_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: The stabilization time in seconds for rolling deploys.
          examples:
            - 300
          title: Stabilization Time Seconds
        promotion_cleanup_strategy:
          anyOf:
            - $ref: '#/components/schemas/PromotionCleanupStrategyV1'
            - type: 'null'
          default: null
          description: The promotion cleanup strategy to use for rolling deploys.
          examples:
            - SCALE_TO_ZERO
      title: UpdateRollingDeployConfigV1
      type: object
    RollingDeployStrategyV1:
      description: The rolling deploy strategy.
      enum:
        - REPLICA
      title: RollingDeployStrategyV1
      type: string
    PromotionCleanupStrategyV1:
      description: The promotion cleanup strategy.
      enum:
        - KEEP
        - SCALE_TO_ZERO
      title: PromotionCleanupStrategyV1
      type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````