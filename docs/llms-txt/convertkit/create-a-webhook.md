# Source: https://developers.kit.com/api-reference/webhooks/create-a-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a webhook

> Available event types:<br/>- `subscriber.subscriber_activate`<br/>- `subscriber.subscriber_unsubscribe`<br/>- `subscriber.subscriber_bounce`<br/>- `subscriber.subscriber_complain`<br/>- `subscriber.form_subscribe`, required parameter `form_id` [Integer]<br/>- `subscriber.course_subscribe`, required parameter `sequence_id` [Integer]<br/>- `subscriber.course_complete`, required parameter `sequence_id` [Integer]<br/>- `subscriber.link_click`, required parameter `initiator_value` [String] as a link URL<br/>- `subscriber.product_purchase`, required parameter `product_id` [Integer]<br/>- `subscriber.tag_add`, required parameter `tag_id` [Integer]<br/>- `subscriber.tag_remove`, required parameter `tag_id` [Integer]<br/>- `purchase.purchase_create`<br/>- `custom_field.field_created`<br/>- `custom_field.field_deleted`<br/>- `custom_field.field_value_updated`, required parameter `custom_field_id` [Integer]



## OpenAPI

````yaml api-reference/v4.json post /v4/webhooks
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/webhooks:
    post:
      tags:
        - Webhooks
      summary: Create a webhook
      description: >-
        Available event types:<br/>- `subscriber.subscriber_activate`<br/>-
        `subscriber.subscriber_unsubscribe`<br/>-
        `subscriber.subscriber_bounce`<br/>-
        `subscriber.subscriber_complain`<br/>- `subscriber.form_subscribe`,
        required parameter `form_id` [Integer]<br/>-
        `subscriber.course_subscribe`, required parameter `sequence_id`
        [Integer]<br/>- `subscriber.course_complete`, required parameter
        `sequence_id` [Integer]<br/>- `subscriber.link_click`, required
        parameter `initiator_value` [String] as a link URL<br/>-
        `subscriber.product_purchase`, required parameter `product_id`
        [Integer]<br/>- `subscriber.tag_add`, required parameter `tag_id`
        [Integer]<br/>- `subscriber.tag_remove`, required parameter `tag_id`
        [Integer]<br/>- `purchase.purchase_create`<br/>-
        `custom_field.field_created`<br/>- `custom_field.field_deleted`<br/>-
        `custom_field.field_value_updated`, required parameter `custom_field_id`
        [Integer]
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                target_url:
                  type: string
                event:
                  type: object
                  properties:
                    name:
                      type: string
                    form_id:
                      nullable: true
                    tag_id:
                      nullable: true
                    sequence_id:
                      nullable: true
                    product_id:
                      nullable: true
                    initiator_value:
                      nullable: true
                    custom_field_id:
                      nullable: true
                  required:
                    - name
                    - form_id
                    - tag_id
                    - sequence_id
                    - product_id
                    - initiator_value
              required:
                - target_url
                - event
            example:
              target_url: https://example.convertkit.dev/
              event:
                name: subscriber.subscriber_activate
                form_id: null
                tag_id: null
                sequence_id: null
                product_id: null
                initiator_value: null
                custom_field_id: null
      responses:
        '201':
          description: Creates the webhook
          content:
            application/json:
              schema:
                type: object
                properties:
                  webhook:
                    type: object
                    properties:
                      id:
                        type: integer
                      account_id:
                        type: integer
                      event:
                        type: object
                        properties:
                          name:
                            type: string
                            description: Product name
                          initiator_value:
                            nullable: true
                        required:
                          - name
                          - initiator_value
                      target_url:
                        type: string
                    required:
                      - id
                      - account_id
                      - event
                      - target_url
                required:
                  - webhook
              example:
                webhook:
                  id: 9
                  account_id: 1109
                  event:
                    name: subscriber_activate
                    initiator_value: null
                  target_url: https://example.convertkit.dev/
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
        '422':
          description: Returns an error when missing required params
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
                  - '`event` and `target` parameters must be provided'
      security:
        - API Key: []
        - OAuth2: []
components:
  securitySchemes:
    API Key:
      description: Authenticate API requests via an API Key
      type: apiKey
      in: header
      name: X-Kit-Api-Key
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