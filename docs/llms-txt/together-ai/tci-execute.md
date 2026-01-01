# Source: https://docs.together.ai/reference/tci-execute.md

# /tci/execute

> Executes the given code snippet and returns the output. Without a session_id, a new session will be created to run the code. If you do pass in a valid session_id, the code will be run in that session. This is useful for running multiple code snippets in the same environment, because dependencies and similar things are persisted
between calls to the same session.




## OpenAPI

````yaml POST /tci/execute
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /tci/execute:
    post:
      tags:
        - Code Interpreter
      description: >
        Executes the given code snippet and returns the output. Without a
        session_id, a new session will be created to run the code. If you do
        pass in a valid session_id, the code will be run in that session. This
        is useful for running multiple code snippets in the same environment,
        because dependencies and similar things are persisted

        between calls to the same session.
      operationId: tci/execute
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExecuteRequest'
        description: Execute Request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExecuteResponse'
          description: Execute Response
      callbacks: {}
components:
  schemas:
    ExecuteRequest:
      title: ExecuteRequest
      required:
        - language
        - code
      properties:
        code:
          description: Code snippet to execute.
          example: print('Hello, world!')
          type: string
        files:
          description: >-
            Files to upload to the session. If present, files will be uploaded
            before executing the given code.
          items:
            properties:
              content:
                type: string
              encoding:
                description: >-
                  Encoding of the file content. Use `string` for text files such
                  as code, and `base64` for binary files, such as images.
                enum:
                  - string
                  - base64
                type: string
              name:
                type: string
            required:
              - name
              - encoding
              - content
            type: object
          type: array
        language:
          default: python
          description: >-
            Programming language for the code to execute. Currently only
            supports Python, but more will be added.
          enum:
            - python
        session_id:
          description: >-
            Identifier of the current session. Used to make follow-up calls.
            Requests will return an error if the session does not belong to the
            caller or has expired.
          example: ses_abcDEF123
          nullable: false
          type: string
    ExecuteResponse:
      title: ExecuteResponse
      type: object
      description: >-
        The result of the execution. If successful, `data` contains the result
        and `errors` will be null. If unsuccessful, `data` will be null and
        `errors` will contain the errors.
      oneOf:
        - title: SuccessfulExecution
          type: object
          required:
            - data
            - errors
          properties:
            errors:
              type: 'null'
            data:
              type: object
              nullable: false
              required:
                - session_id
                - outputs
              properties:
                outputs:
                  type: array
                  items:
                    discriminator:
                      propertyName: type
                    oneOf:
                      - title: StreamOutput
                        description: Outputs that were printed to stdout or stderr
                        type: object
                        required:
                          - type
                          - data
                        properties:
                          type:
                            enum:
                              - stdout
                              - stderr
                            type: string
                          data:
                            type: string
                      - title: ErrorOutput
                        description: >-
                          Errors and exceptions that occurred. If this output
                          type is present, your code did not execute
                          successfully.
                        properties:
                          data:
                            type: string
                          type:
                            enum:
                              - error
                            type: string
                        required:
                          - type
                          - data
                      - properties:
                          data:
                            properties:
                              application/geo+json:
                                type: object
                                additionalProperties: true
                              application/javascript:
                                type: string
                              application/json:
                                type: object
                                additionalProperties: true
                              application/pdf:
                                format: byte
                                type: string
                              application/vnd.vega.v5+json:
                                type: object
                                additionalProperties: true
                              application/vnd.vegalite.v4+json:
                                type: object
                                additionalProperties: true
                              image/gif:
                                format: byte
                                type: string
                              image/jpeg:
                                format: byte
                                type: string
                              image/png:
                                format: byte
                                type: string
                              image/svg+xml:
                                type: string
                              text/html:
                                type: string
                              text/latex:
                                type: string
                              text/markdown:
                                type: string
                              text/plain:
                                type: string
                            type: object
                          type:
                            enum:
                              - display_data
                              - execute_result
                            type: string
                        required:
                          - type
                          - data
                        title: DisplayorExecuteOutput
                    title: InterpreterOutput
                session_id:
                  type: string
                  description: >-
                    Identifier of the current session. Used to make follow-up
                    calls.
                  example: ses_abcDEF123
                  nullable: false
                status:
                  type: string
                  enum:
                    - success
                  description: Status of the execution. Currently only supports success.
        - title: FailedExecution
          type: object
          required:
            - data
            - errors
          properties:
            data:
              type: 'null'
            errors:
              type: array
              items:
                oneOf:
                  - type: string
                  - type: object
                    additionalProperties: true
                title: Error
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt