# Source: https://docs.datafold.com/api-reference/audit-logs/get-audit-logs.md

# Get Audit Logs

## OpenAPI

````yaml get /api/v1/audit_logs
paths:
  path: /api/v1/audit_logs
  method: get
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              end_date:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: End Date
              start_date:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: Start Date
            title: ApiDownloadAuditLogs
            refIdentifier: '#/components/schemas/ApiDownloadAuditLogs'
          - type: 'null'
            title: Data
        examples:
          example:
            value:
              end_date: '2023-11-07T05:31:56Z'
              start_date: '2023-11-07T05:31:56Z'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              logs:
                allOf:
                  - items:
                      $ref: '#/components/schemas/AuditLogs'
                    title: Logs
                    type: array
            title: ApiGetAuditLogs
            refIdentifier: '#/components/schemas/ApiGetAuditLogs'
            requiredProperties:
              - logs
        examples:
          example:
            value:
              logs:
                - action: <string>
                  client_ip: <string>
                  event_uuid: <string>
                  is_support_user: true
                  log_entry: <string>
                  object_id: 123
                  object_type: <string>
                  payload: {}
                  referer: <string>
                  request_type: <string>
                  source: <string>
                  status: <string>
                  timestamp: <string>
                  url: <string>
                  user_agent: <string>
                  user_email: <string>
                  user_id: 123
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    title: Detail
                    type: array
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    AuditLogs:
      properties:
        action:
          anyOf:
            - type: string
            - type: 'null'
          title: Action
        client_ip:
          title: Client Ip
          type: string
        event_uuid:
          title: Event Uuid
          type: string
        is_support_user:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Support User
        log_entry:
          anyOf:
            - type: string
            - type: 'null'
          title: Log Entry
        object_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Object Id
        object_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Object Type
        payload:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Payload
        referer:
          anyOf:
            - type: string
            - type: 'null'
          title: Referer
        request_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Request Type
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        status:
          anyOf:
            - type: string
            - type: 'null'
          title: Status
        timestamp:
          title: Timestamp
          type: string
        url:
          title: Url
          type: string
        user_agent:
          anyOf:
            - type: string
            - type: 'null'
          title: User Agent
        user_email:
          anyOf:
            - type: string
            - type: 'null'
          title: User Email
        user_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: User Id
      required:
        - timestamp
        - event_uuid
        - client_ip
        - url
      title: AuditLogs
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object

````