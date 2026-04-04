# Source: https://docs.together.ai/reference/listendpoints.md

# List All Endpoints

> Returns a list of all endpoints associated with your account. You can filter the results by type (dedicated or serverless).



## OpenAPI

````yaml GET /endpoints
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
  /endpoints:
    get:
      tags:
        - Endpoints
      summary: List all endpoints, can be filtered by type
      description: >-
        Returns a list of all endpoints associated with your account. You can
        filter the results by type (dedicated or serverless).
      operationId: listEndpoints
      parameters:
        - name: type
          in: query
          required: false
          schema:
            type: string
            enum:
              - dedicated
              - serverless
          description: Filter endpoints by type
          example: dedicated
        - name: usage_type
          in: query
          required: false
          schema:
            type: string
            enum:
              - on-demand
              - reserved
          description: Filter endpoints by usage type
          example: on-demand
        - name: mine
          in: query
          required: false
          schema:
            type: boolean
          description: If true, return only endpoints owned by the caller
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                required:
                  - object
                  - data
                properties:
                  object:
                    type: string
                    enum:
                      - list
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/ListEndpoint'
                example:
                  object: list
                  data:
                    - object: endpoint
                      id: endpoint-5c0c20db-62fe-4f41-8ffc-d9e4ea1a264e
                      name: allenai/OLMo-7B
                      model: allenai/OLMo-7B
                      type: serverless
                      owner: together
                      state: STARTED
                      created_at: '2024-02-28T21:34:35.444Z'
        '403':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    ListEndpoint:
      type: object
      description: Details about an endpoint when listed via the list endpoint
      required:
        - id
        - object
        - name
        - model
        - type
        - owner
        - state
        - created_at
      properties:
        object:
          type: string
          enum:
            - endpoint
          description: The type of object
          example: endpoint
        id:
          type: string
          description: Unique identifier for the endpoint
          example: endpoint-d23901de-ef8f-44bf-b3e7-de9c1ca8f2d7
        name:
          type: string
          description: System name for the endpoint
          example: allenai/OLMo-7B
        model:
          type: string
          description: The model deployed on this endpoint
          example: allenai/OLMo-7B
        type:
          type: string
          enum:
            - serverless
            - dedicated
          description: The type of endpoint
          example: serverless
        owner:
          type: string
          description: The owner of this endpoint
          example: together
        state:
          type: string
          enum:
            - PENDING
            - STARTING
            - STARTED
            - STOPPING
            - STOPPED
            - ERROR
          description: Current state of the endpoint
          example: STARTED
        created_at:
          type: string
          format: date-time
          description: Timestamp when the endpoint was created
          example: '2024-02-28T21:34:35.444Z'
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt