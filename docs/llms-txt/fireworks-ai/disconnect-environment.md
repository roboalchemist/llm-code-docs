# Source: https://docs.fireworks.ai/api-reference-dlde/disconnect-environment.md

# Disconnect Environment

> Disconnects the environment from the node pool. Returns an error
if the environment is not connected to a node pool.

## OpenAPI

````yaml post /v1/accounts/{account_id}/environments/{environment_id}:disconnect
paths:
  path: /v1/accounts/{account_id}/environments/{environment_id}:disconnect
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
        environment_id:
          schema:
            - type: string
              required: true
              description: The Environment Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              force:
                allOf:
                  - type: boolean
                    description: >-
                      Disconnect the environment even if snapshotting fails
                      (e.g. due to pod

                      failure). This flag should only be used if you are certain
                      that the pod

                      is gone.
              resetSnapshots:
                allOf:
                  - type: boolean
                    description: >-
                      Forces snapshots to be rebuilt.

                      This can be used when there are too many snapshot layers

                      or when an unforeseen snapshotting logic error has
                      occurred.
            required: true
            refIdentifier: '#/components/schemas/GatewayDisconnectEnvironmentBody'
        examples:
          example:
            value:
              force: true
              resetSnapshots: true
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