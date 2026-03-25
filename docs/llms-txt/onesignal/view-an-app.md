# Source: https://documentation.onesignal.com/reference/view-an-app.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View an app

> View the details of a single OneSignal app

## Overview

Use this API to retrieve metadata and platform configuration for a single OneSignal app associated with your account. This includes app names, App ID, Subscription counts, timestamps, and push platform credentials (Android/FCM, iOS/APNS, Web Push, Safari), making it easy to programmatically manage or audit your applications.

<Note>
  This API does not return the app's API keys. To manage API keys, use the [Create API Key](/reference/create-api-key), [Rotate API Key](/reference/rotate-api-key), and [Delete API Key](/reference/delete-api-key) APIs.
</Note>

***

## How to use this API

To retrieve your app, send a `GET` request to the `/apps` endpoint using your **Organization API Key**. This key can be found in your OneSignal dashboard under [Organization > Keys & IDs](/docs/en/keys-and-ids#organization-api-key).

***

## OpenAPI

````yaml GET /apps/{app_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}:
    get:
      summary: View an app
      description: View the details of a single OneSignal app
      operationId: view-an-app
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
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
                  fcm_v1_service_account_json:
                    description: >-
                      Your FCM Service Account JSON file for Android push
                      notifications. See [Android: Firebase
                      Credentials](/docs/android-firebase-credentials).
                    type: string
                  fcm_sender_id:
                    description: The FCM Sender ID associated with your Firebase project.
                    type: string
                  chrome_web_key:
                    description: >-
                      Web push VAPID public key for Chrome web push
                      notifications.
                    type: string
                  chrome_web_origin:
                    description: >-
                      The HTTPS origin URL for your website. Required for web
                      push notifications.
                    type: string
                  chrome_web_gcm_sender_id:
                    description: The GCM Sender ID used for web push notifications.
                    type: string
                  chrome_web_default_notification_icon:
                    description: >-
                      The full HTTPS URL to your default notification icon.
                      Should be a 256x256px PNG.
                    type: string
                  chrome_web_sub_domain:
                    description: >-
                      The OneSignal subdomain for web push if not using your own
                      origin.
                    type: string
                  apns_env:
                    description: >-
                      The APNS environment: `production` or `development`. See
                      [iOS SDK Setup](/docs/ios-sdk-setup).
                    type: string
                  apns_certificates:
                    description: >-
                      The APNS p12 certificate for iOS push notifications. See
                      [p12 APNS
                      Authentication](/docs/ios-p12-generate-certificates).
                    type: string
                  apns_p8:
                    description: >-
                      The APNS p8 token key for iOS push notifications. See [p8
                      Token-based connection to
                      APNS](/docs/ios-p8-token-based-connection-to-apns).
                    type: string
                  apns_team_id:
                    description: The Apple Team ID associated with your APNS credentials.
                    type: string
                  apns_key_id:
                    description: The APNS Key ID for p8 token-based authentication.
                    type: string
                  apns_bundle_id:
                    description: >-
                      The iOS app Bundle ID associated with your APNS
                      credentials.
                    type: string
                  site_name:
                    description: >-
                      The name of your website, used for web push notification
                      titles.
                    type: string
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
