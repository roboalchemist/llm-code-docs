# Source: https://documentation.onesignal.com/reference/create-api-key.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create API key

> Use the OneSignal API to create a new Rich Authentication Token (App API Key) for a specific app. This guide explains how to authenticate with the Organization API key and configure optional IP allowlists using CIDR notation.

## Overview

Use this API to create a new **App API Key** (also called a **Rich Authentication Token**) for a specific OneSignal app. These keys are used to authenticate API requests at the app level and offer enhanced security features, including optional IP allowlisting.

<Note>
  For background on different OneSignal API keys, see [Keys & IDs](/docs/en/keys-and-ids).
</Note>

***

## How to use this API

Use your [Organization API Key](/docs/en/keys-and-ids#organization-api-key), to authenticate. This key is **different** from the standard REST API key.

### IP allowlisting

By default, the API key will not be restricted to any specific IP addresses. To enable IP allowlisting, you need to set the `ip_allowlist_mode` parameter to `explicit` and provide a list of allowed IP addresses in the `ip_allowlist` parameter.

If you want to set the explicit range of IPs that can use this API key, add them by setting `ip_allowlist_mode` to `explicit` and in `ip_allowlist` add the IPs in CIDRs notation as an array of string values.

***

## OpenAPI

````yaml POST /apps/{app_id}/auth/tokens
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/auth/tokens:
    post:
      summary: Create API key
      description: >-
        Use the OneSignal API to create a new Rich Authentication Token (App API
        Key) for a specific app. This guide explains how to authenticate with
        the Organization API key and configure optional IP allowlists using CIDR
        notation.
      operationId: create-api-key
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
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
              schema:
                type: object
                properties:
                  token_id:
                    type: string
                    description: >-
                      The OneSignal-generated ID specific to the API key. This
                      is not the API key itself.
                  formatted_token:
                    type: string
                    description: >-
                      The Rich Authentication Token (REST API Key). It is shown
                      only once and won’t be stored in OneSignal. Keep it secret
                      and secure, as it can’t be retrieved later. See [Rotate
                      API Key](/reference/rotate-api-key).
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
