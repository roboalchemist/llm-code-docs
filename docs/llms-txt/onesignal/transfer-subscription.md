# Source: https://documentation.onesignal.com/reference/transfer-subscription.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Subscription

> Transfer a Subscription to a different user within the same OneSignal app. Useful for associating existing Subscriptions like push, email, or SMS with a new or updated user identity.

## Overview

Use this API to transfer a Subscription from one user to another within the same OneSignal app.

It is highly recommended to use our web and mobile SDKs to set and update the External ID with the `login` method instead of this API. Your app or website may continue to be setting the wrong External ID. Make sure to only use this API if you are setting the same External ID within your app or website.

This is typically used when:

* You want to reassign an existing push, email, or SMS Subscription to a new or updated user.
* You have changed how you're identifying users (e.g., migrating from anonymous to known users).

<Note>
  - Subscriptions **cannot be transferred across different OneSignal apps**.
  - For email and SMS Subscriptions, you can instead create new ones using [Create User](/reference/create-user).
  - For push Subscriptions, platform limitations may apply—see [Subscriptions](/docs/en/subscriptions#importing-push-subscriptions) for details.
</Note>

***

## How to Use This API

### Required Path Parameter: `subscription_id`

You must know the `subscription_id` of the subscription to be transferred. This is a unique UUID assigned by OneSignal.

### Required Body Parameter: `identity` (object)

This specifies the user the subscription should be moved to. Only **one alias** should be used per request. You can identify the target user using one of:

* `external_id` (recommended)
* `onesignal_id`
* A [custom alias](/docs/en/aliases)

***

## OpenAPI

````yaml PATCH /apps/{app_id}/subscriptions/{subscription_id}/owner
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/subscriptions/{subscription_id}/owner:
    patch:
      summary: Transfer subscription
      description: >-
        Transfer a Subscription to a different user within the same OneSignal
        app. Useful for associating existing Subscriptions like push, email, or
        SMS with a new or updated user identity.
      operationId: transfer-subscription
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: subscription_id
          in: path
          description: >-
            The unique Subscription ID in UUID v4 format to transfer to the new
            user.
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                identity:
                  type: object
                  description: >-
                    Identifies the user that this subscription is moved to. Must
                    contain exactly one alias.
                  properties:
                    external_id:
                      type: string
                      description: >-
                        The main user ID to identify the user. See
                        [Users](/docs/users).
                      default: test_external_id
                    onesignal_id:
                      type: string
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    identity:
                      external_id: the-external-id-transferred-to
                      onesignal_id: the-onesignal-id-transferred-to
              schema:
                type: object
                properties:
                  identity:
                    type: object
                    properties:
                      external_id:
                        type: string
                        example: the-external-id-transferred-to
                      onesignal_id:
                        type: string
                        example: the-onesignal-id-transferred-to
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

````

Built with [Mintlify](https://mintlify.com).
