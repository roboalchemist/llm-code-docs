# Source: https://docs.datafold.com/api-reference/monitors/toggle-a-monitor.md

# Toggle a Monitor

## OpenAPI

````yaml openapi-public.json put /api/v1/monitors/{id}/toggle
paths:
  path: /api/v1/monitors/{id}/toggle
  method: put
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
              description: The unique identifier of the monitor.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              enabled:
                allOf:
                  - description: Indicate whether to enable or disable the monitor.
                    title: Enabled
                    type: boolean
            required: true
            title: Body_toggle_monitor_on_off_api_v1_monitors__id__toggle_put
            refIdentifier: >-
              #/components/schemas/Body_toggle_monitor_on_off_api_v1_monitors__id__toggle_put
            requiredProperties:
              - enabled
        examples:
          example:
            value:
              enabled: true
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