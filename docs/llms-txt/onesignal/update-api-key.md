# Source: https://documentation.onesignal.com/reference/update-api-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update API key

> Update a Rich Authentication Token (App API Key) for a OneSignal app. Modify the token's name or IP allowlist settings using your Organization API Key.

## Overview

Use this API to update the properties of a specific **Rich Authentication Token** (App API Key) for a OneSignal app. You can change the name, IP allowlist mode, or the list of allowed IPs. This is helpful for adjusting access rules without needing to recreate the key.

<Note>
  For background on different OneSignal API keys, see [Keys & IDs](/docs/en/keys-and-ids).
</Note>

***

## How to use this API

Using your Organization API key (available in [Organizations > Keys & IDs](/docs/en/keys-and-ids#organization-api-key)) you can delete an app token associated with a given app.

The `token_id` is a OneSignal-generated ID specific for the API key. This is not the API key itself. It is returned when creating an API key with [Create API key](/reference/create-api-key). It can be found in the OneSignal dashboard and in the response body of the [View API keys](/reference/view-api-keys) request.

***

## OpenAPI

````yaml PATCH /apps/{app_id}/auth/tokens/{token_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/auth/tokens/{token_id}:
    patch:
      summary: Update API key
      description: >-
        Update a Rich Authentication Token (App API Key) for a OneSignal app.
        Modify the token's name or IP allowlist settings using your Organization
        API Key.
      operationId: update-api-key
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
            Your Organization's API key found in [Organizations > Keys &
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: >-
                    An internal name you set to help organize and track API keys
                    (Rich Authentication Tokens). Maximum 128 characters.
                ip_allowlist_mode:
                  type: string
                  description: >-
                    Defaults to `disabled`, can be set to `explicit`. If set to
                    `explicit`, a list of network addresses in the form of CIDRs
                    has to be specified in the `ip_allowlist` parameter.
                  enum:
                    - disabled
                    - explicit
                ip_allowlist:
                  type: array
                  description: >-
                    An array of allowed networks in CIDRs notation. Only IPs in
                    those ranges will be permitted to use the API key.
                  items:
                    type: string
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value: '{}'
              schema:
                type: object
                properties: {}
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
