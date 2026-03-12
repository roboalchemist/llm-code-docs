# Source: https://documentation.onesignal.com/reference/fetch-aliases.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View user identity

> Retrieve all aliases associated with a user using a known alias, such as an `external_id`, `onesignal_id`, or a custom alias. This API helps you map back to a user’s full identity from any one piece of identifying information.

## Overview

Use this API when you want to retrieve the complete identity object for a user, which includes all aliases tied to that user. It is ideal for cases where you know one alias and want to discover others—especially helpful for user mapping, debugging, or linking systems.

This endpoint is similar to the [View user](/reference/view-user) API but only returns the `identity` object—not subscriptions or properties.

<Tip>
  If you only know a subscription\_id, use View user identity (by subscription) instead.
</Tip>

For more context on user identity and aliasing:

* [Users](/docs/en/users)
* [Aliases](/docs/en/aliases)

***

## How to use this API

To identify the user, use:

* `alias_label` – the type of alias you’re using to find the user (e.g. `external_id`, `onesignal_id`, or a custom alias)
* `alias_id` – the actual value of that alias

Common usage patterns:

Using `external_id` (recommended):

* `alias_label`: `external_id`
* `alias_id`: your user ID (e.g., user-123)

Using `onesignal_id`:

* `alias_label`: `onesignal_id`
* `alias_id`: the OneSignal-assigned unique ID

Using a custom alias:

* Define your own alias label (e.g. `shopify_customer_id`) and its value

<Note>
  We strongly recommend setting and using the `external_id` as your primary user identifier for portability and simplicity across your systems.
</Note>

***

## OpenAPI

````yaml GET /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity
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
    get:
      summary: View user identity
      description: >-
        Retrieve all aliases associated with a user using a known alias, such as
        an `external_id`, `onesignal_id`, or a custom alias. This API helps you
        map back to a user’s full identity from any one piece of identifying
        information.
      operationId: fetch-aliases
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
                      external_id:
                        type: string
                        description: The External ID of the user. See [Users](/docs/users).
                        example: the-users-external-id
        '400':
          description: '400'
          content:
            application/json:
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
        '404':
          description: '404'
          content:
            application/json:
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
