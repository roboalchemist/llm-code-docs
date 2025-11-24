# Source: https://docs.fireworks.ai/api-reference-dlde/get-node-pool-stats.md

# Get Node Pool Stats

## OpenAPI

````yaml get /v1/accounts/{account_id}/nodePools/{node_pool_id}:getStats
paths:
  path: /v1/accounts/{account_id}/nodePools/{node_pool_id}:getStats
  method: get
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
        node_pool_id:
          schema:
            - type: string
              required: true
              description: The Node Pool Id
      query:
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              nodeCount:
                allOf:
                  - type: integer
                    format: int32
                    description: The number of nodes currently available in this pool.
              ranksPerNode:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The number of ranks available per node. This is determined
                      by the machine

                      type of the nodes in this node pool.
              environmentCount:
                allOf:
                  - type: integer
                    format: int32
                    description: The number of environments connected to this node pool.
              environmentRanks:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The number of ranks in this node pool that are currently
                      allocated

                      to environment connections.
              batchJobCount:
                allOf:
                  - type: object
                    additionalProperties:
                      type: integer
                      format: int32
                    description: >-
                      The key is the string representation of BatchJob.State
                      (e.g. "RUNNING").

                      The value is the number of batch jobs in that state
                      allocated to this

                      node pool.
              batchJobRanks:
                allOf:
                  - type: object
                    additionalProperties:
                      type: integer
                      format: int32
                    description: >-
                      The key is the string representation of BatchJob.State
                      (e.g. "RUNNING").

                      The value is the number of ranks allocated to batch jobs
                      in that state in

                      this node pool.
            title: 'Next ID: 7'
            refIdentifier: '#/components/schemas/gatewayNodePoolStats'
        examples:
          example:
            value:
              nodeCount: 123
              ranksPerNode: 123
              environmentCount: 123
              environmentRanks: 123
              batchJobCount: {}
              batchJobRanks: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````