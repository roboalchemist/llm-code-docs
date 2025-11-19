# Source: https://docs.datafold.com/api-reference/ci/trigger-a-prmr-run.md

# Trigger a PR/MR run

## OpenAPI

````yaml post /api/v1/ci/{ci_config_id}/trigger
paths:
  path: /api/v1/ci/{ci_config_id}/trigger
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              base_branch:
                allOf:
                  - title: Base Branch
                    type: string
              base_sha:
                allOf:
                  - title: Base Sha
                    type: string
              pr_branch:
                allOf:
                  - title: Pr Branch
                    type: string
              pr_number:
                allOf:
                  - title: Pr Number
                    type: integer
              pr_sha:
                allOf:
                  - title: Pr Sha
                    type: string
            required: true
            title: APIPrDetails
            refIdentifier: '#/components/schemas/APIPrDetails'
            requiredProperties:
              - pr_number
              - pr_branch
              - base_branch
              - pr_sha
              - base_sha
        examples:
          example:
            value:
              base_branch: <string>
              base_sha: <string>
              pr_branch: <string>
              pr_number: 123
              pr_sha: <string>
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