# Source: https://docs.fireworks.ai/api-reference-dlde/delete-node-pool-binding.md

# Delete Node Pool Binding

## OpenAPI

````yaml post /v1/accounts/{account_id}/nodePoolBindings:delete
paths:
  path: /v1/accounts/{account_id}/nodePoolBindings:delete
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
                  - type: string
                    description: >-
                      The principal that is allowed use the node pool. This must
                      be

                      the email address of the user.
            required: true
            title: |-
              The node pool binding being deleted.
              Must specify account_id, cluster_id, node_pool_id, and principal.
        examples:
          example:
            value:
              principal: <string>
        description: |-
          The node pool binding being deleted.
          Must specify account_id, cluster_id, node_pool_id, and principal.
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