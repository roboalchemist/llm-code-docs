# Source: https://docs.asapp.com/apis/conversations/authenticate-a-user-in-a-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticate a user in a conversation

> Stores customer-specific authentication credentials for use in integrated flows.

- Can be called at any point during a conversation
- Commonly used at the start of a conversation or after mid-conversation authentication
- May trigger additional actions, such as GenerativeAgent API signals to customer webhooks

<Note>This API only accepts the customer-specific auth credentials; the customer is responsible for handling 
the specific authentication mechanism.</Note>




## OpenAPI

````yaml api-specs/conversations.yaml post /conversation/v1/conversations/{conversationId}/authenticate
openapi: 3.0.1
info:
  title: Conversations API
  description: Operations to manage ASAPP conversations
  contact:
    email: api-info@asapp.com
  license:
    name: ASAPP Software License
    url: https://api.asapp.com/LICENSE
  version: '0.1'
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: Conversations
    description: Operations to send conversational inputs to ASAPP AI services
paths:
  /conversation/v1/conversations/{conversationId}/authenticate:
    post:
      tags:
        - Conversations
      summary: Authenticate a user in a conversation
      description: >
        Stores customer-specific authentication credentials for use in
        integrated flows.


        - Can be called at any point during a conversation

        - Commonly used at the start of a conversation or after mid-conversation
        authentication

        - May trigger additional actions, such as GenerativeAgent API signals to
        customer webhooks


        <Note>This API only accepts the customer-specific auth credentials; the
        customer is responsible for handling 

        the specific authentication mechanism.</Note>
      operationId: postAuthenticate
      parameters:
        - name: conversationId
          description: The identifier for a conversation.
          in: path
          required: true
          schema:
            type: string
            pattern: ^[A-Z0-9]+$
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: >-
                Contains authentication information for a customer in a
                conversation.
              properties:
                streamId:
                  type: string
                  description: >-
                    The unique identifier for the connection where responses
                    should be sent.
                  example: 97555020-0276-435f-8104-c378221ba292
                customerExternalId:
                  type: string
                  description: >-
                    The unique identifier for the customer in your external
                    system.
                  example: a03839d6-461c-479c-99db-8160174ef12d
                auth:
                  type: object
                  description: >
                    An authentication payload that could contain different types
                    of credentials, such as a token, used to 

                    authenticate an end user. All of the fields are optional,
                    but at least one will be required
                  minProperties: 1
                  properties:
                    body:
                      type: object
                      description: >-
                        Any authentication data to be sent in the request body,
                        if applicable.
                    cookies:
                      type: object
                      description: >-
                        Any authentication data to be sent as cookies, if
                        applicable.
                    headers:
                      type: object
                      description: >-
                        Any authentication data to be sent in the request
                        headers, if applicable.
                    token:
                      type: string
                      description: An authentication token for the user, if applicable.
              required:
                - customerExternalId
                - auth
              example:
                customerExternalId: customer-xyz
                token: cGFzc3dvcmQ=
      responses:
        '204':
          description: 204 - No Content
        '400':
          description: 400 - Bad request
          content:
            application/json:
              schema:
                description: Bad request response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 400-01
                      message: Bad request
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