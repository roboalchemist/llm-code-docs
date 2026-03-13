# Source: https://developers.kit.com/api-reference/custom-fields/update-a-custom-field.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a custom field

> Updates a custom field label (see [Create a custom field](#create-a-custom-field) above for more information on labels). Note that the key will change but the name remains the same when the label is updated.<br/><br/><strong>Warning: </strong>An update to a custom field will break all of the liquid personalization tags in emails that reference it - e.g. if you update a `Zip_Code` custom field to `Post_Code`, all liquid tags referencing `{{ subscriber.Zip_Code }}` would no longer work and need to be replaced with `{{ subscriber.Post_Code }}`.



## OpenAPI

````yaml api-reference/v4.json put /v4/custom_fields/{id}
openapi: 3.0.3
info:
  title: Kit API
  version: '4.0'
servers:
  - url: https://api.kit.com
security: []
paths:
  /v4/custom_fields/{id}:
    put:
      tags:
        - Custom Fields
      summary: Update a custom field
      description: >-
        Updates a custom field label (see [Create a custom
        field](#create-a-custom-field) above for more information on labels).
        Note that the key will change but the name remains the same when the
        label is updated.<br/><br/><strong>Warning: </strong>An update to a
        custom field will break all of the liquid personalization tags in emails
        that reference it - e.g. if you update a `Zip_Code` custom field to
        `Post_Code`, all liquid tags referencing `{{ subscriber.Zip_Code }}`
        would no longer work and need to be replaced with `{{
        subscriber.Post_Code }}`.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          example: 29
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
              label: Last name
      responses:
        '200':
          description: Updates the custom field and returns its details
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
                  id: 27
                  name: ck_field_27_last_name
                  key: last_name
                  label: Last name
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
          description: >-
            Returns a 422 with an error mesage when one or more of the
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