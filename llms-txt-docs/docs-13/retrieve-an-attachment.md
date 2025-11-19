# Source: https://docs.solidfi.com/v2/api-reference/attachments/retrieve-an-attachment.md

# Retrieve an Attachment

> Retrieve an Attachment

## OpenAPI

````yaml get /v2/attachment/{attachment_id}
paths:
  path: /v2/attachment/{attachment_id}
  method: get
  servers:
    - url: https://api.sandbox.solidfi.com
    - url: https://api.prod.solidfi.com
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
    parameters:
      path:
        attachment_id:
          schema:
            - type: string
              required: true
      query: {}
      header:
        api-key:
          schema:
            - type: string
              required: true
              description: >-
                API key is required to call Solid APIs. You can view and manage
                your API keys in the Solid dashboard.
              example: '{{api_key}}'
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    example: att_a8d2b191fa0e960d8e49a4bfd320e07b
                    description: unique id of the attachment created
              reference_id:
                allOf:
                  - type: string
                    example: ctp_8e5541c8a9e50c3af3b0daacf9175130
                    description: resource id to which the attachment belongs
              label:
                allOf:
                  - type: string
                    example: formation
                    description: label of the attachment
              url:
                allOf:
                  - type: string
                    example: http://bucket.s3-website-us-east-1.amazonaws.com
                    description: url to download the attachment
              timestamps:
                allOf:
                  - type: object
                    properties:
                      created_at:
                        type: string
                        example: '2024-04-04T11:06:00Z'
                        description: time at which the attachment was created
                      deleted_at:
                        type: string
                        example: '2024-04-04T11:06:00Z'
                        description: time at which the attachment was deleted
            refIdentifier: '#/components/schemas/attachment'
        examples:
          attachment_example:
            value:
              id: att_a8d2b191fa0e960d8e49a4bfd320e07b
              reference_id: ctp_8e5541c8a9e50c3af3b0daacf9175130
              label: formation
              url: http://bucket.s3-website-us-east-1.amazonaws.com
              created_at: '2024-04-04T11:06:00Z'
        description: Retrieve an Attachment
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          attachment_example:
            value:
              request_id: req_01900e34c96d7abfa970a9f454ab2d5d
              client_id: ''
              method: GET
              status: 401
              error:
                code: ERROR_CODE_UNAUTHORIZED
                message: unauthorized
                field_name: ''
              created_at: '2024-06-12T20:47:38Z'
        description: Unauthorized Error
  deprecated: false
  type: path
components:
  schemas: {}

````