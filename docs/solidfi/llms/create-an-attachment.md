# Source: https://docs.solidfi.com/v2/api-reference/attachments/create-an-attachment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an Attachment

> Create an Attachment



## OpenAPI

````yaml post /v2/attachment
openapi: 3.0.3
info:
  title: Solid v2
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.sandbox.solidfi.com
  - url: https://api.prod.solidfi.com
security: []
tags:
  - name: Master Accounts
  - name: Sub Account Holders
  - name: Sub Accounts
  - name: Counterparties
  - name: Card Holders
  - name: Cards
  - name: Transactions
  - name: Attachments
  - name: Webhooks
  - name: Simulation
  - name: ACH
  - name: Card
paths:
  /v2/attachment:
    post:
      tags:
        - Attachments
      summary: Create an Attachment
      description: Create an Attachment
      operationId: createAnAttachment
      parameters:
        - name: api-key
          in: header
          schema:
            type: string
            example: '{{api_key}}'
            description: >-
              API key is required to call Solid APIs. You can view and manage
              your API keys in the Solid dashboard.
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                reference_id:
                  type: string
                  example: ctp_8e5541c8a9e50c3af3b0daacf9175130
                  description: resource id to which the attachment belongs
                label:
                  type: string
                  example: formation
                  description: label of the attachment
            examples:
              Create an Attachment:
                value:
                  reference_id: ctp_8e5541c8a9e50c3af3b0daacf9175130
                  label: formation
      responses:
        '201':
          description: Create an Attachment
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/create_attachment_response'
                type: object
              examples:
                create_attachment_example:
                  $ref: '#/components/examples/attachment_example'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                attachment_example:
                  $ref: '#/components/examples/unauth_error'
      security:
        - {}
components:
  schemas:
    create_attachment_response:
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
          description: url to upload the attachment
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
  examples:
    attachment_example:
      value:
        id: att_a8d2b191fa0e960d8e49a4bfd320e07b
        reference_id: ctp_8e5541c8a9e50c3af3b0daacf9175130
        label: formation
        url: http://bucket.s3-website-us-east-1.amazonaws.com
        created_at: '2024-04-04T11:06:00Z'
    unauth_error:
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

````