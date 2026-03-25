# Source: https://developers.kit.com/api-reference/forms/add-subscriber-to-form.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add subscriber to form

> The subscriber being added to the form must already exist. Subscribers can be created using the "[Create a subscriber](#create-a-subscriber)" endpoint.



## OpenAPI

````yaml api-reference/v4.json post /v4/forms/{form_id}/subscribers/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/forms/{form_id}/subscribers/{id}:
    post:
      tags:
        - Forms
      summary: Add subscriber to form
      description: >-
        The subscriber being added to the form must already exist. Subscribers
        can be created using the "[Create a subscriber](#create-a-subscriber)"
        endpoint.
      parameters:
        - name: form_id
          in: path
          required: true
          schema:
            type: integer
          example: 190
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 668
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                referrer:
                  type: string
              required:
                - referrer
            example:
              referrer: >-
                https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
      responses:
        '200':
          description: Returns a 200 when the subscriber has already been added to the form
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
                      added_at:
                        type: string
                      fields:
                        type: object
                        properties: {}
                      referrer:
                        type: string
                      referrer_utm_parameters:
                        type: object
                        properties:
                          source:
                            type: string
                          medium:
                            type: string
                          campaign:
                            type: string
                          term:
                            type: string
                          content:
                            type: string
                        required:
                          - source
                          - medium
                          - campaign
                          - term
                          - content
                    required:
                      - id
                      - first_name
                      - email_address
                      - state
                      - created_at
                      - added_at
                      - fields
                      - referrer
                      - referrer_utm_parameters
                required:
                  - subscriber
              example:
                subscriber:
                  id: 662
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  added_at: '2023-02-17T11:43:55Z'
                  fields: {}
                  referrer: >-
                    https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
                  referrer_utm_parameters:
                    source: facebook
                    medium: cpc
                    campaign: black_friday
                    term: car_owners
                    content: get_10_off
        '201':
          description: Adds the subscriber to the form
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
                        nullable: true
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
                        properties: {}
                      referrer:
                        type: string
                      referrer_utm_parameters:
                        type: object
                        properties:
                          source:
                            type: string
                          medium:
                            type: string
                          campaign:
                            type: string
                          term:
                            type: string
                          content:
                            type: string
                        required:
                          - source
                          - medium
                          - campaign
                          - term
                          - content
                    required:
                      - id
                      - first_name
                      - email_address
                      - state
                      - created_at
                      - added_at
                      - fields
                      - referrer
                      - referrer_utm_parameters
                required:
                  - subscriber
              example:
                subscriber:
                  id: 664
                  first_name: Alice
                  email_address: alice@convertkit.dev
                  state: active
                  created_at: '2023-02-17T11:43:55Z'
                  added_at: '2023-02-17T11:43:55Z'
                  fields: {}
                  referrer: >-
                    https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
                  referrer_utm_parameters:
                    source: facebook
                    medium: cpc
                    campaign: black_friday
                    term: car_owners
                    content: get_10_off
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