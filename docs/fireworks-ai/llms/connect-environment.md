# Source: https://docs.fireworks.ai/api-reference-dlde/connect-environment.md

# Connect Environment

> Connects the environment to a node pool.
Returns an error if there is an existing pending connection.

## OpenAPI

````yaml post /v1/accounts/{account_id}/environments/{environment_id}:connect
paths:
  path: /v1/accounts/{account_id}/environments/{environment_id}:connect
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
              connection:
                allOf:
                  - $ref: '#/components/schemas/gatewayEnvironmentConnection'
              vscodeVersion:
                allOf:
                  - type: string
                    title: >-
                      VSCode version on the client side that initiated the
                      connect request
            required: true
            refIdentifier: '#/components/schemas/GatewayConnectEnvironmentBody'
            requiredProperties:
              - connection
        examples:
          example:
            value:
              connection:
                nodePoolId: <string>
                numRanks: 123
                role: <string>
                useLocalStorage: true
              vscodeVersion: <string>
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
  schemas:
    gatewayEnvironmentConnection:
      type: object
      properties:
        nodePoolId:
          type: string
          description: The resource id of the node pool the environment is connected to.
        numRanks:
          type: integer
          format: int32
          description: |-
            For GPU node pools: one GPU per rank w/ host packing,
            for CPU node pools: one host per rank.
            If not specified, the default is 1.
        role:
          type: string
          description: |-
            The ARN of the AWS IAM role that the connection should assume.
            If not specified, the connection will fall back to the node
            pool's node_role.
        zone:
          type: string
          description: >-
            Current for the last zone that this environment is connected to. We

            want to warn the users about cross zone migration latency when they
            are

            connecting to node pool in a different zone as their persistent
            volume.
          readOnly: true
        useLocalStorage:
          type: boolean
          description: >-
            If true, the node's local storage will be mounted on /tmp. This flag
            has

            no effect if the node does not have local storage.
      title: 'Next ID: 8'
      required:
        - nodePoolId

````