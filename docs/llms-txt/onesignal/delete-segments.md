# Source: https://documentation.onesignal.com/reference/delete-segments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete segment

> Delete segments from OneSignal. Does not delete users or subscriptions.

## Overview

The Delete segment method is used when you want to programmatically delete a segment from within the OneSignal Dashboard UI.

<Warning>
  Once a segment is deleted, it cannot be recovered. You will need to create a new segment with the same filters.
</Warning>

***

## How to use this API

You can pass in the `segment_id` dictating which segment from our dashboard will be deleted.

The `segment_id` can be found using the [View segments](/reference/view-segments) API or in the URL of the segment when viewing it in the dashboard as shown below:

<Frame caption="Example shows segment ID">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/reference/b79fdc286b1a385b627266f2950a34d2ad56ecac042710965f05d8f6d08dc3e3-Screenshot_2024-11-18_at_8.43.37_AM.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=fbdfb9881eef84cedcbadd1b14df98a5" width="3334" height="1294" data-path="images/reference/b79fdc286b1a385b627266f2950a34d2ad56ecac042710965f05d8f6d08dc3e3-Screenshot_2024-11-18_at_8.43.37_AM.png" />
</Frame>

***

## OpenAPI

````yaml DELETE /apps/{app_id}/segments/{segment_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/segments/{segment_id}:
    delete:
      summary: Delete segment
      description: Delete segments from OneSignal. Does not delete users or subscriptions.
      operationId: delete-segments
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
        - name: segment_id
          in: path
          description: >-
            The `segment_id` can be found in the URL of the segment when viewing
            it in the dashboard.
          schema:
            type: string
            default: YOUR_SEGMENT_ID
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
              examples:
                Result:
                  value:
                    success: true
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                    default: true
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value:
                    errors:
                      - >-
                        app_id not found. You may be missing a Content-Type:
                        application/json header.
                    reference:
                      - /docs/accounts-and-keys#section-keys-ids
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      example: >-
                        app_id not found. You may be missing a Content-Type:
                        application/json header.
                  reference:
                    type: array
                    items:
                      type: string
                      example: /docs/accounts-and-keys#section-keys-ids
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value:
                    success: false
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                    default: true
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
