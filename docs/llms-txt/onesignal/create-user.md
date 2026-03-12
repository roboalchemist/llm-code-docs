# Source: https://documentation.onesignal.com/reference/create-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create user

> Create a new user or modify the subscriptions associated with an existing User.

<Warning>
  If you are still using pre-User Model APIs or SDKs (Mobile SDKs version 4 or
  lower, Web SDKs version 15 or lower), we recommend thorough testing of this
  endpoint before switching to the new User Model. Discrepancies may occur where
  the External ID set through the SDK and the External ID set through the API do
  not generate matching OneSignal IDs. To ensure a smooth transition, consider
  the following options:

* **Update to the User Model SDKs:** Upgrade to the latest User Model SDKs (Mobile SDK 5+, Web SDK 16+). For more details, refer to the [User Model Migration Guide](/docs/en/user-model-migration-guide).
* **Continue Using Pre-User Model APIs:** If you are not ready to migrate, continue using the existing APIs for [Adding a Device](/reference/add-a-device), [Editing Tags with External User ID](/reference/edit-tags-with-external-user-id), and [Editing a Device](/reference/edit-device) until the SDK migration is complete.
</Warning>

## Overview

This endpoint enables you to create and manage users outside of frontendSDK-based sessions. It's primarily used to:

* Import users from other systems.
* Programmatically define users by assigning identifiers (aliases), properties (e.g., tags), and messaging subscriptions (e.g., email, mobile, SMS).

If you're using the frontend SDKs, user creation is typically handled automatically via methods like `login`, `addEmail`, and `addSms`. See [Users](/docs/en/users) and [Subscriptions](/docs/en/subscriptions) for conceptual guidance.

***

## How to use this API

To successfully create a user via the API:

* You must provide at least one unique identifier via the `identity` and Subscription via the `subscriptions` fields.
* You can optionally include user profile data (`properties`) and one or more messaging `subscriptions`.

## Key Concepts

### Aliases

Aliases uniquely identify a user and should include an `external_id` (the recommended identifier). Up to 20 custom aliases are supported. They allow you to reference users across platforms or external systems.

### Properties

User properties store information such as tags, location, activity, and device data. These attributes help you personalize campaigns and optimize engagement strategies.

### Subscriptions

A user can have up to **20 subscriptions** (across email, SMS, push, etc.). Subscriptions connect users to channels for message delivery and are transferable across users. See [Subscriptions](/docs/en/subscriptions) for more.

***

## OpenAPI

