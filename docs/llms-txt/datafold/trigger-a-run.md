# Source: https://docs.datafold.com/api-reference/monitors/trigger-a-run.md

# Trigger a run

## OpenAPI

````yaml openapi-public.json post /api/v1/monitors/{id}/run
paths:
  path: /api/v1/monitors/{id}/run
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
        id:
          schema:
            - type: integer
              required: true
              title: Id
              description: The unique identifier of the monitor for which to start the run.
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
              run_id:
                allOf:
                  - description: Unique identifier for the monitor run result.
                    title: Run Id
                    type: integer
            title: ApiPublicMonitorTriggerRunResultOut
            refIdentifier: '#/components/schemas/ApiPublicMonitorTriggerRunResultOut'
            requiredProperties:
              - run_id
        examples:
          example:
            value:
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