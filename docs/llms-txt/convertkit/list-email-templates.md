# Source: https://developers.kit.com/api-reference/email-templates/list-email-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List email templates



## OpenAPI

````yaml api-reference/v4.json get /v4/email_templates
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/email_templates:
    get:
      tags:
        - Email Templates
      summary: List email templates
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
      responses:
        '200':
          description: Returns a paginated list of all email templates for your account
          content:
            application/json:
              schema:
                type: object
                properties:
                  email_templates:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        name:
                          type: string
                        is_default:
                          type: boolean
                        category:
                          type: string
                      required:
                        - id
                        - name
                        - is_default
                        - category
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
                  - email_templates
                  - pagination
              example:
                email_templates:
                  - id: 9
                    name: Custom HTML Template
                    is_default: false
                    category: HTML
                  - id: 8
                    name: Story
                    is_default: false
                    category: Starting point
                  - id: 6
                    name: Text Only
                    is_default: true
                    category: HTML
                  - id: 4
                    name: Modern
                    is_default: false
                    category: HTML
                  - id: 2
                    name: Classic
                    is_default: false
                    category: HTML
                  - id: 1
                    name: Card
                    is_default: false
                    category: HTML
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: Wzld
                  end_cursor: WzFd
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