````yaml POST /apps/{app_id}/users
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/users:
    post:
      summary: Create user
      description: >-
        Create a new user or modify the subscriptions associated with an
        existing User.
      operationId: create-user
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                properties:
                  type: object
                  description: >-
                    Represents user profile data for a given user, including
                    tags, preferences, user activity, and other valuable
                    properties.
                  properties:
                    tags:
                      type: object
                      description: >-
                        Custom user events or properties made of key-value pairs
                        of string values. See [Data
                        Tags](/docs/add-user-data-tags). Does not support arrays
                        or other nested objects. Example:
                        `{'foo':'bar','this':'that'}`
                      format: json
                    language:
                      type: string
                      description: >-
                        Language Abbreviation in ISO 639-1 format. See
                        [supported
                        languages](/docs/multi-language-messaging#supported-languages).
                        Must be lower-case.
                      default: en
                    timezone_id:
                      type: string
                      description: >-
                        Timezone ID based on the [tz database "TZ
                        identifier"](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).
                      default: America/Los_Angeles
                    lat:
                      type: number
                      description: >-
                        User's current latitude. Acceptable values range between
                        `-90` to `90`.
                      format: float
                    long:
                      type: number
                      description: >-
                        User's current longitude. Acceptable values range
                        between `-180` to `180`.
                      format: float
                    country:
                      type: string
                      description: >-
                        Country code in [ISO 3166-1 Alpha 2
                        format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).
                        Must be upper-case.
                      default: US
                    first_active:
                      type: integer
                      description: >-
                        Unix timestamp in seconds representing when the user was
                        created.
                      format: int32
                    last_active:
                      type: integer
                      description: >-
                        Unix timestamp in seconds representing the most recent
                        time the user was active in your app.
                      format: int32
                    ip:
                      type: string
                      description: IPv4 or IPv6, response only
                identity:
                  type: object
                  description: >-
                    Defines identifiers for the user. The `external_id` must be
                    used and should be unique across users.
                  properties:
                    external_id:
                      type: string
                      description: >-
                        The main user ID to identify the user. See
                        [Users](/docs/users).
                subscriptions:
                  type: array
                  description: >-
                    The subscriptions object allows for creating or transferring
                    subscriptions to a specified user. See
                    [Subscriptions](/docs/subscriptions).
                  items:
                    properties:
                      type:
                        type: string
                        description: >-
                          The subscription channel type. Must match the format
                          of the token..
                        enum:
                          - Email
                          - SMS
                          - iOSPush
                          - AndroidPush
                          - HuaweiPush
                          - FireOSPush
                          - WindowsPush
                          - macOSPush
                          - ChromePush
                          - FirefoxPush
                          - SafariPush
                      token:
                        type: string
                        description: >-
                          The push token, email address, or phone number
                          associated with the subscription. Ensure the `token`
                          is valid and correctly formatted for the chosen
                          subscription `type`. Email format: Should be a valid
                          email address that you confirmed can receive emails.
                          SMS format: Phone number must be in [E.164
                          format](https://en.wikipedia.org/wiki/E.164). iOSPush
                          APNS token format: 64 characters, hexadecimal
                          characters only (0-9,a-f). AndroidPush FCM token
                          format: Typically 163 characters, alphanumeric
                          characters, may contain hyphens, colons and
                          underscore.
                      enabled:
                        type: boolean
                        description: >-
                          Indicates if the Subscription should be subscribed to
                          the message channel. Defaults to `true` if omitted.
                          Set to `false` to mark as unsubscribed.
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
                          sets this based: Android - Android Studio
                          `versionCode` in your App `build.gradle`. iOS: Xcode
                          App Version.
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
                          `null` or `0` if the token was generated in a
                          Production environment (App Store & Test Flight
                          builds). Set to `1` for Development environment, `2`
                          if it was generated in an Ad-Hoc environment. This
                          ensures OneSignal routes notifications correctly based
                          on the token’s source environment.
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
                    required:
                      - type
                      - token
                    type: object
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                New user created:
                  value:
                    identity:
                      onesignal_id: 567491ee-9105-4a87-9cbc-ed78a571645b
                    properties:
                      tags:
                        first_name: John
                        last_name: Smith
              schema:
                type: object
                properties:
                  identity:
                    type: object
                    properties:
                      onesignal_id:
                        type: string
                        example: 567491ee-9105-4a87-9cbc-ed78a571645b
                  properties:
                    type: object
                    properties:
                      tags:
                        type: object
                        properties:
                          first_name:
                            type: string
                            example: John
                          last_name:
                            type: string
                            example: Smith
        '202':
          description: '202'
          content:
            application/json:
              examples:
                Existing user modified:
                  value:
                    identity:
                      onesignal_id: 567491ee-9105-4a87-9cbc-ed78a571645b
                      external_id: test_external_id-101101
                    subscriptions:
                      - id: f67491ee-9105-4a87-9cbc-ed78a571645b
                        app_id: a67491ee-9105-4a87-9cbc-ed78a571645b
                        token: joe@example.com
                        type: email
                    properties:
                      tags:
                        color: red
              schema:
                type: object
                properties:
                  identity:
                    type: object
                    properties:
                      onesignal_id:
                        type: string
                        example: 567491ee-9105-4a87-9cbc-ed78a571645b
                      external_id:
                        type: string
                        example: test_external_id-101101
                  subscriptions:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The unique Subscription ID in UUID v4 format.
                        app_id:
                          type: string
                          description: Your OneSignal App ID in UUID v4 format.
                        token:
                          type: string
                          description: >-
                            The push token, email address, or phone number
                            associated with the subscription.
                        type:
                          type: string
                          description: The subscription channel type.
                  properties:
                    type: object
                    properties:
                      tags:
                        type: object
                        properties:
                          color:
                            type: string
                            example: red
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: internal error code
                        title: example error title
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
                          example: internal error code
                        title:
                          type: string
                          example: example error title
                        meta:
                          type: object
                          properties: {}
        '409':
          description: '409'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: internal error code
                        title: example error title
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
                          example: internal error code
                        title:
                          type: string
                          example: example error title
                        meta:
                          type: object
                          properties: {}
        '429':
          description: '429'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - API rate limit exceeded
                    limit: App ID
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: API rate limit exceeded
                  limit:
                    type: string
                    example: App ID
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
