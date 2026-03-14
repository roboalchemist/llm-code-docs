# Source: https://developers.kit.com/api-reference/sequences/list-subscribers-for-a-sequence.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List subscribers for a sequence



## OpenAPI

````yaml api-reference/v4.json get /v4/sequences/{sequence_id}/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/sequences/{sequence_id}/subscribers:
    get:
      tags:
        - Sequences
      summary: List subscribers for a sequence
      parameters:
        - name: added_after
          description: >-
            Filter subscribers who have been added to the form after this date
            (format yyyy-mm-dd)
          in: query
          required: false
          schema:
            type: string
            nullable: true
          example: '2023-02-14T11:43:55Z'
        - name: added_before
          description: >-
            Filter subscribers who have been added to the form before this date
            (format yyyy-mm-dd)
          in: query
          required: false
          schema:
            type: string
            nullable: true
          example: '2023-02-18T11:43:55Z'
        - name: after
          description: To fetch next page of results, use `?after=<end_cursor>`
          in: query
          required: false
          schema:
            nullable: true
        - name: before
          description: To fetch previous page of results, use `?before=<start_cursor>`
          in: query
          required: false
          schema:
            nullable: true
        - name: created_after
          description: >-
            Filter subscribers who have been created after this date (format
            yyyy-mm-dd)
          in: query
          required: false
          schema:
            type: string
            nullable: true
          example: '2023-01-17T11:43:55Z'
        - name: created_before
          description: >-
            Filter subscribers who have been created before this date (format
            yyyy-mm-dd)
          in: query
          required: false
          schema:
            type: string
            nullable: true
          example: '2023-02-18T11:43:55Z'
        - name: include_total_count
          description: >-
            To include the total count of records in the response, use `true`.
            For large collections, expect a slightly slower response.
          in: query
          required: false
          schema:
            type: boolean
          example: false
        - name: per_page
          description: Number of results per page. Default 500, maximum 1000.
          in: query
          required: false
          schema:
            nullable: true
        - name: sequence_id
          in: path
          required: true
          schema:
            type: integer
          example: 28
        - name: status
          description: >-
            Filter subscribers who have this status (`active`, `inactive`,
            `bounced`, `complained`, `cancelled` or `all`). Defaults to
            `active`.
          in: query
          required: false
          schema:
            type: string
            enum:
              - active
              - inactive
              - bounced
              - complained
              - cancelled
              - all
          example: all
      responses:
        '200':
          description: Returns a paginated list of subscribers for the specified sequence
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscribers:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        first_name:
                          type: string
                          nullable: true
                        email_address:
                          type: string
                        state:
                          type: string
                          enum:
                            - active
                            - cancelled
                            - bounced
                            - complained
                            - inactive
                        created_at:
                          type: string
                        added_at:
                          type: string
                        fields:
                          type: object
                          properties:
                            category:
                              type: string
                              nullable: true
                          required:
                            - category
                      required:
                        - id
                        - first_name
                        - email_address
                        - state
                        - created_at
                        - added_at
                        - fields
                  pagination:
                    type: object
                    properties:
                      has_previous_page:
                        type: boolean
                      has_next_page:
                        type: boolean
                      start_cursor:
                        type: string
                      end_cursor:
                        type: string
                      per_page:
                        type: integer
                    required:
                      - has_previous_page
                      - has_next_page
                      - start_cursor
                      - end_cursor
                      - per_page
                required:
                  - subscribers
                  - pagination
              example:
                subscribers:
                  - id: 799
                    first_name: null
                    email_address: subscriber481@kit.dev
                    state: active
                    created_at: '2023-02-17T11:43:55Z'
                    added_at: '2023-02-17T11:43:55Z'
                    fields:
                      category: One
                  - id: 798
                    first_name: null
                    email_address: subscriber480@kit.dev
                    state: active
                    created_at: '2023-02-17T11:43:55Z'
                    added_at: '2023-02-17T11:43:55Z'
                    fields:
                      category: null
                  - id: 797
                    first_name: null
                    email_address: subscriber479@kit.dev
                    state: active
                    created_at: '2023-02-17T11:43:55Z'
                    added_at: '2023-02-17T11:43:55Z'
                    fields:
                      category: null
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: Wzc5OV0=
                  end_cursor: Wzc5N10=
                  per_page: 500
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
        '404':
          description: Returns a 404 when the provided id does not exist
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
                  - Not Found
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