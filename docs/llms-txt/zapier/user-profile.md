# Source: https://docs.zapier.com/powered-by-zapier/api-reference/accounts/user-profile.md

# User Profile

> This endpoint returns the authenticated user information

#### OAuth

This endpoint requires the `profile` OAuth scope.

## OpenAPI

````yaml https://api.zapier.com/schema get /v1/profiles/me
paths:
  path: /v1/profiles/me
  method: get
  servers:
    - url: https://api.zapier.com
  request:
    security:
      - title: OAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: oauth2
              description: >-
                See our OAuth2 authentication documentation here:
                https://docs.zapier.com/powered-by-zapier/api-reference/authentication
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Profile'
        examples:
          Profile:
            summary: profile
            value:
              - id: 88998899
                first_name: Jacob
                last_name: Corwin
                full_name: Jacob Corwin
                email: jacob.corwin@zapier.example
                email_confirmed: true
                timezone: America/Toronto
        description: ''
    '401':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 401 Response
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invalid authentication
        examples: {}
        description: Invalid authentication
    '409':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 409 Response
    '429':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 429 Response
    '503':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            additionalProperties:
              allOf:
                - {}
        examples:
          example:
            value: {}
        description: 503 Response
  deprecated: false
  type: path
components:
  schemas:
    Profile:
      type: object
      description: An authenticated user profile.
      properties:
        id:
          type: integer
          description: The numeric identifier of this user
        first_name:
          type: string
          description: The first name of this user
        last_name:
          type: string
          description: The last name of this user
        full_name:
          type: string
          description: The combined full name of this user
        email:
          type: string
          format: email
          description: The email this user's account is associated with
        email_confirmed:
          type: boolean
          description: Whether said email is confirmed yet or not
        timezone:
          type: string
          description: The timezone set for this user
      required:
        - email
        - email_confirmed
        - first_name
        - full_name
        - id
        - last_name
        - timezone

````