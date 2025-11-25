# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment.md

# Source: https://docs.fireworks.ai/api-reference/delete-deployment.md

# Delete Deployment

## OpenAPI

````yaml delete /v1/accounts/{account_id}/deployments/{deployment_id}
paths:
  path: /v1/accounts/{account_id}/deployments/{deployment_id}
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
        deployment_id:
          schema:
            - type: string
              required: true
              description: The Deployment Id
      query:
        hard:
          schema:
            - type: boolean
              required: false
              description: If true, this will perform a hard deletion.
        ignoreChecks:
          schema:
            - type: boolean
              required: false
              description: >-
                If true, this will ignore checks and force the deletion of a
                deployment that is currently

                deployed and is in use.
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