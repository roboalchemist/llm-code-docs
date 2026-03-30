# Source: https://documentation.onesignal.com/reference/view-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View user

> Retrieve a user including aliases, properties, and subscriptions.

## Overview

* Use this API to retrieve a user's full profile, including identity aliases, user properties, and messaging subscription details across channels.
* This is helpful for verifying user data, debugging subscription issues, or syncing OneSignal user data with your internal systems.

For detailed concepts and guides, see [Users](/docs/en/users), [Subscriptions](/docs/en/subscriptions), and [Aliases](/docs/en/aliases) documentation.

## How to use this API

To look up a user, you must provide both an `alias_label` and an `alias_id`. In most cases, your `external_id` will serve as the `alias_label`, and its value will be passed as the `alias_id`. While you may use a custom alias, we strongly recommend setting and using the `external_id` as your primary user identifier for consistency across platforms.

To retrieve a user using their OneSignal ID, set the `alias_label` to `onesignal_id`. **Note**: When querying with any alias other than `onesignal_id`, authentication is required.

***

## OpenAPI

````yaml GET /apps/{app_id}/users/by/{alias_label}/{alias_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/users/by/{alias_label}/{alias_id}:
    get:
      summary: View user
      description: Retrieve a user including aliases, properties, and subscriptions.
      operationId: view-user
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
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    properties:
                      tags:
                        KEY: VALUE
                      country: US
                      first_active: 1673449251
                      last_active: 1678126124
                    identity:
                      external_id: example123
                      onesignal_id: ONESIGNAL_ID
                    subscriptions:
                      - id: SUBSCRIPTION_ID
                        app_id: APP_ID
                        type: Email
                        token: example@example.com
                        enabled: true
                        notification_types: -99
                        session_time: 3670
                        session_count: 129
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
                  properties:
                    type: object
                    properties:
                      tags:
                        type: object
                        properties:
                          KEY:
                            type: string
                            example: VALUE
                      country:
                        type: string
                        example: US
                      first_active:
                        type: integer
                        example: 1673449251
                        default: 0
                      last_active:
                        type: integer
                        example: 1678126124
                        default: 0
                  identity:
                    type: object
                    properties:
                      external_id:
                        type: string
                        example: example123
                      onesignal_id:
                        type: string
                        example: ONESIGNAL_ID
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
                          descriptions: >-
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
                            Indicates the reason for the Subscription's status.
                            Values are updated automatically as events are
                            detected by our frontend SDKs but you should set
                            this manually when updating via our REST API. `1` is
                            subscribed and `-31` is reserved for unsubscribed
                            via the API. See
                            [Subscriptions](/docs/subscriptions#notification-types).
                        session_time:
                          type: integer
                          description: >-
                            The total amount of time the user has had the app
                            open in seconds.
                          format: int32
                        session_count:
                          type: integer
                          description: >-
                            The total amount of times the user has opened the
                            app.
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
                            used for generating the iOS push token. `null` or
                            `0` if the token was generated in a Production
                            environment (App Store & Test Flight builds). `1`
                            for Development environment, `2` if it was generated
                            in an Ad-Hoc environment. This ensures OneSignal
                            routes notifications correctly based on the token’s
                            source environment.
                          format: int32
                        app_version:
                          type: string
                          description: >-
                            The version of your mobile app as detected by our
                            frontend SDKs or a value you set via our API. Our
                            SDK sets this based: Android - Android Studio
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
        '401':
          description: '401'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: auth-1
                        title: >-
                          This operation requires 'Authorization' in the HTTP
                          header
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
                          example: auth-1
                        title:
                          type: string
                          example: >-
                            This operation requires 'Authorization' in the HTTP
                            header
        '404':
          description: '404'
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
