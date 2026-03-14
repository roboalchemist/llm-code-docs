# Source: https://documentation.onesignal.com/reference/create-alias.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or update alias

> Create or update one or more user aliases when you already know an existing alias. This API performs an upsert on the user’s identity object—either adding new aliases or updating existing ones.

## Overview

Use this API to manage user aliases by providing one known alias (such as `external_id`, `onesignal_id`, or a custom alias) and specifying additional aliases to add or update.

This endpoint focuses solely on the `identity` object. If you need to fully create a user with subscriptions and properties, use the [Create user](/reference/create-user) API instead.

<Note>
  * If an alias with the same `alias_label` already exists for the user, it will be updated. If it doesn’t exist, a new alias will be created.
  * Want to use a subscription instead of an alias to identify the user? Use [Create alias (by subscription)](/reference/create-alias-by-subscription).
</Note>

See also:

* [Users](/docs/en/users) – for details on OneSignal ID and External ID
* [Aliases](/docs/en/aliases) – for setting and managing custom aliases
* [Delete alias](/reference/delete-alias) – for removing aliases

***

## How to use this API

To identify the user:

* Use `alias_label` for the type of alias you know (e.g., `external_id`, `onesignal_id`, or a custom alias)
* Use `alias_id` for the value of that alias

<Note>
  We strongly recommend setting the `external_id` as your primary user identifier. This can be done through our frontend SDK's login method when a user signs in to your app or website. It helps OneSignal associate the user's push, email, and SMS subscriptions to a unified user identity.
</Note>

Changes to the identity object take effect immediately upon request.

***

## OpenAPI

````yaml PATCH /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity:
    patch:
      summary: Create or update alias
      description: >-
        Create or update one or more user aliases when you already know an
        existing alias. This API performs an upsert on the user’s identity
        object—either adding new aliases or updating existing ones.
      operationId: create-alias
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                identity:
                  type: object
                  description: One or more aliases to be created for this user.
                  properties:
                    external_id:
                      type: string
                      description: >-
                        The main user ID to identify the user. See
                        [Users](/docs/users).
                      default: test_external_id
                    onesignal_id:
                      type: string
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  identity:
                    type: object
                    properties:
                      onesignal_id:
                        type: string
                        description: >-
                          The OneSignal ID of the user. See
                          [Users](/docs/users).
                        example: OneSignal-ID-in-UUID-v4-format
                      custom_alias_label:
                        type: string
                        description: >-
                          A custom alias of the user. See
                          [Aliases](/docs/aliases).
                        example: the-users-custom-alias-id
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: request-1
                        title: Invalid UUID
                        meta:
                          onesignal_id: '123'
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
                          example: request-1
                        title:
                          type: string
                          example: Invalid UUID
                        meta:
                          type: object
                          properties:
                            onesignal_id:
                              type: string
                              example: '123'
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
                          example: Subscription Limit Exceeded
                        title:
                          type: string
                          example: Example error title
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
                      - code: Rate Limit Exceeded
                        title: Example error title
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
                          example: Rate Limit Exceeded
                        title:
                          type: string
                          example: Example error title
                        meta:
                          type: object
                          properties: {}
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
