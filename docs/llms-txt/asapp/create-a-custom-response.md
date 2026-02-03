# Source: https://docs.asapp.com/apis/autocompose/create-a-custom-response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a custom response

> Add a single custom response for an agent



## OpenAPI

````yaml api-specs/autocompose.yaml post /autocompose/v1/responses/customs/response
openapi: 3.0.1
info:
  title: AutoCompose API
  description: >
    Autocompose API to suggest the next agent message.

    Suggestions are based on the conversation history, conversation metadata,
    and

    the in-progress message text the agent has already typed into the composer.
  version: 0.0.3
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: AutoCompose
    description: Improve agent productivity with AutoCompose API
paths:
  /autocompose/v1/responses/customs/response:
    parameters:
      - name: agentId
        description: Identifier of the agent, data format is expected to be UUID
        in: query
        required: true
        schema:
          type: string
    post:
      tags:
        - AutoCompose
      summary: Create a custom response
      description: Add a single custom response for an agent
      operationId: addCustomResponse
      requestBody:
        description: The custom response to be added
        content:
          application/json:
            schema:
              type: object
              properties:
                text:
                  type: string
                  description: The text of the response
                title:
                  type: string
                  description: The title of the response
                folderId:
                  type: string
                  description: >-
                    the ID of the folder the response belongs to (used for
                    custom responses).
                metadata:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: the name of this metadata item
                      allowedValues:
                        type: array
                        items:
                          type: string
                        description: the list of allowed values for this metadata item
                  description: >-
                    free-form metadata, in the form of a map of keys to lists of
                    allowed values for each key, that can be added to any
                    response. At least one of the values in the list for each
                    key included  here must match what gets sent when requesting
                    suggestions, so that responses can be filtered
                    appropriately.
              required:
                - text
                - title
              example:
                text: fold text
                title: folder title
                folderId: '123'
        required: true
      responses:
        '200':
          description: Acknowledgement that the response was successfully added
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of this response, data format is UUID
                    readOnly: true
                  text:
                    type: string
                    description: The text of the response
                  title:
                    type: string
                    description: >-
                      The title of the response. Always non-empty for custom
                      responses, but may be empty for other types of responses
                      (global and organic).
                  folderId:
                    type: string
                    description: the ID of the folder the response belongs to.
                  metadata:
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                          description: the name of this metadata item
                        allowedValues:
                          type: array
                          items:
                            type: string
                          description: the list of allowed values for this metadata item
                    description: >-
                      free-form metadata, in the form of a map of keys to lists
                      of allowed values for each key, that can be added to any
                      response. At least one of the values in the list for each
                      key included  here must match what gets sent when
                      requesting suggestions, so that responses can be filtered
                      appropriately.
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