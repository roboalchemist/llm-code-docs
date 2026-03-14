# Source: https://developers.kit.com/api-reference/subscribers/update-a-subscriber.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a subscriber

> We will ignore custom fields that don't already exist in your account. We will not return an error if you try to add data to a custom field that does not exist. Please use <a href="#create-a-custom-field">Create a custom field</a> to create custom fields before setting for subscribers.<br/><br/><strong>NOTE: </strong>We support creating/updating a maximum of 140 custom fields at a time.



## OpenAPI

````yaml api-reference/v4.json put /v4/subscribers/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/subscribers/{id}:
    put:
      tags:
        - Subscribers
      summary: Update a subscriber
      description: >-
        We will ignore custom fields that don't already exist in your account.
        We will not return an error if you try to add data to a custom field
        that does not exist. Please use <a href="#create-a-custom-field">Create
        a custom field</a> to create custom fields before setting for
        subscribers.<br/><br/><strong>NOTE: </strong>We support
        creating/updating a maximum of 140 custom fields at a time.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 314
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                first_name:
                  type: string
                  nullable: true
                email_address:
                  type: string
                fields:
                  type: object
                  nullable: true
                  properties:
                    Last name:
                      type: string
                    Birthday:
                      type: string
                    Source:
                      type: string
                    Role:
                      type: string
                    Company:
                      type: string
                    Postal code:
                      type: string
                    Website:
                      type: string
                    Social media:
                      type: string
                    How did you hear about us?:
                      type: string
                    Interests:
                      type: string
                    Coupon:
                      type: string
                  required:
                    - Last name
                    - Birthday
                    - Source
              required:
                - email_address
            example:
              first_name: Alice
              email_address: alice@convertkit.dev
              fields:
                Last name: Lamarr
                Birthday: Feb 17
                Source: landing page
                Role: Software developer
                Company: Convertkit
                Postal code: '83702'
                Website: convertkit.com
                Social media: https://www.linkedin.com/company/convertkit
                How did you hear about us?: Social media
                Interests: Monetization
                Coupon: ''
      responses:
        '200':
          description: Updates the subscriber's email address and first name
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscriber:
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
                      fields:
                        type: object
                        properties: {}
                    required:
                      - id
                      - first_name
                      - email_address
                      - state
                      - created_at
                      - fields
                required:
                  - subscriber
              example:
                subscriber:
                  id: 309
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  fields: {}
        '202':
          description: >-
            Returns a 202 and asynchronously updates custom fields for the
            subscriber when more than 10 custom fields are included in the
            request
          content:
            application/json:
              schema:
                type: object
                properties:
                  subscriber:
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
                      fields:
                        type: object
                        properties: {}
                    required:
                      - id
                      - first_name
                      - email_address
                      - state
                      - created_at
                      - fields
                required:
                  - subscriber
              example:
                subscriber:
                  id: 311
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  fields: {}
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
        '422':
          description: Returns 422 with an error when email address is already in use
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
                  - Email address has already been taken
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