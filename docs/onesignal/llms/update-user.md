# Source: https://documentation.onesignal.com/reference/update-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update user

> Modify a user's properties.

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

This endpoint updates user-level properties for an existing user in your OneSignal app.

* To change a user's `identity` like `external_id` or custom [Aliases](/docs/en/aliases), use the [Create alias](/reference/create-alias) and [Delete alias](/reference/delete-alias) APIs.
* To manage a user's `subscriptions`, use the [Create Subscription by alias](/reference/create-subscription) or [Create user](/reference/create-user) APIs.

***

## How to use this API

You must supply an alias in the request path:

* `alias_label`: The type of identifier (e.g., `external_id`, `onesignal_id`, or a custom alias label).
* `alias_id`: The corresponding value for that label.

See [Users](/docs/en/users) and [Aliases](/docs/en/aliases) for more info.

***

## OpenAPI

````yaml PATCH /apps/{app_id}/users/by/{alias_label}/{alias_id}
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
    patch:
      summary: Update user
      description: Modify a user's properties.
      operationId: update-user
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
        - name: onesignal-subscription-id
          in: header
          description: >-
            Optional. Identifies a specific subscription to update. Some user
            properties, such as Session Time and Session Count, will update
            values on both the User and the Subscription.
          schema:
            type: string
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
                deltas:
                  type: object
                  description: >-
                    User properties that change frequently and generally only
                    increment.
                  properties:
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
                    purchases:
                      type: array
                      description: List of purchases
                      items:
                        properties:
                          sku:
                            type: string
                            description: The SKU of the item purchased.
                          iso:
                            type: string
                            description: The Currency Code
                            default: USD
                          amount:
                            type: string
                            description: The amount spent on the item.
                          count:
                            type: integer
                            description: The number of times the item has been purchased.
                        type: object
      responses:
        '202':
          description: '202'
          content:
            application/json:
              examples:
                Result:
                  value:
                    properties:
                      language: en
                      timezone_id: PST
                      lat: 90
                      long: 135
                      country: US
                      first_active: 1678215680
                      last_active: 1678215682
                      purchases:
                        - amount: $33.33
                          count: 3
                          iso: USD
                          sku: item
              schema:
                type: object
                properties:
                  properties:
                    type: object
                    properties:
                      language:
                        type: string
                        example: en
                      timezone_id:
                        type: string
                        example: PST
                      lat:
                        type: integer
                        example: 90
                        default: 0
                      long:
                        type: integer
                        example: 135
                        default: 0
                      country:
                        type: string
                        example: US
                      first_active:
                        type: integer
                        example: 1678215680
                        default: 0
                      last_active:
                        type: integer
                        example: 1678215682
                        default: 0
                      purchases:
                        type: array
                        items:
                          type: object
                          properties:
                            amount:
                              type: string
                              example: $33.33
                            count:
                              type: integer
                              example: 3
                              default: 0
                            iso:
                              type: string
                              example: USD
                            sku:
                              type: string
                              example: item
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
        '409':
          description: '409'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: Subscription Limit Exceeded
                        title: Example error title
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
                          example: Subscription Limit Exceeded
                        title:
                          type: string
                          example: Example error title
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
