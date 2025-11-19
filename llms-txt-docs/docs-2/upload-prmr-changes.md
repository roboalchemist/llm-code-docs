# Source: https://docs.datafold.com/api-reference/ci/upload-prmr-changes.md

# Upload PR/MR changes

## OpenAPI

````yaml post /api/v1/ci/{ci_config_id}/{pr_num}
paths:
  path: /api/v1/ci/{ci_config_id}/{pr_num}
  method: post
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
        pr_num:
          schema:
            - type: integer
              required: true
              title: Pull request/Merge request number
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/CiDiff'
            required: true
            title: Diffs
        examples:
          example:
            value:
              - exclude_columns: []
                include_columns: []
                pk:
                  - <string>
                pr: <string>
                prod: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              ci_run_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Ci Run Id
              run_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Run Id
            title: SubmitCiJob
            refIdentifier: '#/components/schemas/SubmitCiJob'
        examples:
          example:
            value:
              ci_run_id: 123
              run_id: 123
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
    CiDiff:
      properties:
        exclude_columns:
          default: []
          items:
            type: string
          title: Exclude Columns
          type: array
        include_columns:
          default: []
          items:
            type: string
          title: Include Columns
          type: array
        pk:
          anyOf:
            - items:
                type: string
              type: array
              uniqueItems: true
            - type: 'null'
          title: Pk
        pr:
          title: Pr
          type: string
        prod:
          title: Prod
          type: string
      required:
        - prod
        - pr
      title: CiDiff
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