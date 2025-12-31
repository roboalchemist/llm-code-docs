# Source: https://infisical.com/docs/api-reference/endpoints/audit-logs/export-audit-log.md

# Export

> Get all audit logs for an organization

## OpenAPI

````yaml GET /api/v1/organization/audit-logs
paths:
  path: /api/v1/organization/audit-logs
  method: get
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path: {}
      query:
        projectId:
          schema:
            - type: string
              required: false
              description: >-
                Optionally filter logs by project ID. If not provided, logs from
                the entire organization will be returned.
        environment:
          schema:
            - type: string
              required: false
              description: >-
                The environment to filter logs by. If not provided, logs from
                all environments will be returned. Note that the projectId
                parameter must also be provided.
        actorType:
          schema:
            - type: enum<string>
              enum:
                - platform
                - kmipClient
                - user
                - service
                - identity
                - machine
                - scimClient
                - acmeAccount
                - unknownUser
              required: false
        secretPath:
          schema:
            - type: string
              required: false
              description: >-
                The path of the secret to query audit logs for. Note that the
                projectId parameter must also be provided.
        secretKey:
          schema:
            - type: string
              required: false
              description: >-
                The key of the secret to query audit logs for. Note that the
                projectId parameter must also be provided.
        eventType:
          schema:
            - type: string
              required: false
        userAgentType:
          schema:
            - type: enum<string>
              enum:
                - web
                - cli
                - k8-operator
                - terraform
                - other
                - InfisicalPythonSDK
                - InfisicalNodeSDK
              required: false
              description: Choose which consuming application to export audit logs for.
        eventMetadata:
          schema:
            - type: string
              required: false
              description: >-
                Filter by event metadata key-value pairs. Formatted as
                `key1=value1,key2=value2`, with comma-separation.
        startDate:
          schema:
            - type: string
              required: false
              description: The date to start the export from.
              format: date-time
        endDate:
          schema:
            - type: string
              required: false
              description: The date to end the export at.
              format: date-time
        offset:
          schema:
            - type: number
              required: false
              description: >-
                The offset to start from. If you enter 10, it will start from
                the 10th audit log.
              default: 0
        limit:
          schema:
            - type: number
              required: false
              description: The number of audit logs to return.
              maximum: 1000
              default: 20
        actor:
          schema:
            - type: string
              required: false
              description: The actor to filter the audit logs by.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              auditLogs:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        ipAddress:
                          type: string
                          nullable: true
                        userAgent:
                          type: string
                          nullable: true
                        userAgentType:
                          type: string
                          nullable: true
                        expiresAt:
                          type: string
                          format: date-time
                          nullable: true
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                        orgId:
                          type: string
                          format: uuid
                          nullable: true
                        projectId:
                          type: string
                          nullable: true
                        projectName:
                          type: string
                          nullable: true
                        event:
                          type: object
                          properties:
                            type:
                              type: string
                            metadata: {}
                          required:
                            - type
                          additionalProperties: false
                        actor:
                          type: object
                          properties:
                            type:
                              type: string
                            metadata: {}
                          required:
                            - type
                          additionalProperties: false
                      required:
                        - id
                        - createdAt
                        - updatedAt
                        - event
                        - actor
                      additionalProperties: false
            requiredProperties:
              - auditLogs
            additionalProperties: false
        examples:
          example:
            value:
              auditLogs:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  ipAddress: <string>
                  userAgent: <string>
                  userAgentType: <string>
                  expiresAt: '2023-11-07T05:31:56Z'
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  projectId: <string>
                  projectName: <string>
                  event:
                    type: <string>
                    metadata: <any>
                  actor:
                    type: <string>
                    metadata: <any>
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````