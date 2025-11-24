# Source: https://mintlify.com/docs/api/update/trigger.md

# Trigger update

> Queue a deployment update for your documentation project. Returns a status ID that can be used to track the update progress. By default, the update is triggered from your configured deployment branch.

## OpenAPI

````yaml POST /project/update/{projectId}
paths:
  path: /project/update/{projectId}
  method: post
  servers:
    - url: https://api.mintlify.com/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        projectId:
          schema:
            - type: string
              required: true
              description: >-
                Your project ID. Can be copied from the [API
                keys](https://dashboard.mintlify.com/settings/organization/api-keys)
                page in your dashboard.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              statusId:
                allOf:
                  - type: string
                    description: The status ID of the triggered updated.
        examples:
          example:
            value:
              statusId: <string>
        description: A successful response
  deprecated: false
  type: path
components:
  schemas: {}

````