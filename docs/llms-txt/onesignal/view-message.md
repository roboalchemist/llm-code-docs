# Source: https://documentation.onesignal.com/reference/view-message.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View message

> View the details of a single message and the Outcomes associated with it.

## Overview

The View message API allows you to fetch data from a single push, email, or SMS message at a time. If you want to get multiple messages at a time, use the [View messages](/reference/view-messages) API. In most cases, you will likely want to use [Event Streams](/docs/en/event-streams) instead.

Currently this API does not provide Journey-sent messages. See [Journey analytics](/docs/en/journeys-analytics) for details.

Messages sent through the API are only **accessible 30 days after creation**; however, messages sent using the OneSignal dashboard are accessible for the app's lifetime.

See our [Rate limits](/reference/rate-limits) for details on how often you can pull your message data with this API.

***

## How to use this API

This API is most commonly used when sending [Transactional messages](/docs/en/transactional-messages) to individual users. The response of our Create message API has an `id` which corresponds to the `message_id` used in this request. You can store this `message_id` on your server and (after giving your users some time to interact with the message) pull the data if desired.

For example, if you send a message targeting the `include_aliases` parameter, the response will include the aliases you set. If you send with the `included_segments` parameter, then the response will only provide the segments you set. When targeting segments or filters, you can use the [Export audience activity CSV](/reference/export-csv-of-events) API to get the user event data.

To view outcome data for the message, you must include the `outcome_name` parameter with the name of the outcome you want to fetch, along with the accompanying aggregation type (.count or .sum), for example: `os__click.count`. For more information on outcome definitions, see [View Outcomes](/reference/view-outcomes).

***

## OpenAPI

````yaml GET /notifications/{message_id}?app_id={app_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /notifications/{message_id}?app_id={app_id}:
    get:
      summary: View message
      description: >-
        View the details of a single message and the Outcomes associated with
        it.
      operationId: view-message
      parameters:
        - name: message_id
          in: path
          description: >-
            The identifier of the message in UUID v4 format. Get this `id` in
            the response of your Create Message API request, the [View Messages
            API](/reference/view-messages), and in your OneSignal dashboard
            Message Reports.
          schema:
            type: string
          required: true
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
        - name: outcome_names
          in: query
          description: >-
            The name and aggregation type of the outcome(s) you want to fetch.
            Example: `my_outcome.count` or `my_outcome.sum`. For clicks, use
            `os__click.count`. For confirmed deliveries, use
            `os__confirmed_delivery.count`. For session duration, use
            `os__session_duration.count`.
          schema:
            type: array
            items:
              type: string
              default:
                - os__click.count
                - os__confirmed_delivery.count
                - os__session_duration.count
        - name: outcome_time_range
          in: query
          description: >-
            Time range for the returned data. Available values: `1h` (1 hour),
            `1d` (1 day), `1mo` (1 month)
          schema:
            type: string
            enum:
              - 1h
              - 1d
              - 1mo
            default: 1h
        - name: outcome_platforms
          in: query
          description: >-
            The platforms in which you want to pull the data represented as the
            `device_type` integer.
          schema:
            type: string
            default: 0,1,2,5,8,11,14,17
        - name: outcome_attribution
          in: query
          description: Attribution type for the outcomes.
          schema:
            type: string
            enum:
              - direct
              - influenced
              - unattributed
              - total
            default: total
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Returns all message properties set. See the [Push
                  notifications](/reference/push-notification),
                  [Email](/reference/email), and/or [SMS](/reference/sms)
                  Message Create APIs for all properties. Most commonly used
                  properties for this endpoint are listed.
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
                      messages. Not shown to recipients. Maximum 128 characters.
                  contents:
                    description: >-
                      The main message body with [language-specific
                      values](/docs/multi-language-messaging#supported-languages).
                    type: object
                    properties:
                      en:
                        type: string
                        description: >-
                          The required message language type. See [Supported
                          Languages](/docs/multi-language-messaging#supported-languages).
                  converted:
                    type: integer
                    description: The number of times the push was clicked.
                  data:
                    type: object
                    description: The JSON data set in the push notification if applicable.
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
                      The number of messages that have not been sent yet. If
                      `null`, then the system is still processing the audience,
                      try again later.
                  errored:
                    type: integer
                    description: The number of times the message errored.
                  excluded_segments:
                    type: array
                    description: The segments excluded from the message if applicable.
                  failed:
                    type: integer
                    description: >-
                      The number of subscriptions reported unsubscribed for the
                      message.
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
                      Unix timestamp of when the message delivery was scheduled
                      to begin.
                  completed_at:
                    type: integer
                    description: >-
                      Unix timestamp of when the message delivery was completed.
                      The delivery duration from start to finish can be
                      calculated with `completed_at - send_after`. 
                  successful:
                    type: integer
                    description: >-
                      The number of messages successfully delivered to the push,
                      email, or SMS servers.
                  received:
                    type: integer
                    description: >-
                      The number of messages that confirmed being received aka
                      [Confirmed Deliveries](/docs/confirmed-delivery).
                  filters:
                    type: object
                    description: The filters set for the message if applicable.
                  template_id:
                    type: string
                    description: >-
                      The template ID in UUID v4 format set for the message if
                      applicable. See [Templates](/docs/templates).
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
                    description: The URL of the push notification for mobile subscriptions.
                  platform_delivery_stats:
                    type: object
                    description: >-
                      The successful, errored, failed, converted, received and
                      frequency cap counts for each platform applicable.
                  throttle_rate_per_minute:
                    type: number
                    description: The throttle rate of the push notification if applicable.
                  fcap_status:
                    type: string
                    description: >-
                      The frequency cap status of the push notification if
                      applicable.
                  outcomes:
                    type: object
                    description: >-
                      The id, value, and aggregation type of the outcome set in
                      the request.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
