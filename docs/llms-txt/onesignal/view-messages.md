# Source: https://documentation.onesignal.com/reference/view-messages.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View messages

> View the details for a collection of messages.

## Overview

The View messages API allows you to fetch data from up to 50 push, email, or SMS message at a time. If you want to get a single message's data, use the [View message](/reference/view-message) API. In most cases, you will likely want to use [Event Streams](/docs/en/event-streams) instead.

Currently this API does not provide Journey-sent messages. See [Journey analytics](/docs/en/journeys-analytics) for details.

Messages sent through the API are only **accessible 30 days after creation**; however, messages sent using the OneSignal dashboard are accessible for the app's lifetime.

See our [Rate limits](/reference/rate-limits) for details on how often you can pull your message data with this API.

***

## How to use this API

### Standard Pagination

Using the `limit` and `offset` parameters you can make multiple requests to page through the notifications for an app. You can pull a maximum of 50 messages at a time and with each request, use `limit` to specify the result size and `offset` to increment by the limit value each time. The default`limit` if not specified is `50`.

For example, your first request can have `offset=0`, second request will have `offset=50`, third request `offset=100`, etc.

Pagination queries using `limit` and `offset` are convenient but can suffer from poor latency especially as the `offset` value grows. Therefore standard pagination is not well suited to any ETL use cases. Consider using [Event Streams](/docs/en/event-streams) instead.

### Optimized Pagination - Time Offset

