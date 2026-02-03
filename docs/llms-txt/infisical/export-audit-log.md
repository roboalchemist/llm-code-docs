# Source: https://infisical.com/docs/api-reference/endpoints/audit-logs/export-audit-log.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Export

> Get all audit logs for an organization



## OpenAPI

````yaml GET /api/v1/organization/audit-logs
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/organization/audit-logs:
    get:
      tags:
        - Audit Logs
      description: Get all audit logs for an organization
      operationId: listOrganizationAuditLogs
      parameters:
        - schema:
            type: string
          in: query
          name: projectId
          required: false
          description: >-
            Optionally filter logs by project ID. If not provided, logs from the
            entire organization will be returned.
        - schema:
            type: string
          in: query
          name: environment
          required: false
          description: >-
            The environment to filter logs by. If not provided, logs from all
            environments will be returned. Note that the projectId parameter
            must also be provided.
        - schema:
            type: string
            enum:
              - platform
              - kmipClient
              - user
              - service
              - identity
              - scimClient
              - acmeProfile
              - acmeAccount
              - estAccount
              - unknownUser
          in: query
          name: actorType
          required: false
        - schema:
            type: string
          in: query
          name: secretPath
          required: false
          description: >-
            The path of the secret to query audit logs for. Note that the
            projectId parameter must also be provided.
        - schema:
            type: string
          in: query
          name: secretKey
          required: false
          description: >-
            The key of the secret to query audit logs for. Note that the
            projectId parameter must also be provided.
        - schema:
            type: string
          in: query
          name: eventType
          required: false
        - schema:
            type: string
            enum:
              - web
              - cli
              - k8-operator
              - terraform
              - other
              - InfisicalPythonSDK
              - InfisicalNodeSDK
          in: query
          name: userAgentType
          required: false
          description: Choose which consuming application to export audit logs for.
        - schema:
            type: string
          in: query
          name: eventMetadata
          required: false
          description: >-
            Filter by event metadata key-value pairs. Formatted as
            `key1=value1,key2=value2`, with comma-separation.
        - schema:
            type: string
            format: date-time
          in: query
          name: startDate
          required: false
          description: The date to start the export from.
        - schema:
            type: string
            format: date-time
          in: query
          name: endDate
          required: false
          description: The date to end the export at.
        - schema:
            type: number
            default: 0
          in: query
          name: offset
          required: false
          description: >-
            The offset to start from. If you enter 10, it will start from the
            10th audit log.
        - schema:
            type: number
            maximum: 1000
            default: 20
          in: query
          name: limit
          required: false
          description: The number of audit logs to return.
        - schema:
            type: string
          in: query
          name: actor
          required: false
          description: The actor to filter the audit logs by.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  auditLogs:
                    type: array
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
                required:
                  - auditLogs
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false

````