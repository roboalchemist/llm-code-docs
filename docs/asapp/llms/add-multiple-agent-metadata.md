# Source: https://docs.asapp.com/apis/metadata/add-multiple-agent-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add multiple agent metadata

> Add multiple agent metadata items; submit items in a batch in one request




## OpenAPI

````yaml api-specs/metadata-ingestion.yaml post /metadata-ingestion/v1/many-agent-metadata
openapi: 3.0.1
info:
  title: Metadata Ingestion API
  description: >
    The Metadata Ingestion API is a mechanism to submit attributes about a
    single entity or multiple entities to ASAPP. Supported entities to which
    attributes can be appended include customers, agents, and conversations.
  version: 1.0.0
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: Metadata
    description: API to submit entity's attributes to ASAPP
paths:
  /metadata-ingestion/v1/many-agent-metadata:
    post:
      tags:
        - Metadata
      summary: Add multiple agent metadata
      description: >
        Add multiple agent metadata items; submit items in a batch in one
        request
      operationId: manyAgentMetadata
      requestBody:
        required: true
        content:
          application/json:
            schema:
              description: >-
                A request to send more than one agent metadata; send a list of
                items
              type: object
              properties:
                items:
                  type: array
                  items:
                    description: A set of agent metadata attributes
                    type: object
                    properties:
                      externalAgentId:
                        description: The agent id in question
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        example: agent158
                      eventId:
                        description: >
                          An event id used to track the submission; if none is
                          provided, service will generate one
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: eventId-158
                      startTs:
                        description: The date and time when the agent is hired in ISO-8601
                        type: string
                        format: date-time
                        nullable: true
                        example: '2022-07-08T11:15:53.237517000Z'
                      lobId:
                        description: The line of business id
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: '1038'
                      lobName:
                        description: The descriptive name of the line of business
                        type: string
                        maxLength: 256
                        nullable: true
                        example: manufacturing
                      groupId:
                        description: The group id of which the agent belong to
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: group5
                      groupName:
                        description: The descriptive name of the group
                        type: string
                        maxLength: 256
                        nullable: true
                        example: XYZ
                      agentName:
                        description: The name of the agent
                        type: string
                        maxLength: 256
                        nullable: true
                        example: Jane Doe
                      agentLocation:
                        description: The location (or address) of where the agent worked
                        type: string
                        maxLength: 256
                        nullable: true
                        example: Northern-California
                      supervisorId:
                        description: The supervisor id of who the agent report to
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: '3080'
                      supervisorName:
                        description: The name of the agent's supervisor
                        type: string
                        maxLength: 256
                        nullable: true
                        example: Linda Lemon
                      languages:
                        description: |
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
                        description: The number of issues that an agent can take at a time
                        type: integer
                        nullable: true
                        example: 3
                      categoryLabel:
                        description: >-
                          The category label that indicates the types of
                          workflows an agent have access to or problems they
                          solved
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: Tier-2-Escalation
                      accountAccessLevel:
                        description: >-
                          The levels of mapping that an agent have access to
                          make changes to customer accounts
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: High-Profile
                      ranking:
                        description: >-
                          Some numerical value indicating relative or absolute
                          performance on a single scale
                        type: integer
                        nullable: true
                        example: 78
                      vendor:
                        description: >-
                          Vendor or BPO (Business Process Outsourcing) that the
                          agent is part of
                        type: string
                        maxLength: 256
                        nullable: true
                        example: Contracting
                      jobTitle:
                        description: The agent's job title
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: Booking-Manager
                      jobRole:
                        description: The agent's role
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: booking
                      workShift:
                        description: The hours or shift name they work
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: afternoon
                      emailAddress:
                        description: The agent's email address
                        type: string
                        format: email
                        nullable: true
                        example: jdoe@example.com
                      attributes:
                        description: A map of key-value pairs for extra metadata attributes
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
                  minItems: 1
                  maxItems: 1000
              example:
                items:
                  - externalAgentId: agent158
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
                      - es-pe
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
                  - externalAgentId: agent392
                    startTs: '2021-09-02T11:15:53.237517000Z'
                    lobId: '968'
                    lobName: insurance
                    groupId: group3
                    groupName: DFG
                    agentName: Jonathan Master
                    agentLocation: Southern-California
                    supervisorId: '1290'
                    supervisorName: John Luna
                    languages:
                      - en-us
                    concurrency: 3
                    categoryLabel: Tier-1-Service
                    accountAccessLevel: High-Profile
                    ranking: 75
                    vendor: Contracting
                    jobTitle: Customer-Service
                    jobRole: Support
                    workShift: afternoon
                    emailAddress: jmaster@example.com
                    attributes:
                      - name: attr1_name
                        value: attr1_value
                  - externalAgentId: agent6922
                    startTs: null
                  - externalAgentId: agent222
                  - externalAgentId: agent333
                    emailAddress: jdoe@example.com
      responses:
        '200':
          description: >
            200 - Success | Partial Success

            Submit a batch of items to the service to be ingested. Record can be
            traced back to the submitted record by the eventId.

            If any of the records encounter issue during the ingestion, a
            message sent status will be returned with an error message for each
            record.

            A 200 success is returned as long as there is one item ingested
            successfully, i.e., "partial success".
          content:
            application/json:
              schema:
                type: object
                properties:
                  errorCount:
                    description: Number of message sent with error(s)
                    type: integer
                  results:
                    description: A list of send result
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
                required:
                  - errorCount
                  - results
                example:
                  errorCount: 1
                  results:
                    - eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                      error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                    - eventId: fcf99667-feaf-11ec-a42e-11799134528c
                      error: ''
        '400':
          description: >
            400 - Bad request

            Submit a batch of items to the service to be ingested. Record can be
            traced back to the submitted record by the eventId.

            If any of the records encounter issue during the ingestion, a
            message sent status will be returned with an error message for each
            record.

            All items in the batch encountered client input validation failures.
          content:
            application/json:
              schema:
                type: object
                properties:
                  errorCount:
                    description: Number of message sent with error(s)
                    type: integer
                  results:
                    description: A list of send result
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
                required:
                  - errorCount
                  - results
                example:
                  errorCount: 1
                  results:
                    - eventId: 5484e507-feaf-11ec-bfc1-fda566fa9333
                      error: 'FAIL_BAD_PARAMS: ERROR: agent id cannot be blank'
                    - eventId: fcf99667-feaf-11ec-a42e-11799134528c
                      error: ''
        '401':
          description: 401 - Unauthorized
          content:
            application/json:
              schema:
                description: Unauthorized response
                type: object
                properties:
                  error:
                    example:
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
        '403':
          description: 403 - Forbidden
          content:
            application/json:
              schema:
                description: Forbidden response
                type: object
                properties:
                  error:
                    example:
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
        '404':
          description: 404 - Not Found
          content:
            application/json:
              schema:
                description: Not Found response
                type: object
                properties:
                  error:
                    example:
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
        '409':
          description: 409 - Conflict
          content:
            application/json:
              schema:
                description: Conflict response
                type: object
                properties:
                  error:
                    example:
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
        '413':
          description: 413 - Request Entity Too Large
          content:
            application/json:
              schema:
                description: Request Entity Too Large response
                type: object
                properties:
                  error:
                    example:
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
        '422':
          description: 422 - Unprocessable Entity
          content:
            application/json:
              schema:
                description: Unprocessable Entity response
                type: object
                properties:
                  error:
                    example:
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
        '429':
          description: 429 - Too Many Requests
          content:
            application/json:
              schema:
                description: Too Many Requests response
                type: object
                properties:
                  error:
                    example:
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
        '503':
          description: 503 - Service Unavailable
          content:
            application/json:
              schema:
                description: Service Unavailable response
                type: object
                properties:
                  error:
                    example:
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
        default:
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
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
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````