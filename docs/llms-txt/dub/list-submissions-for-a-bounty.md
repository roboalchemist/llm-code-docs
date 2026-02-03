# Source: https://dub.co/docs/api-reference/endpoint/list-submissions-for-a-bounty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List bounty submissions

> List all submissions for a specific bounty.



## OpenAPI

````yaml get /bounties/{bountyId}/submissions
openapi: 3.0.3
info:
  title: Dub API
  description: >-
    Dub is the modern link attribution platform for short links, conversion
    tracking, and affiliate programs.
  version: 0.0.1
  contact:
    name: Dub Support
    email: support@dub.co
    url: https://dub.co/api
  license:
    name: AGPL-3.0 license
    url: https://github.com/dubinc/dub/blob/main/LICENSE.md
servers:
  - url: https://api.dub.co
    description: Production API
security: []
paths:
  /bounties/{bountyId}/submissions:
    get:
      tags:
        - Bounties
      summary: List bounty submissions
      description: List all submissions for a specific bounty.
      operationId: listBountySubmissions
      parameters:
        - in: path
          name: bountyId
          schema:
            type: string
          required: true
        - in: query
          name: status
          schema:
            description: The status of the submissions to list.
            type: string
            enum:
              - draft
              - submitted
              - approved
              - rejected
          description: The status of the submissions to list.
        - in: query
          name: groupId
          schema:
            description: The ID of the group to list submissions for.
            type: string
          description: The ID of the group to list submissions for.
        - in: query
          name: partnerId
          schema:
            description: The ID of the partner to list submissions for.
            type: string
          description: The ID of the partner to list submissions for.
        - in: query
          name: sortBy
          schema:
            default: completedAt
            description: The field to sort the submissions by.
            type: string
            enum:
              - completedAt
              - performanceCount
          description: The field to sort the submissions by.
        - in: query
          name: sortOrder
          schema:
            default: asc
            description: The order to sort the submissions by.
            type: string
            enum:
              - asc
              - desc
          description: The order to sort the submissions by.
        - in: query
          name: page
          schema:
            default: 1
            description: The page number for pagination.
            example: 1
            type: number
            minimum: 0
            exclusiveMinimum: true
          description: The page number for pagination.
        - in: query
          name: pageSize
          schema:
            default: 100
            description: The number of items per page.
            example: 50
            type: number
            minimum: 0
            exclusiveMinimum: true
            maximum: 100
          description: The number of items per page.
      responses:
        '200':
          description: The list of bounty submissions.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                    bountyId:
                      type: string
                    partnerId:
                      type: string
                    description:
                      nullable: true
                      type: string
                    urls:
                      nullable: true
                      type: array
                      items:
                        type: string
                    files:
                      nullable: true
                      type: array
                      items:
                        type: object
                        properties:
                          url:
                            type: string
                          fileName:
                            type: string
                          size:
                            type: number
                        required:
                          - url
                          - fileName
                          - size
                        additionalProperties: false
                    status:
                      type: string
                      enum:
                        - draft
                        - submitted
                        - approved
                        - rejected
                    performanceCount:
                      nullable: true
                      type: number
                    createdAt:
                      type: string
                    completedAt:
                      nullable: true
                      type: string
                    reviewedAt:
                      nullable: true
                      type: string
                    rejectionReason:
                      nullable: true
                      type: string
                    rejectionNote:
                      nullable: true
                      type: string
                  required:
                    - id
                    - bountyId
                    - partnerId
                    - description
                    - urls
                    - files
                    - status
                    - performanceCount
                    - createdAt
                    - completedAt
                    - reviewedAt
                    - rejectionReason
                    - rejectionNote
                  additionalProperties: false
        '400':
          $ref: '#/components/responses/400'
        '401':
          $ref: '#/components/responses/401'
        '403':
          $ref: '#/components/responses/403'
        '404':
          $ref: '#/components/responses/404'
        '409':
          $ref: '#/components/responses/409'
        '410':
          $ref: '#/components/responses/410'
        '422':
          $ref: '#/components/responses/422'
        '429':
          $ref: '#/components/responses/429'
        '500':
          $ref: '#/components/responses/500'
      security:
        - token: []
