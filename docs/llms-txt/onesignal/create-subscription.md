# Source: https://documentation.onesignal.com/reference/create-subscription.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Subscription by alias

> Use this API to attach a new subscription—such as email, SMS, or push notification—to an existing OneSignal user identified by an alias.

## Overview

This API allows you to add a **new Subscription** to an existing [User](/docs/en/users) via an alias identifier. A *Subscription* reflects a user's intent to receive messages through a specific communication channel, such as email, SMS, or push notifications. See [Subscriptions](/docs/en/subscriptions) for additional context.

If you're looking to **create a new user and add Subscriptions simultaneously**, use the [Create User](/reference/create-user) API instead.

***

## How to use this API

To attach a Subscription, the user must already exist and be referenced using an alias. The `alias_label` and `alias_id` path parameters define how the user is identified:

* Common alias: `external_id`
* Other options: `onesignal_id`, or custom aliases

For details, refer to [Users](/docs/en/users) and [Aliases](/docs/en/aliases).

## Required Fields

Each Subscription must include at least:

* `type`: the channel (e.g., `Email`, `SMS`, `iOSPush`)
* `token`: the unique identifier for the channel (e.g., email address, phone number, push token)

If the specified `type` and `token` already exist in the app, the Subscription will be transferred to the user identified in the path parameters.

***

## OpenAPI

````yaml POST /apps/{app_id}/users/by/{alias_label}/{alias_id}/subscriptions
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/users/by/{alias_label}/{alias_id}/subscriptions:
    post:
      summary: Create Subscription by alias
      description: >-
        Use this API to attach a new subscription—such as email, SMS, or push
        notification—to an existing OneSignal user identified by an alias.
      operationId: create-subscription
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: alias_label
          in: path
          description: >-
            The alias name or key to locate the user. Most commonly set as
            `external_id` but can be the `onesignal_id` or a [custom
            alias](/docs/aliases).
          schema:
            type: string
            default: external_id
          required: true
        - name: alias_id
          in: path
          description: The specific identifier for the given alias to identify the user.
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
                - subscription
              properties:
                subscription:
                  type: object
                  description: The subscription's properties.
                  required:
                    - type
                    - token
                  properties:
                    type:
                      type: string
                      description: >-
                        The subscription channel type. Must match the format of
                        the token.
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
                        - SafariLegacyPush
                        - FirefoxPush
                        - SafariPush
                    token:
                      type: string
                      description: >-
                        The push token, email address, or phone number
                        associated with the subscription. Ensure the `token` is
                        valid and correctly formatted for the chosen
                        subscription `type`. Email format: Should be a valid
                        email address that you confirmed can receive emails. SMS
                        format: Phone number must be in [E.164
                        format](https://en.wikipedia.org/wiki/E.164). iOSPush
                        APNS token format: 64 characters, hexadecimal characters
                        only (0-9,a-f). AndroidPush FCM token format: Typically
                        163 characters, alphanumeric characters, may contain
                        hyphens, colons and underscore.
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
        '200':
          description: '200'
          content:
            application/json:
              examples:
                New subscription created:
                  value: {}
              schema:
                type: object
                properties: {}
        '202':
          description: '202'
          content:
            application/json:
              examples:
                Existing subscription transferred:
                  value:
                    subscription:
                      id: 29131af9-ccfc-4398-89bb-9a4663941f14
                      app_id: 1db1662c-7609-4a90-b0ad-15b45407d628
                      type: Email
                      token: new-email@test.com
                      enabled: true
                      notification_types: -99
                      session_time: 0
                      session_count: 1
                      sdk: ''
                      device_model: ''
                      device_os: ''
                      rooted: false
                      test_type: 0
                      app_version: ''
                      net_type: 0
                      carrier: ''
                      web_auth: ''
                      web_p256: ''
              schema:
                type: object
                properties:
                  subscription:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The unique Subscription ID in UUID v4 format.
                      app_id:
                        type: string
                        description: >-
                          Your OneSignal App ID in UUID v4 format. See [Keys &
                          IDs](/docs/keys-and-ids).
                      type:
                        type: string
                        description: The subscription channel type.
                      token:
                        type: string
                        description: >-
                          The push token, email address, or phone number
                          associated with the subscription.
                      enabled:
                        type: boolean
                        description: >-
                          Indicates if the Subscription is subscribed (`true`)
                          or unsubscribed (`false`).
                      notification_types:
                        type: integer
                        description: >-
                          Indicates the reason for the subscription status.
                          Values are updated automatically as events are
                          detected by our frontend SDKs but you should set this
                          manually when updating via our REST API. `1` is
                          subscribed and `-31` is reserved for unsubscribed via
                          the API. See
                          [Subscriptions](/docs/subscriptions#notification-types).
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
                      sdk:
                        type: string
                        description: >-
                          Set by our frontend SDK. Indicates the OneSignal SDK
                          version.
                      device_model:
                        type: string
                        description: The model of the user's device (e.g., iPhone 16).
                      device_os:
                        type: string
                        description: The device or browser's system version.
                      rooted:
                        type: boolean
                        description: Indicates if the Android device is jail-broken.
                      test_type:
                        type: integer
                        description: >-
                          Specifies the [APS environment
                          entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)
                          used for generating the iOS push token. `null` or `0`
                          if the token was generated in a Production environment
                          (App Store & Test Flight builds). `1` for Development
                          environment, `2` if it was generated in an Ad-Hoc
                          environment. This ensures OneSignal routes
                          notifications correctly based on the token’s source
                          environment.
                        format: int32
                      app_version:
                        type: string
                        description: >-
                          The version of your mobile app as detected by our
                          frontend SDKs or a value you set via our API. Our SDK
                          sets this based: Android - Android Studio
                          `versionCode` in your App `build.gradle`. iOS: Xcode
                          App Version.
                      net_type:
                        type: integer
                        example: 0
                        default: 0
                      carrier:
                        type: string
                        example: ''
                      web_auth:
                        type: string
                        description: The web auth token set by our web SDK.
                      web_p256:
                        type: string
                        description: The web 256 key set by our web SDK.
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
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: Details about the error.
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
