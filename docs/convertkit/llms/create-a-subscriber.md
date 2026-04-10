# Source: https://developers.kit.com/api-reference/subscribers/create-a-subscriber.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a subscriber

> Behaves as an upsert. If a subscriber with the provided email address does not exist, it creates one with the specified first name and state. If a subscriber with the provided email address already exists, it updates the first name.<br/><br/>We will ignore custom fields that don't already exist in your account. We will not return an error if you try to add data to a custom field that does not exist. Please use <a href="#create-a-custom-field">Create a custom field</a> to create custom fields before setting for subscribers.<br/><br/><strong>NOTE:</strong> Updating the subscriber state with this endpoint is not supported at this time.<br/><strong>NOTE:</strong> We support creating/updating a maximum of 140 custom fields at a time.



## OpenAPI

````yaml api-reference/v4.json post /v4/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/subscribers:
    post:
      tags:
        - Subscribers
      summary: Create a subscriber
      description: >-
        Behaves as an upsert. If a subscriber with the provided email address
        does not exist, it creates one with the specified first name and state.
        If a subscriber with the provided email address already exists, it
        updates the first name.<br/><br/>We will ignore custom fields that don't
        already exist in your account. We will not return an error if you try to
        add data to a custom field that does not exist. Please use <a
        href="#create-a-custom-field">Create a custom field</a> to create custom
        fields before setting for subscribers.<br/><br/><strong>NOTE:</strong>
        Updating the subscriber state with this endpoint is not supported at
        this time.<br/><strong>NOTE:</strong> We support creating/updating a
        maximum of 140 custom fields at a time.
      parameters: []
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
                state:
                  type: string
                  nullable: true
                  enum:
                    - active
                    - cancelled
                    - bounced
                    - complained
                    - inactive
                  description: >-
                    Create subscriber in this state (`active`, `bounced`,
                    `cancelled`, `complained` or `inactive`). Defaults to
                    `active`.
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
                    Phone Number:
                      type: string
                    Enrolled in Coaching:
                      type: string
                    Lead Score:
                      type: string
              required:
                - email_address
            example:
              first_name: Alice
              email_address: alice@convertkit.dev
              state: active
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
                Phone Number: 555-555-5555
                Enrolled in Coaching: 'true'
                Lead Score: '87'
      responses:
        '200':
          description: >-
            Returns a 200 and updates the subscriber first name when a
            subscriber with provided email already exists
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
                  id: 289
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: inactive
                  created_at: '2023-02-17T11:43:55Z'
                  fields: {}
        '201':
          description: Creates a new subscriber
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
                  id: 286
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  fields: {}
        '202':
          description: >-
            Returns a 202 and asynchronously adds custom fields for the new
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
                  id: 288
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
        '422':
          description: >-
            Returns a 422 with an error message when one or more of the
            parameters are invalid
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
                  - Email address is invalid
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