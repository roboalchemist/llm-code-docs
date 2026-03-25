# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits/read-concurrency-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Concurrency Limits

> Query for concurrency limits.

For each concurrency limit the `active slots` field contains a list of TaskRun IDs
currently using a concurrency slot for the specified tag.



## OpenAPI

````yaml post /concurrency_limits/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /concurrency_limits/filter:
    post:
      tags:
        - Concurrency Limits
      summary: Read Concurrency Limits
      description: >-
        Query for concurrency limits.


        For each concurrency limit the `active slots` field contains a list of
        TaskRun IDs

        currently using a concurrency slot for the specified tag.
      operationId: read_concurrency_limits_concurrency_limits_filter_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_read_concurrency_limits_concurrency_limits_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ConcurrencyLimit'
                title: >-
                  Response Read Concurrency Limits Concurrency Limits Filter
                  Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_concurrency_limits_concurrency_limits_filter_post:
      properties:
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_concurrency_limits_concurrency_limits_filter_post
    ConcurrencyLimit:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        tag:
          type: string
          title: Tag
          description: A tag the concurrency limit is applied to.
        concurrency_limit:
          type: integer
          title: Concurrency Limit
          description: The concurrency limit.
        active_slots:
          items:
            type: string
            format: uuid
          type: array
          title: Active Slots
          description: A list of active run ids using a concurrency slot
      type: object
      required:
        - tag
        - concurrency_limit
        - id
        - created
        - updated
      title: ConcurrencyLimit
      description: An ORM representation of a concurrency limit.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).