# Source: https://documentation.onesignal.com/reference/rotate-api-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rotate API key

> Rotate an existing App API Key (Rich Authentication Token) for a OneSignal app. Useful when a token is compromised or needs replacement without creating a new key from scratch.

## Overview

Use this API to rotate a **Rich Authentication Token** (App API Key) for a specific OneSignal app. Rotating a key revokes the current token and generates a new one under the same configuration—ideal when a token is lost or compromised but you don’t want to recreate and reconfigure it from scratch.

<Note>
  For background on different OneSignal API keys, see [Keys & IDs](/docs/en/keys-and-ids).
</Note>

***

## How to use this API

Using your Organization API key (available in [Organizations > Keys & IDs](/docs/en/keys-and-ids#organization-api-key)) you can rotate an app token associated with a given app.

The `token_id` is a OneSignal-generated ID specific for the API key. This is not the API key itself. It is returned when creating an API key with [Create API key](/reference/create-api-key). It can be found in the OneSignal dashboard and in the response body of the [View API keys](/reference/view-api-keys) request.

***

## OpenAPI

````yaml POST /apps/{app_id}/auth/tokens/{token_id}/rotate
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/auth/tokens/{token_id}/rotate:
    post:
      summary: Rotate API key
      description: >-
        Rotate an existing App API Key (Rich Authentication Token) for a
        OneSignal app. Useful when a token is compromised or needs replacement
        without creating a new key from scratch.
      operationId: rotate-api-key
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
            default: YOUR_APP_ID
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
        - name: token_id
          in: path
          description: >-
            The OneSignal-generated ID specific to the API key. This is not the
            API key itself. It is returned when creating an API key with [Create
            API key](/reference/create-api-key). It can be found in the
            OneSignal dashboard and in the response body of the [View API
            keys](/reference/view-api-keys) request.
          schema:
            type: string
          required: true
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  formatted_token:
                    type: string
                    description: >-
                      The Rich Authentication Token (REST API Key). It is shown
                      only once and won’t be stored in OneSignal. Keep it secret
                      and secure, as it can’t be retrieved later.
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value: '{}'
              schema:
                type: object
                properties: {}
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
