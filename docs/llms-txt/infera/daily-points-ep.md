# Source: https://docs.infera.org/api-reference/endpoint/daily-points-ep.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Daily Points Ep

> Endpoint to fetch daily points for a specific node by making a request to the storage service.

:param request: Request payload containing node_name and last_days.
:return: List of daily points for the specified node fetched from the storage service.



## OpenAPI

````yaml post /daily_points
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /daily_points:
    post:
      summary: Daily Points Ep
      description: >-
        Endpoint to fetch daily points for a specific node by making a request
        to the storage service.


        :param request: Request payload containing node_name and last_days.

        :return: List of daily points for the specified node fetched from the
        storage service.
      operationId: daily_points_ep_daily_points_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DailyPointsRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/DailyPoints'
                type: array
                title: Response Daily Points Ep Daily Points Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
components:
  schemas:
    DailyPointsRequest:
      properties:
        node_name:
          type: string
          title: Node Name
        last_days:
          type: integer
          title: Last Days
      type: object
      required:
        - node_name
        - last_days
      title: DailyPointsRequest
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````