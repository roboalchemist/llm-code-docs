# Source: https://documentation.onesignal.com/reference/delete-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete template

> Permanently delete a specific message template from your OneSignal app using its template ID. Templates used in Journeys must be removed from those Journeys before deletion.

## Overview

This endpoint allows you to delete a single template associated with your OneSignal app. Deletion is **immediate and irreversible**.

<Warning>
  If the template is currently used in a Journey, it cannot be deleted until that Journey has been deleted.
</Warning>

***

## How to use this API

Required Parameters

* `template_id` (path param): The OneSignal-generated UUID of the template to delete.
* `app_id` (query param): Your OneSignal App ID.

### Where to Find `template_id`

Each template has a unique OneSignal-generated `template_id` (UUID v4). You can find it:

* Using the [View Templates API](/reference/view-templates)
* In the OneSignal Dashboard under **Messages > Templates > Options > Copy Template ID**

<Frame caption="Copy Template ID">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/templates/copy-template-id.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=b1b94df3f7ad6cdc5dc985e5c2f7ffeb" alt="Copy Template ID in OneSignal Dashboard" width="2208" height="1038" data-path="images/dashboard/templates/copy-template-id.png" />
</Frame>

***

## OpenAPI

````yaml DELETE /templates/{template_id}?app_id={app_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /templates/{template_id}?app_id={app_id}:
    delete:
      summary: Delete template
      description: >-
        Permanently delete a specific message template from your OneSignal app
        using its template ID. Templates used in Journeys must be removed from
        those Journeys before deletion.
      operationId: delete-template
      parameters:
        - name: template_id
          in: path
          description: The template ID in UUID v4 format. See [Templates](/docs/templates).
          schema:
            type: string
            default: YOUR_TEMPLATE_ID
          required: true
        - name: app_id
          in: query
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: YOUR_APP_ID
        - name: Authorization
          in: header
          description: >-
            Your App's API key found in [Settings > Keys &
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
                  success:
                    type: boolean
                    example: true
        '400':
          description: '400'
          content:
            application/json:
              schema:
                oneOf:
                  - title: Bad Request (Missing App ID)
                    type: object
                    properties:
                      errors:
                        type: array
                        items:
                          type: string
                          example: >-
                            Request is malformed: Failed to parse app_id from
                            request
                  - title: Bad Request (Template In Use)
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: false
                        default: true
                      errors:
                        type: array
                        items:
                          type: string
                          example: >-
                            Can not delete a template that has journeys using
                            it.
        '404':
          description: '404'
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: false
                    default: true
                  errors:
                    type: array
                    items:
                      type: string
                      example: template not found
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
