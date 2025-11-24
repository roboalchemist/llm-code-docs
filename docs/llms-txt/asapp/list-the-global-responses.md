# Source: https://docs.asapp.com/apis/autocompose/list-the-global-responses.md

# List the global responses

> Get the global responses and folder organization for a company. Responses are sorted by text, and folders are sorted by name.

## OpenAPI

````yaml api-specs/autocompose.yaml get /autocompose/v1/responses/globals
paths:
  path: /autocompose/v1/responses/globals
  method: get
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
      query:
        folderId:
          schema:
            - type: string
              required: false
              description: >-
                Optional identifier for the ID of the folder containing
                responses to be retrieved. If this is omitted, all global
                responses are returned.  Data format is expected to be UUID. The
                special value '__root' can also be used to retrieve top level
                folders/responses.
        resourceType:
          schema:
            - type: enum<string>
              enum:
                - folders
                - responses
                - all
              required: false
              description: >-
                Optional identifier for the ID of the type of responses to be
                retrieved. A value of 'folders' will return only folder
                information describing the way responses are organized. A value
                of 'responses' will return only responses. A value of 'all' will
                return a mix of folders and responses. Note that if the folderId
                parameter is specified as well, only the resource type
                identified here that exists within the specified folder will be
                returned. If this is omitted, all resources are returned.
              default: all
        searchTerm:
          schema:
            - type: string
              required: false
              description: >-
                Search term to search for global responses. This will search for
                matching folder names, response text or both, depending on the
                resourceType parameter value.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                This service responds with a set of global responses. These are
                divided into pages, with maxPerPage items in each page. This
                parameter is the page token returned in the call prior to this
                one. If this is the first call being made, this field should be
                omitted. The server will respond with global responses following
                the one previously sent.
        maxPerPage:
          schema:
            - type: integer
              required: false
              description: >-
                The maximum number of custom responses the client can handle
                within one page
              default: 1000
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              responses:
                allOf:
                  - type: object
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
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        description: The ID of this version of the global responses
                        readOnly: true
                      description:
                        type: string
                        description: A human-readable description of the version
        examples:
          example:
            value:
              responses:
                responsesList:
                  - id: <string>
                    text: <string>
                    title: <string>
                    folderId: <string>
                    metadata:
                      - name: <string>
                        allowedValues:
                          - <string>
                folderList:
                  - id: '123'
                    parentFolderId: '456'
                    name: folder name
                pageToken: <string>
              version:
                id: <string>
                description: <string>
        description: The global responses for this company
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Bad request response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 400-01
                message: Bad request
        description: 400 - Bad request
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