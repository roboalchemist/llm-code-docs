# Source: https://www.quo.com/docs/mdx/api-reference/contacts/delete-a-contact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a contact

> Delete a contact by its unique identifier.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json delete /v1/contacts/{id}
openapi: 3.1.0
info:
  title: OpenPhone Public API
  version: 1.0.0
  description: API for connecting with OpenPhone.
  contact:
    name: OpenPhone Support
    email: support@openphone.com
    url: https://support.openphone.com/hc/en-us
  termsOfService: https://www.openphone.com/terms
servers:
  - description: Production server
    url: https://api.openphone.com
security:
  - apiKey: []
tags:
  - description: Operations related to calls
    name: Calls
  - description: >-
      Operations related to call summaries, including AI-generated summaries and
      Sona voice assistant summaries
    name: Call Summaries
  - description: >-
      Operations related to call transcripts, including AI-generated transcripts
      and Sona voice assistant transcripts
    name: Call Transcripts
  - description: Operations related to contacts
    name: Contacts
  - description: Operations related to conversations
    name: Conversations
  - description: Operations related to text messages
    name: Messages
  - description: Operations related to phone numbers
    name: Phone Numbers
  - description: Operations related to users
    name: Users
  - description: Operations related to webhooks
    name: Webhooks
paths:
  /v1/contacts/{id}:
    delete:
      tags:
        - Contacts
      summary: Delete a contact
      description: Delete a contact by its unique identifier.
      operationId: deleteContact_v1
      parameters:
        - in: path
          name: id
          required: true
          schema:
            description: The unique identifier of the contact.
            examples:
              - 66d0d87e8dc1211467372303
            type: string
      responses:
        '204':
          description: Success
        '400':
          description: Invalid Custom Field Item
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0801400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Invalid Custom Field Item
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                  description:
                    const: Invalid Custom Field Item
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0800401'
                    type: string
                  status:
                    const: 401
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unauthorized
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '403':
          description: Not Phone Number User
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0801403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Phone Number User
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                  description:
                    const: Not Phone Number User
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0800404'
                    type: string
                  status:
                    const: 404
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Found
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0800409'
                    type: string
                  status:
                    const: 409
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Conflict
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '500':
          description: Unknown Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0801500'
                    type: string
                  status:
                    const: 500
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unknown
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      in: header
      name: Authorization
      type: apiKey

````