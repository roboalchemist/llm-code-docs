# Source: https://documentation.onesignal.com/reference/cancel-message.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel message

> Stop a scheduled or currently outgoing message.

## Overview

The Cancel message API can be used to stop scheduled messages from being sent. It does not delete or remove the message from the app. If a message is in the process of sending, then canceling it may not fully prevent all targeted users from receiving it.

***

## How to use this API

This API is most commonly used when sending [Transactional messages](/docs/en/transactional-messages) to individual users, scheduling the message in the future with `send_after`. The response of our Create message API has an `id` which corresponds to the `message_id` used in this request. You can store this `message_id` on your server and use this API to cancel sending the message to the user if not needed anymore.

If you need a way to remove a notification already sent to a user, see [Remove notifications & TTL](/docs/en/push).

***

## OpenAPI

````yaml DELETE /notifications/{message_id}?app_id={app_id}
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
    delete:
      summary: Cancel message
      description: Stop a scheduled or currently outgoing message.
      operationId: cancel-message
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
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Indicates if the message was successfully canceled.
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
                      description: >-
                        Reason for the message not being canceled. Usually due
                        to the message already being sent to all recipients.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
