# Source: https://docs.infera.org/api-reference/endpoint/update-result.md

# Update Result

## OpenAPI

````yaml post /worker/update_result
paths:
  path: /worker/update_result
  method: post
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              job_id:
                allOf:
                  - type: string
                    title: Job Id
              api_key:
                allOf:
                  - type: string
                    title: Api Key
              model_name:
                allOf:
                  - type: string
                    title: Model Name
              result:
                allOf:
                  - type: object
                    title: Result
              status:
                allOf:
                  - type: string
                    title: Status
            required: true
            title: JobResult
            refIdentifier: '#/components/schemas/JobResult'
            requiredProperties:
              - job_id
              - api_key
              - model_name
              - result
              - status
        examples:
          example:
            value:
              job_id: <string>
              api_key: <string>
              model_name: <string>
              result: {}
              status: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
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
                    type: array
                    title: Detail
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
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````