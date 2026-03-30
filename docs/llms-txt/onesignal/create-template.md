# Source: https://documentation.onesignal.com/reference/create-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create template

> Create reusable message templates for push, email, and SMS channels. Templates can be accessed through both the dashboard and API using a `template_id`.

## Overview

Use this endpoint to create a new message template in your OneSignal app. Once created, the template becomes available for use when sending messages via both the Dashboard and the REST API by referencing the `template_id`.

Templates streamline and standardize message content across push, email, and SMS channels.

<Note>See [Templates](/docs/en/templates) for more information.</Note>

***

## How to use this API

Before using this endpoint, ensure that the target channel (push, email, or SMS) is properly configured in your OneSignal app. See [Channel Setup](/docs/en/channel-setup) for guidance.

### Push Templates

**Requirements:**

* Set the `contents` property with the English (`en`) language key.
* All [Push Channel Properties](/reference/push-notification) are valid for use in push templates.
* By default, all push platforms are enabled. You can target specific platforms by explicitly setting them (e.g., `isAndroid: true` disables others).

### Email Templates

**Requirements:**

* Set `isEmail: true`.
* Include both `email_subject` and `email_body`.
* All [Email Channel Properties](/reference/email) are valid for use in email templates.

### SMS Templates

**Requirements:**

* Set `isSMS: true`.
* Provide SMS-specific parameters like `contents`.
* All [SMS Channel Properties](/reference/sms) are valid for use in SMS templates.

***

## OpenAPI

````yaml POST /templates
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /templates:
    post:
      summary: Create template
      description: >-
        Create reusable message templates for push, email, and SMS channels.
        Templates can be accessed through both the dashboard and API using a
        `template_id`.
      operationId: create-template
      parameters:
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - app_id
                - name
              properties:
                app_id:
                  type: string
                  description: >-
                    Your OneSignal App ID in UUID v4 format. See [Keys &
                    IDs](/docs/keys-and-ids).
                  default: YOUR_APP_ID
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
                    Required for push and SMS templates. Supports [Message
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
                email_subject:
                  type: string
                  description: >-
                    Required for email templates. The subject of the email.
                    Supports [Message
                    Personalization](/docs/message-personalization).
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
              examples:
                Result:
                  value: |-
                    {
                      "id": "b17ebe45-ae35-4dce-11f8-8c3b3894a432",
                      "name": "new template created via the API",
                      "created_at": "2023-08-02T18:09:02Z",
                      "updated_at": "2023-08-02T18:09:02Z",
                      "content": {
                        "isAndroid": true,
                        "isIos": true,
                        "isMacOSX": true,
                        "isAdm": true,
                        "isAlexa": null,
                        "isWP": true,
                        "isWP_WNS": true,
                        "isChrome": true,
                        "isChromeWeb": true,
                        "isSafari": true,
                        "isFirefox": true,
                        "isEdge": true,
                        "headings": {
                          "en": "hello from the api!"
                        },
                        "subtitle": null,
                        "contents": {
                          "en": "why hello there!"
                        },
                        "global_image": null,
                        "url": "https://example.com",
                        "isEmail": null,
                        "email_body": null,
                        "email_subject": null,
                        "email_preheader": null,
                        "isSMS": null,
                        "sms_from": null,
                        "sms_media_urls": null,
                        "email_reply_to_address": null,
                        "disable_email_click_tracking": null
                      }
                    }
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: b17ebe45-ae35-4dce-11f8-8c3b3894a432
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
                  content:
                    type: object
                    properties:
                      isAndroid:
                        type: boolean
                        example: true
                        default: true
                      isIos:
                        type: boolean
                        example: true
                        default: true
                      isMacOSX:
                        type: boolean
                        example: true
                        default: true
                      isAdm:
                        type: boolean
                        example: true
                        default: true
                      isAlexa: {}
                      isWP:
                        type: boolean
                        example: true
                        default: true
                      isWP_WNS:
                        type: boolean
                        example: true
                        default: true
                      isChrome:
                        type: boolean
                        example: true
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
                        properties:
                          en:
                            type: string
                            example: hello from the api!
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
                        type: string
                        description: >-
                          The subject of the email. Required if `template_id` is
                          not set. Supports [Message
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
              examples:
                Bad Request (Email):
                  value: >-
                    // returned if isEmail:true, but there is no email body
                    content available in the request.

                    {
                        "success": false,
                        "errors": [
                            "'message' Email body can not be blank"
                        ]
                    }
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
                      example: '''message'' Email body can not be blank'
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: >-
                    <!-- returned when the request does not contain any contents
                    available to be saved in the template -->

                    <!-- can also be returned if creating a push template
                    without setting the value as an object -->

                    <title>The change you wanted was rejected (422)</title>
      deprecated: false
      security: []

````

Built with [Mintlify](https://mintlify.com).
