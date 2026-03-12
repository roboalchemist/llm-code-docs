# Source: https://documentation.onesignal.com/reference/copy-template-to-another-app.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Copy template to another app

> Create a duplicate of a template in another app. The new template will be completely separate from the original (including having a new template_id) but will be created with all the same content.

## Overview

This API allows you to copy a template from one app (`app_id`) to another (`target_app_id`). The duplicated template will have the same content as the original, but a new unique `template_id`.

<Note>
  If you are trying to copy an email template, we also have an [Email Template Forwarding](/docs/en/email-template-forwarding) feature that does not require an API call.

  Both options support HTML and Drag & Drop email templates.
</Note>

***

## Requirements

* **Organization Membership:** Both the `app_id` and `target_app_id` must belong to the same [Organization](/docs/en/apps-organizations).
* **Authorization Required:** You must use your [Organization API key](/docs/en/keys-and-ids#organization-api-key), not an app-level REST API key.
* **Permissions Note:** Your user must have admin-level access to both the source and target apps. If not, the request will fail with a "permission denied" error.

***

## Parameters

* `template_id` (path param): UUID of the template to be copied.
* `app_id` (query param): ID of the app where the original template exists.
* `target_app_id` (body param): ID of the app where the template will be duplicated.

***

## How to Use

### 1. Locate the Template ID

Each template has a unique OneSignal-generated `template_id` (UUID v4). You can find it:

* Using the [View Templates API](/reference/view-templates)
* In the OneSignal Dashboard under **Messages > Templates > Options > Copy Template ID**

<Frame caption="Copy Template ID">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/templates/copy-template-id.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=b1b94df3f7ad6cdc5dc985e5c2f7ffeb" alt="Copy Template ID in OneSignal Dashboard" width="2208" height="1038" data-path="images/dashboard/templates/copy-template-id.png" />
</Frame>

### 2. Get App IDs

Refer to [Keys & IDs](/docs/en/keys-and-ids) to find your `app_id` and `target_app_id`.

***

## Response

The response will include:

* The new `template_id` for the copied template
* Confirmation of successful creation
* Any warnings if applicable (e.g., limited fields copied)

***

## OpenAPI

````yaml POST /templates/{template_id}/copy_to_app?app_id={app_id}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /templates/{template_id}/copy_to_app?app_id={app_id}:
    post:
      summary: Copy template to another app
      description: >-
        Create a duplicate of a OneSignal message template in another app within
        the same organization. The new template will retain the same content but
        have a unique template ID.
      operationId: copy-template-to-another-app
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
                - target_app_id
              properties:
                target_app_id:
                  type: string
                  description: >-
                    Specifies the OneSignal app ID that the template will be
                    copied to. Cannot be the same as the `app_id`.
                  default: YOUR_OTHER_APP_ID
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
                    description: Whether the template was copied successfully.
        '400':
          description: '400'
          content:
            application/json:
              schema:
                oneOf:
                  - title: Bad Request (Missing Body Parameter)
                    type: object
                    properties:
                      errors:
                        type: array
                        items:
                          type: string
                          description: >-
                            Missing body parameter.Request is malformed: Failed
                            to parse app_id from request
                  - title: Bad Request (Missing Query Parameter)
                    type: object
                    properties:
                      errors:
                        type: array
                        items:
                          type: string
                          description: >-
                            Missing query parameter. app_id not found. You may
                            be missing a Content-Type: application/json header.
        '404':
          description: '404'
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Whether the template was copied successfully.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
