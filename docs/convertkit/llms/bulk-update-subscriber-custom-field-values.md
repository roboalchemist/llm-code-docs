# Source: https://developers.kit.com/api-reference/custom-fields/bulk-update-subscriber-custom-field-values.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk update subscriber custom field values



## OpenAPI

````yaml api-reference/v4.json post /v4/bulk/custom_fields/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/custom_fields/subscribers:
    post:
      tags:
        - Custom Fields
      summary: Bulk update subscriber custom field values
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                custom_field_values:
                  type: array
                  items:
                    type: object
                    properties:
                      subscriber_id:
                        type: integer
                        nullable: true
                      subscriber_custom_field_id:
                        type: integer
                      value:
                        type: string
                    required:
                      - subscriber_id
                      - subscriber_custom_field_id
                      - value
                callback_url:
                  nullable: true
              required:
                - custom_field_values
                - callback_url
            example:
              custom_field_values:
                - subscriber_id: 0
                  subscriber_custom_field_id: 0
                  value: value_0
                - subscriber_id: 1
                  subscriber_custom_field_id: 1
                  value: value_1
                - subscriber_id: 2
                  subscriber_custom_field_id: 2
                  value: value_2
                - subscriber_id: 3
                  subscriber_custom_field_id: 3
                  value: value_3
              callback_url: null
      responses:
        '200':
          description: >-
            Creates or updates custom field values synchronously when 100 or
            less values are requested
          content:
            application/json:
              schema:
                type: object
                properties:
                  custom_field_values:
                    type: array
                    items:
                      type: object
                      properties:
                        subscriber_id:
                          type: integer
                        subscriber_custom_field_id:
                          type: integer
                        value:
                          type: string
                      required:
                        - subscriber_id
                        - subscriber_custom_field_id
                        - value
                  failures:
                    type: array
                    items:
                      type: object
                      properties:
                        errors:
                          type: array
                          items:
                            type: string
                        custom_field_value:
                          type: object
                          properties:
                            subscriber_id:
                              type: integer
                              nullable: true
                            subscriber_custom_field_id:
                              type: integer
                            value:
                              type: string
                          required:
                            - subscriber_id
                            - subscriber_custom_field_id
                            - value
                      required:
                        - errors
                        - custom_field_value
                required:
                  - custom_field_values
                  - failures
              example:
                custom_field_values:
                  - subscriber_id: 526
                    subscriber_custom_field_id: 109
                    value: Smith
                  - subscriber_id: 526
                    subscriber_custom_field_id: 110
                    value: Acme Inc
                failures:
                  - errors:
                      - Subscriber does not exist
                    custom_field_value:
                      subscriber_id: null
                      subscriber_custom_field_id: 109
                      value: Jones
                  - errors:
                      - Custom field does not exist
                    custom_field_value:
                      subscriber_id: 526
                      subscriber_custom_field_id: 999999
                      value: Test
        '202':
          description: >-
            Creates or updates custom field values asynchronously when more than
            100 values are requested
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example: {}
        '401':
          description: Returns a 401 if the token and/or account cannot be authenticated
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - The access token is invalid
        '413':
          description: >-
            Returns a 413 when the size of the request would exceed the
            account's data limit for enqueued bulk requests
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - >-
                    This request exceeds your queued bulk requests limit. Please
                    wait while we process your existing requests and try again
                    later.
        '422':
          description: Returns a 422 when `custom_field_values` is empty or not an array
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                required:
                  - errors
              example:
                errors:
                  - No custom field values included for processing
      security:
        - OAuth2: []
components:
  securitySchemes:
    OAuth2:
      description: Authenticate API requests via an OAuth token
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://api.kit.com/v4/oauth/authorize
          tokenUrl: https://api.kit.com/v4/oauth/token
          refreshUrl: https://api.kit.com/v4/oauth/token
          scopes:
            read: Read access to Kit API v4
            write: Write access to Kit API v4

````

Built with [Mintlify](https://mintlify.com).