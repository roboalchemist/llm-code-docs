# Source: https://www.activepieces.com/docs/endpoints/sample-data/get.md

# Source: https://www.activepieces.com/docs/endpoints/folders/get.md

# Source: https://www.activepieces.com/docs/endpoints/flows/get.md

# Source: https://www.activepieces.com/docs/endpoints/flow-templates/get.md

# Source: https://www.activepieces.com/docs/endpoints/flow-runs/get.md

# Get Flow Run

> Get Flow Run

## OpenAPI

````yaml GET /v1/flow-runs/{id}
paths:
  path: /v1/flow-runs/{id}
  method: get
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Use your api key generated from the admin console
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              created:
                allOf:
                  - type: string
              updated:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              flowId:
                allOf:
                  - type: string
              parentRunId:
                allOf:
                  - type: string
              failParentOnFailure:
                allOf:
                  - type: boolean
              tags:
                allOf:
                  - type: array
                    items:
                      type: string
              flowVersionId:
                allOf:
                  - type: string
              flowVersion:
                allOf:
                  - type: object
                    properties:
                      displayName:
                        type: string
              logsFileId:
                allOf:
                  - type: string
                    nullable: true
              tasks:
                allOf:
                  - type: number
              status:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - FAILED
                      - type: string
                        enum:
                          - QUOTA_EXCEEDED
                      - type: string
                        enum:
                          - INTERNAL_ERROR
                      - type: string
                        enum:
                          - PAUSED
                      - type: string
                        enum:
                          - QUEUED
                      - type: string
                        enum:
                          - RUNNING
                      - type: string
                        enum:
                          - SUCCEEDED
                      - type: string
                        enum:
                          - MEMORY_LIMIT_EXCEEDED
                      - type: string
                        enum:
                          - TIMEOUT
              duration:
                allOf:
                  - type: number
              startTime:
                allOf:
                  - type: string
              finishTime:
                allOf:
                  - type: string
              environment:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - PRODUCTION
                      - type: string
                        enum:
                          - TESTING
              steps:
                allOf:
                  - type: object
                    nullable: true
                    additionalProperties: {}
              failedStepName:
                allOf:
                  - type: string
              stepNameToTest:
                allOf:
                  - type: string
            requiredProperties:
              - id
              - created
              - updated
              - projectId
              - flowId
              - failParentOnFailure
              - flowVersionId
              - status
              - startTime
              - environment
        examples:
          example:
            value:
              id: <string>
              created: <string>
              updated: <string>
              projectId: <string>
              flowId: <string>
              parentRunId: <string>
              failParentOnFailure: true
              tags:
                - <string>
              flowVersionId: <string>
              flowVersion:
                displayName: <string>
              logsFileId: <string>
              tasks: 123
              status: FAILED
              duration: 123
              startTime: <string>
              finishTime: <string>
              environment: PRODUCTION
              steps: {}
              failedStepName: <string>
              stepNameToTest: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````