# Source: https://docs.asapp.com/apis/metadata/add-an-agent-metadata.md

# Add an agent metadata

> Add metadata attributes of one agent


## OpenAPI

````yaml api-specs/metadata-ingestion.yaml post /metadata-ingestion/v1/single-agent-metadata
paths:
  path: /metadata-ingestion/v1/single-agent-metadata
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
              externalAgentId:
                allOf:
                  - description: The agent id in question
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    example: agent158
              eventId:
                allOf:
                  - description: >
                      An event id used to track the submission; if none is
                      provided, service will generate one
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: eventId-158
              startTs:
                allOf:
                  - description: The date and time when the agent is hired in ISO-8601
                    type: string
                    format: date-time
                    nullable: true
                    example: '2022-07-08T11:15:53.237517000Z'
              lobId:
                allOf:
                  - description: The line of business id
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: '1038'
              lobName:
                allOf:
                  - description: The descriptive name of the line of business
                    type: string
                    maxLength: 256
                    nullable: true
                    example: manufacturing
              groupId:
                allOf:
                  - description: The group id of which the agent belong to
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: group5
              groupName:
                allOf:
                  - description: The descriptive name of the group
                    type: string
                    maxLength: 256
                    nullable: true
                    example: XYZ
              agentName:
                allOf:
                  - description: The name of the agent
                    type: string
                    maxLength: 256
                    nullable: true
                    example: Jane Doe
              agentLocation:
                allOf:
                  - description: The location (or address) of where the agent worked
                    type: string
                    maxLength: 256
                    nullable: true
                    example: Northern-California
              supervisorId:
                allOf:
                  - description: The supervisor id of who the agent report to
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: '3080'
              supervisorName:
                allOf:
                  - description: The name of the agent's supervisor
                    type: string
                    maxLength: 256
                    nullable: true
                    example: Linda Lemon
              languages:
                allOf:
                  - description: |
                      A list of agent's known language codes in ISO 639
                      e.g., English (United States) code = en-US
                    type: array
                    items:
                      type: string
                      pattern: '[a-zA-Z0-9\-]+'
                      maxLength: 16
                    nullable: true
                    example:
                      - en-us
                      - zh-hans-hk
              concurrency:
                allOf:
                  - description: The number of issues that an agent can take at a time
                    type: integer
                    nullable: true
                    example: 3
              categoryLabel:
                allOf:
                  - description: >-
                      The category label that indicates the types of workflows
                      an agent have access to or problems they solved
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: Tier-2-Escalation
              accountAccessLevel:
                allOf:
                  - description: >-
                      The levels of mapping that an agent have access to make
                      changes to customer accounts
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: High-Profile
              ranking:
                allOf:
                  - description: >-
                      Some numerical value indicating relative or absolute
                      performance on a single scale
                    type: integer
                    nullable: true
                    example: 78
              vendor:
                allOf:
                  - description: >-
                      Vendor or BPO (Business Process Outsourcing) that the
                      agent is part of
                    type: string
                    maxLength: 256
                    nullable: true
                    example: Contracting
              jobTitle:
                allOf:
                  - description: The agent's job title
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: Booking-Manager
              jobRole:
                allOf:
                  - description: The agent's role
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: booking
              workShift:
                allOf:
                  - description: The hours or shift name they work
                    type: string
                    pattern: '[a-zA-Z0-9\-\_]+'
                    maxLength: 256
                    nullable: true
                    example: afternoon
              emailAddress:
                allOf:
                  - description: The agent's email address
                    type: string
                    format: email
                    nullable: true
                    example: jdoe@example.com
              attributes:
                allOf:
                  - description: A map of key-value pairs for extra metadata attributes
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
            required: true
            description: A set of agent metadata attributes
            requiredProperties:
              - externalAgentId
            example:
              externalAgentId: agent158
              startTs: '2022-07-08T11:15:53.237517000Z'
              lobId: '1038'
              lobName: manufacturing
              groupId: group5
              groupName: XYZ
              agentName: Jane Doe
              agentLocation: Northern-California
              supervisorId: '3080'
              supervisorName: Linda Lemon
              languages:
                - en-us
                - zh-hans-hk
              concurrency: 3
              categoryLabel: Tier-2-Escalation
              accountAccessLevel: High-Profile
              ranking: 78
              vendor: Contracting
              jobTitle: Booking-Manager
              jobRole: booking
              workShift: afternoon
              emailAddress: jdoe@example.com
              attributes:
                - name: attr1_name
                  value: attr1_value
                - name: attr2_name
                  value: attr2_value
        examples:
          example:
            value:
              externalAgentId: agent158
              startTs: '2022-07-08T11:15:53.237517000Z'
              lobId: '1038'
              lobName: manufacturing
              groupId: group5
              groupName: XYZ
              agentName: Jane Doe
              agentLocation: Northern-California
              supervisorId: '3080'
              supervisorName: Linda Lemon
              languages:
                - en-us
                - zh-hans-hk
              concurrency: 3
              categoryLabel: Tier-2-Escalation
              accountAccessLevel: High-Profile
              ranking: 78
              vendor: Contracting
              jobTitle: Booking-Manager
              jobRole: booking
              workShift: afternoon
              emailAddress: jdoe@example.com
              attributes:
                - name: attr1_name
                  value: attr1_value
                - name: attr2_name
                  value: attr2_value
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              result:
                allOf:
                  - description: A response with the status of a sent message
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
              - result
            example:
              result:
                eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
        examples:
          example:
            value:
              result:
                eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
        description: >
          200 - Success

          Submit a single item to the service to be ingested. Record can be
          traced back to the submitted record by the eventId.

          A message sent status will be returned with no error message for
          successful input checks.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              result:
                allOf:
                  - description: A response with the status of a sent message
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
              - result
            example:
              result:
                eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
        examples:
          example:
            value:
              result:
                eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
        description: >
          400 - Bad request

          Submit a single item to the service to be ingested. Record can be
          traced back to the submitted record by the eventId.

          A message sent status will be returned with an error message for bad
          input failure.
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