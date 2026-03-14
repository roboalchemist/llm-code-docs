# Source: https://developers.kit.com/api-reference/custom-fields/bulk-create-custom-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk create custom fields

> See "[Bulk & async processing](#bulk-amp-async-processing)" for more information.



## OpenAPI

````yaml api-reference/v4.json post /v4/bulk/custom_fields
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/custom_fields:
    post:
      tags:
        - Custom Fields
      summary: Bulk create custom fields
      description: >-
        See "[Bulk & async processing](#bulk-amp-async-processing)" for more
        information.
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                custom_fields:
                  type: array
                  items:
                    type: object
                    properties:
                      label:
                        type: string
                    required:
                      - label
                callback_url:
                  type: string
                  nullable: true
              required:
                - custom_fields
            example:
              custom_fields:
                - label: Test Custom Field 0
                - label: Test Custom Field 1
                - label: Test Custom Field 2
                - label: Test Custom Field 3
              callback_url: null
      responses:
        '200':
          description: >-
            Creates the custom_fields synchronously when 100 or less custom
            fields are requested
          content:
            application/json:
              schema:
                type: object
                properties:
                  custom_fields:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        label:
                          type: string
                        key:
                          type: string
                        name:
                          type: string
                        created_at:
                          type: string
                      required:
                        - id
                        - key
                        - label
                        - name
                        - created_at
                  failures:
                    type: array
                    items: {}
                required:
                  - custom_fields
                  - failures
              example:
                custom_fields:
                  - id: 96
                    key: existing_custom_field
                    label: Existing Custom Field
                    name: ck_field_96_existing_custom_field
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 98
                    key: interests
                    label: Interests
                    name: ck_field_98_interests
                    created_at: '2023-02-17T11:43:55Z'
                  - id: 97
                    key: last_name
                    label: Last name
                    name: ck_field_97_last_name
                    created_at: '2023-02-17T11:43:55Z'
                failures: []
        '202':
          description: >-
            Creates or updates custom_fields asynchronously when more than 100
            custom fields are requested
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
          description: Returns a 422 when `custom_fields` is empty or not an array
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
                  - No custom fields included for processing
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