# Source: https://documentation.onesignal.com/reference/csv-export.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Export subscriptions CSV

> Generate a GZip-compressed CSV export of your current subscription data using this API endpoint.

## Overview

Use this endpoint to request a GZip-compressed CSV export of all your [Subscriptions data](/docs/en/subscriptions) from OneSignal. The export includes both default and optional user data fields, and supports filters to refine the dataset. The file is downloadable via a URL returned in the API response.

***

## How to use this API

By default, this will export all Subscriptions within the app.

**Optional filters:**

You can narrow the export using:

* `segment_name`: Only export Subscriptions from a specific segment.
* `last_active_since`: Export Subscriptions where their `last_session` was after a specific Unix timestamp. Example: Use `1704067200` for Subscriptions active since January 1st, 2024.
* `include_unsubscribed`: When exporting a segment, set to `true` to include unsubscribed subscriptions alongside subscribed ones. By default, segment-filtered exports only return subscribed subscriptions. This parameter has no effect when `segment_name` is not provided.

**Example successful response:**

```json 200 OK theme={null}
{
  "csv_file_url": "https://onesignal.com/csv_exports/b2f7f966.../users_1849..._2024-11-10.csv.gz"
}
```

**Export time considerations:**

* Generation speed: \~2,000 records per second.
* File readiness: The `csv_file_url` may return a 404 until generation completes.
* Download retry: Poll the file URL at intervals until the file is ready.
* File expiration: The file remains available for 3 days after generation.
* Concurrency: Only one export per OneSignal account can run at a time.

**File not ready (404 response)**

```xml 404 CSV GET  theme={null}
This XML file does not appear to have any style information
associated with it. The document tree is shown below.
<Error>
  <Code>NoSuchKey</Code>
  <Message>The specified key does not exist.</Message>
</Error>
```

<Info>
  You can safely poll the `csv_file_url` until the file becomes available. Implement retry logic based on expected data volume and generation speed.

  Only one export is allowed at a time per account. Wait until the `.csv.gz` file is downloaded before triggering another export.
</Info>

***

## CSV data contents

The export includes two types of fields:

* **Default fields**: Always included unless excluded by schema changes.
* **Extra fields**: Must be explicitly requested using the `extra_fields` parameter.

### Default fields

* `id`: The Subscription ID.
* `identifier`: The push token, email address, or phone number depending on the Subscription type.
* `session_count`: The number of times the user has opened the app.
* `language`: The user's language in ISO 639-1 format.
* `timezone`: Deprecated — use `timezone_id` instead.
* `game_version`: The version of your app that the user is currently using.
* `device_os`: The device's operating system version.
* `device_type`: Integer representing channel/device type.
  * `0`: iOSPush
  * `1`: AndroidPush
  * `2`: FireOSPush
  * `5`: ChromePush
  * `7,17`: SafariPush
  * `11`: Email
  * `14`: SMS
* `device_model`: The device's hardware string.
* `ad_id`: Deprecated.
* `tags`: Custom key/value data.
* `last_active`: The last time the user was active.
* `playtime`: The total amount of time in seconds the user had the mobile app open.
* `amount_spent`: The total amount the user spent on consumable in-app purchases.
* `created_at`: The first time the user was seen.
* `invalid_identifier`: Boolean flag for unsubscribed state.
  * `t`: Unsubscribed
  * `f`: Subscribed

### Extra fields (`extra_fields`)

Pass `extra_fields` in your request to include any of the following:

* `external_user_id`: Maps to the `external_id` of the user.
* `onesignal_id`: OneSignal's user ID.
* `location`: Adds the `lat` and `long` coordinates if set.
* `country`: The user's country in ISO 3166-1 Alpha 2 format.
* `rooted`: Only available to OneSignal SDKs. Indicates if the Android device is rooted or jail-broken.
* `ip`: The IP address if detected. Can be IPv4 or IPv6 format.
* `web_auth`: Only available to OneSignal SDKs. The `web_auth` key for web push.
* `web_p256`: Only available to OneSignal SDKs. The `web_p256` for web push.
* `unsubscribed_at`: The date and time the user last unsubscribed. They may resubscribe at any time. Check the `invalid_identifier` field to determine if they are currently subscribed.
* `notification_types`: Indicates the reason for the subscription status. Values are updated automatically as events are detected by our frontend SDKs but you should set this manually when updating via our REST API. `1` is subscribed and `-31` is reserved for unsubscribed via the API. See [Subscriptions](/docs/en/subscriptions#notification-types).
* `timezone_id`: The user's timezone in IANA format.

***

## OpenAPI

````yaml POST /players/csv_export
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /players/csv_export:
    post:
      summary: Export subscriptions CSV
      description: >-
        Generate a GZip-compressed CSV export of your current subscription data
        using this API endpoint.
      operationId: csv-export
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                extra_fields:
                  type: array
                  description: Additional properties that you can include in the CSV.
                  default:
                    - external_user_id
                    - country
                    - timezone_id
                  items:
                    type: string
                    enum:
                      - external_user_id
                      - onesignal_id
                      - location
                      - country
                      - rooted
                      - ip
                      - web_auth
                      - web_p256
                      - unsubscribed_at
                      - notification_types
                      - timezone_id
                last_active_since:
                  type: string
                  description: >-
                    A Unix timestamp (in seconds) used to filter Subscriptions
                    based on recent activity. Only Subscriptions with a
                    `last_session` timestamp after this value will be included
                    in the export. Example: To export Subscriptions active since
                    January 1st, 2024, use `1704067200`.
                segment_name:
                  type: string
                  description: >-
                    The name of a specific segment to filter the export. Only
                    subscriptions that belong to this segment will be included
                    in the CSV. Omit this field to export all subscriptions in
                    the app.
                include_unsubscribed:
                  type: boolean
                  description: >-
                    When used with `segment_name`, set to `true` to include
                    unsubscribed subscriptions in the export. By default,
                    segment-filtered exports only return subscribed
                    subscriptions. This parameter has no effect when
                    `segment_name` is not provided.
                  default: false
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  csv_file_url:
                    type: string
                    description: >-
                      The URL to download the CSV file. The file is available
                      for 3 days after generation.
        '400':
          description: '400'
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: >-
                        Request is malformed: Failed to parse app_id from
                        request
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
