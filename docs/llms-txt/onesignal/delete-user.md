# Source: https://documentation.onesignal.com/reference/delete-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete user

> Delete a user including all associated properties, subscriptions, and identity.

## Overview

Use this API to permanently delete a user from your OneSignal project, including all associated subscriptions, properties, and aliases. The operation is asynchronous—user data will be deleted shortly after the request is accepted.

***

## How to use this API

To delete a user, you must be able to identify them using one of the following alias types:

* `external_id` (recommended and most common)
* `onesignal_id`
* A custom Alias that you have set

Pass the appropriate `alias_label` and corresponding `alias_id` in the request path.

<Warning>
  This operation deletes all data associated with the user, including:

* All identity aliases
* All channel subscriptions (push, email, SMS, etc.)
* All custom user properties
</Warning>

## Because this is an irreversible operation, be sure that you really intend to delete the user and all their data

## OpenAPI

````yaml DELETE /apps/{app_id}/users/by/{alias_label}/{alias_id}
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
    delete:
      summary: Delete user
      description: >-
        Delete a user including all associated properties, subscriptions, and
        identity.
      operationId: delete-user
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
        '202':
          description: '202'
          content:
            application/json:
              examples:
                Result:
                  value:
                    identity:
                      onesignal_id: 567491ee-9105-4a87-9cbc-ed78a571645b
              schema:
                type: object
                properties:
                  identity:
                    type: object
                    properties:
                      onesignal_id:
                        type: string
                        example: 567491ee-9105-4a87-9cbc-ed78a571645b
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
