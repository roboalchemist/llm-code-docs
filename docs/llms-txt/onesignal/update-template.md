# Source: https://documentation.onesignal.com/reference/update-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update template

> Update existing OneSignal message templates for push, email, or SMS. Changes apply immediately across dashboard and API usage via the `template_id` reference.

## Overview

This endpoint allows you to update an existing push, email, or SMS template in your OneSignal app. Once updated, the changes are applied immediately and reflected across both the Dashboard and API when using the associated `template_id`.

Templates are updated using the same structure as when [creating templates](/reference/create-template).

<Note>See [Templates](/docs/en/templates) for more information.</Note>

***

## How to use this API

To update a template, you must supply:

* Your **OneSignal App ID** found in [Keys & IDs](/docs/en/keys-and-ids).
* The **Template ID**

### Template ID

Each template has a unique OneSignal-generated `template_id` (UUID v4). You can find it:

* Using the [View Templates API](/reference/view-templates)
* In the OneSignal Dashboard under **Messages > Templates > Options > Copy Template ID**

<Frame caption="Copy Template ID">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/templates/copy-template-id.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=b1b94df3f7ad6cdc5dc985e5c2f7ffeb" alt="Copy Template ID in OneSignal Dashboard" width="2208" height="1038" data-path="images/dashboard/templates/copy-template-id.png" />
</Frame>

***

## Channel-Specific Requirements

### Push Templates

* The `contents` property must use the `en` (English) key along with other languages you want to support.
* All [Push Notification Properties](/reference/push-notification) are valid.
* All platforms are enabled by default. To limit, explicitly enable desired ones (e.g., `isAndroid: true` disables iOS and Web).

### Email Templates

* Set `isEmail: true`
* Include `email_subject` and `email_body`
* All [Email Channel Properties](/reference/email) are supported.

### SMS Templates

* Set `isSMS: true`
* All [SMS Channel Properties](/reference/sms) are supported.

***

## OpenAPI

````yaml PATCH /templates/{template_id}?app_id={app_id}
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
    patch:
      summary: Update template
      description: >-
        Update existing OneSignal message templates for push, email, or SMS.
        Changes apply immediately across dashboard and API usage via the
        `template_id` reference.
      operationId: update-template
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
              required:
                - name
              properties:
                name:
                  type: string
                  description: >-
                    An internal name you set to help organize and track
                    Templates. Maximum 128 characters.
                  default: YOUR_TEMPLATE_NAME
                contents:
                  type: object
                  description: >-
                    The main message body with [language-specific
                    values](/docs/multi-language-messaging#supported-languages).
                    Supports [Message
                    Personalization](/docs/message-personalization).
                  required:
                    - en
                  properties:
                    en:
                      type: string
                      description: >-
                        The required message language type. See [Supported
                        Languages](/docs/multi-language-messaging#supported-languages).
                isEmail:
                  type: boolean
                  description: Required to be set `true` for email templates.
                email_body:
                  type: string
                  description: >-
                    The body of the email in HTML format. Required for email
                    templates. Supports [Message
                    Personalization](/docs/message-personalization).
                isSMS:
                  type: boolean
                  description: Required to be set `true` for SMS templates.
                dynamic_content:
                  type: object
                  description: >-
                    Add personalization to your templates programmatically. No
                    need to upload a CSV. See [Dynamic
                    Content](/docs/dynamic-content) for details.
                  example: >-
                    {"campaign_id": {"A": {"title": "Custom Title A", "message":
                    "Custom Message A", "url": "https://www.onesignal.com"},
                    "B": {"title": "Custom Title B", "message": "Custom Message
                    B", "url": "https://www.onesignal.com/login"}}}
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the template in UUID v4 format.
                    example: 15b739e8-93f9-4840-8c94-e115c30afddd
                  name:
                    type: string
                    description: >-
                      An internal name you set to help organize and track
                      Templates. Maximum 128 characters.
                  created_at:
                    type: string
                    description: >-
                      The date and time the template was created in ISO 8601
                      format.
                  updated_at:
                    type: string
                    description: >-
                      The date and time the template was last updated in ISO
                      8601 format.
                  channel:
                    type: string
                    description: 'Options are: `push`, `email`, and `SMS`.'
                  content:
                    type: object
                    properties:
                      isAndroid: {}
                      isIos: {}
                      isMacOSX:
                        type: boolean
                        example: false
                        default: true
                      isAdm: {}
                      isAlexa: {}
                      isWP: {}
                      isWP_WNS: {}
                      isChrome:
                        type: boolean
                        example: false
                        default: true
                      isChromeWeb:
                        type: boolean
                        example: true
                        default: true
                      isSafari:
                        type: boolean
                        example: true
                        default: true
                      isFirefox:
                        type: boolean
                        example: true
                        default: true
                      isEdge:
                        type: boolean
                        example: true
                        default: true
                      headings:
                        type: object
                        properties: {}
                      subtitle: {}
                      contents:
                        type: object
                        description: >-
                          The main message body with [language-specific
                          values](/docs/multi-language-messaging#supported-languages).
                          Supports [Message
                          Personalization](/docs/message-personalization).
                        required:
                          - en
                        properties:
                          en:
                            type: string
                            description: >-
                              The required message language type. See [Supported
                              Languages](/docs/multi-language-messaging#supported-languages).
                      global_image: {}
                      url: {}
                      isEmail:
                        type: boolean
                        description: Required to be set `true` for email templates.
                      email_body:
                        type: string
                        description: >-
                          The body of the email in HTML format. Required if
                          `template_id` is not set. Supports [Message
                          Personalization](/docs/message-personalization).
                      email_subject:
                        type: string
                        description: >-
                          The subject of the email. Supports [Message
                          Personalization](/docs/message-personalization).
                      email_preheader: {}
                      isSMS:
                        type: boolean
                        description: Required to be set `true` for SMS templates.
                      sms_from: {}
                      sms_media_urls: {}
                      email_reply_to_address: {}
                      disable_email_click_tracking: {}
        '400':
          description: '400'
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
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
                            'message' Notifications must have Any/English
                            language content
                  - title: Bad Request (Email)
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
                          example: '''message'' Email body can not be blank'
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
