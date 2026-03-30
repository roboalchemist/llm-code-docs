# Source: https://docs.salad.com/reference/saladcloud-api/logs/query-log-entries.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Log Entries

> Retrieve a collection of _log entries_ for the _organization_ identified by `{organization_name}` matching the log query.

*Last Updated: July 1, 2025*


## OpenAPI

````yaml api-specs/salad-cloud.yaml post /organizations/{organization_name}/log-entries
openapi: 3.1.0
info:
  title: SaladCloud API
  description: >-
    The SaladCloud REST API. Please refer to the [SaladCloud API
    Documentation](https://docs.salad.com/api-reference) for more details.
  termsOfService: https://salad.com/terms
  contact:
    name: SaladCloud Support
    url: https://salad.com
    email: cloud@salad.com
  license:
    name: MIT License
    identifier: MIT
  version: 0.9.0-alpha.16
servers:
  - url: https://api.salad.com/api/public
security:
  - ApiKeyAuth: []
tags:
  - name: container_groups
    description: Container Groups
  - name: inference_endpoints
    description: Inference Endpoints
  - name: organization_data
    description: Auxiliary organization data and info
  - name: queues
    description: Job Queues
  - name: quotas
    description: quotas
  - name: system_logs
    description: System Logs
  - name: webhook_secret_key
    description: Webhook Secret Key
  - name: logs
    description: Platform and Application Log Entries
paths:
  /organizations/{organization_name}/log-entries:
    parameters:
      - $ref: '#/components/parameters/organization_name'
    post:
      tags:
        - logs
      summary: Query Log Entries
      description: >-
        Retrieve a collection of _log entries_ for the _organization_ identified
        by `{organization_name}` matching the log query.
      operationId: query_log_entries
      requestBody:
        $ref: '#/components/requestBodies/QueryLogEntries'
      responses:
        '200':
          $ref: '#/components/responses/QueryLogEntries'
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '403':
          $ref: '#/components/responses/403'
        '404':
          $ref: '#/components/responses/404'
        '429':
          $ref: '#/components/responses/429'
        default:
          $ref: '#/components/responses/UnknownError'
components:
  parameters:
    organization_name:
      name: organization_name
      in: path
      description: >-
        Your organization name. This identifies the billing context for the API
        operation and represents a security boundary for SaladCloud resources.
        The organization must be created before using the API, and you must be a
        member of the organization.
      required: true
      schema:
        $ref: '#/components/schemas/OrganizationName'
  requestBodies:
    QueryLogEntries:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/LogEntryQuery'
  responses:
    '400':
      description: Bad Request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '401':
      description: Unauthorized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '403':
      description: Forbidden
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '404':
      description: Not Found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    '429':
      description: Too Many Requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
    QueryLogEntries:
      description: OK
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/LogEntryCollection'
    UnknownError:
      description: Unknown Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
  schemas:
    OrganizationName:
      description: The organization name.
      type: string
      examples:
        - acme-corp
      maxLength: 63
      minLength: 2
      pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      title: Organization Name
    LogEntryQuery:
      description: Represents a query for logs
      type: object
      properties:
        end_time:
          description: The end time of the time range
          type: string
          format: date-time
        page_size:
          $ref: '#/components/schemas/PageSize'
        query:
          description: The query string for filtering logs
          maxLength: 20000
          minLength: 0
          type: string
        sort_order:
          $ref: '#/components/schemas/LogEntryQuerySortOrder'
        start_time:
          description: The start time of the time range
          type: string
          format: date-time
      required:
        - end_time
        - query
        - start_time
    LogEntryCollection:
      description: Represents a page of organization logs
      type: object
      properties:
        items:
          description: A collection of log entries
          type: array
          items:
            $ref: '#/components/schemas/LogEntry'
          maxItems: 10000
          minItems: 0
        organization_name:
          $ref: '#/components/schemas/OrganizationName'
        page_max_time:
          description: >-
            The maximum time page boundary. This may be used when getting
            paginated results.
          type: string
          format: date-time
        page_min_time:
          description: >-
            The minimum time page boundary. This may be used when getting
            paginated results.
          type: string
          format: date-time
      required:
        - items
        - organization_name
        - page_max_time
        - page_min_time
    ProblemDetails:
      description: Represents an API error
      type: object
      properties:
        type:
          description: The URI reference that identifies the error type.
          type: string
          format: url
          default: about:blank
          examples:
            - https://example.com/errors/invalid-request
          maxLength: 2048
          minLength: 1
        title:
          description: The short, human-readable summary of the error type.
          type: string
          examples:
            - Not Found
          maxLength: 2000
          minLength: 1
        status:
          description: >-
            The HTTP status code generated by the origin server for this
            occurrence of the error.
          type: integer
          format: int32
          examples:
            - 404
          maximum: 599
          minimum: 100
        detail:
          description: >-
            The human-readable explanation specific to this occurrence of the
            error.
          type: string
          examples:
            - The container group could not be found.
          maxLength: 2000
          minLength: 1
        instance:
          description: >-
            The URI reference that identifies the specific occurrence of the
            error.
          type: string
          format: url
          examples:
            - https://example.com/error-instances/12345
          maxLength: 2048
          minLength: 1
    PageSize:
      description: The maximum number of items per page.
      type: integer
      format: int32
      examples:
        - 1
      maximum: 100
      minimum: 1
    LogEntryQuerySortOrder:
      description: >-
        The sort order of the log entries. `asc` will sort the log entries in
        chronological order. `desc` will sort the log entries in reverse
        chronological order.
      type: string
      default: desc
      enum:
        - desc
        - asc
    LogEntry:
      type: object
      properties:
        json_log:
          description: The log message in JSON format.
          type: object
          additionalProperties: true
        parent_span_id:
          description: The parent span ID of the log entry
          type: string
          maxLength: 1000
          minLength: 1
        receive_time:
          description: The time when the log entry was received
          type: string
          format: date-time
        resource:
          $ref: '#/components/schemas/LogEntryResource'
        severity:
          $ref: '#/components/schemas/LogEntrySeverity'
        span_Id:
          description: The span ID of the log entry
          type: string
          maxLength: 1000
          minLength: 1
        text_log:
          description: The log message in text format.
          type: string
          maxLength: 10000
          minLength: 0
        time:
          description: The timestamp of the log entry
          type: string
          format: date-time
        trace_Id:
          description: The trace ID of the log entry
          type: string
          maxLength: 1000
          minLength: 1
      required:
        - receive_time
        - resource
        - severity
        - time
    LogEntryResource:
      description: The resource associated with the log entry
      type: object
      properties:
        labels:
          description: The labels associated with the resource
          type: object
          additionalProperties:
            type: string
            minLength: 1
            maxLength: 1000
          maxProperties: 100
          minProperties: 0
        type:
          description: The type of the resource
          type: string
          maxLength: 1000
          minLength: 1
      additionalProperties: false
      required:
        - labels
        - type
    LogEntrySeverity:
      description: The severity level of the log entry
      type: string
      enum:
        - default
        - debug
        - info
        - notice
        - warning
        - error
        - critical
        - alert
        - emergency
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````