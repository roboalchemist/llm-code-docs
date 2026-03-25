# Source: https://documentation.onesignal.com/reference/unsubscribe-with-token.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unsubscribe email with token

> Unsubscribe an email address from future messages by calling this API from your custom unsubscribe page. Automatically disables the associated email subscription using a token-based approach.

## Overview

Use this API to unsubscribe an email address directly from your custom unsubscribe landing page. It is ideal when building branded opt-out experiences and enables you to track which email caused the unsubscribe.

When invoked, this endpoint:

* Sets the email Subscription's `enabled` property to `false`
* Prevents further messages from being sent to the email address unless explicitly overridden (see [Overriding unsubscribes](/reference/email#body-include-unsubscribed))
* Email Subscriptions can be re-subscribed using the [Update Subscription](/reference/update-subscription) API

<Tip>
  For instructions on setting up a custom unsubscribe page, see [Create a Custom Unsubscribe Page](/docs/en/create-custom-unsubscribe-page).
</Tip>

***

## How to Use This API

### Step 1: Set Up Your Custom Unsubscribe Page

Follow the guide to [Create a Custom Unsubscribe Page](/docs/en/create-custom-unsubscribe-page). You'll add a custom unsubscribe URL to your email templates using Liquid syntax.

Example URL in your email template:

```liquid  theme={null}
https://yourdomain.com/unsubscribe?app_id={{ app_id }}&notification_id={{ notification_id }}&token={{ token }}
```

### Step 2: Extract the Parameters

When a user clicks the unsubscribe link, your custom unsubscribe page should extract the following from the URL:

* `app_id`: OneSignal app ID
* `notification_id`: The ID of the specific email message sent
* `token`: The email token, a secure reference to the subscription

### Step 3: Call the API

When the user confirms they want to unsubscribe (e.g., clicks a button on your unsubscribe page), make a POST request to this endpoint:

```
POST /apps/{app_id}/notifications/{notification_id}/unsubscribe?token={token}
```

Example Request (JavaScript):

```js  theme={null}
fetch("https://api.onesignal.com/apps/your-app-id/notifications/your-notification-id/unsubscribe?token=abc123xyz", {
  method: "POST"
});
```

<Info>
  No request body or authentication is required. The token acts as a secure identifier.
</Info>

<Note>
  * This API only works for email subscriptions.
  * It should only be used from a server or frontend context that you control (e.g., your custom unsubscribe page).
  * Once unsubscribed, the email address will not receive future emails from your app unless resubscribed.
</Note>

***

## OpenAPI

````yaml POST /apps/{app_id}/notifications/{notification_id}/unsubscribe?token={token}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/notifications/{notification_id}/unsubscribe?token={token}:
    post:
      summary: Unsubscribe email (with token)
      description: >-
        Unsubscribe an email address from future messages by calling this API
        from your custom unsubscribe page. Automatically disables the associated
        email subscription using a token-based approach.
      operationId: unsubscribe-with-token
      parameters:
        - name: token
          in: query
          description: >-
            The unsubscribe token that is generated via liquid syntax
            `{{subscription.unsubscribe_token}}` when personalizing an email.
            See [Create a Custom Unsubscribe
            Page](/docs/create-custom-unsubscribe-page) for setup details.
          schema:
            type: string
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: notification_id
          in: path
          description: >-
            The "id" of the email message. Can be passed into the request from
            the email received by the user with liquid syntax `{{message.id}}`.
            See [Create a Custom Unsubscribe
            Page](/docs/create-custom-unsubscribe-page) for setup details.
          schema:
            type: string
          required: true
      responses:
        '202':
          description: '202'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: 'true'
              schema:
                type: object
                properties:
                  success:
                    type: string
                    example: 'true'
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
                      example: Details about the error.
        '403':
          description: '403'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - Forbidden
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: Forbidden
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: subscription-0
                        title: Subscription not found
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        code:
                          type: string
                          example: subscription-0
                        title:
                          type: string
                          example: Subscription not found
        '429':
          description: '429'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: Rate Limit Exceeded
                        title: Example error title
                        meta: {}
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        code:
                          type: string
                          example: Rate Limit Exceeded
                        title:
                          type: string
                          example: Example error title
                        meta:
                          type: object
                          properties: {}
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
