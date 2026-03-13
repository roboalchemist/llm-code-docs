# Source: https://developers.kit.com/api-reference/custom-fields/create-a-custom-field.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a custom field

> Create a custom field for your account. The label field must be unique to your account. Whitespace will be removed from the beginning and the end of your label.<br/><br/>Additionally, a key field and a name field will be generated for you. The key is an ASCII-only, lowercased, underscored representation of your label. This key must be unique to your account. Keys are used in personalization tags in sequences and broadcasts. Names are unique identifiers for use in the HTML of custom forms. They are made up of a combination of ID and the key of the custom field prefixed with "ck_field".



## OpenAPI

````yaml api-reference/v4.json post /v4/custom_fields
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/custom_fields:
    post:
      tags:
        - Custom Fields
      summary: Create a custom field
      description: >-
        Create a custom field for your account. The label field must be unique
        to your account. Whitespace will be removed from the beginning and the
        end of your label.<br/><br/>Additionally, a key field and a name field
        will be generated for you. The key is an ASCII-only, lowercased,
        underscored representation of your label. This key must be unique to
        your account. Keys are used in personalization tags in sequences and
        broadcasts. Names are unique identifiers for use in the HTML of custom
        forms. They are made up of a combination of ID and the key of the custom
        field prefixed with "ck_field".
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                label:
                  type: string
              required:
                - label
            example:
              label: Interests
      responses:
        '200':
          description: Returns a 200 and the custom field if it already exists
          content:
            application/json:
              schema:
                type: object
                properties:
                  custom_field:
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
                required:
                  - custom_field
              example:
                custom_field:
                  id: 8
                  name: ck_field_8_interests
                  key: interests
                  label: Interests
        '201':
          description: Creates a new custom field and returns its details
          content:
            application/json:
              schema:
                type: object
                properties:
                  custom_field:
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
                required:
                  - custom_field
              example:
                custom_field:
                  id: 6
                  name: ck_field_6_interests
                  key: interests
                  label: Interests
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
          description: Returns a 422 with an error message when the label is missing
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
                  - Label can't be blank
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