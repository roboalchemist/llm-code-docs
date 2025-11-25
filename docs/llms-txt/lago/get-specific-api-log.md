# Source: https://getlago.com/docs/api-reference/audit-logs/get-specific-api-log.md

# Retrieve an API log

> This endpoint retrieves an existing api log that represents a request made to the API. The api log is identified by its unique request_id.

## OpenAPI

````yaml GET /api_logs/{request_id}
paths:
  path: /api_logs/{request_id}
  method: get
  servers:
    - url: https://api.getlago.com/api/v1
      description: US Lago cluster
    - url: https://api.eu.getlago.com/api/v1
      description: EU Lago cluster
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        request_id:
          schema:
            - type: string
              required: true
              description: The Request Id of the existing api log.
              example: bdc0eda6-ea52-4f72-a46a-94f47a89b546
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
              api_log:
                allOf:
                  - $ref: '#/components/schemas/ApiLogObject'
            refIdentifier: '#/components/schemas/ApiLog'
            requiredProperties:
              - api_log
        examples:
          example:
            value:
              api_log:
                api_version: v1
                client: Lago Ruby v1.26.0
                http_method: post
                http_status: 200
                logged_at: '2025-03-31T12:31:44Z'
                request_body: >-
                  { "billable_metric": { "name": "Storage", "code": "storage" }
                  }
                request_origin: https://app.lago.dev/
                request_path: /billable_metrics
                created_at: '2022-04-29T08:59:51Z'
                request_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                request_response: '{ "lago_id": "b9155544-e261-4e92-b54e-f65d7609294c", ... }'
        description: Api Log
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 401
              error:
                allOf:
                  - type: string
                    example: Unauthorized
            refIdentifier: '#/components/schemas/ApiErrorUnauthorized'
            requiredProperties:
              - status
              - error
        examples:
          example:
            value:
              status: 401
              error: Unauthorized
        description: Unauthorized error
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    example: 404
              error:
                allOf:
                  - type: string
                    example: Not Found
              code:
                allOf:
                  - type: string
                    example: object_not_found
            refIdentifier: '#/components/schemas/ApiErrorNotFound'
            requiredProperties:
              - status
              - error
              - code
        examples:
          example:
            value:
              status: 404
              error: Not Found
              code: object_not_found
        description: Not Found error
  deprecated: false
  type: path
components:
  schemas:
    ApiLogObject:
      type: object
      required:
        - api_version
        - client
        - http_method
        - http_status
        - logged_at
        - request_body
        - request_origin
        - request_path
        - created_at
        - request_id
      properties:
        api_version:
          type: string
          example: v1
          description: Lago API version used in the request.
        client:
          type: string
          example: Lago Ruby v1.26.0
          description: The client used to make the request to the API.
        http_method:
          type: string
          example: post
          enum:
            - post
            - put
            - delete
          description: This field represents the HTTP method of the request.
        http_status:
          type: integer
          example: 200
          description: This field represents the HTTP status of the requests.
        logged_at:
          type: string
          format: date-time
          example: '2025-03-31T12:31:44Z'
          description: >-
            The logged date of the api log, presented in the ISO 8601 datetime
            format, specifically in Coordinated Universal Time (UTC). It
            provides the precise timestamp of when the event's record was
            created within the Lago application
        request_body:
          type: string
          format: object
          example: '{ "billable_metric": { "name": "Storage", "code": "storage" } }'
        request_origin:
          type: string
          description: This field represents the API origin of the requested URL
          example: https://app.lago.dev/
        request_path:
          type: string
          description: This field represents the API path of the requested URL
          example: /billable_metrics
        created_at:
          type: string
          format: date-time
          example: '2022-04-29T08:59:51Z'
          description: >-
            The creation date of the api log record in the Lago application,
            presented in the ISO 8601 datetime format, specifically in
            Coordinated Universal Time (UTC). It provides the precise timestamp
            of when the event's record was created within the Lago application
        request_id:
          type: string
          format: uuid
          description: Unique identifier for the api log.
          example: 1a901a90-1a90-1a90-1a90-1a901a901a90
        request_response:
          type: string
          format: object
          example: '{ "lago_id": "b9155544-e261-4e92-b54e-f65d7609294c", ... }'

````