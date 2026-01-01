# Source: https://docs.together.ai/reference/tci-sessions.md

# /tci/sessions

> Lists all your currently active sessions.




## OpenAPI

````yaml GET /tci/sessions
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
  /tci/sessions:
    get:
      tags:
        - Code Interpreter
      description: |
        Lists all your currently active sessions.
      operationId: sessions/list
      parameters: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SessionListResponse'
          description: List Response
      callbacks: {}
components:
  schemas:
    SessionListResponse:
      allOf:
        - properties:
            errors:
              type: array
              items:
                oneOf:
                  - type: string
                  - type: object
                    additionalProperties: true
                title: Error
          title: Response
          type: object
        - properties:
            data:
              properties:
                sessions:
                  items:
                    properties:
                      execute_count:
                        type: integer
                      expires_at:
                        type: string
                        format: date-time
                      id:
                        description: Session Identifier. Used to make follow-up calls.
                        example: ses_abcDEF123
                        type: string
                      last_execute_at:
                        type: string
                        format: date-time
                      started_at:
                        type: string
                        format: date-time
                    required:
                      - execute_count
                      - expires_at
                      - id
                      - last_execute_at
                      - started_at
                    type: object
                  type: array
              required:
                - sessions
          type: object
      title: SessionListResponse
      type: object
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt