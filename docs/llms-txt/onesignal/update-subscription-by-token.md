# Source: https://documentation.onesignal.com/reference/update-subscription-by-token.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Subscription by token

> Update properties on an existing Subscription using its token. Commonly used to enable or disable subscription status when managing outside of the OneSignal SDK.

## Overview

Use this API to update an existing Subscription's properties.

This API can be useful if:

* You only know the `token` and `token_type` and want to update metadata or status flags directly.
* You are managing Subscription status outside of the OneSignal SDK. Like with a [custom preference page or unsubscribe page](/docs/en/create-custom-unsubscribe-page).

***

## How to use this API

To update a Subscription, you must know the `token_type` and the `token`.

The `token_type` is the [Subscription's type](/docs/en/server-sdk-reference#subscription-types) (e.g., `Email`, `SMS`, `iOSPush`, `AndroidPush`, etc.).

The `token` is the push token, email address, or phone number associated with the Subscription.

Ensure the `token` is valid and correctly formatted for the chosen `token_type`.

* **Email format:** Should be a valid email address that you confirmed can receive emails.
* **SMS format:** Phone number must be in [E.164 format](https://en.wikipedia.org/wiki/E.164).
* **iOSPush APNS token format:** 64 characters, hexadecimal characters only (0-9,a-f).
* **AndroidPush FCM token format:** Typically 163 characters, alphanumeric characters, may contain hyphens, colons and underscore.

<Warning>
  You **cannot** update the `token_type` and `token` of a Subscription with this API. If the `token_type` is incorrect:

  1. Use [Delete Subscription](/reference/delete-subscription) to remove the incorrect entry.
  2. Use [Create Subscription by alias](/reference/create-subscription) to recreate the subscription with the correct type.

  If multiple Subscriptions are found for the `token` and `token_type`, an `Http 400` error is returned with a list of subscription IDs that match the criteria.
</Warning>

***

## OpenAPI

````yaml PATCH /apps/{app_id}/subscriptions_by_token/{token_type}/{token}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/subscriptions_by_token/{token_type}/{token}:
    patch:
      summary: Update subscription By Token
      description: >-
        Update properties on an existing Subscription using its token. Commonly
        used to enable or disable subscription status when managing outside of
        the OneSignal SDK.
      operationId: update-subscription-by-token
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: token_type
          in: path
          description: The subscription channel type. Must match the format of the token.
          schema:
            type: string
            enum:
              - Email
              - SMS
              - iOSPush
              - AndroidPush
              - HuaweiPush
              - FireOSPush
              - WindowsPush
              - macOSPush
              - ChromeExtensionPush
              - ChromePush
              - FirefoxPush
              - SafariPush
          required: true
        - name: token
          in: path
          description: >-
            The push token, email address, or phone number associated with the
            subscription. Ensure the `token` is valid and correctly formatted
            for the chosen subscription `type`. Email format: Should be a valid
            email address that you confirmed can receive emails. SMS format:
            Phone number must be in [E.164
            format](https://en.wikipedia.org/wiki/E.164). iOSPush APNS token
            format: 64 characters, hexadecimal characters only (0-9,a-f).
            AndroidPush FCM token format: Typically 163 characters, alphanumeric
            characters, may contain hyphens, colons and underscore.
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
              properties:
                subscription:
                  type: object
                  description: The subscription's properties.
                  required:
                    - type
                    - token
                  properties:
                    enabled:
                      type: boolean
                      description: >-
                        Indicates if the Subscription should be subscribed to
                        the message channel. Defaults to `true` if omitted. Set
                        to `false` to mark as unsubscribed.
                    notification_types:
                      type: integer
                      description: >-
                        Indicates the reason for the subscription status. Values
                        are updated automatically as events are detected by our
                        frontend SDKs but you should set this manually when
                        updating via our REST API. `1` is subscribed and `-31`
                        is reserved for unsubscribed via the API. See
                        [Subscriptions](/docs/subscriptions#notification-types).
                      format: int32
                    session_time:
                      type: integer
                      description: >-
                        The total amount of time the user has had the app open
                        in seconds.
                      format: int32
                    session_count:
                      type: integer
                      description: The total amount of times the user has opened the app.
                      format: int32
                    app_version:
                      type: string
                      description: >-
                        The version of your mobile app as detected by our
                        frontend SDKs or a value you set via our API. Our SDK
                        sets this based: Android - Android Studio `versionCode`
                        in your App `build.gradle`. iOS: Xcode App Version.
                    device_model:
                      type: string
                      description: The model of the user's device (e.g., iPhone 16).
                    device_os:
                      type: string
                      description: The device or browser's system version.
                    test_type:
                      type: integer
                      description: >-
                        Specifies the [APS environment
                        entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)
                        used for generating the iOS push token. Omit, set to
                        `null` or `0` if the token was generated in a Production
                        environment (App Store & Test Flight builds). Set to `1`
                        for Development environment, `2` if it was generated in
                        an Ad-Hoc environment. This ensures OneSignal routes
                        notifications correctly based on the token’s source
                        environment.
                      format: int32
                    sdk:
                      type: string
                      description: >-
                        Set by our frontend SDK. Do not use this field.
                        Indicates the OneSignal SDK version.
                    rooted:
                      type: boolean
                      description: Indicates if the Android device is jail-broken.
                    web_auth:
                      type: string
                      description: >-
                        The web auth token set by our web SDK. Do not use this
                        field. See [Migrating to OneSignal from another
                        service](/docs/migrating-to-onesignal).
                    web_p256:
                      type: string
                      description: >-
                        The web 256 key set by our web SDK. Do not use this
                        field. See [Migrating to OneSignal from another
                        service](/docs/migrating-to-onesignal).
      responses:
        '202':
          description: '202'
          content:
            application/json:
              schema:
                type: object
                description: >-
                  The Subscription update request has been accepted
                  successfully. This process is asynchronous and may take a few
                  seconds to complete.
        '400':
          description: '400'
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Bad request or multiple Subscriptions are found for the token
                  and token_type provided. Check the errors for details.
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        code:
                          type: string
                          description: The error code.
                        title:
                          type: string
                          description: The error details.
        '401':
          description: '401'
          content:
            application/json:
              schema:
                type: object
                description: Missing Authorization header.
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        code:
                          type: string
                          description: auth-1
                        title:
                          type: string
                          description: >-
                            This operation requires 'Authorization' in the HTTP
                            header
        '404':
          description: '404'
          content:
            application/json:
              schema:
                type: object
                description: >-
                  No subscription record found for the token and token type
                  provided.
                properties:
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        code:
                          type: string
                          description: The error code.
                        title:
                          type: string
                          description: The error details.

````

Built with [Mintlify](https://mintlify.com).
