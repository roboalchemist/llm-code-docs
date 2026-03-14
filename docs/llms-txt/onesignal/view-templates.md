# Source: https://documentation.onesignal.com/reference/view-templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View templates

> Retrieve a paginated list of message templates from your OneSignal app. This endpoint returns summary information for each template, including ID, name, creation, and update timestamps.

## Overview

Use this endpoint to retrieve a list of message templates associated with a specific OneSignal app. The response provides summary information only:

* `template_id`
* `name`
* `created_at`
* `updated_at`

<Note>
  This endpoint does **not** return full template content such as message bodies, channel properties, or delivery configuration. For detailed template data, use the [View Template](/reference/view-template) endpoint.
</Note>

***

## How to Use This API

### Required Parameters

* **`app_id`** (query param): The OneSignal App ID whose templates you want to retrieve.

### Optional Parameters

* **`limit`** (query param): Number of templates to return (default: `50`, maximum: `50`).
* **`offset`** (query param): Number of templates to skip. Use for pagination.

### Pagination Example

If your app has 125 templates and you're using the default limit of 50:

1. First request (first 50 templates):\
   `GET /templates?app_id={app_id}&offset=0`

2. Second request (next 50 templates):\
   `GET /templates?app_id={app_id}&offset=50`

3. Third request (final 25 templates):\
   `GET /templates?app_id={app_id}&offset=100`

Repeat the request while adjusting the `offset` until you've retrieved all templates.

***

## OpenAPI

````yaml GET /templates?app_id={app_id}&limit={limit}&offset={offset}
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /templates?app_id={app_id}&limit={limit}&offset={offset}:
    get:
      summary: View templates
      description: >-
        Retrieve a paginated list of message templates from your OneSignal app.
        This endpoint returns summary information for each template, including
        ID, name, creation, and update timestamps.
      operationId: view-templates
      parameters:
        - name: app_id
          in: query
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: YOUR_APP_ID
        - name: limit
          in: query
          description: >-
            The maximum number of templates returned per request. The default
            (if omitted) and maximum is 50 templates per request.
          schema:
            type: integer
            format: int32
            default: 50
        - name: offset
          in: query
          description: >-
            The pagination or "starting point" of the templates to be returned.
            Setting it to 0 with a limit of 50 will retrieve the first 50
            templates. Increasing the offset by 50 will return the next set of
            templates, and so on.
          schema:
            type: integer
            format: int32
            default: 0
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
        - name: channel
          in: query
          description: >-
            Filter the fetched templates by the delivery channel. Available
            options are: `push`, `email`, and `SMS`.
          schema:
            type: string
            enum:
              - push
              - email
              - sms
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value: |-
                    {
                        "limit": 50,
                        "offset": 0,
                        "templates": [
                            {
                                "id": "9e778dd4-6453-40d7-888d-9d9f327b9b66",
                                "name": "OneSignal Push: New Feature Announcement (Template)",
                                "created_at": "2021-07-23T18:02:23.956Z",
                                "updated_at": "2021-07-23T18:02:23.956Z"
                            },
                            {
                                "id": "806b4356-67af-4d33-8133-75e502f6d3b7",
                                "name": "OneSignal Push: User Action Notification (Template)",
                                "created_at": "2021-07-23T18:02:23.963Z",
                                "updated_at": "2021-07-23T18:02:23.963Z"
                            },
                            {
                                "id": "172f55b5-df07-49ae-8a8d-67037679487f",
                                "name": "OneSignal Push: Rating (Template)",
                                "created_at": "2021-07-23T18:02:23.984Z",
                                "updated_at": "2021-07-23T18:02:23.984Z"
                            }
                        ],
                        "total_count": 3
                    }
              schema:
                type: object
                properties:
                  limit:
                    type: integer
                    example: 50
                    default: 0
                  offset:
                    type: integer
                    example: 0
                    default: 0
                  templates:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: The ID of the template in UUID v4 format.
                        name:
                          type: string
                          description: >-
                            An internal name you set to help organize and track
                            Templates. Maximum 128 characters.
                        created_at:
                          type: string
                          description: >-
                            The date and time the template was created in ISO
                            8601 format.
                        updated_at:
                          type: string
                          description: >-
                            The date and time the template was last updated in
                            ISO 8601 format.
                  total_count:
                    type: integer
                    example: 3
                    default: 0
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Bad Request (Missing App ID):
                  value: |
                    {
                      "errors": ["Request is malformed: Failed to parse app_id from request", "JSON body is None for app_id_location=body request"]
                    }
                Bad Request (Invalid Limit):
                  value: |-
                    {
                        "errors": [
                            "Invalid limit, must be within 1 to 50"
                        ]
                    }
                Bad Request (Invalid Channel):
                  value: |-
                    {
                        "errors": [
                            "Invalid channel"
                        ]
                    }
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
                  - title: Bad Request (Invalid Limit)
                    type: object
                    properties:
                      errors:
                        type: array
                        items:
                          type: string
                          example: Invalid limit, must be within 1 to 50
                  - title: Bad Request (Invalid Channel)
                    type: object
                    properties:
                      errors:
                        type: array
                        items:
                          type: string
                          example: Invalid channel
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
