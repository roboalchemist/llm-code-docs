# Source: https://docs.datafold.com/api-reference/ci/list-ci-runs.md

# List CI runs

## OpenAPI

````yaml get /api/v1/ci/{ci_config_id}/runs
paths:
  path: /api/v1/ci/{ci_config_id}/runs
  method: get
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path:
        ci_config_id:
          schema:
            - type: integer
              required: true
              title: CI config id
      query:
        pr_sha:
          schema:
            - type: string
              required: false
              title: Pr Sha
            - type: 'null'
              required: false
              title: Pr Sha
        pr_num:
          schema:
            - type: string
              required: false
              title: Pr Num
            - type: 'null'
              required: false
              title: Pr Num
        limit:
          schema:
            - type: integer
              required: false
              title: Limit
              default: 100
        offset:
          schema:
            - type: integer
              required: false
              title: Offset
              default: 0
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/ApiCiRun'
            title: Response Get Ci Api V1 Ci  Ci Config Id  Runs Get
        examples:
          example:
            value:
              - base_branch: <string>
                base_sha: <string>
                id: 123
                pr_branch: <string>
                pr_num: <string>
                pr_sha: <string>
                source: <string>
                status: <string>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    title: Detail
                    type: array
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    ApiCiRun:
      properties:
        base_branch:
          title: Base Branch
          type: string
        base_sha:
          title: Base Sha
          type: string
        id:
          title: Id
          type: integer
        pr_branch:
          title: Pr Branch
          type: string
        pr_num:
          title: Pr Num
          type: string
        pr_sha:
          title: Pr Sha
          type: string
        source:
          title: Source
          type: string
        status:
          title: Status
          type: string
      required:
        - id
        - base_branch
        - base_sha
        - pr_branch
        - pr_sha
        - pr_num
        - status
        - source
      title: ApiCiRun
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object

````