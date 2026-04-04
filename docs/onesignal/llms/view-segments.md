# Source: https://documentation.onesignal.com/reference/view-segments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View segments

> Retrieve a list of segments associated with a specific OneSignal app. Useful for programmatically accessing segment metadata such as name, creation date, and status.

## Overview

Retrieve a list of segments associated with a specific OneSignal app. This is helpful when you want to access segment metadata programmatically instead of using the OneSignal Dashboard UI.

<Warning>
  This endpoint only retrieves existing segment metadata. It does not provide the segment filters or user data.
</Warning>

***

## OpenAPI

````yaml GET /apps/{app_id}/segments
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/segments:
    get:
      summary: View segments
      description: >-
        Retrieve a list of segments associated with a specific OneSignal app.
        Useful for programmatically accessing segment metadata such as name,
        creation date, and status.
      operationId: view-segments
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
        - name: Authorization
          in: header
          description: >-
            Your App API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: Key YOUR_APP_API_KEY
        - name: offset
          in: query
          description: >-
            The index to start returning segments from. Defaults to `0`.
            Segments are sorted by their creation date (`created_at`) in
            ascending order.
          schema:
            type: integer
            format: int32
            default: 0
        - name: limit
          in: query
          description: >-
            The maximum number of segments to return. Default/Max: `300`. Ideal
            for controlling data volume in large-scale applications.
          schema:
            type: integer
            format: int32
            default: 300
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    total_count: 1
                    offset: 0
                    limit: 300
                    segments:
                      - id: 4414c404-56a3-11ed-9b6a-0242ac120002
                        name: Subscribed Users
                        created_at: '2022-07-23T13:44:10.324Z'
                        updated_at: '2022-09-18T11:33:02.451Z'
                        app_id: 65c10914-56a3-11ed-9b6a-0242ac120002
                        read_only: false
                        is_active: true
              schema:
                type: object
                properties:
                  total_count:
                    type: integer
                    description: The total number of segments available for the app.
                  offset:
                    type: integer
                    description: Value set in the `offset` query parameter.
                  limit:
                    type: integer
                    description: Value set in the `limit` query parameter.
                  segments:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: >-
                            The unique identifier for the segment in UUID v4
                            format.
                        name:
                          type: string
                          description: >-
                            An internal name you set to help organize and track
                            Segments. Maximum 128 characters.
                        created_at:
                          type: string
                          description: >-
                            The date and time the segment was created in ISO
                            8601 format.
                        updated_at:
                          type: string
                          description: >-
                            The date and time the segment was last updated in
                            ISO 8601 format.
                        app_id:
                          type: string
                          description: >-
                            Your OneSignal App ID in UUID v4 format. See [Keys &
                            IDs](/docs/keys-and-ids).
                        read_only:
                          type: boolean
                          description: Indicates if the segment is read-only.
                        is_active:
                          type: boolean
                          description: >-
                            Indicates if the segment is active. `false` means
                            the segment is paused and cannot be used to send
                            messages.
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - code: example error code
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
                          example: example error code
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
      security: []

````

Built with [Mintlify](https://mintlify.com).
