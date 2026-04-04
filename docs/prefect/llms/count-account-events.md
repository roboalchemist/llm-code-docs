# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/events/count-account-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Count Account Events

> Returns distinct objects and the count of events associated with them.  Objects
that can be counted include the day the event occurred, the type of event, or
the IDs of the resources associated with the event.



## OpenAPI

````yaml post /events/count-by/{countable}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /events/count-by/{countable}:
    post:
      tags:
        - Events
      summary: Count Account Events
      description: >-
        Returns distinct objects and the count of events associated with them. 
        Objects

        that can be counted include the day the event occurred, the type of
        event, or

        the IDs of the resources associated with the event.
      operationId: count_account_events_events_count_by__countable__post
      parameters:
        - name: countable
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/Countable'
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_count_account_events_events_count_by__countable__post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/EventCount'
                title: Response Count Account Events Events Count By  Countable  Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Countable:
      type: string
      enum:
        - day
        - time
        - event
        - resource
      title: Countable
    Body_count_account_events_events_count_by__countable__post:
      properties:
        filter:
          $ref: '#/components/schemas/EventFilter'
        time_unit:
          $ref: '#/components/schemas/TimeUnit'
          default: day
        time_interval:
          type: number
          minimum: 0.01
          title: Time Interval
          default: 1
      type: object
      required:
        - filter
      title: Body_count_account_events_events_count_by__countable__post
    EventCount:
      properties:
        value:
          type: string
          title: Value
          description: The value to use for filtering
        label:
          type: string
          title: Label
          description: The value to display for this count
        count:
          type: integer
          title: Count
          description: The count of matching events
        start_time:
          type: string
          format: date-time
          title: Start Time
          description: The start time of this group of events
        end_time:
          type: string
          format: date-time
          title: End Time
          description: The end time of this group of events
      type: object
      required:
        - value
        - label
        - count
        - start_time
        - end_time
      title: EventCount
      description: The count of events with the given filter value
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    EventFilter:
      properties:
        occurred:
          $ref: '#/components/schemas/EventOccurredFilter'
          description: Filter criteria for when the events occurred
        event:
          anyOf:
            - $ref: '#/components/schemas/EventNameFilter'
            - type: 'null'
          description: Filter criteria for the event name
        resource:
          anyOf:
            - $ref: '#/components/schemas/EventResourceFilter'
            - type: 'null'
          description: Filter criteria for the resource of the event
        related:
          anyOf:
            - $ref: '#/components/schemas/EventRelatedFilter'
            - items:
                $ref: '#/components/schemas/EventRelatedFilter'
              type: array
            - type: 'null'
          title: Related
          description: Filter criteria for the related resources of the event
        any_resource:
          anyOf:
            - $ref: '#/components/schemas/EventAnyResourceFilter'
            - items:
                $ref: '#/components/schemas/EventAnyResourceFilter'
              type: array
            - type: 'null'
          title: Any Resource
          description: Filter criteria for any resource involved in the event
        id:
          $ref: '#/components/schemas/EventIDFilter'
          description: Filter criteria for the events' ID
        text:
          anyOf:
            - $ref: '#/components/schemas/EventTextFilter'
            - type: 'null'
          description: Filter criteria for text search across event content
        order:
          $ref: '#/components/schemas/EventOrder'
          description: The order to return filtered events
          default: DESC
      additionalProperties: false
      type: object
      title: EventFilter
    TimeUnit:
      type: string
      enum:
        - week
        - day
        - hour
        - minute
        - second
      title: TimeUnit
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
    EventOccurredFilter:
      properties:
        since:
          type: string
          format: date-time
          title: Since
          description: Only include events after this time (inclusive)
        until:
          type: string
          format: date-time
          title: Until
          description: Only include events prior to this time (inclusive)
      additionalProperties: false
      type: object
      title: EventOccurredFilter
    EventNameFilter:
      properties:
        prefix:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Prefix
          description: Only include events matching one of these prefixes
        exclude_prefix:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Exclude Prefix
          description: Exclude events matching one of these prefixes
        name:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Name
          description: Only include events matching one of these names exactly
        exclude_name:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Exclude Name
          description: Exclude events matching one of these names exactly
      additionalProperties: false
      type: object
      title: EventNameFilter
    EventResourceFilter:
      properties:
        id:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Id
          description: Only include events for resources with these IDs
        id_prefix:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Id Prefix
          description: >-
            Only include events for resources with IDs starting with these
            prefixes.
        labels:
          anyOf:
            - $ref: '#/components/schemas/ResourceSpecification'
            - type: 'null'
          description: Only include events for resources with these labels
        distinct:
          type: boolean
          title: Distinct
          description: Only include events for distinct resources
          default: false
      additionalProperties: false
      type: object
      title: EventResourceFilter
    EventRelatedFilter:
      properties:
        id:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Id
          description: Only include events for related resources with these IDs
        role:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Role
          description: Only include events for related resources in these roles
        resources_in_roles:
          anyOf:
            - items:
                prefixItems:
                  - type: string
                  - type: string
                type: array
                maxItems: 2
                minItems: 2
              type: array
            - type: 'null'
          title: Resources In Roles
          description: >-
            Only include events with specific related resources in specific
            roles
        labels:
          anyOf:
            - $ref: '#/components/schemas/ResourceSpecification'
            - type: 'null'
          description: Only include events for related resources with these labels
      additionalProperties: false
      type: object
      title: EventRelatedFilter
    EventAnyResourceFilter:
      properties:
        id:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Id
          description: Only include events for resources with these IDs
        id_prefix:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Id Prefix
          description: >-
            Only include events for resources with IDs starting with these
            prefixes
        labels:
          anyOf:
            - $ref: '#/components/schemas/ResourceSpecification'
            - type: 'null'
          description: Only include events for related resources with these labels
      additionalProperties: false
      type: object
      title: EventAnyResourceFilter
    EventIDFilter:
      properties:
        id:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Id
          description: Only include events with one of these IDs
      additionalProperties: false
      type: object
      title: EventIDFilter
    EventTextFilter:
      properties:
        query:
          type: string
          maxLength: 200
          title: Query
          description: Text search query string
          examples:
            - error
            - error -debug
            - '"connection timeout"'
            - +required -excluded
      additionalProperties: false
      type: object
      required:
        - query
      title: EventTextFilter
      description: Filter by text search across event content.
    EventOrder:
      type: string
      enum:
        - ASC
        - DESC
      title: EventOrder
    ResourceSpecification:
      additionalProperties:
        anyOf:
          - type: string
          - items:
              type: string
            type: array
      type: object
      title: ResourceSpecification

````

Built with [Mintlify](https://mintlify.com).