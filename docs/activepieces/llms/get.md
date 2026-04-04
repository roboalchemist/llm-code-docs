# Source: https://www.activepieces.com/docs/endpoints/templates/get.md

# Source: https://www.activepieces.com/docs/endpoints/sample-data/get.md

# Source: https://www.activepieces.com/docs/endpoints/folders/get.md

# Source: https://www.activepieces.com/docs/endpoints/flows/get.md

# Source: https://www.activepieces.com/docs/endpoints/flow-runs/get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Flow Run

> Get Flow Run



## OpenAPI

````yaml GET /v1/flow-runs/{id}
openapi: 3.0.3
info:
  title: Activepieces Documentation
  version: 0.0.0
servers:
  - url: https://cloud.activepieces.com/api
    description: Production Server
security: []
externalDocs:
  url: https://www.activepieces.com/docs
  description: Find more info here
paths:
  /v1/flow-runs/{id}:
    get:
      tags:
        - flow-runs
      description: Get Flow Run
      parameters:
        - schema:
            pattern: ^[0-9a-zA-Z]{21}$
            type: string
          in: path
          name: id
          required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  created:
                    type: string
                  updated:
                    type: string
                  projectId:
                    type: string
                  flowId:
                    type: string
                  parentRunId:
                    type: string
                  failParentOnFailure:
                    type: boolean
                  triggeredBy:
                    type: string
                  tags:
                    type: array
                    items:
                      type: string
                  flowVersionId:
                    type: string
                  flowVersion:
                    type: object
                    properties:
                      displayName:
                        type: string
                  logsFileId:
                    type: string
                    nullable: true
                  status:
                    anyOf:
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
                      - type: string
                        enum:
                          - CANCELED
                  startTime:
                    type: string
                  finishTime:
                    type: string
                  environment:
                    anyOf:
                      - type: string
                        enum:
                          - PRODUCTION
                      - type: string
                        enum:
                          - TESTING
                  steps:
                    type: object
                    nullable: true
                    additionalProperties: {}
                  failedStep:
                    type: object
                    properties:
                      name:
                        type: string
                      displayName:
                        type: string
                    required:
                      - name
                      - displayName
                  stepNameToTest:
                    type: string
                  archivedAt:
                    default: null
                    type: string
                    nullable: true
                  stepsCount:
                    type: number
                required:
                  - id
                  - created
                  - updated
                  - projectId
                  - flowId
                  - failParentOnFailure
                  - flowVersionId
                  - status
                  - environment
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````