# Source: https://documentation.onesignal.com/reference/message-history.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Message history

> View which subscriptions received a particular message

## Overview

This API enables you to retrieve all [Subscriptions](/docs/en/subscriptions) that received a specific push notification or email. You can access the notification's history for up to seven days after it was sent. Please note that notifications sent to fewer than 1,000 recipients will not record a "received" event, but they will still record "sent" events.

***

## How to Use this API

1. Submit a request to generate a report.

2. Decide delivery method

   * After receiving a successful response, **poll the destination URL** until the file becomes available. Exports typically complete within 1-3 minutes; we recommend a 10-second polling interval.
   * Alternatively, you can opt to receive an email to the address specified in the optional `email` parameter when the report is ready.

### Requirements

* A [OneSignal Professional or Enterprise Plan](https://onesignal.com/pricing).
* Enabled the "Send History via OneSignal API" option in Settings -> Integrations; notifications sent before this setting is enabled can't be retrieved.
* Requests must be made within seven days of sending the notification.

### Polling

Use the `csv_file_url` property in the response to test if the report is complete. If you receive a '403' error response, retry fetching the file after a short period; it only means we're still generating the report.

### Sample Report

The generated report is a simple CSV file that can be imported into any system for further processing.

```csv report.csv theme={null}
player_id,onesignal_id,external_id,target_channel,timestamp
"2c4fac95-7dfb-4113-9347-aba3a92ff557","ccddf35a-1233-4423-8a57-ac8c4b38eb81","a07aec27-2586-4b92-a24f-62660a1517fa","push","1628189160"
"68f5cf73-b20a-4de9-b6ee-79a863b8e7d8","d2f9f2f8-94af-4942-8183-115cef1213d5","4b66359f-3d94-4a73-806d-8ef5f0430b3d","push","1628187816"

```

### Limitations

* Querying for `opens` events are not supported.
* The `timestamp` column is included only for `clicked` events.

***

## OpenAPI

````yaml POST /notifications/{message_id}/history
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /notifications/{message_id}/history:
    post:
      summary: Message history
      description: View which subscriptions received a particular message
      operationId: message-history
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
              required:
                - app_id
                - events
              properties:
                app_id:
                  type: string
                  description: >-
                    Your OneSignal App ID in UUID v4 format. See [Keys &
                    IDs](/docs/keys-and-ids).
                  default: YOUR_APP_ID
                events:
                  type: string
                  description: >-
                    Specifies the type of event to retrieve. `sent` — retrieves
                    all subscriptions sent the specified message. Note: sent
                    events are not recorded for messages targeting fewer than
                    1,000 recipients. `clicked` — retrieves all subscriptions
                    that interacted with the message. Note: There isn't a
                    recipient count threshold for tracking clicked event.
                  default: sent
                email:
                  type: string
                  description: The email address in which to deliver the report.
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: true
                    destination_url: https://onesignal-aws-link.csv
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                    default: true
                  destination_url:
                    type: string
                    example: https://onesignal-aws-link.csv
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - param `email` must be a valid email
                    success: false
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: param `email` must be a valid email
                  success:
                    type: boolean
                    example: false
                    default: true
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
