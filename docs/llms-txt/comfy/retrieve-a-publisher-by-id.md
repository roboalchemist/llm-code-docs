# Source: https://docs.comfy.org/api-reference/registry/retrieve-a-publisher-by-id.md

# Retrieve a publisher by ID

## OpenAPI

````yaml https://api.comfy.org/openapi get /publishers/{publisherId}
paths:
  path: /publishers/{publisherId}
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path:
        publisherId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              createdAt:
                allOf:
                  - description: The date and time the publisher was created.
                    format: date-time
                    type: string
              description:
                allOf:
                  - type: string
              id:
                allOf:
                  - description: >-
                      The unique identifier for the publisher. It's akin to a
                      username. Should be lowercase.
                    type: string
              logo:
                allOf:
                  - description: URL to the publisher's logo.
                    type: string
              members:
                allOf:
                  - description: A list of members in the publisher.
                    items:
                      $ref: '#/components/schemas/PublisherMember'
                    type: array
              name:
                allOf:
                  - type: string
              source_code_repo:
                allOf:
                  - type: string
              status:
                allOf:
                  - $ref: '#/components/schemas/PublisherStatus'
              support:
                allOf:
                  - type: string
              website:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Publisher'
        examples:
          example:
            value:
              createdAt: '2023-11-07T05:31:56Z'
              description: <string>
              id: <string>
              logo: <string>
              members:
                - id: <string>
                  role: <string>
                  user:
                    email: <string>
                    id: <string>
                    name: <string>
              name: <string>
              source_code_repo: <string>
              status: PublisherStatusActive
              support: <string>
              website: <string>
        description: Publisher retrieved successfully
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Publisher not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas:
    PublisherMember:
      properties:
        id:
          description: The unique identifier for the publisher member.
          type: string
        role:
          description: The role of the user in the publisher.
          type: string
        user:
          $ref: '#/components/schemas/PublisherUser'
      type: object
    PublisherStatus:
      enum:
        - PublisherStatusActive
        - PublisherStatusBanned
      type: string
    PublisherUser:
      properties:
        email:
          description: The email address for this user.
          type: string
        id:
          description: The unique id for this user.
          type: string
        name:
          description: The name for this user.
          type: string
      type: object

````