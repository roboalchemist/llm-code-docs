# Source: https://documentation.onesignal.com/reference/view-apps.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View apps

> Retrieve a list of all OneSignal apps associated with your account, including key app details like name, App ID, subscription counts, and timestamps. Useful for managing multiple apps through the OneSignal API.

## Overview

Use this API to retrieve metadata for all OneSignal apps associated with your account. This includes app names, App IDs, subscription counts, and timestamps, making it easy to programmatically manage or audit your applications.

<Note>
  This API does not return the app's API keys. To manage API keys, use the [Create API Key](/reference/create-api-key), [Rotate API Key](/reference/rotate-api-key), and [Delete API Key](/reference/delete-api-key) APIs.
</Note>

<Warning>
  This API is limited to return a maximum of 1000 Apps. If you need access to more, then you should store the `app_id` and `name` for each of your apps on your own server to look up with the [View an app](/reference/view-an-app) API to get data for each app separately. Also, if you need to delete apps, then you can provide the `app_id` and `name` to OneSignal Support and ask for these to be deleted.
</Warning>

***

## How to use this API

To retrieve your apps, send a `GET` request to the `/apps` endpoint using your **Organization API Key**. This key can be found in your OneSignal dashboard under [Organization > Keys & IDs](/docs/en/keys-and-ids#organization-api-key).

***

## OpenAPI

````yaml GET /apps
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
    get:
      summary: View apps
      description: >-
        Retrieve a list of all OneSignal apps associated with your account,
        including key app details like name, App ID, subscription counts, and
        timestamps. Useful for managing multiple apps through the OneSignal API.
      operationId: view-apps
      parameters:
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
                type: array
                items:
                  type: object
                  properties:
                    id:
                      description: The OneSignal App ID in UUID v4 format.
                      type: string
                    name:
                      description: >-
                        An internal name you set to help organize and track
                        Apps. Maximum 128 characters.
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
