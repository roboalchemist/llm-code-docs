# Source: https://smartcar.com/docs/api-reference/get-signals.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Signals

> Get all available Signals for a Vehicle



## OpenAPI

````yaml get /vehicles/{vehicleId}/signals
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
  /vehicles/{vehicleId}/signals:
    get:
      summary: GET signals
      operationId: getVehicleSignals
      parameters:
        - in: path
          name: vehicleId
          required: true
          description: The unique identifier for the vehicle.
          schema:
            type: string
      responses:
        '200':
          description: List of signals for the vehicle
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SignalsResponse'
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
    SignalsResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/SignalResource'
        meta:
          type: object
          allOf:
            - $ref: '#/components/schemas/PagingMetaData'
        links:
          type: object
          allOf:
            - $ref: '#/components/schemas/SelfLink'
            - $ref: '#/components/schemas/PagingLinks'
        included:
          type: object
          properties:
            vehicle:
              $ref: '#/components/schemas/VehicleResource'
    SignalResource:
      type: object
      properties:
        id:
          type: string
          description: |
            The unique human readable identifier for the signal.
        type:
          type: string
          enum:
            - signal
        attributes:
          $ref: '#/components/schemas/SignalAttributes'
        meta:
          type: object
          allOf:
            - $ref: '#/components/schemas/DateMetaData'
        links:
          type: object
          allOf:
            - $ref: '#/components/schemas/SelfLink'
            - type: object
              properties:
                values:
                  type: string
                  description: URL to the values for this signal
                vehicle:
                  type: string
                  description: URL to the vehicle associated with this signal
    PagingMetaData:
      type: object
      properties:
        page:
          type: integer
          description: |
            The current page number of the paginated results.
        pageSize:
          type: integer
          description: |
            The number of items returned per page.
        totalCount:
          type: integer
          description: |
            The total number of items available across all pages.
      example:
        page: 1
        pageSize: 10
        totalCount: 5
    SelfLink:
      type: object
      properties:
        self:
          type: string
          description: |
            The URL to access the current resource.
    PagingLinks:
      type: object
      properties:
        self:
          type: string
          description: |
            The URL to access the current page of results.
        first:
          type: string
          description: |
            The URL to access the first page of results.
        previous:
          type: string
          description: |
            The URL to access the previous page of results.
        next:
          type: string
          description: |
            The URL to access the next page of results.
        last:
          type: string
          description: |
            The URL to access the last page of results.
      example:
        self: /vehicles/vehicle123/signals?page=1&pageSize=10
        first: /vehicles/vehicle123/signals?page=1&pageSize=10
        previous: null
        next: /vehicles/vehicle123/signals?page=2&pageSize=10
        last: /vehicles/vehicle123/signals?page=5&pageSize=10
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
    SignalAttributes:
      type: object
      properties:
        code:
          type: string
          description: |
            The unique identifier for the  data point.
        name:
          type: string
          description: |
            The name of the datapoint, which is a human-readable identifier.
        group:
          type: string
          description: |
            The group to which the data point belongs, used for categorization.
        status:
          $ref: '#/components/schemas/SignalStatus'
        body:
          type: object
          description: |
            The body of the signal or attribute
          oneOf:
            - $ref: '#/components/schemas/UnitValue'
            - $ref: '#/components/schemas/SingleValue'
            - $ref: '#/components/schemas/AdditionalValues'
            - $ref: '#/components/schemas/ValuesArrayType'
            - $ref: '#/components/schemas/ObjectValue'
      example:
        code: charge-voltage
        name: Voltage
        group: Charge
        status:
          value: SUCCESS
        body:
          unit: volts
          value: 85
    DateMetaData:
      type: object
      properties:
        retrievedAt:
          type: integer
          format: int64
          description: |
            epoch time of the last retrieval of this data point
        oemUpdatedAt:
          type: integer
          format: int64
          description: |
            The epoch time of the last update of this data point by the OEM
      example:
        retrievedAt: 1696156800
        oemUpdatedAt: 1696156799
    VehicleAttributes:
      type: object
      properties:
        make:
          type: string
        model:
          type: string
        year:
          type: integer
    SignalStatus:
      type: object
      properties:
        value:
          type: string
          description: >
            The state of the signal, indicating whether it is active, inactive,
            or in an error state.
          enum:
            - SUCCESS
            - ERROR
            - UNAVAILABLE
        error:
          $ref: '#/components/schemas/SignalError'
      example:
        value: ERROR
        error:
          type: SignalError
          code: SIGNAL_NOT_FOUND
          description: The requested signal does not exist.
          resolution:
            type: REAUTHENTICATE
    UnitValue:
      type: object
      properties:
        unit:
          type: string
          enum:
            - volts
            - ampere
            - watts
            - percentage
            - degrees
            - kilometers
            - liters
            - kilowatt-hours
            - kilowatts
            - bar
            - seconds
            - minutes
            - hours
            - degrees-celsius
          description: |
            The unit of measurement related to the value
        value:
          type: number
          description: |
            The numerical value of the signal.
    SingleValue:
      type: object
      properties:
        value:
          description: >
            The value of the signal, which can be a number, string, or other
            data type.
          oneOf:
            - type: number
            - type: string
            - type: boolean
    AdditionalValues:
      type: object
      allOf:
        - anyOf:
            - $ref: '#/components/schemas/UnitValue'
            - $ref: '#/components/schemas/SingleValue'
            - $ref: '#/components/schemas/ObjectValue'
        - type: object
          properties:
            type:
              type: string
              description: >
                The type of additional values, which can be used to categorize
                the data.
            additionalValues:
              type: array
              items:
                anyOf:
                  - $ref: '#/components/schemas/UnitValue'
                  - $ref: '#/components/schemas/SingleValue'
                  - $ref: '#/components/schemas/ObjectValue'
      description: >
        Represents a selected value from a set of possible values housed in
        "additional values"
    ValuesArrayType:
      type: object
      properties:
        values:
          type: array
          items:
            type: object
    ObjectValue:
      type: object
      additionalProperties: true
    SignalError:
      type: object
      properties:
        type:
          type: string
          description: |
            The type of error that occurred, indicating the nature of the issue.
        code:
          type: string
          description: >
            A code representing the specific error, used for error handling and
            debugging.
        description:
          type: string
          description: |
            A human-readable message describing the error.
        resolution:
          type: object
          properties:
            type:
              type: string
              description: Describes types of actions to be take to resolve an error state
      example:
        type: CONNECTED_SERVICES_ACCOUNT
        code: AUTHENTICATION_FAILED
        message: The authentication for the connected services account failed.
        resolution:
          type: REAUTHENTICATE
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