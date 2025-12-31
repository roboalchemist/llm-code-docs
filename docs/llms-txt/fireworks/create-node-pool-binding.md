# Source: https://docs.fireworks.ai/api-reference-dlde/create-node-pool-binding.md

# Create Node Pool Binding

## OpenAPI

````yaml post /v1/accounts/{account_id}/nodePoolBindings
paths:
  path: /v1/accounts/{account_id}/nodePoolBindings
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              principal:
                allOf:
                  - &ref_0
                    type: string
                    description: >-
                      The principal that is allowed use the node pool. This must
                      be

                      the email address of the user.
            required: true
            refIdentifier: '#/components/schemas/gatewayNodePoolBinding'
            requiredProperties: &ref_1
              - principal
        examples:
          example:
            value:
              principal: <string>
        description: The properties of the node pool binding being created.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              accountId:
                allOf:
                  - type: string
                    description: The account ID that this binding is associated with.
                    readOnly: true
              clusterId:
                allOf:
                  - type: string
                    description: The cluster ID that this binding is associated with.
                    readOnly: true
              nodePoolId:
                allOf:
                  - type: string
                    description: The node pool ID that this binding is associated with.
                    readOnly: true
              createTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The creation time of the node pool binding.
                    readOnly: true
              principal:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/gatewayNodePoolBinding'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              accountId: <string>
              clusterId: <string>
              nodePoolId: <string>
              createTime: '2023-11-07T05:31:56Z'
              principal: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````