To efficiently retrieve all available messages for an app, use `time_offset`-based pagination. When `time_offset` is specified, the sort order changes from descending to ascending, meaning the oldest messages appear first based on the [`send_after` date](/reference/create-message#send-after).

#### `time_offset` Accepted Values

* [ISO8601 formatted timestamp](https://www.timestamp-converter.com/) – e.g., 2025-01-01T00:00:00.000Z (January 1st, 2025, at 12:00 AM UTC).
* Base64 integer token – provided in the API response.

<Steps>
  <Step title="Initial Fetch">
    To fetch messages from a specific date onward, set `time_offset` to an [ISO8601 formatted timestamp](https://www.timestamp-converter.com/). For example, to retrieve messages sent since January 1st, 2025 - `time_offset=2025-01-01T00:00:00.000Z`

    <Frame caption="ISO8601 formatted timestamp">
      <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/reference/64ede8a0c83ec3c104768aded27c70c369b54d3b01ee5db69fcb63518b7259fc-Screenshot_2025-01-08_at_1.01.01_PM.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=2444f162155f0af85839520676e1d5b0" width="1214" height="700" data-path="images/reference/64ede8a0c83ec3c104768aded27c70c369b54d3b01ee5db69fcb63518b7259fc-Screenshot_2025-01-08_at_1.01.01_PM.png" />
    </Frame>

    <Note>
      Important Notes:

      * `time_offset` cannot be used with the standard `offset` parameter.
      * It excludes messages that match the exact timestamp to avoid duplicates.
      * Messages created through our API are typically retained for 30 days.
      * The response includes `next_time_offset`, a cursor token for the next page. No decoding of the token required. For example: `"next_time_offset": "MjAyNS0wMi0xOVQxOToxNjo0OS41Njg5NTFaIzQ2ZWVjMTAzLWQ5OGYtNGQzZC04MzA5LWQxNWI1M2QzMjQ5Nw=="`
    </Note>
  </Step>

  <Step title="Fetch Additional Pages">
    Use `next_time_offset` from the previous response as the `time_offset` value in the next request. For example `time_offset=MjAyNS0wMi0xOVQxOToxNjo0OS41Njg5NTFaIzQ2ZWVjMTAzLWQ5OGYtNGQzZC04MzA5LWQxNWI1M2QzMjQ5Nw==`
  </Step>

  <Step title="Continue Until Completion">
    Repeat the requests until an empty `"notifications"` array is returned, indicating all messages have been fetched.
  </Step>

  <Step title="Handling New Messages">
    Since sorting is in ascending order, new messages are added to the end of the results. To resume fetching from where you left off, reuse the last `next_time_offset` that returned an empty response.
  </Step>
</Steps>

***

## OpenAPI

````yaml GET /notifications?app_id={app_id}&limit={limit}&offset={offset}&kind={kind}&template_id={template_id}&time_offset={time_offset}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /notifications?app_id={app_id}&limit={limit}&offset={offset}&kind={kind}&template_id={template_id}&time_offset={time_offset}:
    get:
      summary: View messages
      description: View the details for a collection of messages.
      operationId: view-messages
      parameters:
        - name: app_id
          in: query
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: YOUR_APP_ID
        - name: Authorization
          in: header
          description: >-
            Your App API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: Key YOUR_APP_API_KEY
        - name: limit
          in: query
          description: >-
            Specifies the maximum number of messages to return in a single
            query. The maximum and default is **50** messages per request.
          schema:
            type: integer
            format: int32
        - name: offset
          in: query
          description: >-
            Controls the starting point for the notifications being returned.
            Default is **0**. Results are returned and sorted in descending
            order by `queued_at`.
          schema:
            type: integer
            format: int32
        - name: kind
          in: query
          description: >-
            Specifies which push notifications to return based on how it was
            created. Use this to segment push by their creation method, allowing
            for targeted analysis or management of notification types. All push
            types are returned by default. `0` - Notifications created through
            the dashboard. `1` - Notifications sent via API calls. `3` -
            Notifications triggered through automated systems.
          schema:
            type: integer
            format: int32
        - name: template_id
          in: query
          description: >-
            The template ID in UUID v4 format set for the message if applicable.
            See [Templates](/docs/templates).
          schema:
            type: string
        - name: time_offset
          in: query
          description: >-
            An ISO 8601 formatted timestamp or Base64 integer token (provided in
            the API response). See [`time_offset` Accepted
            Values](#time_offset-accepted-values).
          schema:
            type: string
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Returns all message properties for up to 50 messages per
                  request. See the [Push
                  notifications](/reference/push-notification),
                  [Email](/reference/email), and/or [SMS](/reference/sms)
                  Message Create APIs for all properties. Most commonly used
                  properties for this endpoint are listed.
                properties:
                  total_count:
                    type: integer
                    description: >-
                      The total number of messages available in the dashboard
                      irrespective of page
                  time_offset:
                    type: string
                    description: The `time_offset` if specified in the request.
                  next_time_offset:
                    type: integer
                    description: >-
                      A Base64 integer token representing the next group of
                      messages to fetch if `time_offset` provided.
                  offset:
                    type: integer
                    description: >-
                      The offset specified. Defaults to `0` if not provided in
                      the request.
                  limit:
                    type: integer
                    description: >-
                      The `limit` specified. Defaults to `50` if not provided in
                      the request.
                  notifications:
                    type: array
                    description: >-
                      An array of message objects. `notifications: []` indicates
                      no more messages to fetch. The data provided is generally
                      the most desired from this request
                    items:
                      type: object
                      properties:
                        app_id:
                          type: string
                          description: >-
                            Your OneSignal App ID in UUID v4 format. See [Keys &
                            IDs](/docs/keys-and-ids).
                        big_picture:
                          description: The URL of the image set in the push notification.
                          type: string
                        canceled:
                          description: Whether the message was canceled.
                          type: boolean
                        chrome_web_icon:
                          description: The URL of the icon set in the push notification.
                          type: string
                        chrome_web_image:
                          description: The URL of the image set in the push notification.
                          type: string
                        name:
                          type: string
                          description: >-
                            An internal name you set to help organize and track
                            messages. Not shown to recipients. Maximum 128
                            characters.
                        contents:
                          description: >-
                            The main message body with [language-specific
                            values](/docs/multi-language-messaging#supported-languages).
                          type: object
                          properties:
                            en:
                              type: string
                              description: >-
                                The required message language type. See
                                [Supported
                                Languages](/docs/multi-language-messaging#supported-languages).
                        converted:
                          type: integer
                          description: The number of times the push was clicked.
                        data:
                          type: object
                          description: >-
                            The JSON data set in the push notification if
                            applicable.
                        delayed_option:
                          type: string
                          description: The per-user delay option set for the message.
                        delivery_time_of_day:
                          type: string
                          description: >-
                            The delivery time of day set for the message if
                            `delayed_option` is `timezone`.
                        remaining:
                          type: integer
                          description: >-
                            The number of messages that have not been sent yet.
                            If `null`, then the system is still processing the
                            audience, try again later.
                        errored:
                          type: integer
                          description: The number of times the message errored.
                        excluded_segments:
                          type: array
                          description: >-
                            The segments excluded from the message if
                            applicable.
                        failed:
                          type: integer
                          description: >-
                            The number of subscriptions reported unsubscribed
                            for the message.
                        global_image:
                          description: The URL of the image set in the push notification.
                          type: string
                        headings:
                          type: object
                          description: The title of the push notification.
                        id:
                          type: string
                          description: The identifier of the message in UUID v4 format.
                        included_segments:
                          type: array
                          description: The segments included in the message if applicable.
                        ios_badgeCount:
                          type: integer
                          description: The badge count set for the message if applicable.
                        ios_badgeType:
                          type: string
                          description: The badge type set for the message if applicable.
                        queued_at:
                          type: integer
                          description: Unix timestamp of when the message was created.
                        send_after:
                          type: integer
                          description: >-
                            Unix timestamp of when the message delivery was
                            scheduled to begin.
                        completed_at:
                          type: integer
                          description: >-
                            Unix timestamp of when the message delivery was
                            completed. The delivery duration from start to
                            finish can be calculated with `completed_at -
                            send_after`. 
                        successful:
                          type: integer
                          description: >-
                            The number of messages successfully delivered to the
                            push, email, or SMS servers.
                        received:
                          type: integer
                          description: >-
                            The number of messages that confirmed being received
                            aka [Confirmed
                            Deliveries](/docs/confirmed-delivery).
                        filters:
                          type: object
                          description: The filters set for the message if applicable.
                        template_id:
                          type: string
                          description: >-
                            The template ID in UUID v4 format set for the
                            message if applicable. See
                            [Templates](/docs/templates).
                        url:
                          type: string
                          description: The URL of the push notification.
                        web_url:
                          type: string
                          description: >-
                            The URL of the push notification for web push
                            subscriptions.
                        app_url:
                          type: string
                          description: >-
                            The URL of the push notification for mobile
                            subscriptions.
                        platform_delivery_stats:
                          type: object
                          description: >-
                            The successful, errored, failed, converted, received
                            and frequency cap counts for each platform
                            applicable.
                        throttle_rate_per_minute:
                          type: number
                          description: >-
                            The throttle rate of the push notification if
                            applicable.
                        fcap_status:
                          type: string
                          description: >-
                            The frequency cap status of the push notification if
                            applicable.
                        outcomes:
                          type: object
                          description: >-
                            The id, value, and aggregation type of the outcome
                            set in the request.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
