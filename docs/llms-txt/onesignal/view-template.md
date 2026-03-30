# Source: https://documentation.onesignal.com/reference/view-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View template

> Retrieve the details of a specific message template in your OneSignal app using its template ID. This API returns the template content, target channel, and timestamps for creation and last update.

## Overview

This endpoint returns metadata and content for a single template, including:

* Template body/content
* Target delivery channel (e.g., push, email, SMS)
* Creation and last updated timestamps

This is useful for inspecting existing templates before using or updating them.

<Note>See [Templates](/docs/en/templates) for more information.</Note>

***

## How to use this API

Required parameters:

* `app_id` (query param): Your OneSignal App ID.
* `template_id` (path param): The unique ID of the template.

### Template ID

Each template has a unique OneSignal-generated `template_id` (UUID v4). You can find it:

* Using the [View Templates API](/reference/view-templates)
* In the OneSignal Dashboard under **Messages > Templates > Options > Copy Template ID**

<Frame caption="Copy Template ID">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/templates/copy-template-id.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=b1b94df3f7ad6cdc5dc985e5c2f7ffeb" alt="Copy Template ID in OneSignal Dashboard" width="2208" height="1038" data-path="images/dashboard/templates/copy-template-id.png" />
</Frame>

***

## OpenAPI

````yaml GET /templates/{template_id}?app_id={app_id}
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
    get:
      summary: View template
      description: >-
        Retrieve the details of a specific message template in your OneSignal
        app using its template ID. This API returns the template content, target
        channel, and timestamps for creation and last update.
      operationId: view-template
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
        - name: Content-Type
          in: header
          required: true
          schema:
            type: string
            default: application/json; charset=utf-8
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                oneOf:
                  - title: 200 OK - Push
                    type: object
                    properties:
                      id:
                        type: string
                        description: The template ID in UUID v4 format.
                        example: Template-ID-in-UUID-v4-format
                      name:
                        type: string
                        description: >-
                          An internal name you set to help organize and track
                          Templates. Maximum 128 characters.
                      channel:
                        type: string
                        description: 'Options are: `push`, `email`, and `SMS`.'
                        example: push
                      created_at:
                        type: string
                        description: >-
                          The date and time the template was created in ISO 8601
                          format.
                        example: '2023-07-20T19:16:55Z'
                      updated_at:
                        type: string
                        description: >-
                          The date and time the template was last updated in ISO
                          8601 format.
                        example: '2023-07-20T19:16:55Z'
                      content:
                        type: object
                        description: The template content.
                        properties:
                          isAndroid:
                            type: boolean
                            description: Template enabled for Android.
                          isIos:
                            type: boolean
                            description: Template enabled for iOS.
                          isMacOSX:
                            type: boolean
                            description: Template enabled for macOS.
                          isAdm:
                            type: boolean
                            description: Template enabled for Amazon.
                          isWP_WNS:
                            type: boolean
                            description: Template enabled for Windows.
                          isChromeWeb:
                            type: boolean
                            description: Template enabled for Chrome Web.
                          isSafari:
                            type: boolean
                            description: Template enabled for Safari.
                          isFirefox:
                            type: boolean
                            description: Template enabled for Firefox.
                          isEdge:
                            type: boolean
                            description: Template enabled for Edge.
                          headings:
                            type: object
                            properties:
                              en:
                                type: string
                                description: >-
                                  The push message title in each set language
                                  type. See [Supported
                                  Languages](/docs/multi-language-messaging#supported-languages).
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
                                  The required message language type. See
                                  [Supported
                                  Languages](/docs/multi-language-messaging#supported-languages).
                          global_image: {}
                          url:
                            type: string
                            example: https://example.com
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
                            description: >-
                              The subject of the email. Supports [Message
                              Personalization](/docs/message-personalization).
                            default: This is your email subject.
                          email_preheader:
                            description: >-
                              The preheader text of the email. Supports [Message
                              Personalization](/docs/message-personalization).
                          email_from_address:
                            type: string
                            description: >-
                              The full email address shown in the 'From' field
                              of the email (e.g.,
                              `promotions@news.example.com`). This is what
                              recipients see as the sender. If not specified,
                              OneSignal uses the default 'Sender Email' set in
                              your Dashboard's Email Settings. See
                              [Senders](/docs/senders).
                          email_from_name:
                            description: The name of the sender.
                          isSMS:
                            type: boolean
                            description: Required to be set `true` for SMS templates.
                          sms_from: {}
                          sms_media_urls: {}
                          email_reply_to_address: {}
                          disable_email_click_tracking: {}
                  - title: 200 OK - Email
                    type: object
                    properties:
                      id:
                        type: string
                        example: 05b5d060-5e07-40ec-953c-4f2b8be0c83e
                      name:
                        type: string
                        example: >-
                          An internal name you set to help organize and track
                          Templates. Maximum 128 characters.
                      created_at:
                        type: string
                        example: '2022-06-30T23:23:22Z'
                      updated_at:
                        type: string
                        example: '2023-06-29T23:34:07Z'
                      content:
                        type: object
                        properties:
                          isAndroid: {}
                          isIos: {}
                          isMacOSX: {}
                          isAdm: {}
                          isAlexa: {}
                          isWP: {}
                          isWP_WNS: {}
                          isChrome: {}
                          isChromeWeb: {}
                          isSafari: {}
                          isFirefox: {}
                          isEdge: {}
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
                                  The required message language type. See
                                  [Supported
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
                          email_preheader:
                            type: string
                            example: ''
                          isSMS:
                            type: boolean
                            description: Required to be set `true` for SMS templates.
                          sms_from: {}
                          sms_media_urls: {}
                          email_reply_to_address:
                            type: string
                            example: ''
                          disable_email_click_tracking:
                            type: boolean
                            example: false
                            default: true
                          email_from_address:
                            type: string
                            example: ''
                          email_from_name:
                            type: string
                            example: ''
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
                      type: string
                      example: >-
                        Request is malformed: Failed to parse app_id from
                        request
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
