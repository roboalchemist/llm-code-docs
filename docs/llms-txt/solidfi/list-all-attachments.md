# Source: https://docs.solidfi.com/v2/api-reference/attachments/list-all-attachments.md

# List all Attachments

> List all Attachments

## OpenAPI

````yaml get /v2/attachment
paths:
  path: /v2/attachment
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
      path: {}
      query:
        limit:
          schema:
            - type: number
              description: number of records to return
              example: 10
        starting_after:
          schema:
            - type: string
              description: >-
                A cursor for use in pagination. `starting_after` is an ID that
                defines your place in the list. For instance, if you make a list
                request and receive 50 records, ending with
                `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                subsequent call can include
                `starting_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`
                in order to fetch the next page of the list.
              example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
        ending_before:
          schema:
            - type: string
              description: >-
                A cursor for use in pagination. `ending_before` is an ID that
                defines your place in the list. For instance, if you make a list
                request and receive 50 records, starting with
                `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                subsequent call can include `ending_before=
                Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in order to
                fetch the previous page of the list.
              example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
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
              total:
                allOf:
                  - type: number
                    example: 1
                    description: total number of records
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/attachment'
              has_more:
                allOf:
                  - type: string
                    example: 'true'
                    description: if there are more records to iterate or not
                    enum:
                      - 'true'
                      - 'false'
              starting_after:
                allOf:
                  - type: string
                    example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
                    description: >-
                      A cursor for use in pagination. `starting_after` is an ID
                      that defines your place in the list. For instance, if you
                      make a list request and receive 50 records, ending with
                      `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                      subsequent call can include
                      `starting_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`
                      in order to fetch the next page of the list.
              ending_before:
                allOf:
                  - type: string
                    example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
                    description: >-
                      A cursor for use in pagination. `ending_before` is an ID
                      that defines your place in the list. For instance, if you
                      make a list request and receive 50 records, starting with
                      `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                      subsequent call can include `ending_before=
                      Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in order
                      to fetch the previous page of the list.
            refIdentifier: '#/components/schemas/list_attachment'
        examples:
          list_attachment_example:
            value:
              total: 1
              data:
                - id: att_a8d2b191fa0e960d8e49a4bfd320e07b
                  reference_id: ctp_8e5541c8a9e50c3af3b0daacf9175130
                  label: formation
                  url: ''
                  created_at: '2024-04-04T11:06:00Z'
              has_more: 'true'
              starting_after: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
              ending_before: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
        description: List all Attachments
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          list_attachment_example:
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
  schemas:
    attachment:
      type: object
      properties:
        id:
          type: string
          example: att_a8d2b191fa0e960d8e49a4bfd320e07b
          description: unique id of the attachment created
        reference_id:
          type: string
          example: ctp_8e5541c8a9e50c3af3b0daacf9175130
          description: resource id to which the attachment belongs
        label:
          type: string
          example: formation
          description: label of the attachment
        url:
          type: string
          example: http://bucket.s3-website-us-east-1.amazonaws.com
          description: url to download the attachment
        timestamps:
          type: object
          properties:
            created_at:
              type: string
              example: '2024-04-04T11:06:00Z'
              description: time at which the attachment was created
            deleted_at:
              type: string
              example: '2024-04-04T11:06:00Z'
              description: time at which the attachment was deleted

````