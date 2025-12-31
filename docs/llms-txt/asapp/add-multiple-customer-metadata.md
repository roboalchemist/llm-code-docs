# Source: https://docs.asapp.com/apis/metadata/add-multiple-customer-metadata.md

# Add multiple customer metadata

> Add multiple customer metadata items; submit items in a batch in one request


## OpenAPI

````yaml api-specs/metadata-ingestion.yaml post /metadata-ingestion/v1/many-customer-metadata
paths:
  path: /metadata-ingestion/v1/many-customer-metadata
  method: post
  servers:
    - url: https://api.sandbox.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
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
              items:
                allOf:
                  - type: array
                    items:
                      description: A set of customer metadata attributes
                      type: object
                      properties:
                        externalConversationId:
                          description: >-
                            Conversation ID from the external chat / voice
                            system
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 256
                          example: issue509
                        externalCustomerId:
                          description: >-
                            The customer id involved in respect to the issue in
                            question
                          type: string
                          pattern: '[a-zA-Z0-9\-\_\.\@]+'
                          maxLength: 256
                          example: 555.555.0100-jdoe@example.com
                        eventId:
                          description: >
                            An event id used to track the submission; if none is
                            provided, service will generate one
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 256
                          nullable: true
                          example: eventId-1938
                        status:
                          description: >-
                            The descriptive label to describe the customer's
                            status and/or type
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 256
                          nullable: true
                          example: new
                        phoneNumber:
                          description: The customer's phone number
                          type: string
                          pattern: '[0-9\-\.\(\)\+]+'
                          maxLength: 32
                          nullable: true
                          example: (555)555-0100
                        emailAddress:
                          description: The customer's email address
                          type: string
                          format: email
                          nullable: true
                          example: jdoe@example.com
                        userId:
                          description: The customer's user Id
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 256
                          nullable: true
                          example: user908038
                        addressCountry:
                          description: The country portion of the customer's address
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 128
                          nullable: true
                          example: United-States
                        addressState:
                          description: The state portion of the customer's address
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 128
                          nullable: true
                          example: New-York
                        addressZipcode:
                          description: >-
                            The zipcode/postal code portion of the customer's
                            address
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 16
                          nullable: true
                          example: '10001'
                        attributes:
                          description: >-
                            A map of key-value pairs for extra metadata
                            attributes
                          type: array
                          items:
                            description: A key-value pair of additional metadata attributes
                            type: object
                            properties:
                              name:
                                description: The name of the attribute
                                type: string
                                maxLength: 256
                              value:
                                description: The value of the named attribute
                                type: string
                                maxLength: 1024
                            example:
                              - name: attr1_name
                                value: attr1_value
                              - name: attr2_name
                                value: attr2_value
                          maxItems: 10
                          nullable: true
                          example:
                            - name: attr1_name
                              value: attr1_value
                            - name: attr2_name
                              value: attr2_value
                      required:
                        - externalConversationId
                        - externalCustomerId
                      example:
                        externalConversationId: id-509
                        externalCustomerId: 555.555.0100-jdoe@example.com
                        eventId: eventId-1938
                        status: new
                        phoneNumber: (555)555-0100
                        emailAddress: jdoe@example.com
                        userId: user908038
                        addressCountry: United-States
                        addressState: New-York
                        addressZipcode: '10001'
                        attributes:
                          - name: attr1_name
                            value: attr1_value
                          - name: attr2_name
                            value: attr2_value
                    minItems: 1
                    maxItems: 1000
            required: true
            description: >-
              A request to send more than one customer metadata; send a list of
              items
            example:
              items:
                - externalConversationId: id-509
                  externalCustomerId: 555.555.0100-jdoe@example.com
                  eventId: eventId-1938
                  status: new
                  phoneNumber: (555)555-0100
                  emailAddress: jdoe@example.com
                  userId: user908038
                  addressCountry: United-States
                  addressState: New-York
                  addressZipcode: '10001'
                  attributes:
                    - name: attr1_name
                      value: attr1_value
                    - name: attr2_name
                      value: attr2_value
                - externalConversationId: id-203
                  externalCustomerId: 555.555.0101-mdoe@example.com
                  eventId: eventId-1331
                  status: existing
                  phoneNumber: (555)555-0101
                  emailAddress: mdoe@example.com
                  userId: user3201033
                  addressCountry: United-States
                  addressState: New-York
                  addressZipcode: '10002'
                  attributes:
                    - name: attr1_name
                      value: attr1_value
                    - name: attr2_name
                      value: attr2_value
                - externalConversationId: id-69221
                  externalCustomerId: 555.555.0191
                  attributes: null
                - externalConversationId: id-69223
                  externalCustomerId: 555.555.0193
                - externalConversationId: id-69229
                  externalCustomerId: zdoe@example.com
                  phoneNumber: null
                  userId: null
                  addressCountry: null
        examples:
          example:
            value:
              items:
                - externalConversationId: id-509
                  externalCustomerId: 555.555.0100-jdoe@example.com
                  eventId: eventId-1938
                  status: new
                  phoneNumber: (555)555-0100
                  emailAddress: jdoe@example.com
                  userId: user908038
                  addressCountry: United-States
                  addressState: New-York
                  addressZipcode: '10001'
                  attributes:
                    - name: attr1_name
                      value: attr1_value
                    - name: attr2_name
                      value: attr2_value
                - externalConversationId: id-203
                  externalCustomerId: 555.555.0101-mdoe@example.com
                  eventId: eventId-1331
                  status: existing
                  phoneNumber: (555)555-0101
                  emailAddress: mdoe@example.com
                  userId: user3201033
                  addressCountry: United-States
                  addressState: New-York
                  addressZipcode: '10002'
                  attributes:
                    - name: attr1_name
                      value: attr1_value
                    - name: attr2_name
                      value: attr2_value
                - externalConversationId: id-69221
                  externalCustomerId: 555.555.0191
                  attributes: null
                - externalConversationId: id-69223
                  externalCustomerId: 555.555.0193
                - externalConversationId: id-69229
                  externalCustomerId: zdoe@example.com
                  phoneNumber: null
                  userId: null
                  addressCountry: null
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              errorCount:
                allOf:
                  - description: Number of message sent with error(s)
                    type: integer
              results:
                allOf:
                  - description: A list of send result
                    type: array
                    items:
                      description: A response with the status of a sent message
                      type: object
                      properties:
                        eventId:
                          description: >-
                            An UUID identifier string computed for the submitted
                            event message
                          type: string
                          example: 5484e507-feaf-11ec-bfc1-fda566fa9333
                        error:
                          description: >-
                            Status of the failed message if value is not blank;
                            the error is contained in the string
                          type: string
                          example: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                      example:
                        eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                        error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
            requiredProperties:
              - errorCount
              - results
            example:
              errorCount: 1
              results:
                - eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                  error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                - eventId: fcf99667-feaf-11ec-a42e-11799134528c
                  error: ''
        examples:
          example:
            value:
              errorCount: 1
              results:
                - eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                  error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                - eventId: fcf99667-feaf-11ec-a42e-11799134528c
                  error: ''
        description: >
          200 - Success | Partial Success

          Submit a batch of items to the service to be ingested. Record can be
          traced back to the submitted record by the eventId.

          If any of the records encounter issue during the ingestion, a message
          sent status will be returned with an error message for each record.

          A 200 success is returned as long as there is one item ingested
          successfully, i.e., "partial success".
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              errorCount:
                allOf:
                  - description: Number of message sent with error(s)
                    type: integer
              results:
                allOf:
                  - description: A list of send result
                    type: array
                    items:
                      description: A response with the status of a sent message
                      type: object
                      properties:
                        eventId:
                          description: >-
                            An UUID identifier string computed for the submitted
                            event message
                          type: string
                          example: 5484e507-feaf-11ec-bfc1-fda566fa9333
                        error:
                          description: >-
                            Status of the failed message if value is not blank;
                            the error is contained in the string
                          type: string
                          example: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                      example:
                        eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                        error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
            requiredProperties:
              - errorCount
              - results
            example:
              errorCount: 1
              results:
                - eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                  error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                - eventId: fcf99667-feaf-11ec-a42e-11799134528c
                  error: ''
        examples:
          example:
            value:
              errorCount: 1
              results:
                - eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                  error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                - eventId: fcf99667-feaf-11ec-a42e-11799134528c
                  error: ''
        description: >
          400 - Bad request

          Submit a batch of items to the service to be ingested. Record can be
          traced back to the submitted record by the eventId.

          If any of the records encounter issue during the ingestion, a message
          sent status will be returned with an error message for each record.

          All items in the batch encountered client input validation failures.
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 401-01
                      message: Unauthorized
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unauthorized response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 401-01
                message: Unauthorized
        description: 401 - Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 403-01
                      message: Forbidden Response
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Forbidden response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 403-01
                message: Forbidden Response
        description: 403 - Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 404-01
                      message: Not Found
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Not Found response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 404-01
                message: Not Found
        description: 404 - Not Found
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 409-01
                      message: Conflict
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Conflict response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 409-01
                message: Conflict
        description: 409 - Conflict
    '413':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 413-01
                      message: Request Entity Too Large
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Request Entity Too Large response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 413-01
                message: Request Entity Too Large
        description: 413 - Request Entity Too Large
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 422-01
                      message: Unprocessable Entity
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unprocessable Entity response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 422-01
                message: Unprocessable Entity
        description: 422 - Unprocessable Entity
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 429-01
                      message: Too Many Requests
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Too Many Requests response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 429-01
                message: Too Many Requests
        description: 429 - Too Many Requests
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 503-01
                      message: Service Unavailable
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Service Unavailable response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 503-01
                message: Service Unavailable
        description: 503 - Service Unavailable
    default:
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Default error response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 500-01
                message: Internal server error
        description: 500 - Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````