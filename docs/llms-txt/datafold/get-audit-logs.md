# Source: https://docs.datafold.com/api-reference/audit-logs/get-audit-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Audit Logs



## OpenAPI

````yaml get /api/v1/audit_logs
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/audit_logs:
    get:
      tags:
        - Audit Logs
      summary: Get Audit Logs
      operationId: get_audit_logs_api_v1_audit_logs_get
      requestBody:
        content:
          application/json:
            schema:
              anyOf:
                - $ref: '#/components/schemas/ApiDownloadAuditLogs'
                - type: 'null'
              title: Data
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiGetAuditLogs'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiDownloadAuditLogs:
      properties:
        end_date:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: End Date
        start_date:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Start Date
      title: ApiDownloadAuditLogs
      type: object
    ApiGetAuditLogs:
      properties:
        logs:
          items:
            $ref: '#/components/schemas/AuditLogs'
          title: Logs
          type: array
      required:
        - logs
      title: ApiGetAuditLogs
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
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
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````