# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/events/read-account-events-page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Account Events Page

> Returns the next page of Events for a previous query against the given Account, and
the URL to request the next page (if there are more results).



## OpenAPI

````yaml get /events/filter/next
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /events/filter/next:
    get:
      tags:
        - Events
      summary: Read Account Events Page
      description: >-
        Returns the next page of Events for a previous query against the given
        Account, and

        the URL to request the next page (if there are more results).
      operationId: read_account_events_page_events_filter_next_get
      parameters:
        - name: page-token
          in: query
          required: true
          schema:
            type: string
            title: Page-Token
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
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

````

Built with [Mintlify](https://mintlify.com).