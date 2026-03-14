# Source: https://developers.kit.com/api-reference/forms/list-forms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List forms



## OpenAPI

````yaml api-reference/v4.json get /v4/forms
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/forms:
    get:
      tags:
        - Forms
      summary: List forms
      parameters:
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
        - name: status
          description: >-
            Filter forms that have this status (`active`, `archived`, `trashed`,
            or `all`). Defaults to `active`.
          in: query
          required: false
          schema:
            type: string
            enum:
              - active
              - archived
              - trashed
              - all
            nullable: true
        - name: type
          description: >-
            Filter forms and landing pages by type. Use `embed` for embedded
            forms. Use `hosted` for landing pages.
          in: query
          required: false
          schema:
            nullable: true
      responses:
        '200':
          description: >-
            Returns a paginated list of all forms and landing pages (embedded
            and hosted) for your account (including active and archived)
          content:
            application/json:
              schema:
                type: object
                properties:
                  forms:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        name:
                          type: string
                        created_at:
                          type: string
                        type:
                          type: string
                        format:
                          nullable: true
                        embed_js:
                          type: string
                        embed_url:
                          type: string
                        archived:
                          type: boolean
                        uid:
                          type: string
                      required:
                        - id
                        - name
                        - created_at
                        - type
                        - format
                        - embed_js
                        - embed_url
                        - archived
                        - uid
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
                  - forms
                  - pagination
              example:
                forms:
                  - id: 49
                    name: Sign up
                    created_at: '2023-02-17T11:43:55Z'
                    type: embed
                    format: null
                    embed_js: https://kit-greetings.kit.com/f049e3d9ab/index.js
                    embed_url: https://kit-greetings.kit.com/f049e3d9ab
                    archived: false
                    uid: f049e3d9ab
                  - id: 48
                    name: Lead gen
                    created_at: '2023-02-17T11:43:55Z'
                    type: hosted
                    format: null
                    embed_js: https://kit-greetings.kit.com/ae7c1adaa1/index.js
                    embed_url: https://kit-greetings.kit.com/ae7c1adaa1
                    archived: false
                    uid: ae7c1adaa1
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: WzQ5XQ==
                  end_cursor: WzQ4XQ==
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