components:
  responses:
    '400':
      description: >-
        The server cannot or will not process the request due to something that
        is perceived to be a client error (e.g., malformed request syntax,
        invalid request message framing, or deceptive request routing).
      content:
        application/json:
          schema:
            x-speakeasy-name-override: BadRequest
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - bad_request
                    description: A short code indicating the error code returned.
                    example: bad_request
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#bad-request
                required:
                  - code
                  - message
            required:
              - error
    '401':
      description: >-
        Although the HTTP standard specifies "unauthorized", semantically this
        response means "unauthenticated". That is, the client must authenticate
        itself to get the requested response.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: Unauthorized
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - unauthorized
                    description: A short code indicating the error code returned.
                    example: unauthorized
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#unauthorized
                required:
                  - code
                  - message
            required:
              - error
    '403':
      description: >-
        The client does not have access rights to the content; that is, it is
        unauthorized, so the server is refusing to give the requested resource.
        Unlike 401 Unauthorized, the client's identity is known to the server.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: Forbidden
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - forbidden
                    description: A short code indicating the error code returned.
                    example: forbidden
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#forbidden
                required:
                  - code
                  - message
            required:
              - error
    '404':
      description: The server cannot find the requested resource.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: NotFound
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - not_found
                    description: A short code indicating the error code returned.
                    example: not_found
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#not-found
                required:
                  - code
                  - message
            required:
              - error
    '409':
      description: >-
        This response is sent when a request conflicts with the current state of
        the server.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: Conflict
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - conflict
                    description: A short code indicating the error code returned.
                    example: conflict
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#conflict
                required:
                  - code
                  - message
            required:
              - error
    '410':
      description: >-
        This response is sent when the requested content has been permanently
        deleted from server, with no forwarding address.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: InviteExpired
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - invite_expired
                    description: A short code indicating the error code returned.
                    example: invite_expired
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: https://dub.co/docs/api-reference/errors#invite-expired
                required:
                  - code
                  - message
            required:
              - error
    '422':
      description: >-
        The request was well-formed but was unable to be followed due to
        semantic errors.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: UnprocessableEntity
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - unprocessable_entity
                    description: A short code indicating the error code returned.
                    example: unprocessable_entity
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: >-
                      https://dub.co/docs/api-reference/errors#unprocessable-entity
                required:
                  - code
                  - message
            required:
              - error
    '429':
      description: >-
        The user has sent too many requests in a given amount of time ("rate
        limiting")
      content:
        application/json:
          schema:
            x-speakeasy-name-override: RateLimitExceeded
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - rate_limit_exceeded
                    description: A short code indicating the error code returned.
                    example: rate_limit_exceeded
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: >-
                      https://dub.co/docs/api-reference/errors#rate-limit_exceeded
                required:
                  - code
                  - message
            required:
              - error
    '500':
      description: The server has encountered a situation it does not know how to handle.
      content:
        application/json:
          schema:
            x-speakeasy-name-override: InternalServerError
            type: object
            properties:
              error:
                type: object
                properties:
                  code:
                    type: string
                    enum:
                      - internal_server_error
                    description: A short code indicating the error code returned.
                    example: internal_server_error
                  message:
                    x-speakeasy-error-message: true
                    type: string
                    description: A human readable explanation of what went wrong.
                    example: The requested resource was not found.
                  doc_url:
                    type: string
                    description: >-
                      A link to our documentation with more details about this
                      error code
                    example: >-
                      https://dub.co/docs/api-reference/errors#internal-server_error
                required:
                  - code
                  - message
            required:
              - error
  securitySchemes:
    token:
      type: http
      description: Default authentication mechanism
      scheme: bearer
      x-speakeasy-example: DUB_API_KEY

````