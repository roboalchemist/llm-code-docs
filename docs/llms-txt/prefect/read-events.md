# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/events/read-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Events

> Queries for Events matching the given filter criteria in the given Account.  Returns
the first page of results, and the URL to request the next page (if there are more
results).



## OpenAPI

````yaml post /events/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /events/filter:
    post:
      tags:
        - Events
      summary: Read Events
      description: >-
        Queries for Events matching the given filter criteria in the given
        Account.  Returns

        the first page of results, and the URL to request the next page (if
        there are more

        results).
      operationId: read_events_events_filter_post
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
              $ref: '#/components/schemas/Body_read_events_events_filter_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventPage'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_events_events_filter_post:
      properties:
        filter:
          anyOf:
            - $ref: '#/components/schemas/EventFilter'
            - type: 'null'
          description: Additional optional filter criteria to narrow down the set of Events
        limit:
          type: integer
          maximum: 50
          minimum: 0
          title: Limit
          description: The number of events to return with each page
          default: 50
      type: object
      title: Body_read_events_events_filter_post
    EventPage:
      properties:
        events:
          items:
            $ref: '#/components/schemas/ReceivedEvent'
          type: array
          title: Events
          description: The Events matching the query
        total:
          type: integer
          title: Total
          description: The total number of matching Events
        next_page:
          anyOf:
            - type: string
              minLength: 1
              format: uri
            - type: 'null'
          title: Next Page
          description: The URL for the next page of results, if there are more
      type: object
      required:
        - events
        - total
        - next_page
      title: EventPage
      description: >-
        A single page of events returned from the API, with an optional link to
        the

        next page of results
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
    ReceivedEvent:
      properties:
        occurred:
          type: string
          format: date-time
          title: Occurred
          description: When the event happened from the sender's perspective
        event:
          type: string
          title: Event
          description: The name of the event that happened
        resource:
          $ref: '#/components/schemas/Resource'
          description: The primary Resource this event concerns
        related:
          items:
            $ref: '#/components/schemas/RelatedResource'
          type: array
          title: Related
          description: A list of additional Resources involved in this event
        payload:
          additionalProperties: true
          type: object
          title: Payload
          description: An open-ended set of data describing what happened
        id:
          type: string
          format: uuid
          title: Id
          description: The client-provided identifier of this event
        follows:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Follows
          description: >-
            The ID of an event that is known to have occurred prior to this one.
            If set, this may be used to establish a more precise ordering of
            causally-related events when they occur close enough together in
            time that the system may receive them out-of-order.
        received:
          type: string
          format: date-time
          title: Received
          description: When the event was received by Prefect Cloud
      type: object
      required:
        - occurred
        - event
        - resource
        - id
      title: ReceivedEvent
      description: >-
        The server-side view of an event that has happened to a Resource after
        it has

        been received by the server
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
    Resource:
      additionalProperties:
        type: string
      type: object
      title: Resource
      description: An observable business object of interest to the user
    RelatedResource:
      additionalProperties:
        type: string
      type: object
      title: RelatedResource
      description: A Resource with a specific role in an Event
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