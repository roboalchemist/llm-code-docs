# Source: https://www.quo.com/docs/mdx/api-reference/conversations/list-conversations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Conversations

> Fetch a paginated list of conversations of OpenPhone conversations. Can be filtered by user and/or phone numbers. Defaults to all conversations in the OpenPhone organization. Results are returned in descending order based on the most recent conversation.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/conversations
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
  /v1/conversations:
    get:
      tags:
        - Conversations
      summary: List Conversations
      description: >-
        Fetch a paginated list of conversations of OpenPhone conversations. Can
        be filtered by user and/or phone numbers. Defaults to all conversations
        in the OpenPhone organization. Results are returned in descending order
        based on the most recent conversation.
      operationId: listConversations_v1
      parameters:
        - in: query
          name: phoneNumber
          required: false
          schema:
            description: >-
              DEPRECATED, use `phoneNumbers` instead. If both `phoneNumber` and
              `phoneNumbers` are provided, `phoneNumbers` will be used. Filters
              results to only include conversations with the specified OpenPhone
              phone number. Can be either your OpenPhone phone number ID or the
              full phone number in E.164 format.
            examples:
              - '+15555555555'
              - PN123abc
            deprecated: true
            anyOf:
              - description: A phone number in E.164 format, including the country code.
                examples:
                  - '+15555555555'
                pattern: ^\+[1-9]\d{1,14}$
                type: string
              - pattern: ^PN(.*)$
                type: string
        - in: query
          name: phoneNumbers
          required: false
          schema:
            description: >-
              Filters results to only include conversations with the specified
              OpenPhone phone numbers. Each item can be either an OpenPhone
              phone number ID or a full phone number in E.164 format.
            examples:
              - - '+15555555555'
                - PN123abc
            minItems: 1
            maxItems: 100
            type: array
            items:
              anyOf:
                - description: A phone number in E.164 format, including the country code.
                  examples:
                    - '+15555555555'
                  pattern: ^\+[1-9]\d{1,14}$
                  type: string
                - pattern: ^PN(.*)$
                  type: string
        - in: query
          name: userId
          required: false
          schema:
            description: >-
              The unique identifier of the user the making the request. Used to
              filter results to only include the user's conversations.
            examples:
              - US123abc
            pattern: ^US(.*)$
            type: string
        - in: query
          name: createdAfter
          required: false
          schema:
            description: >-
              Filter results to only include conversations created after the
              specified date and time, in ISO_8601 format.
            examples:
              - '2022-01-01T00:00:00Z'
            format: date-time
            type: string
        - in: query
          name: createdBefore
          required: false
          schema:
            description: >-
              Filter results to only include conversations created before the
              specified date and time, in ISO_8601 format.
            examples:
              - '2022-01-01T00:00:00Z'
            format: date-time
            type: string
        - in: query
          name: excludeInactive
          required: false
          schema:
            description: Exclude inactive conversations from the results.
            examples:
              - true
            type: boolean
        - in: query
          name: updatedAfter
          required: false
          schema:
            description: >-
              Filter results to only include conversations updated after the
              specified date and time, in ISO_8601 format.
            examples:
              - '2022-01-01T00:00:00Z'
            format: date-time
            type: string
        - in: query
          name: updatedBefore
          required: false
          schema:
            description: >-
              Filter results to only include conversations updated before the
              specified date and time, in ISO_8601 format.
            examples:
              - '2022-01-01T00:00:00Z'
            format: date-time
            type: string
        - in: query
          name: maxResults
          required: true
          schema:
            description: Maximum number of results to return per page.
            default: 10
            maximum: 100
            minimum: 1
            type: integer
        - in: query
          name: pageToken
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        assignedTo:
                          anyOf:
                            - type: string
                            - type: 'null'
                        createdAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        deletedAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        id:
                          pattern: ^CN(.*)$
                          type: string
                        lastActivityAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        lastActivityId:
                          anyOf:
                            - pattern: ^AC(.*)$
                              type: string
                            - type: 'null'
                        mutedUntil:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        name:
                          anyOf:
                            - type: string
                            - type: 'null'
                        participants:
                          type: array
                          items:
                            description: >-
                              A phone number in E.164 format, including the
                              country code.
                            examples:
                              - '+15555555555'
                            pattern: ^\+[1-9]\d{1,14}$
                            type: string
                        phoneNumberId:
                          pattern: ^PN(.*)$
                          type: string
                        snoozedUntil:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        updatedAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                      required:
                        - assignedTo
                        - createdAt
                        - deletedAt
                        - id
                        - lastActivityAt
                        - lastActivityId
                        - mutedUntil
                        - name
                        - participants
                        - phoneNumberId
                        - snoozedUntil
                        - updatedAt
                  totalItems:
                    description: >-
                      Total number of items available. ⚠️ Note: `totalItems` is
                      not accurately returning the total number of items that
                      can be paginated. We are working on fixing this issue.
                    type: integer
                  nextPageToken:
                    anyOf:
                      - type: string
                      - type: 'null'
                required:
                  - data
                  - totalItems
                  - nextPageToken
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '1000400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Bad Request
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
                    const: '1000401'
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
                    const: '1001403'
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
                    const: '1000404'
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
                    const: '1001500'
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