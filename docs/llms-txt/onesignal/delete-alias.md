# Source: https://documentation.onesignal.com/reference/delete-alias.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove alias

> Remove a specific alias from a user.

## Overview

Use this API to remove a specific alias from a user’s identity object without deleting the user. This operation only affects user identity labels—subscriptions and the core user record remain intact. To delete a user entirely, including all associated aliases and subscriptions, see the [Delete user](/reference/delete-user) API.

***

## How to use this API

To remove an alias from a user:

1. Identify the user via a known alias by specifying:

   * `alias_label` – the type of alias (e.g., email, external\_id)
   * `alias_id` – the unique identifier for that alias

2. Specify the alias to remove using:

   * `alias_label_to_delete` – the label of the alias to be deleted

   The `alias_label_to_delete` can be the same as the `alias_label` used to identify the user.

3. This action is performed synchronously—the alias is deleted immediately after the request is processed.

<Warning>
  The `onesignal_id` alias cannot be deleted. Only secondary aliases (like email, external\_id, etc.) are removable.
</Warning>

For a full explanation of identity management, see [Users](/docs/en/users) and [Aliases](/docs/en/aliases).

***

## FAQ

### Can I delete the same alias that I used to look up the user?

Yes. This is a common scenario—especially if an alias was set incorrectly and needs to be removed. Just be sure to include that alias both as the identifier and as alias\_label\_to\_delete.

If you want to delete the entire user and all associated data, use the [Delete user](/reference/delete-user) API.

### What happens if I delete all aliases associated with the user?

A user will always retain at least one alias, the onesignal\_id. Even if you remove all other aliases, the user and their subscriptions remain linked to the onesignal\_id.

***

## OpenAPI

````yaml DELETE /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity/{alias_label_to_delete}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity/{alias_label_to_delete}:
    delete:
      summary: Delete alias
      description: Remove a specific alias from a user.
      operationId: delete-alias
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
            default: external_id
          required: true
        - name: alias_id
          in: path
          description: The specific identifier for the given alias to identify the user.
          schema:
            type: string
          required: true
        - name: alias_label_to_delete
          in: path
          description: The name of the alias to remove.
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
                  identity:
                    type: object
                    properties:
                      onesignal_id:
                        type: string
                        description: >-
                          The OneSignal ID of the user. See
                          [Users](/docs/users).
                        example: OneSignal-ID-in-UUID-v4-format
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
