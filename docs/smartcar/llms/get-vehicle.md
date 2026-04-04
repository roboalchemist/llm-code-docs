# Source: https://smartcar.com/docs/api-reference/get-vehicle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicle

> Get details for a single Vehicle.



## OpenAPI

````yaml get /vehicles/{vehicleId}
openapi: 3.0.3
info:
  title: Smartcar Vehicle Data API
  version: 1.0.0
  description: |
    API for returning signal and attribute signals
servers:
  - url: https://vehicle.api.smartcar.com/v3
    description: Smartcar Vehicle APIs
security: []
paths:
  /vehicles/{vehicleId}:
    get:
      summary: GET vehicle
      operationId: getVehicle
      parameters:
        - in: path
          name: vehicleId
          required: true
          schema:
            type: string
      responses:
        '200':
          description: List of data associated with the vehicle
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VehicleResource'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
      security:
        - bearerAuth: []
components:
  schemas:
    VehicleResource:
      type: object
      properties:
        id:
          type: string
          description: |
            The unique identifier for the vehicle.
        type:
          type: string
          enum:
            - vehicle
        attributes:
          $ref: '#/components/schemas/VehicleAttributes'
        links:
          type: object
          allOf:
            - $ref: '#/components/schemas/SelfLink'
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
    ErrorResponse:
      type: object
      properties:
        errors:
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
  responses:
    BadRequest:
      description: 400 Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            errors:
              - status: '400'
                code: bad_request
                title: Bad Request
                detail: >-
                  The request could not be understood by the server due to
                  malformed syntax.
    Unauthorized:
      description: 401 Unauthorized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            errors:
              - status: '401'
                code: unauthorized
                title: Unauthorized
                detail: The Authorization token is missing or invalid.
    Forbidden:
      description: 403 Forbidden
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            errors:
              - status: '403'
                code: forbidden
                title: Forbidden
                detail: You do not have permission to access this resource.
    NotFound:
      description: 404 Not Found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            errors:
              - status: '404'
                code: not_found
                title: Not Found
                detail: The requested resource could not be found.
    InternalError:
      description: 500 Internal Server Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            errors:
              - status: '500'
                code: internal_error
                title: Internal Server Error
                detail: An unexpected error occurred on the server.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````