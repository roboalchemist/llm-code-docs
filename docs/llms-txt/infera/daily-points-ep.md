# Source: https://docs.infera.org/api-reference/endpoint/daily-points-ep.md

# Daily Points Ep

> Endpoint to fetch daily points for a specific node by making a request to the storage service.

:param request: Request payload containing node_name and last_days.
:return: List of daily points for the specified node fetched from the storage service.

## OpenAPI

````yaml post /daily_points
paths:
  path: /daily_points
  method: post
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security:
      - title: APIKeyHeader
        parameters:
          query: {}
          header:
            api_key:
              type: apiKey
          cookie: {}
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
              node_name:
                allOf:
                  - type: string
                    title: Node Name
              last_days:
                allOf:
                  - type: integer
                    title: Last Days
            required: true
            title: DailyPointsRequest
            refIdentifier: '#/components/schemas/DailyPointsRequest'
            requiredProperties:
              - node_name
              - last_days
        examples:
          example:
            value:
              node_name: <string>
              last_days: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/DailyPoints'
            title: Response Daily Points Ep Daily Points Post
        examples:
          example:
            value:
              - date: <any>
                points: 123
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
    DailyPoints:
      properties:
        date:
          title: Date
        points:
          type: number
          title: Points
      type: object
      required:
        - date
        - points
      title: DailyPoints
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