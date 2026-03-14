# Source: https://developers.kit.com/api-reference/custom-fields/list-custom-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List custom fields

> A custom field allows you to collect subscriber information beyond the standard fields of first name and email address. An example would be a custom field called last name so you can get the full names of your subscribers.<br/><br/>You create a custom field, and then you're able to use that in your forms or emails.



## OpenAPI

````yaml api-reference/v4.json get /v4/custom_fields
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/custom_fields:
    get:
      tags:
        - Custom Fields
      summary: List custom fields
      description: >-
        A custom field allows you to collect subscriber information beyond the
        standard fields of first name and email address. An example would be a
        custom field called last name so you can get the full names of your
        subscribers.<br/><br/>You create a custom field, and then you're able to
        use that in your forms or emails.
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
          description: Returns a paginated list of all custom fields for your account
          content:
            application/json:
              schema:
                type: object
                properties:
                  custom_fields:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        name:
                          type: string
                        key:
                          type: string
                        label:
                          type: string
                      required:
                        - id
                        - name
                        - key
                        - label
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
                  - custom_fields
                  - pagination
              example:
                custom_fields:
                  - id: 1
                    name: ck_field_1_last_name
                    key: last_name
                    label: Last name
                pagination:
                  has_previous_page: false
                  has_next_page: false
                  start_cursor: WzFd
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