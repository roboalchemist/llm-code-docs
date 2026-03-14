# Source: https://documentation.onesignal.com/reference/view-outcomes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View outcomes

> View and export push notification outcome metrics such as clicks, conversions, and custom events.

View the details of all the outcomes associated with your app.

## Overview

Use this API to retrieve Outcome metrics associated with your OneSignal app, including push notification interactions and custom-defined events. Outcomes include data points like:

* **Clicks**: Number of users who clicked on a push.
* **Confirmed Deliveries**: Number of confirmed message deliveries.
* **Session Durations**: Number of sessions initiated.
* **Custom Events**: Actions like purchases, form submissions, or any event your app tracks via custom Outcome names.

For details on configuring custom Outcomes, refer to the [Outcomes documentation](/docs/en/custom-outcomes).

<Info>
  Outcomes are stored for approximately 30 days. To retain this data, you should regularly export it before it expires.
</Info>

***

## How to use this API

This API allows you to filter and aggregate Outcome data using several query parameters.

### `outcome_names`

Specify one or more Outcome names with an aggregation type suffix (`.count` or `.sum`).

**Default Outcome names:**

* `os__click.count` – Push notification clicks.
* `os__confirmed_delivery.count` – Confirmed deliveries.
* `os__session_duration.count` – Total sessions.

**Custom Outcome names:**

* You can track any custom event name (e.g. `Purchase`, `Signup`).
* If the custom name contains a comma, include only one name per request to avoid parsing issues.
* Example: `outcome_names=os__click.count,Purchase.count`

### `outcome_time_range`

The time range values can be one of the following:

* `1h` = (default) the last 1 hour data.
* `1d` = the last 1 day data.
* `1mo` = the last 1 month data.

### `outcome_platforms`

Maps to the subscription type property. Default is data from all platforms enabled for your OneSignal App.

| `device_type` | `type`      |
| ------------- | ----------- |
| 0             | iOSPush     |
| 1             | AndroidPush |
| 2             | FireOSPush  |
| 5             | ChromePush  |
| 8             | FirefoxPush |
| 11            | Email       |
| 14            | SMS         |
| 17            | SafariPush  |

Example: `outcome_platform=0` for iOS `outcome_platform=17,8` for Safari and Firefox.

### `outcome_attribution`

The way in which the Outcome occurred:

* `direct` = the Outcome occurred when the user interacted with the message. Some Outcomes only have `direct` attribution like `os__click` and `os__confirmed_delivery` because they only occur as the direct result of the message.
* `influenced` = the Outcome occurred within the Time Window of the message being sent, but the user never interacted with the message. See [Outcomes](/docs/en/custom-outcomes) for details.
* `unattributed` = the Outcome occurred without a direct or influenced attribute.
* `total` = (default) the sum of direct+influenced+unattributed.

***

## OpenAPI

````yaml GET /apps/{app_id}/outcomes?outcome_names={outcome_names}&outcome_time_range={outcome_time_range}&outcome_platforms={outcome_platforms}&outcome_attribution={outcome_attribution}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/outcomes?outcome_names={outcome_names}&outcome_time_range={outcome_time_range}&outcome_platforms={outcome_platforms}&outcome_attribution={outcome_attribution}:
    get:
      summary: View outcomes
      description: >-
        View and export push notification outcome metrics such as clicks,
        conversions, and custom events.
      operationId: view-outcomes
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
                properties:
                  outcomes:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          example: os__session_duration
                        value:
                          type: integer
                          example: 100
                          default: 0
                        aggregation:
                          type: string
                          example: sum
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - Add .sum or .count to every requested outcome id
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: Add .sum or .count to every requested outcome id
        '403':
          description: '403'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - >-
                        Access denied.  Please include an 'Authorization: ...'
                        header with a valid API key (/docs/accounts-and-keys).
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: >-
                        Access denied.  Please include an 'Authorization: ...'
                        header with a valid API key (/docs/accounts-and-keys).
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
