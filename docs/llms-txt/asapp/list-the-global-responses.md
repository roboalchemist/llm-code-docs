# Source: https://docs.asapp.com/apis/autocompose/list-the-global-responses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List the global responses

> Get the global responses and folder organization for a company. Responses are sorted by text, and folders are sorted by name.



## OpenAPI

````yaml api-specs/autocompose.yaml get /autocompose/v1/responses/globals
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
  /autocompose/v1/responses/globals:
    get:
      tags:
        - AutoCompose
      summary: List the global responses
      description: >-
        Get the global responses and folder organization for a company.
        Responses are sorted by text, and folders are sorted by name.
      operationId: getGlobalResponses
      parameters:
        - in: query
          name: folderId
          schema:
            type: string
          required: false
          description: >-
            Optional identifier for the ID of the folder containing responses to
            be retrieved. If this is omitted, all global responses are
            returned.  Data format is expected to be UUID. The special value
            '__root' can also be used to retrieve top level folders/responses.
        - in: query
          name: resourceType
          schema:
            type: string
            enum:
              - folders
              - responses
              - all
            default: all
          required: false
          description: >-
            Optional identifier for the ID of the type of responses to be
            retrieved. A value of 'folders' will return only folder information
            describing the way responses are organized. A value of 'responses'
            will return only responses. A value of 'all' will return a mix of
            folders and responses. Note that if the folderId parameter is
            specified as well, only the resource type identified here that
            exists within the specified folder will be returned. If this is
            omitted, all resources are returned.
        - in: query
          name: searchTerm
          schema:
            type: string
          required: false
          description: >-
            Search term to search for global responses. This will search for
            matching folder names, response text or both, depending on the
            resourceType parameter value.
          example: greetings
        - in: query
          name: pageToken
          description: >-
            This service responds with a set of global responses. These are
            divided into pages, with maxPerPage items in each page. This
            parameter is the page token returned in the call prior to this one.
            If this is the first call being made, this field should be omitted.
            The server will respond with global responses following the one
            previously sent.
          required: false
          schema:
            type: string
          example: '3'
        - in: query
          name: maxPerPage
          description: >-
            The maximum number of custom responses the client can handle within
            one page
          required: false
          schema:
            type: integer
            default: 1000
      responses:
        '200':
          description: The global responses for this company
          content:
            application/json:
              schema:
                type: object
                properties:
                  responses:
                    type: object
                    description: A set of responses and folders for an agent
                    properties:
                      responsesList:
                        type: array
                        description: the list of responses with their associated metadata
                        items:
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
                                The title of the response. Always non-empty for
                                custom responses, but may be empty for other
                                types of responses (global and organic).
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
                                    description: >-
                                      the list of allowed values for this
                                      metadata item
                              description: >-
                                free-form metadata, in the form of a map of keys
                                to lists of allowed values for each key, that
                                can be added to any response. At least one of
                                the values in the list for each key included 
                                here must match what gets sent when requesting
                                suggestions, so that responses can be filtered
                                appropriately.
                      folderList:
                        type: array
                        description: the list of folders
                        items:
                          type: object
                          description: A folder of responses
                          properties:
                            id:
                              type: string
                              description: The ID of the folder
                              readOnly: true
                            parentFolderId:
                              type: string
                              description: The ID of the parent folder.
                            name:
                              type: string
                              description: the name of the folder
                          required:
                            - name
                          example:
                            id: '123'
                            parentFolderId: '456'
                            name: folder name
                      pageToken:
                        type: string
                        description: >-
                          the token to the next page if there is one, otherwise
                          empty
                  version:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID of this version of the global responses
                        readOnly: true
                      description:
                        type: string
                        description: A human-readable description of the version
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