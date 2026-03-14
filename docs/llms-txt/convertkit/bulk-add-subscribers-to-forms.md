# Source: https://developers.kit.com/api-reference/forms/bulk-add-subscribers-to-forms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk add subscribers to forms

> Adding subscribers to double opt-in forms will trigger sending an Incentive Email. Subscribers already added to the specified form will not receive the Incentive Email again. For more information about double opt-in see "[Double opt-in](#double-opt-in)". <br/><br/>The subscribers being added to the form must already exist. Subscribers can be created in bulk using the "[Bulk create subscriber](#bulk-create-subscribers)" endpoint.<br/><br/>See "[Bulk & async processing](#bulk-amp-async-processing)" for more information.



## OpenAPI

````yaml api-reference/v4.json post /v4/bulk/forms/subscribers
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/bulk/forms/subscribers:
    post:
      tags:
        - Forms
      summary: Bulk add subscribers to forms
      description: >-
        Adding subscribers to double opt-in forms will trigger sending an
        Incentive Email. Subscribers already added to the specified form will
        not receive the Incentive Email again. For more information about double
        opt-in see "[Double opt-in](#double-opt-in)". <br/><br/>The subscribers
        being added to the form must already exist. Subscribers can be created
        in bulk using the "[Bulk create subscriber](#bulk-create-subscribers)"
        endpoint.<br/><br/>See "[Bulk & async
        processing](#bulk-amp-async-processing)" for more information.
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                additions:
                  type: array
                  items:
                    type: object
                    properties:
                      form_id:
                        type: integer
                        nullable: true
                      subscriber_id:
                        type: integer
                        nullable: true
                      referrer:
                        type: string
                    required:
                      - form_id
                      - subscriber_id
                callback_url:
                  type: string
                  nullable: true
              required:
                - additions
            example:
              additions:
                - form_id: 0
                  subscriber_id: 0
                - form_id: 1
                  subscriber_id: 1
                - form_id: 2
                  subscriber_id: 2
                - form_id: 3
                  subscriber_id: 3
              callback_url: null
      responses:
        '200':
          description: >-
            Adds subscribers to forms synchronously when 100 or less
            form/subscribers are requested
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
                        email_address:
                          type: string
                        created_at:
                          type: string
                        added_at:
                          type: string
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
                        - created_at
                        - added_at
                        - referrer
                        - referrer_utm_parameters
                  failures:
                    type: array
                    items:
                      type: object
                      properties:
                        errors:
                          type: array
                          items:
                            type: string
                        subscription:
                          type: object
                          properties:
                            form_id:
                              type: integer
                              nullable: true
                            subscriber_id:
                              type: integer
                              nullable: true
                            referrer:
                              type: string
                          required:
                            - form_id
                            - subscriber_id
                            - referrer
                      required:
                        - errors
                        - subscription
                required:
                  - subscribers
                  - failures
              example:
                subscribers:
                  - id: 544
                    first_name: Sub
                    email_address: sub@example.com
                    created_at: '2023-02-17T11:43:55Z'
                    added_at: '2023-02-17T11:43:55Z'
                    referrer: >-
                      https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
                    referrer_utm_parameters:
                      source: facebook
                      medium: cpc
                      campaign: black_friday
                      term: car_owners
                      content: get_10_off
                  - id: 544
                    first_name: Sub
                    email_address: sub@example.com
                    created_at: '2023-02-17T11:43:55Z'
                    added_at: '2023-02-17T11:43:55Z'
                    referrer: >-
                      https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
                    referrer_utm_parameters:
                      source: facebook
                      medium: cpc
                      campaign: black_friday
                      term: car_owners
                      content: get_10_off
                failures:
                  - errors:
                      - Subscriber does not exist
                    subscription:
                      form_id: 122
                      subscriber_id: null
                      referrer: >-
                        https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
                  - errors:
                      - Form does not exist
                    subscription:
                      form_id: null
                      subscriber_id: 544
                      referrer: >-
                        https://mywebsite.com/bfpromo/?utm_source=facebook&utm_medium=cpc&utm_campaign=black_friday&utm_term=car_owners&utm_content=get_10_off
        '202':
          description: >-
            Adds subscribers to forms asynchronously when more than 100
            form/subscribers are requested
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example: {}
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
        '413':
          description: >-
            Returns a 413 when the size of the request would exceed the
            account's data limit for enqueued bulk requests
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
                  - >-
                    This request exceeds your queued bulk requests limit. Please
                    wait while we process your existing requests and try again
                    later.
        '422':
          description: Returns a 422 when `additions` is empty or not an array
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
                  - No additions included for processing
      security:
        - OAuth2: []
components:
  securitySchemes:
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