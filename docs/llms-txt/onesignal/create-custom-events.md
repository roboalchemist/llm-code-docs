# Source: https://documentation.onesignal.com/reference/create-custom-events.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create custom events

> The Custom Events API allows you to record user events. Custom events can represent any action users take in your application, such as completing a purchase, viewing content, or achieving milestones.

## Overview

The Custom Events API allows you to track user events. Custom events can represent any action users take in your application, such as completing a purchase, viewing content, or achieving milestones. See [Custom events](/docs/en/custom-events) for more information.

### Use Cases

Custom events can be used to:

* Enter users into [Journeys](/docs/en/journeys-settings)
* Trigger Journey [Wait Until](/docs/en/journeys-actions) nodes

### Error handling

If individual events can't be processed, an `errors` key will be returned in the response (with HTTP status 202) containing information about each failing event. The most common event-specific error is a failure to find a user associated with the External ID or OneSignal ID in the event.

If you'd like to retry sending events in the case of a failure, you only need to re-send the events for which errors were returned -- events that don't have an error associated with them are still processed. However, if a 5xx HTTP response is returned, you must retry the entire batch of events.

In either case, if you are implementing retry, make sure to also pass an [`idempotency_key`](/reference/idempotent-notification-requests).

### Duplicate events

If you implement retry behavior for your custom event delivery, please provide the [`idempotency_key`](/reference/idempotent-notification-requests) field. Each unique event should get its own unique UUID, and when retrying delivery for events, the same UUID must be provided. Duplicate events with the same `idempotency_key` will be ignored on a best-effort basis within a 4-hour period. This allows you to avoid erroneously triggering Journeys multiple times or incurring charges for storing unnecessary duplicate events.

***

## OpenAPI

````yaml POST /apps/{app_id}/custom_events
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/custom_events:
    post:
      summary: Create Custom Events
      description: >-
        The Custom Events API allows you to record user events. Custom events
        can represent any action users take in your application, such as
        completing a purchase, viewing content, or achieving milestones.
      operationId: create-custom-events
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: Authorization
          in: header
          description: >-
            Your app API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
            default: Key YOUR_APP_API_KEY
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - events
              properties:
                events:
                  type: array
                  description: >-
                    Array of event objects to be recorded. Maximum size for each
                    event is `2024` bytes. Maximum size of request is `1` MB.
                  items:
                    properties:
                      name:
                        type: string
                        description: >-
                          The identifier or name of the event. Maximum 128
                          characters.
                      external_id:
                        type: string
                        description: >-
                          The external ID of the user targeted for the event.
                          Either the user's External ID or OneSignal ID is
                          required.
                      onesignal_id:
                        type: string
                        description: >-
                          The OneSignal ID of the user targeted for the event.
                          Either the user's External ID or OneSignal ID is
                          required.
                      timestamp:
                        type: string
                        description: >-
                          Time the event occurred as an [ISO8601 formatted
                          string](https://www.timestamp-converter.com/).
                          Defaults to the current time if not provided. If the
                          timestamp provided is in the future, it will be reset
                          to the current time.
                      idempotency_key:
                        type: string
                        description: >-
                          A unique UUID for avoiding duplicate custom event
                          processing. Repeated events with the same
                          idempotency_key will not be processed.
                      properties:
                        type: object
                        description: >-
                          Properties or data related to the event, like
                          {"geography": "USA"}
                    required:
                      - name
                    type: object
      responses:
        '202':
          description: '202'
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    description: >-
                      Errors for specific events in the payload. If this is
                      returned, only the specified events have failed -- other
                      events in the same payload were successfully processed.
                    items:
                      type: object
                      properties:
                        event_user_id:
                          type: string
                          description: The External ID in the event that failed.
                          example: abc123
                        event_id:
                          type: string
                          description: >-
                            The value of the `event_id` property in the event,
                            if it has one.
                          example: 567491ee-9105-4a87-9cbc-ed78a571645b
                        error:
                          type: object
                          description: >-
                            Information about the error that caused the event to
                            not be processed.
                          properties:
                            code:
                              type: string
                              description: A short error code describing the error.
                              example: not found
                            title:
                              type: string
                              description: >-
                                Human-readable information about what caused the
                                error.
                              example: failed to find a onesignal_id for user_id abc123
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value: '{}'
              schema:
                type: object
                properties: {}
        '401':
          description: '401'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
        '429':
          description: '429'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
