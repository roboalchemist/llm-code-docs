# Source: https://docs.fireworks.ai/api-reference-dlde/delete-snapshot.md

# Delete Snapshot

## OpenAPI

````yaml delete /v1/accounts/{account_id}/snapshots/{snapshot_id}
paths:
  path: /v1/accounts/{account_id}/snapshots/{snapshot_id}
  method: delete
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
        snapshot_id:
          schema:
            - type: string
              required: true
              description: The Snapshot Id
      query: {}
      header: {}
      cookie: {}
    body: {}
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