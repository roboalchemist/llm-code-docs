# Source: https://getlago.com/docs/api-reference/audit-logs/get-all-api-logs.md

# List all API logs

> This endpoint retrieves all existing api logs that represent requests performed to Lago's API.

## OpenAPI

````yaml GET /api_logs
paths:
  path: /api_logs
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
      path: {}
      query:
        page:
          schema:
            - type: integer
              required: false
              description: Page number.
              example: 1
          explode: true
        per_page:
          schema:
            - type: integer
              required: false
              description: Number of records per page.
              example: 20
          explode: true
        from_date:
          schema:
            - type: string
              required: false
              description: Filter api logs from a specific date.
              format: date
              example: '2022-08-09'
          explode: true
        to_date:
          schema:
            - type: string
              required: false
              description: Filter api logs up to a specific date.
              format: date
              example: '2022-08-09'
          explode: true
        http_methods[]:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
                    enum:
                      - post
                      - put
                      - delete
              required: false
              description: Filter results by HTTP methods
              example:
                - post
                - put
          explode: true
        http_statuses[]:
          schema:
            - type: array
              items:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - succeeded
                          - failed
                      - type: integer
                        minimum: 100
                        maximum: 599
              required: false
              description: Filter results by HTTP status or by generic request status
              example:
                - failed
                - succeeded
                - 404
          explode: true
        api_version:
          schema:
            - type: string
              required: false
              description: Filter results by API version
              example: v1
          explode: true
        request_paths:
          schema:
            - type: string
              required: false
              description: Filter results by the path of the request
              example: /billable_metrics/
          explode: true
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              api_logs:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/ApiLogObject'
              meta:
                allOf:
                  - $ref: '#/components/schemas/PaginationMeta'
            refIdentifier: '#/components/schemas/ApiLogsPaginated'
            requiredProperties:
              - api_logs
              - meta
        examples:
          example:
            value:
              api_logs:
                - api_version: v1
                  client: Lago Ruby v1.26.0
                  http_method: post
                  http_status: 200
                  logged_at: '2025-03-31T12:31:44Z'
                  request_body: >-
                    { "billable_metric": { "name": "Storage", "code": "storage"
                    } }
                  request_origin: https://app.lago.dev/
                  request_path: /billable_metrics
                  created_at: '2022-04-29T08:59:51Z'
                  request_id: 1a901a90-1a90-1a90-1a90-1a901a901a90
                  request_response: '{ "lago_id": "b9155544-e261-4e92-b54e-f65d7609294c", ... }'
              meta:
                current_page: 2
                next_page: 3
                prev_page: 1
                total_pages: 4
                total_count: 70
        description: List of api logs
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
  deprecated: false
  type: path
components:
  schemas:
    PaginationMeta:
      type: object
      required:
        - current_page
        - total_pages
        - total_count
      properties:
        current_page:
          type: integer
          description: Current page.
          example: 2
        next_page:
          type:
            - integer
            - 'null'
          description: Next page.
          example: 3
        prev_page:
          type:
            - integer
            - 'null'
          description: Previous page.
          example: 1
        total_pages:
          type: integer
          description: Total number of pages.
          example: 4
        total_count:
          type: integer
          description: Total number of records.
          example: 70
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