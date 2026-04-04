# Source: https://documentation.onesignal.com/reference/view-api-keys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View API keys

> View the details of all of your current app API keys (Rich Authentication Token) for a single OneSignal app.

## Overview

This API is helpful for auditing and managing the API keys (Rich Authentication Tokens) associated with an app. It returns metadata for each token, including:

* Token name and ID
* IP allow list mode and associated CIDR ranges (if any)
* Creation and last updated timestamps

<Note>
  For background on different OneSignal API keys, see [Keys & IDs](/docs/en/keys-and-ids).
</Note>

***

## How to use this API

Use your [Organization API Key](/docs/en/keys-and-ids#organization-api-key), to authenticate. This key is **different** from the standard REST API key.

***

## OpenAPI

````yaml GET /apps/{app_id}/auth/tokens
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
    get:
      summary: View API keys
      description: >-
        View the details of all of your current app API keys (Rich
        Authentication Token) for a single OneSignal app.
      operationId: view-api-keys
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
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  tokens:
                    type: array
                    items:
                      type: object
                      properties:
                        token_id:
                          type: string
                          description: >-
                            The OneSignal-generated ID specific to the API key.
                            This is not the API key itself.
                        updated_at:
                          type: string
                          description: The date and time the token was last updated.
                        created_at:
                          type: string
                          description: The date and time the token was created.
                        name:
                          type: string
                          description: >-
                            An internal name you set to help organize and track
                            API keys (Rich Authentication Tokens). Maximum 128
                            characters.
                        ip_allowlist_mode:
                          type: string
                          description: >-
                            Defaults to `disabled`, can be set to `explicit`. If
                            set to `explicit`, a list of network addresses in
                            the form of CIDRs has to be specified in the
                            `ip_allowlist` parameter.
                          enum:
                            - disabled
                            - explicit
                        ip_allowlist:
                          type: array
                          items:
                            type: string
                            description: The IP allow list of the token.
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
