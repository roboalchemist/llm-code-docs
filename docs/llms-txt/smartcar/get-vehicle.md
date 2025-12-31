# Source: https://smartcar.com/docs/api-reference/get-vehicle.md

# Vehicle

> Get details for a single Vehicle.

## OpenAPI

````yaml get /vehicles/{vehicleId}
paths:
  path: /vehicles/{vehicleId}
  method: get
  servers:
    - url: https://vehicle.api.smartcar.com/v3
      description: Smartcar Vehicle APIs
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
        vehicleId:
          schema:
            - type: string
              required: true
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
              id:
                allOf:
                  - type: string
                    description: |
                      The unique identifier for the vehicle.
              type:
                allOf:
                  - type: string
                    enum:
                      - vehicle
              attributes:
                allOf:
                  - $ref: '#/components/schemas/VehicleAttributes'
              links:
                allOf:
                  - type: object
                    allOf:
                      - $ref: '#/components/schemas/SelfLink'
            refIdentifier: '#/components/schemas/VehicleResource'
        examples:
          example:
            value:
              id: <string>
              type: vehicle
              attributes:
                make: <string>
                model: <string>
                year: 123
              links:
                self: <string>
        description: List of data associated with the vehicle
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - &ref_0
                    type: array
                    items:
                      type: object
                      properties:
                        links:
                          type: object
                          properties:
                            about:
                              type: string
                        status:
                          type: string
                        code:
                          type: string
                        title:
                          type: string
                        detail:
                          type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              errors:
                - status: '400'
                  code: bad_request
                  title: Bad Request
                  detail: >-
                    The request could not be understood by the server due to
                    malformed syntax.
        description: 400 Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              errors:
                - status: '401'
                  code: unauthorized
                  title: Unauthorized
                  detail: The Authorization token is missing or invalid.
        description: 401 Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              errors:
                - status: '403'
                  code: forbidden
                  title: Forbidden
                  detail: You do not have permission to access this resource.
        description: 403 Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              errors:
                - status: '404'
                  code: not_found
                  title: Not Found
                  detail: The requested resource could not be found.
        description: 404 Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              errors:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              errors:
                - status: '500'
                  code: internal_error
                  title: Internal Server Error
                  detail: An unexpected error occurred on the server.
        description: 500 Internal Server Error
  deprecated: false
  type: path
components:
  schemas:
    VehicleAttributes:
      type: object
      properties:
        make:
          type: string
        model:
          type: string
        year:
          type: integer
    SelfLink:
      type: object
      properties:
        self:
          type: string
          description: |
            The URL to access the current resource.

````