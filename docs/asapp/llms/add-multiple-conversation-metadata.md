# Source: https://docs.asapp.com/apis/metadata/add-multiple-conversation-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add multiple conversation metadata

> Add multiple issue/conversation metadata items; submit items in a batch in one request




## OpenAPI

````yaml api-specs/metadata-ingestion.yaml post /metadata-ingestion/v1/many-convo-metadata
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
  /metadata-ingestion/v1/many-convo-metadata:
    post:
      tags:
        - Metadata
      summary: Add multiple conversation metadata
      description: >
        Add multiple issue/conversation metadata items; submit items in a batch
        in one request
      operationId: manyConversationMetadata
      requestBody:
        required: true
        content:
          application/json:
            schema:
              description: >
                A request to send more than one conversation metadata
                attributes; send a list of items
              type: object
              properties:
                items:
                  type: array
                  items:
                    description: A set of conversation metadata attributes
                    type: object
                    properties:
                      externalConversationId:
                        description: Conversation ID from the external chat / voice system
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        example: issue1389
                      eventId:
                        description: >
                          An event id used to track the submission; if none is
                          provided, service will generate one
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: eventId-1388
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
                        example: group59
                      groupName:
                        description: The descriptive name of the group
                        type: string
                        maxLength: 256
                        nullable: true
                        example: groupXYZ
                      agentRoutingCode:
                        description: The agent's routing attribute
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: route-13988
                      campaign:
                        description: The activities related to the issue
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: campaign-A
                      deviceType:
                        description: The client's device type
                        type: string
                        enum:
                          - TABLET
                          - PHONE
                          - DESKTOP
                          - WATCH
                          - OTHER
                        nullable: true
                        example: TABLET
                      platform:
                        description: |
                          The client's platform type
                          WAB: WhatsApp Business
                        type: string
                        enum:
                          - SMS
                          - WEB
                          - IOS
                          - ANDROID
                          - APP
                          - LOCAL
                          - VOICE
                          - VOICE_IOS
                          - VOICE_ANDROID
                          - VOICE_ECHO
                          - VOICE_HOMEPOD
                          - VOICE_GGLHOME
                          - VOICE_WEB
                          - APPLEBIZ
                          - GOOGLEBIZ
                          - GBM
                          - WAB
                        nullable: true
                        example: IOS
                      companySegment:
                        description: The company's segment of which the issue belongs to
                        type: array
                        items:
                          type: string
                          pattern: '[a-zA-Z0-9\-\_]+'
                          maxLength: 64
                        nullable: true
                        example:
                          - Sales
                          - Marketing
                      companySubdivision:
                        description: >-
                          The company's subdivision of which the issue belongs
                          to
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: Operating
                      businessRule:
                        description: The business rule to use
                        type: string
                        maxLength: 256
                        nullable: true
                        example: Apply customer's discount
                      entryType:
                        description: The way the issue started and created in the system
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 256
                        nullable: true
                        example: reactive
                      operatingSystem:
                        description: The operating system used to enter the issue
                        type: string
                        enum:
                          - MAC_OS
                          - LINUX
                          - WINDOWS
                          - ANDROID
                          - IOS
                          - OTHER
                        nullable: true
                        example: MAC_OS
                      browserType:
                        description: The browser type used
                        type: string
                        pattern: '[a-zA-Z0-9\-\_]+'
                        maxLength: 64
                        nullable: true
                        example: Safari
                      browserVersion:
                        description: The browser version used
                        type: string
                        pattern: '[a-zA-Z0-9\-\_\.]+'
                        maxLength: 16
                        nullable: true
                        example: 14.1.2
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
                      - externalConversationId
                    example:
                      externalConversationId: id-1389
                      eventId: eventId-1388
                      lobId: '1038'
                      lobName: manufacturing
                      groupId: group59
                      groupName: groupXYZ
                      agentRoutingCode: route-13988
                      campaign: campaign-A
                      deviceType: TABLET
                      platform: IOS
                      companySegment:
                        - Sales
                        - Marketing
                      companySubdivision: operating
                      businessRule: Apply customer's discount
                      entryType: reactive
                      operatingSystem: MAC_OS
                      browserType: Safari
                      browserVersion: 14.1.2
                      attributes:
                        - name: attr1_name
                          value: attr1_value
                        - name: attr2_name
                          value: attr2_value
                  minItems: 1
                  maxItems: 1000
              example:
                items:
                  - externalConversationId: id-1389
                    eventId: eventId-1388
                    lobId: '1038'
                    lobName: manufacturing
                    groupId: group59
                    groupName: groupXYZ
                    agentRoutingCode: route-13988
                    campaign: campaign-A
                    deviceType: TABLET
                    platform: IOS
                    companySegment:
                      - Sales
                      - Marketing
                    companySubdivision: operating
                    businessRule: Apply customer's discount
                    entryType: reactive
                    operatingSystem: MAC_OS
                    browserType: Safari
                    browserVersion: 14.1.2
                    attributes:
                      - name: attr1_name
                        value: attr1_value
                      - name: attr2_name
                        value: attr2_value
                  - externlConversationId: issue1390
                    eventId: eventId-1268
                    lobId: '930'
                    lobName: retail
                    groupId: store-93
                    groupName: PlazaA
                    agentRoutingCode: route-1983
                    campaign: campaign-B
                    deviceType: PHONE
                    platform: ANDROID
                    companySegment:
                      - SALES
                      - FINANCE
                    companySubdivision: operating
                    businessRule: Apply customer's discount
                    entryType: proactive
                    operatingSystem: ANDROID
                    browserType: Chrome
                    browserVersion: 103.0.5060.128
                    attributes:
                      - name: attr1_name
                        value: attr1_value
                      - name: attr2_name
                        value: attr2_value
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