# Source: https://docs.fireworks.ai/api-reference-dlde/get-cluster-connection-info.md

# Get Cluster Connection Info

> Retrieve connection settings for the cluster to be put in kubeconfig

## OpenAPI

````yaml get /v1/accounts/{account_id}/clusters/{cluster_id}:getConnectionInfo
paths:
  path: /v1/accounts/{account_id}/clusters/{cluster_id}:getConnectionInfo
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
        cluster_id:
          schema:
            - type: string
              required: true
              description: The Cluster Id
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
              endpoint:
                allOf:
                  - type: string
                    description: The cluster's Kubernetes API server endpoint.
              caData:
                allOf:
                  - type: string
                    description: Base64-encoded cluster's CA certificate.
            refIdentifier: '#/components/schemas/gatewayClusterConnectionInfo'
        examples:
          example:
            value:
              endpoint: <string>
              caData: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````