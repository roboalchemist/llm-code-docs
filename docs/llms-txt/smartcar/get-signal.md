# Source: https://smartcar.com/docs/api-reference/get-signal.md

# Signal

> Get a specific Signal for a Vehicle.

## OpenAPI

````yaml get /vehicles/{vehicleId}/signals/{signalCode}
paths:
  path: /vehicles/{vehicleId}/signals/{signalCode}
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
              description: The unique identifier for the vehicle.
        signalCode:
          schema:
            - type: string
              required: true
              description: The unique identifier for the signal.
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
                      The unique human readable identifier for the signal.
              type:
                allOf:
                  - type: string
                    enum:
                      - signal
              attributes:
                allOf:
                  - $ref: '#/components/schemas/SignalAttributes'
              meta:
                allOf:
                  - type: object
                    allOf:
                      - $ref: '#/components/schemas/DateMetaData'
              links:
                allOf:
                  - type: object
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
            refIdentifier: '#/components/schemas/SignalResource'
        examples:
          example:
            value:
              id: <string>
              type: signal
              attributes:
                code: charge-voltage
                name: Voltage
                group: Charge
                status:
                  value: SUCCESS
                body:
                  unit: volts
                  value: 85
              meta:
                retrievedAt: 1696156800
                oemUpdatedAt: 1696156799
              links:
                self: <string>
                values: <string>
                vehicle: <string>
        description: Individual signal details
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
    SelfLink:
      type: object
      properties:
        self:
          type: string
          description: |
            The URL to access the current resource.
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

````