# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/events/create-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Events

> Record a batch of Events.

For more information, see https://docs.prefect.io/v3/concepts/events.



## OpenAPI

````yaml post /events
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /events:
    post:
      tags:
        - Events
      summary: Create Events
      description: |-
        Record a batch of Events.

        For more information, see https://docs.prefect.io/v3/concepts/events.
      operationId: create_events_events_post
      parameters:
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
              type: array
              items:
                $ref: '#/components/schemas/Event'
              title: Events
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Event:
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
      type: object
      required:
        - occurred
        - event
        - resource
        - id
      title: Event
      description: The client-side view of an event that has happened to a Resource
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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