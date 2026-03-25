# Source: https://documentation.onesignal.com/reference/export-csv-of-events.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Export audience activity CSV

> Export a compressed CSV report of audience-level delivery and engagement data for a specific message. This includes sent, delivered, clicked, failed, and unsubscribed events across Push, Email, and SMS channels.

## Overview

This API mirrors the **Audience Activity** CSV export functionality available in the OneSignal dashboard. It lets you download a full list of event records (e.g., sends, clicks, failures) for push, email, and SMS messages:

* [Push Notification Message Reports](/docs/en/push-notification-message-reports)
* [Email Message Reports](/docs/en/email-message-reports)
* [SMS Message Reports](/docs/en/sms-message-reports)

The output varies depending on the channel used by the message.

***

## How to use this API

You will need the `id` of the message you want to export. You can retrieve this via the [Create Message](/reference/create-message) or [View Messages](/reference/view-messages) APIs.

After you make this request, you will likely get a `200 OK` response with a `csv_file_url`.

**Example successful response:**

```json 200 OK theme={null}
{
    "csv_file_url": "https://onesignal-data.onesignal.com/csv_exports/YOUR_APP_ID/events_audience-activity-YOUR_MESSAGE_ID-push-2024-10-21T06-49-23PMUTC.csv.gz"
}
```

Depending on how large the file is, the URL may `404` with the following error:

```xml 404 CSV GET  theme={null}
This XML file does not appear to have any style information
associated with it. The document tree is shown below.
<Error>
  <Code>NoSuchKey</Code>
  <Message>The specified key does not exist.</Message>
</Error>
```

The export file is generated at \~2,000 records per second. For large audiences, the file can take several minutes. Implement retries with exponential backoff or a similar strategy.

<Info>
  * The CSV download URL is valid for **3 days** after creation.
  * File names contain a random UUID to prevent guessing.
  * **Only one concurrent export** is allowed per OneSignal account. Always download the `.csv.gz` file before starting a new export.
</Info>

To check file availability, send a GET request to the `csv_file_url`. If the file is ready, it will download. If not, retry after some delay.

***

## CSV data contents

The exported CSV includes the following fields:

* `external_user_id` — Maps to the External ID. See [Users](/docs/en/users).
* `subscription_id` — Maps to the Subscription ID. See [Subscriptions](/docs/en/subscriptions).
* `device_type` — The platform/channel the Subscription is for.
* `sent` — Timestamp of when the message was sent.
* `delivered` — Timestamp of confirmed delivery. See [Confirmed Delivery](/docs/en/confirmed-delivery).
* `clicked` — Timestamp of click event (if any).
* `onesignal_id` — Maps to the internal OneSignal User ID.
* `failed` — Timestamp of delivery failure.
* `unsubscribed` — Timestamp of unsubscription event.
* `failure_message` — Description of the failure, if any. See [Push message reports](/docs/en/push-notification-message-reports#what-are-failed-notifications).

***

## OpenAPI

````yaml POST /notifications/{message_id}/export_events
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /notifications/{message_id}/export_events:
    post:
      summary: Export audience activity CSV
      description: >-
        Export a compressed CSV report of audience-level delivery and engagement
        data for a specific message. This includes sent, delivered, clicked,
        failed, and unsubscribed events across Push, Email, and SMS channels.
      operationId: export-csv-of-events
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
            default: YOUR_NOTIFICATION_ID
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
                      description: The reason for the error.
        '404':
          description: '404'
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      description: The reason for the error.
                  success:
                    type: boolean
                    description: Indicates if the request was successful.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
