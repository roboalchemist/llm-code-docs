# Source: https://documentation.onesignal.com/reference/create-an-app.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an app

> Programmatically create a new OneSignal app via the REST API. This guide explains required fields, supported platform configurations (Web, Android, iOS), and how to properly authenticate using your Organization API key.

## Overview

Use this API to programmatically create a new OneSignal app. This is useful for automating app setup, particularly when managing multiple apps or organizations, and avoids needing to manually use the OneSignal Dashboard.

You can create an app under an existing organization or generate a new one. Push platform configurations for Web, Android, and iOS can be defined during app creation, though **Email** and **SMS** must be set up manually via the [OneSignal Dashboard](/docs/en/channel-setup).

<Note>
  For an overview of how apps and organizations work in OneSignal, see [Apps & Organizations](/docs/en/apps-organizations).
</Note>

***

## How to use this API

Use your [Organization API Key](/docs/en/keys-and-ids#organization-api-key), to authenticate. This key is **different** from the standard REST API key.

The Organization API key must be assocated with the `organization_id` in the request body.

### Web push configuration

The following parameters are **required** for web push setup:

* `site_name`
* `chrome_web_origin`
* `safari_site_origin`
* `safari_apns_p12`: Empty string OR your Base64 encoded p12 certificate for Safari Push Notifications.
* `safari_apns_p12_password`: Empty string OR Password for your `safari_apns_p12` file if set.

URLs must use `https://` and match your site’s [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin).

<Note>
  `safari_apns_p12` and `safari_apns_p12_password` are required for `safari_site_origin` to be set. If you do not have your own Safari p12 certificate, they should be included with blank values.

  If you use your own p12 certificate, you must update it every year.
  If you need help Base64 encoding your p12 certificate, you can use the following site: [https://www.base64encode.org](https://www.base64encode.org)
</Note>

**Recommended parameters**:

* `chrome_web_default_notification_icon`: URL of a `256x256px` PNG for Chrome.
* `safari_icon_256_256`: URL of a `256x256px` PNG for Safari.

***

### Android mobile push configuration

The following parameter is **required** for Android push notifications. See [Android: Firebase Credentials](/docs/en/android-firebase-credentials).

* `fcm_v1_service_account_json`

<Note>
  If you need help Base64 encoding your FCM Service Account JSON file, you can use the following site: [https://www.base64encode.org](https://www.base64encode.org)
</Note>

***

### iOS mobile push configuration

iOS mobile push can be configured using either a p8 or a p12 authentication.

<Note>
  If you need to Base64 encode your p8 key or p12 certificate, you can use the following site: [https://www.base64encode.org](https://www.base64encode.org)
</Note>

The following parameters are **required** if using [p8 Token-based connection to APNS](/docs/en/ios-p8-token-based-connection-to-apns):

* `apns_key_id`
* `apns_team_id`
* `apns_bundle_id`
* `apns_p8`

The following parameters are **required** if using [p12 APNS Authentication](/docs/en/ios-p12-generate-certificates):

* `apns_p12`
* `apns_p12_password`

**Optional parameters** :

* `additional_data_as_root_payload`: If set to `true`, the `data` paramater in your push notification payload will be added to the root payload of the notification. Helpful for customizations that require access to the data outside of our [OSNotification payload `additionalData` property](/docs/en/osnotification-payload).

***

## OpenAPI

````yaml POST /apps
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps:
    post:
      summary: Create an app
      description: >-
        Programmatically create a new OneSignal app via the REST API. This guide
        explains required fields, supported platform configurations (Web,
        Android, iOS), and how to properly authenticate using your Organization
        API key.
      operationId: create-an-app
      parameters:
        - name: Content-Type
          in: header
          required: true
          schema:
            type: string
            default: application/json
        - name: Authorization
          in: header
          description: >-
            Your Organization API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: Key YOUR_ORGANIZATION_API_KEY
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - organization_id
              properties:
                name:
                  type: string
                  description: >-
                    An internal name you set to help organize and track Apps.
                    Maximum 128 characters.
                  default: NAME_OF_NEW_APP
                organization_id:
                  type: string
                  description: >-
                    The [Organization ID](/docs/keys-and-ids#organization-id)
                    that the app will be associated with.
                  default: YOUR_ORG_ID
                chrome_web_origin:
                  type: string
                  description: >-
                    The HTTPS
                    [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
                    URL for your website. Required for web push notifications.
                site_name:
                  type: string
                  description: >-
                    The name of your website. Used for web push notification
                    titles when omitted from the notification payload. Required
                    for web push notifications.
                  default: SITE_NAME
                safari_site_origin:
                  type: string
                  description: >-
                    The HTTPS
                    [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
                    URL for your website. Required for web push notifications
                    for Safari and should be the same as `chrome_web_origin`.
                chrome_web_default_notification_icon:
                  type: string
                  description: >-
                    The full `https` URL to your default icon resource. The icon
                    should be a `256x256px` PNG.
                safari_icon_256_256:
                  type: string
                  description: >-
                    The full `https` URL to your default icon resource. The icon
                    should be a `256x256px` PNG.
                safari_apns_p12:
                  type: string
                  description: >-
                    A Base64 encoded p12 certificate for Safari Push
                    Notifications. If omitted, we will assign one to your app
                    for you.
                safari_apns_p12_password:
                  type: string
                  description: The password for the `safari_apns_p12` file if applicable.
                fcm_v1_service_account_json:
                  type: string
                  description: >-
                    Your FCM Service Account JSON file converted to base64
                    format. See [Android: Firebase
                    Credentials](/docs/android-firebase-credentials). Required
                    for Android mobile push notifications.
                apns_p8:
                  type: string
                  description: >-
                    A Base64 encoded p8 file for iOS mobile Push Notifications.
                    Omit if using `apns_p12`. See [p8 Token-based connection to
                    APNS](/docs/ios-p8-token-based-connection-to-apns).
                apns_env:
                  type: string
                  description: >-
                    The [APS Environment
                    Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)
                    to specify whether this is a `production` or `development`
                    environment. Defaults to `production`. Use with `apns_p8`.
                  Enum:
                    - production
                    - development
                apns_key_id:
                  type: string
                  description: >-
                    The APNS Key ID. Use with `apns_p8`. See [p8 Token-based
                    connection to
                    APNS](/docs/ios-p8-token-based-connection-to-apns).
                apns_team_id:
                  type: string
                  description: >-
                    The APNS Team ID. Use with `apns_p8`. See [p8 Token-based
                    connection to
                    APNS](/docs/ios-p8-token-based-connection-to-apns).
                apns_bundle_id:
                  type: string
                  description: >-
                    The Bundle ID for your app. Use with `apns_p8`. See [p8
                    Token-based connection to
                    APNS](/docs/ios-p8-token-based-connection-to-apns).
                apns_p12:
                  type: string
                  description: >-
                    A Base64 encoded p12 certificate for iOS mobile push
                    notifications. Omit if using `apns_p8`. See [p12 APNS
                    Authentication](/docs/ios-p12-generate-certificates).
                apns_p12_password:
                  type: string
                  description: The password for the `apns_p12` file if applicable.
                additional_data_is_root_payload:
                  type: boolean
                  description: >-
                    If set to `true`, the `data` paramater in your push
                    notification payload will be added to the root payload of
                    the notification. Helpful for customizations that require
                    access to the data outside of our [OSNotification payload
                    `additionalData` property](/docs/osnotification-payload).
                  default: false
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    description: The OneSignal App ID in UUID v4 format.
                    type: string
                  name:
                    description: >-
                      An internal name you set to help organize and track Apps.
                      Maximum 128 characters.
                    type: string
                  players:
                    description: The total number of Subscriptions in the app.
                    type: integer
                  messageable_players:
                    description: >-
                      The number of Subscriptions eligible to receive messages
                      in the app.
                    type: integer
                  created_at:
                    description: The date and time the app was created.
                    type: string
                  updated_at:
                    description: The date and time the app was last updated.
                    type: string
                  organization_id:
                    description: The Organization ID in which the app was created.
                    type: string
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
