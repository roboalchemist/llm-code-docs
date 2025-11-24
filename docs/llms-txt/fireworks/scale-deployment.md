# Source: https://docs.fireworks.ai/api-reference/scale-deployment.md

# Scale Deployment to a specific number of replicas or to zero

## OpenAPI

````yaml patch /v1/accounts/{account_id}/deployments/{deployment_id}:scale
paths:
  path: /v1/accounts/{account_id}/deployments/{deployment_id}:scale
  method: patch
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
        deployment_id:
          schema:
            - type: string
              required: true
              description: The Deployment Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              replicaCount:
                allOf:
                  - type: integer
                    format: int32
                    description: The desired number of replicas.
            required: true
            refIdentifier: '#/components/schemas/GatewayScaleDeploymentBody'
        examples:
          example:
            value:
              replicaCount: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````